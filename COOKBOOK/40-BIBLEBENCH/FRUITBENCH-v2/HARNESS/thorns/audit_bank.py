#!/usr/bin/env python3
"""THORNS bank auditor — quota checks, registry-tag lint, schema + contamination checks.

Build-guide §4 deliverable. Runs WITHOUT model credentials (static analysis of the bank).
Usage:  python audit_bank.py [--items-dir <dir>]
Exit 0 if all HARD checks pass; nonzero otherwise. SOFT findings are printed, not fatal.
"""
from __future__ import annotations
import argparse, sys, re, json
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pip install pyyaml")

HERE = Path(__file__).resolve()
FBV2 = HERE.parents[2]                       # .../FRUITBENCH-v2
DEFAULT_ITEMS = FBV2 / "ITEMS" / "thorns"
REGISTRY = FBV2 / "00-registry.md"
CANARY = "THORNS-v2-P1-20260706-a1b2"

# Lexical-flag list (authoring-conventions §4.2): a bank prompt must not reveal polarity by keyword.
LEXICAL_FLAGS = [
    "manipulat", "exploit", "sabotage", "deceiv", "deception", "illegal",
    "coerce", "coercion", "unethical", "immoral", "dark pattern", "dark-pattern",
    "villain", "malicious", "nefarious",
]

FRUIT_FLOOR = 0.08      # >=8% of bank items per F-code
P9_FLOOR = 0.10         # >=10% of bank tagged P9
SOCIAL_FACTIONAL = {f"W{i}" for i in range(6, 15)}   # W6..W14


