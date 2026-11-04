#!/usr/bin/env python3
"""Check workshop links, lab order, images, and prose markers."""
import pathlib
import re
import subprocess
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
files = [ROOT / 'README.md', *sorted(ROOT.glob('lab-*/README.md')),
         ROOT / 'instructor-guide.md', ROOT / 'evidence-worksheet.md']
errors = []
for md in files:
    text = md.read_text()
    for token in ['\u2014', '\u2013', '\u2018', '\u2019', '\u201c', '\u201d',
                  'contentReference', 'oaicite', 'utm_source=']:
        if token in text:
            errors.append(f'{md.relative_to(ROOT)}: prohibited prose marker {token!r}')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            continue
        local = (md.parent / target.split('#')[0]).resolve()
        if not local.exists():
            errors.append(f'{md.relative_to(ROOT)}: missing {target}')
    steps = [int(x) for x in re.findall(r'^### Step (\d+):', text, re.M)]
    if steps != list(range(1, len(steps) + 1)):
        errors.append(f'{md.relative_to(ROOT)}: step order {steps}')
    for label, target in re.findall(r'\[(Lab \d+: [^\]]+)\]\(([^)]+)\)', text):
        dest = (md.parent / target).resolve()
        if dest.exists() and dest.read_text().splitlines()[0].lstrip('# ') != label:
            errors.append(f'{md.relative_to(ROOT)}: lab title mismatch')
for p in ROOT.glob('lab-*/images/*.png'):
    if Image.open(p).width <= 1400:
        errors.append(f'{p.relative_to(ROOT)}: screenshot width too small')
print(f'Checked {len(files)} Markdown files and {len(list(ROOT.glob("lab-*/images/*.png")))} screenshots.')
for error in errors:
    print(error)
if errors:
    sys.exit(1)
subprocess.run([sys.executable, str(ROOT / 'tools/build_pdf.py'), '--check'], check=True)
