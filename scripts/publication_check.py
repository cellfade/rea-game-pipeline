#!/usr/bin/env python3
"""Allowlist publication staging plus heuristic privacy checks. No network access."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {'skills', 'harness', 'scripts', 'tests', 'docs', 'evals', 'examples', '.github'}
FILES = {'README.md', 'LICENSE', 'VERSION', 'AGENTS.md', 'CONTRIBUTING.md', 'SECURITY.md', 'THIRD_PARTY.md', '.gitignore'}
SUFFIXES = {'.md', '.py', '.json', '.txt', '.yml', '.yaml'}
IGNORED = {'.git', '__pycache__', '.venv'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export', help='New directory outside this checkout; refuses overwrite')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('pipeline', ROOT / 'harness/pipeline.py')
    pipeline = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pipeline)
    errors, files = [], []
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in IGNORED for part in rel.parts): continue
        if path.is_symlink():
            errors.append({'path': str(rel), 'reason': 'symlink rejected'}); continue
        if not path.is_file(): continue
        skill_license = len(rel.parts) == 3 and rel.parts[0] == 'skills' and rel.name == 'LICENSE'
        allowed = (len(rel.parts) == 1 and rel.name in FILES) or (rel.parts[0] in DIRECTORIES and path.suffix in SUFFIXES) or skill_license
        if not allowed:
            errors.append({'path': str(rel), 'reason': 'not on public allowlist'}); continue
        files.append(rel)
    with tempfile.TemporaryDirectory(prefix='pipeline-public-review-') as temp:
        stage = Path(temp)
        for rel in files:
            (stage / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, stage / rel)
        errors.extend(pipeline.privacy(stage))
        if args.export and not errors:
            dest = Path(args.export).expanduser().resolve()
            if dest == ROOT or ROOT in dest.parents: raise ValueError('export must be outside checkout')
            if dest.exists(): raise ValueError('export destination exists')
            shutil.copytree(stage, dest)
    print(json.dumps({'ok': not errors, 'files': len(files), 'findings': errors,
                      'limitations': 'Allowlist and heuristics; manual content, provenance and Git-history review still required.'}, indent=2))
    return bool(errors)

if __name__ == '__main__':
    try: sys.exit(main())
    except (OSError, ValueError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)})); sys.exit(2)
