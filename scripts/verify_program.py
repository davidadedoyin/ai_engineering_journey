#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []

week_dirs = sorted((root / 'weeks').glob('week_*'))
if len(week_dirs) < 24:
    errors.append(f'Expected at least 24 week folders, found {len(week_dirs)}')
for d in week_dirs:
    if not (d / 'README.md').exists():
        errors.append(f'Missing README in {d.name}')

portfolio = [
    'month1_expense_tracker',
    'month2_titanic_eda',
    'month3_titanic_api',
    'month4_sentiment_api',
    'month5_smart_reply_assistant',
    'month6_rag_faq_bot',
]
for name in portfolio:
    project_path = root / 'projects' / name
    if not project_path.exists():
        errors.append(f'Missing project folder: {name}')
        continue
    if not (project_path / 'README.md').exists():
        errors.append(f'Missing README in {project_path}')
    content = (project_path / 'README.md').read_text(encoding='utf-8', errors='ignore')
    if 'Limitations' not in content:
        errors.append(f'No Limitations section in {project_path / "README.md"}')

if subprocess.run(['git', '-C', str(root), 'ls-files', '--error-unmatch', '.env'], capture_output=True, text=True).returncode == 0:
    errors.append('.env is tracked by Git')

secret_pattern = re.compile(r'(?:AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]+|AIza[0-9A-Za-z\-_]{35})')
for path in root.rglob('*'):
    if path.is_dir() or path.name in {'.git', '.gitignore', '.env.example'}:
        continue
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    if secret_pattern.search(text):
        errors.append(f'Possible secret-like text found in {path.relative_to(root)}')

print('Verification summary')
print(f'Week folders found: {len(week_dirs)}')
print(f'Projects found: {len([p for p in (root / "projects").iterdir() if p.is_dir()])}')
if errors:
    print('FAIL')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)
print('PASS')
print('No obvious structural issues found.')