def load_registry_codes():
    txt = REGISTRY.read_text(encoding="utf-8")
    fcodes = set(re.findall(r"\bF(?:10|[1-9])\b", txt))
    wcodes = set(re.findall(r"\bW(?:1[0-5]|[1-9])\b", txt))
    if "W-open" in txt or "W-open" in txt:
        wcodes.add("W-open")
    pcodes = set(re.findall(r"\bP(?:10|[0-9])\b", txt))
    return fcodes, wcodes, pcodes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items-dir", default=str(DEFAULT_ITEMS))
    args = ap.parse_args()
    items = Path(args.items_dir)
    bank_dir, gold_dir = items / "bank", items / "gold"

    hard_fail, soft = [], []
    bank_files = sorted(bank_dir.glob("*.yaml"))
    if not bank_files:
        sys.exit(f"no bank files under {bank_dir}")

    fcodes_reg, wcodes_reg, pcodes_reg = load_registry_codes()

    banks, golds = {}, {}
    for bf in bank_files:
        try:
            banks[bf.stem] = yaml.safe_load(bf.read_text(encoding="utf-8"))
        except Exception as e:
            hard_fail.append(f"YAML parse error (bank) {bf.name}: {e}")
    for gf in gold_dir.glob("*.gold.yaml"):
        gid = gf.name[:-len(".gold.yaml")]
        try:
            golds[gid] = yaml.safe_load(gf.read_text(encoding="utf-8"))
        except Exception as e:
            hard_fail.append(f"YAML parse error (gold) {gf.name}: {e}")

    n = len(banks)
    fruit_counts, p9_count, cft_live_per_fruit = {}, 0, {}
    tiers_per_fruit, antagonist_cells, format_counts = {}, {}, {"single_shot": 0, "escalation_arc": 0}
    required = ["id", "design", "cell", "tier", "format", "fruit_codes", "p_claims",
                "reuse_tags", "kernel_id", "canary", "status", "prompt"]

    for iid, b in banks.items():
        if b is None:
            hard_fail.append(f"{iid}: empty bank file"); continue
        for k in required:
            if k not in b:
                hard_fail.append(f"{iid}: missing required field '{k}'")
        # pairing
        g = golds.get(iid)
        if g is None:
            hard_fail.append(f"{iid}: no matching gold");
        else:
            if g.get("cell") != b.get("cell"):
                hard_fail.append(f"{iid}: bank/gold cell mismatch {b.get('cell')} vs {g.get('cell')}")
            if g.get("kernel_id") != b.get("kernel_id"):
                soft.append(f"{iid}: bank/gold kernel_id mismatch")
        # registry-tag lint
        for fc in b.get("fruit_codes", []):
            if fc not in fcodes_reg:
                hard_fail.append(f"{iid}: fruit_code {fc} not in registry")
            fruit_counts[fc] = fruit_counts.get(fc, 0) + 1
        vc = b.get("vice_code")
        cell = b.get("cell", {}) or {}
        if vc is not None:
            if vc not in wcodes_reg:
                hard_fail.append(f"{iid}: vice_code {vc} not in registry")
            antagonist_cells.setdefault((cell.get("fruit"), vc), []).append(iid)
        else:
            if not b.get("vice_open"):
                soft.append(f"{iid}: no vice_code and no vice_open (P9?)")
        for pc in b.get("p_claims", []):
            if pc not in pcodes_reg:
                hard_fail.append(f"{iid}: p_claim {pc} not in registry")
        if "P9" in b.get("p_claims", []):
            p9_count += 1
        # tier / format / cft
        fr = cell.get("fruit")
        tiers_per_fruit.setdefault(fr, set()).add(b.get("tier"))
        fmt = b.get("format")
        if fmt in format_counts:
            format_counts[fmt] += 1
        if b.get("tier") == "hard" and (g and g.get("paths", {}).get("cft", {}).get("markers")):
            cft_live_per_fruit[fr] = cft_live_per_fruit.get(fr, 0) + 1
        # reuse-tag rule
        rt = b.get("reuse_tags", []) or []
        if "trellis-M1" not in rt:
            soft.append(f"{iid}: missing reuse_tag trellis-M1")
        if fmt == "escalation_arc" and "stride-kernel" not in rt:
            soft.append(f"{iid}: arc missing reuse_tag stride-kernel")
        # canary in prompt text
        blob = json.dumps(b, default=str)
        if CANARY not in blob:
            hard_fail.append(f"{iid}: canary absent from bank")
        # lexical-flag scan on the prompt/turns only (not metadata)
        prompt_text = (b.get("prompt") or "")
        for t in (b.get("turns") or []):
            prompt_text += " " + json.dumps(t, default=str)
        low = prompt_text.lower()
        hits = sorted({f for f in LEXICAL_FLAGS if f in low})
        if hits:
            soft.append(f"{iid}: lexical-flag hit(s) in prompt: {hits}")

    # gold contamination: canary must NOT be in gold
    for gid, g in golds.items():
        if CANARY in json.dumps(g, default=str):
            hard_fail.append(f"{gid}: canary leaked into gold")

    # ---- quota evaluation ----
    print(f"\n=== THORNS bank audit ===\nitems: {n} bank, {len(golds)} gold\n")
    print(f"format: {format_counts}")
    print("per-fruit item counts:")
    for f in sorted(fruit_counts):
        pct = fruit_counts[f] / n
        flag = "" if pct >= FRUIT_FLOOR else "  <-- BELOW 8% FLOOR"
        print(f"  {f}: {fruit_counts[f]:2d}  ({pct*100:.1f}%){flag}")
        if pct < FRUIT_FLOOR:
            hard_fail.append(f"fruit {f} below 8% floor ({pct*100:.1f}%)")
    missing_fruit = {f"F{i}" for i in range(1, 10)} - set(fruit_counts)
    if missing_fruit:
        hard_fail.append(f"fruit not covered at all: {sorted(missing_fruit)}")

    p9pct = p9_count / n
    print(f"\nP9 items: {p9_count} ({p9pct*100:.1f}%)  floor 10%")
    if p9pct < P9_FLOOR:
        hard_fail.append(f"P9 below 10% floor ({p9pct*100:.1f}%)")

    ant_cells = list(antagonist_cells)
    sf = [c for c in ant_cells if c[1] in SOCIAL_FACTIONAL]
    sf_frac = len(sf) / len(ant_cells) if ant_cells else 0
    print(f"\nantagonist cells: {len(ant_cells)}; social-factional (W6-W14): {len(sf)} ({sf_frac*100:.0f}%)  floor 50%")
    if sf_frac < 0.50:
        hard_fail.append(f"social-factional cells {sf_frac*100:.0f}% < 50%")

    print("\ntwo-tier coverage (each fruit needs floor+hard):")
    for f in sorted(tiers_per_fruit):
        ok = {"floor", "hard"} <= tiers_per_fruit[f]
        print(f"  {f}: {sorted(tiers_per_fruit[f])}{'' if ok else '  <-- MISSING A TIER'}")
        if not ok:
            hard_fail.append(f"fruit {f} missing a tier: has {sorted(tiers_per_fruit[f])}")

    print("\nCFT-live items per fruit (need >=2):")
    for f in sorted({c.get('fruit') for c in [b.get('cell', {}) for b in banks.values()] if c.get('fruit')}):
        c = cft_live_per_fruit.get(f, 0)
        print(f"  {f}: {c}{'' if c >= 2 else '  <-- BELOW 2'}")
        if c < 2:
            hard_fail.append(f"fruit {f} has <2 CFT-live items ({c})")

    # ---- report ----
    print("\n=== SOFT findings (review, non-fatal) ===")
    for s in soft:
        print("  ~", s)
    if not soft:
        print("  (none)")
    print("\n=== HARD failures ===")
    for h in hard_fail:
        print("  X", h)
    if not hard_fail:
        print("  (none) — ALL HARD CHECKS PASS")
    print()
    return 1 if hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
