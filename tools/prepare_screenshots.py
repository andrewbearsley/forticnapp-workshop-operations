#!/usr/bin/env python3
"""Redact screenshot text regions and add selected control callouts."""
import argparse
import json
import pathlib
import re
import subprocess

from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
SENSITIVE = re.compile(
    r"@|arn:|\b\d{12}\b|\b(?:\d{1,3}\.){3}\d{1,3}\b|"
    r"\bip-\d|\bi-[0-9a-f]{8,}\b|(?:FORTINET|FORTIDEM)_[A-Z0-9]+|"
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.I,
)


def rectangle(row, pad=3):
    return (int(row['x']) - pad, int(row['y']) - pad,
            int(row['x'] + row['w']) + pad, int(row['y'] + row['h']) + pad)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=pathlib.Path, required=True)
    parser.add_argument('--ocr', required=True)
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'tools/screenshots.json').read_text())
    for item in manifest:
        if item['tenant'] != 'FORTIDEMO-2026-04':
            raise ValueError('All screenshots must use the demo tenant.')
        src = args.source / item['source']
        rows = json.loads(subprocess.check_output([args.ocr, str(src)]))
        im = Image.open(src).convert('RGB')
        assert im.width > 1400, src
        draw = ImageDraw.Draw(im)
        redactions = []
        for row in rows:
            if SENSITIVE.search(row['text']) or any(
                text.lower() in row['text'].lower() for text in item.get('redact', [])
            ):
                box = rectangle(row)
                draw.rectangle(box, fill='black')
                redactions.append(box)
        for label in item.get('callouts', []):
            matches = [r for r in rows if r['text'].strip().lower() == label.lower()]
            if not matches:
                raise ValueError(f'Callout label absent: {src.name}: {label}')
            draw.rounded_rectangle(rectangle(matches[0], 7), radius=4,
                                   outline='#FF2D95', width=3)
        for box in item.get('boxes', []):
            draw.rounded_rectangle(tuple(box), radius=4, outline='#FF2D95', width=3)
        dest = ROOT / item['output']
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest)
        for attempt in range(4):
            checked = json.loads(subprocess.check_output([args.ocr, str(dest)]))
            leaks = [r for r in checked if SENSITIVE.search(r['text'])]
            if not leaks:
                break
            for row in leaks:
                box = rectangle(row, 5)
                draw.rectangle(box, fill='black')
                redactions.append(box)
            im.save(dest)
        else:
            raise ValueError(f'Sensitive text remains in {dest.name}; inspect locally.')
        print(f'{dest.relative_to(ROOT)}: {len(redactions)} redacted regions', flush=True)


if __name__ == '__main__':
    main()
