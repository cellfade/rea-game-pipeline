#!/usr/bin/env python3
"""Structural package checks; not a full YAML parser or behavioral evaluator."""
from pathlib import Path
import json
import re
import sys
root = Path(__file__).resolve().parents[1]
errors = []
for folder in sorted((root / 'skills').iterdir()):
    if not folder.is_dir(): continue
    text = (folder / 'SKILL.md').read_text()
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        errors.append(folder.name + ': frontmatter missing'); continue
    front = text.split('---', 2)[1]
    name = re.search(r'^name:\s*(.+)$', front, re.M)
    desc = re.search(r'^description:\s*(.+)$', front, re.M)
    if not name or name.group(1).strip(' "\'') != folder.name: errors.append(folder.name + ': name mismatch')
    if not desc or not 1 <= len(desc.group(1)) <= 1024: errors.append(folder.name + ': description missing/oversized')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not (folder / target.split('#')[0]).is_file(): errors.append(folder.name + ': broken reference')
    meta = folder / 'agents/openai.yaml'
    if not meta.is_file() or '$' + folder.name not in meta.read_text(): errors.append(folder.name + ': invocation metadata missing')
for required in ['LICENSE', 'README.md', 'VERSION', 'harness/pipeline.py', 'docs/workflow.md', 'evals/scenarios.json']:
    if not (root / required).is_file(): errors.append('missing ' + required)
for document in [root / 'README.md', *(root / 'docs').glob('*.md')]:
    for target in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        if '://' not in target and not target.startswith('#') and not (document.parent / target.split('#')[0]).is_file():
            errors.append(str(document.relative_to(root)) + ': broken reference ' + target)
print(json.dumps({'ok': not errors, 'errors': errors, 'scope': 'Structure and internal references only'}, indent=2))
sys.exit(bool(errors))
