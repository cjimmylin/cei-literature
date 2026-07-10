#!/usr/bin/env python3
"""Extract compact question format for manual evaluation."""
from __future__ import annotations
import json, re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SAMPLE = BASE / "trials" / "20260404-trial-T2-sample-30.json"

# Map Arabic share terms to short labels
SHARE_MAP = {
    "النصف": "1/2",
    "الثلث": "1/3",
    "السدس": "1/6",
    "الربع": "1/4",
    "الثمن": "1/8",
    "الثلثان": "2/3",
    "باقي التركة": "remainder",
    "باقى التركة": "remainder",
    "لا شيء": "nothing",
    "محجوب": "blocked",
    "عصبة": "asaba",
    "كل التركة": "all",
}

def extract_share(option_text: str) -> str:
    """Extract the share designation from option text."""
    # Pattern: نصيبه هو X، والدليل:
    m = re.search(r'نصيبه هو (.+?)،', option_text)
    if m:
        raw = m.group(1).strip()
        return SHARE_MAP.get(raw, raw)
    return option_text[:30]

with open(SAMPLE, encoding="utf-8") as f:
    items = json.load(f)

for item in items:
    # Extract target heir from question
    q = item["question"]
    # Pattern: كم النصيب الأصلي لـ X من التركة
    target_m = re.search(r'لـ\s*(.+?)\s*من التركة', q)
    target = target_m.group(1) if target_m else "?"

    # Extract heir list from question
    # Pattern: مات وترك: X كم
    heirs_m = re.search(r'مات وترك:\s*(.+?)\s*كم', q)
    heirs = heirs_m.group(1) if heirs_m else "?"

    # For Advanced items, question pattern may differ
    if "كم عدد" in q or "كم نصيب" in q:
        # Advanced calculation question
        calc_m = re.search(r'كم\s+(.+?)$', q)
        calc_type = calc_m.group(1)[:80] if calc_m else q[-80:]
    else:
        calc_type = ""

    # Extract short options
    opts = {}
    for letter, text in item["options"].items():
        opts[letter] = extract_share(text)

    print(f"#{item['index']:2d} [{item['level'][:3]}] Gold={item['gold']}")
    print(f"  Heirs: {heirs[:120]}")
    print(f"  Target: {target}")
    if calc_type:
        print(f"  Calc: {calc_type}")
    print(f"  Options: {' | '.join(f'{k}={v}' for k,v in opts.items())}")
    print()
