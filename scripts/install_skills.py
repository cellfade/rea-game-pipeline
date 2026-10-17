#!/usr/bin/env python3
"""Copy portable skills to an explicitly selected discovery directory."""
import argparse
import filecmp
import json
from pathlib import Path
import shutil
import sys
import tempfile


def same_tree(a, b):
    left = sorted(str(p.relative_to(a)) for p in a.rglob('*'))
    right = sorted(str(p.relative_to(b)) for p in b.rglob('*'))
    if left != right or any(p.is_symlink() for p in b.rglob('*')):
        return False
    return all(not p.is_file() or filecmp.cmp(p, b / p.relative_to(a), shallow=False) for p in a.rglob('*'))


def install(source, destination, dry_run=False):
    source, destination = Path(source), Path(destination)
    if destination.is_symlink():
        raise ValueError('destination itself must not be a symlink')
    # Normalize host aliases once (some systems alias their temporary root).
    # This is a user-selected destination, not a filesystem sandbox.
    destination = destination.parent.resolve() / destination.name
    if destination.exists() and not destination.is_dir():
        raise ValueError('destination must be a directory')
    skills = sorted(p for p in source.iterdir() if p.is_dir())
    if not skills:
        raise ValueError('no skills found')
    plan = []
    for skill in skills:
        if skill.is_symlink() or any(p.is_symlink() for p in skill.rglob('*')):
            raise ValueError('source skills must not contain symlinks')
        if not (skill / 'SKILL.md').is_file():
            raise ValueError('skill entrypoint missing')
        target = destination / skill.name
        if target.exists() or target.is_symlink():
            if not target.is_dir() or target.is_symlink() or not same_tree(skill, target):
                raise ValueError('conflicting existing skill: ' + skill.name)
            action = 'unchanged'
        else:
            action = 'install'
        plan.append({'skill': skill.name, 'action': action})
    if not dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.skill-stage-', dir=destination) as temp:
            stage = Path(temp)
            for entry in plan:
                if entry['action'] == 'install':
                    shutil.copytree(source / entry['skill'], stage / entry['skill'])
            for entry in plan:
                if entry['action'] == 'install':
                    target = destination / entry['skill']
                    if target.exists() or target.is_symlink():
                        raise ValueError('destination changed during install; retry after review')
                    (stage / entry['skill']).rename(target)
    return {'ok': True, 'dry_run': dry_run, 'plan': plan,
            'limit': 'Sequential installer; do not run concurrent writers against the same destination.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1] / 'skills', Path(args.dest).expanduser(), args.dry_run)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}))
        return 1

if __name__ == '__main__':
    sys.exit(main())
