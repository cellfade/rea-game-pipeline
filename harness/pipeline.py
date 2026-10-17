#!/usr/bin/env python3
"""Evidence-led planning checks. Never executes tickets or modifies its own rules."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys

STATUSES = {'planned', 'active', 'review', 'done', 'blocked'}
EVIDENCE = {'observed', 'derived', 'inferred', 'proposed', 'unknown'}
DIGEST = re.compile(r'^[0-9a-f]{64}$')

def safe_path(value):
    return isinstance(value, str) and bool(value) and str(PurePosixPath(value)) == value and not any(ord(c) < 32 or ord(c) == 127 for c in value) and '\\' not in value and not PurePosixPath(value).is_absolute() and '..' not in PurePosixPath(value).parts and ':' not in value

def overlaps(a, b):
    a, b = a.rstrip('/'), b.rstrip('/')
    return a == b or a.startswith(b + '/') or b.startswith(a + '/') or a == '.' or b == '.'

def validate(p):
    errors = []
    if not isinstance(p, dict): return ['project must be object']
    for key in ('tasks', 'evidence', 'receipts', 'reviews', 'uat', 'failures'):
        value = p.get(key, [])
        if not isinstance(value, list) or any(not isinstance(item, dict) for item in value): return [f'{key} must be a list of objects']
    for key in ('evidence', 'failures'):
        ids = [item.get('id') for item in p.get(key, [])]
        if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids): return [f'{key} IDs must be unique nonempty strings']
    for e in p.get('evidence', []):
        if not isinstance(e.get('source'), dict): return ['evidence source must be object']
    for key, fields in (('reviews', ('task_id','author','reviewer','subject_digest','verdict')), ('receipts', ('task_id','test','status','revision')), ('uat', ('task_id','revision','status','reviewer'))):
        for item in p.get(key, []):
            if any(not isinstance(item.get(f), str) or not item.get(f) for f in fields): return [f'{key} fields must be nonempty strings']
    if p.get('schema_version') != 1: errors.append('schema_version must be 1')
    if type(p.get('max_workers')) is not int or not 1 <= p['max_workers'] <= 16: errors.append('max_workers must be 1..16')
    tasks = p.get('tasks', [])
    if not isinstance(tasks, list): return errors + ['tasks must be a list']
    ids = [t.get('id') for t in tasks if isinstance(t, dict)]
    if len(ids) != len(tasks) or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids): return errors + ['task IDs must be unique nonempty strings']
    by = {t['id']: t for t in tasks}
    for t in tasks:
        name = t['id']
        if not isinstance(t.get('status'), str) or t.get('status') not in STATUSES: errors.append(f'{name}: invalid status')
        for field in ('depends_on', 'allowed_files', 'resources', 'required_tests'):
            if not isinstance(t.get(field), list) or any(not isinstance(x, str) for x in t.get(field, [])): return errors + [f'{name}: {field} must be string list']
        if any(not safe_path(x) for x in t.get('allowed_files', [])): errors.append(f'{name}: unsafe write path')
        if any(d not in by for d in t.get('depends_on', [])): errors.append(f'{name}: missing dependency')
        if isinstance(t.get('status'), str) and t.get('status') in {'active', 'review', 'done'} and any(by.get(d, {}).get('status') != 'done' for d in t['depends_on']): errors.append(f'{name}: prerequisite must be done')
        if not isinstance(t.get('evidence_ids', []), list) or any(not isinstance(x, str) for x in t.get('evidence_ids', [])): return errors + [f'{name}: evidence_ids must be string list']
        if not isinstance(t.get('author'), str) or not t.get('author'): errors.append(f'{name}: author required')
        if not DIGEST.fullmatch(str(t.get('revision', ''))): errors.append(f'{name}: revision must be SHA256 digest')
    visiting, visited = set(), set()
    def visit(i):
        if i in visiting: errors.append('dependency cycle'); return
        if i in visited: return
        visiting.add(i)
        for d in by[i].get('depends_on', []):
            if d in by: visit(d)
        visiting.remove(i); visited.add(i)
    for i in by: visit(i)
    for e in p.get('evidence', []):
        if not isinstance(e.get('status'), str) or e.get('status') not in EVIDENCE or not isinstance(e.get('claim'), str) or not e.get('claim') or not all(isinstance(e.get('source', {}).get(k), str) and e['source'][k] for k in ('identity', 'locator')): errors.append('evidence needs status, claim, source identity and locator')
    active = [t for t in tasks if t.get('status') == 'active']
    if type(p.get('max_workers')) is int and len(active) > p['max_workers']: errors.append('active worker bound exceeded')
    for n, a in enumerate(active):
        for b in active[n+1:]:
            if conflict(a, b): errors.append(f"active conflict: {a['id']} / {b['id']}")
    return sorted(set(errors))

def conflict(a, b):
    return bool(set(a['resources']) & set(b['resources'])) or any(overlaps(x, y) for x in a['allowed_files'] for y in b['allowed_files'])

def ready(p):
    by = {t['id']: t for t in p['tasks']}
    selected = [t for t in p['tasks'] if t['status'] == 'active']
    result = []
    for t in p['tasks']:
        if len(selected) >= p['max_workers']: break
        if t['status'] == 'planned' and all(by[d]['status'] == 'done' for d in t['depends_on']) and not any(conflict(t, s) for s in selected):
            selected.append(t); result.append(t['id'])
    return result

def audit(p, level):
    errors = validate(p)
    if errors: return errors
    scope = p.get('release_tasks', [])
    if not isinstance(scope, list) or not scope or any(not isinstance(x, str) for x in scope):
        errors.append('nonempty release_tasks audit scope required'); scope = []
    by = {t['id']: t for t in p.get('tasks', [])}
    required = set()
    def include(tid):
        if tid in required: return
        required.add(tid)
        for dep in by.get(tid, {}).get('depends_on', []): include(dep)
    for tid in scope: include(tid)
    for tid in required:
        if by.get(tid, {}).get('status') != 'done': errors.append(f'{tid}: required release task unfinished or missing')
    for t in p.get('tasks', []):
        if t.get('id') not in required or t.get('status') != 'done': continue
        tid, rev = t['id'], t['revision']
        if any(by.get(d, {}).get('status') != 'done' for d in t['depends_on']): errors.append(f'{tid}: unfinished dependency')
        for test in t['required_tests']:
            matches = [r for r in p.get('receipts', []) if r.get('task_id') == tid and r.get('test') == test and r.get('revision') == rev]
            if not matches or matches[-1].get('status') != 'pass': errors.append(f'{tid}: no current passing receipt for {test}')
        eligible = [r for r in p.get('reviews', []) if r['task_id'] == tid and r['author'] == t['author'] and r['reviewer'] != t['author'] and r['subject_digest'] == rev]
        latest = {r['reviewer']: r for r in eligible}
        if not latest or any(r['verdict'] != 'pass' for r in latest.values()): errors.append(f'{tid}: independent exact revision review missing or failing')
        if level == 'reference':
            evidence_by = {e.get('id'): e for e in p.get('evidence', [])}
            links = t.get('evidence_ids', [])
            if not links or any(eid not in evidence_by or evidence_by[eid].get('status') not in {'observed', 'derived'} or evidence_by[eid].get('verified') is not True or not evidence_by[eid].get('reviewer') or evidence_by[eid].get('reviewer') == t['author'] for eid in links): errors.append(f'{tid}: verified task evidence missing')
        if level == 'reference':
            eligible_uat = [u for u in p.get('uat', []) if u['task_id'] == tid and u['revision'] == rev and u['reviewer'] != t['author']]
            latest_uat = {u['reviewer']: u for u in eligible_uat}
            if not latest_uat or any(u['status'] != 'pass' for u in latest_uat.values()): errors.append(f'{tid}: independent human UAT missing or failing')
    if level == 'reference':
        if not p.get('evidence'): errors.append('reference evidence missing')
        for e in p.get('evidence', []):
            if e.get('status') in {'observed', 'derived'} and (e.get('verified') is not True or not e.get('reviewer')): errors.append(f"{e.get('id', 'evidence')}: reviewer verification missing")
    return sorted(set(errors))

def privacy(directory):
    patterns = [re.compile(x, re.I) for x in (r'/' + r'Users/[^/\s]+', r'/' + r'home/[^/\s]+', r'[A-Z]:\\Users\\[^\\\s]+', r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----', r'gh[pousr]_[A-Za-z0-9]{20,}', r'sk-(?:proj-)?[A-Za-z0-9_-]{20,}', r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b')]
    unsafe = {'.blend', '.rom', '.sfc', '.smc', '.sav', '.env', '.pem', '.key', '.sqlite', '.db'}
    findings = []
    for f in sorted(Path(directory).rglob('*')):
        if f.is_symlink(): findings.append({'path': str(f.relative_to(directory)), 'reason': 'symlink requires manual review'}); continue
        if not f.is_file(): continue
        rel = str(f.relative_to(directory))
        if f.suffix.lower() in unsafe or f.name.startswith('.env'): findings.append({'path': rel, 'reason': 'unsafe artifact extension'})
        if f.stat().st_size > 2_000_000: findings.append({'path': rel, 'reason': 'large file not scanned'}); continue
        try: content = f.read_text(encoding='utf-8')
        except UnicodeDecodeError: findings.append({'path': rel, 'reason': 'binary requires manual review'}); continue
        for line, text in enumerate(content.splitlines(), 1):
            if any(p.search(text) for p in patterns): findings.append({'path': rel, 'line': line, 'reason': 'potential private data; value redacted'})
    return findings

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('init').add_argument('path')
    for command in ('validate', 'ready', 'dispatch', 'audit', 'propose-improvement'):
        q = sub.add_parser(command); q.add_argument('path')
        if command == 'dispatch': q.add_argument('task_id')
        if command == 'audit': q.add_argument('--level', choices=('prototype', 'reference'), default='prototype')
        if command == 'propose-improvement': q.add_argument('failure_id')
    sub.add_parser('privacy').add_argument('path')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            root = Path(args.path); root.mkdir(parents=True, exist_ok=True)
            p = {'schema_version': 1, 'max_workers': 2, 'tasks': [], 'release_tasks': [], 'evidence': [], 'receipts': [], 'reviews': [], 'uat': [], 'failures': []}
            target = root / 'project.json'
            with target.open('x') as f: json.dump(p, f, indent=2)
            result = {'ok': True, 'created': str(target), 'project': p}
        elif args.command == 'privacy':
            if not Path(args.path).is_dir(): raise ValueError('privacy target must be directory')
            findings = privacy(args.path); result = {'ok': not findings, 'findings': findings, 'limitation': 'Heuristics only; not a comprehensive privacy or security review.'}
        else:
            p = json.loads(Path(args.path).read_text()); errors = validate(p)
            result = {'ok': not errors, 'errors': errors}
            if not errors:
                if args.command == 'ready': result['ready'] = ready(p)
                elif args.command == 'audit':
                    result['errors'] = audit(p, args.level); result['ok'] = not result['errors']; result['level'] = args.level
                elif args.command == 'dispatch':
                    if args.task_id not in ready(p): raise ValueError('task is not schedulable now')
                    result['ticket'] = next(t for t in p['tasks'] if t['id'] == args.task_id); result['execution'] = 'planning only; no state mutation or tool execution'
                elif args.command == 'propose-improvement':
                    failure = next((f for f in p.get('failures', []) if f.get('id') == args.failure_id), None)
                    if failure is None: raise ValueError('unknown failure ID')
                    result['proposal'] = {'failure_id': args.failure_id, 'status': 'candidate', 'evidence': failure, 'required_gates': ['reproduce failure', 'add regression check', 'independent review', 'human approval'], 'automatic_application': False}
        print(json.dumps(result, indent=2)); return 0 if result['ok'] else 1
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as e:
        print(json.dumps({'ok': False, 'error': str(e)})); return 2

if __name__ == '__main__': sys.exit(main())
