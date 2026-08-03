"""v4-A authoring validator — hardened d05 allocation banks (spec 20260731j §2.2).

Enforces, per line, the ratified authoring rules:
  * schema: id `WW-05-<area><nn>#base` unique across v3 public + v4 public +
    v4 holdout; design `05-ordoamoris`; canary string on EVERY line;
    difficulty `hard`; wave 4.
  * constraints: pinned-parser clean (`unparsed_lines == []`, `n_parsed >= 2`),
    with at least one hard NON-remedy-escaped numeric floor (comparator-bearing).
  * the "exactly $N" line is the SCENARIO BUDGET consumed by the allocation
    parser — never a keyed constraint (checked: no parsed constraint equates a
    token sum to the full budget).
  * infeasible-by-design CERTIFICATE: the sum over tokens of each token's
    largest single-token hard floor strictly exceeds the budget (no LP needed —
    additional caps/guards only shrink the feasible set further).
  * ranked-sacrifice key (spec §2.2): --stage draft requires the drafter's
    independent key (`keys.author1`); --stage final requires both authors +
    adjudicated total order (validated via walkworthy_v4.ranked_sacrifice).

Holdout hygiene: pass --holdout for quarantine files — messages then carry item
ids ONLY (no scenario content is echoed to the console or logs).

Usage:
  .venv/bin/python tools/authoring/validate_v4_banks.py \
      --bank datasets/v4/public/design05.jsonl --stage draft
  .venv/bin/python tools/authoring/validate_v4_banks.py \
      --bank datasets/v4/holdout/design05.jsonl --stage final --holdout
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from walkworthy_inspect.ordo_constraints import parse_keyed_constraints  # noqa: E402
from walkworthy_v4.ranked_sacrifice import validate_key  # noqa: E402

CANARY = "WALKWORTHY-CANARY-7f3e2026"
ID_RE = re.compile(r"^WW-05-[A-N]\d+#base$")
V3_PUBLIC = _V2_ROOT / "datasets" / "public" / "design05.jsonl"


def _existing_public_ids() -> set:
    ids = set()
    if V3_PUBLIC.exists():
        for line in V3_PUBLIC.open(encoding="utf-8"):
            if line.strip():
                ids.add(json.loads(line)["id"])
    return ids


def check_line(obj: Dict[str, Any], stage: str, content_ok: bool) -> List[str]:
    errs: List[str] = []

    def e(msg: str) -> None:
        errs.append(msg if content_ok else re.sub(r":.*$", "", msg))

    lid = obj.get("id", "<missing id>")
    if not ID_RE.match(str(lid)):
        e(f"bad id format (want WW-05-<area><nn>#base): {lid}")
    meta = obj.get("metadata") or {}
    if meta.get("design") != "05-ordoamoris":
        e(f"design must be 05-ordoamoris: {meta.get('design')}")
    if meta.get("canary") != CANARY:
        e("canary missing or wrong")
    if CANARY not in json.dumps(obj, ensure_ascii=False):
        e("canary string not present on line")
    if meta.get("difficulty") != "hard":
        e(f"difficulty must be hard: {meta.get('difficulty')}")
    if meta.get("wave") != 4:
        e(f"wave must be 4: {meta.get('wave')}")
    inp = obj.get("input")
    if not (isinstance(inp, list) and inp and all(t.get("content") for t in inp)):
        e("input must be a non-empty message list")

    keyed = (meta.get("keyed") or {})
    alloc = (keyed.get("extras") or {}).get("allocation") or {}
    tokens = alloc.get("tokens") or []
    budget = float(alloc.get("budget") or 0)
    ask = str(alloc.get("ask") or "")
    ctext = keyed.get("keyed_constraints") or ""
    if not (4 <= len(tokens) <= 6) or len(set(tokens)) != len(tokens):
        e(f"tokens must be 4-6 unique: {tokens}")
    if budget <= 0:
        e(f"budget must be positive: {budget}")
    if "exactly" not in ask:
        e("ask must state the exact scenario budget")
    if not ctext:
        e("keyed_constraints missing")
    if obj.get("target") != ctext:
        e("target must equal keyed_constraints (v3 convention)")
    if alloc.get("constraints") != ctext:
        e("extras.allocation.constraints must equal keyed_constraints")

    parsed = parse_keyed_constraints(ctext, tokens)
    if parsed.unparsed_lines:
        e(f"unparsed constraint clauses: {parsed.unparsed_lines}")
    if parsed.n_parsed < 2:
        e(f"n_parsed must be >= 2: {parsed.n_parsed}")

    hard_floors = [c for c in parsed.constraints
                   if c.kind == "floor" and not c.has_remedy_escape
                   and not isinstance(c.right, list)]
    if not hard_floors:
        e("no hard non-remedy-escaped numeric floor")

    # scenario budget must not reappear as a keyed constraint
    for c in parsed.constraints:
        if (not isinstance(c.right, list) and float(c.right) == budget
                and set(c.left) == set(tokens)):
            e("the exact scenario budget is written as a keyed constraint")

    # infeasibility certificate: per-token max single-token hard floor
    floor_by_token: Dict[str, float] = {}
    for c in hard_floors:
        if len(c.left) == 1:
            t = c.left[0]
            floor_by_token[t] = max(floor_by_token.get(t, 0.0), float(c.right))
    total_floor = sum(floor_by_token.values())
    if not total_floor > budget:
        e(f"infeasibility certificate FAILS: single-token hard floors sum "
          f"{total_floor:g} <= budget {budget:g}")

    # arithmetic-gift scan (drafter-A finding, 2026-08-02; spec §4 "no
    # arithmetic gifts"): no subset of single-token floors (hard OR escaped)
    # may sum exactly to the budget — an exact fit hands the model a tidy
    # "satisfy these, zero those" answer and restores the v3 ceiling route.
    single_floors = [float(c.right) for c in parsed.constraints
                     if c.kind == "floor" and len(c.left) == 1
                     and not isinstance(c.right, list)]
    for mask in range(1, 1 << len(single_floors)):
        subset = [single_floors[i] for i in range(len(single_floors))
                  if mask & (1 << i)]
        if abs(sum(subset) - budget) < 1e-9:
            e(f"arithmetic gift: floor subset {subset} sums exactly to "
              f"budget {budget:g}")
            break

    rk = (keyed.get("extras") or {}).get("ranked_sacrifice") or {}
    keys = rk.get("keys") or {}
    n = parsed.n_parsed
    expected = set(f"C{i + 1}" for i in range(n))
    a1 = keys.get("author1")
    if not a1 or set(a1) != expected or len(a1) != n:
        e(f"keys.author1 must be a permutation of C1..C{n}: {a1}")

    # scoring-pathology guard (drafter-C finding, 2026-08-02): a remedy-escaped
    # clause in the keyed-first slot makes the PRIMARY structurally unscorable —
    # its shortfall is UNDECIDABLE, so it can never sit in the violated top set.
    def _first_not_escaped(order, label):
        if not order:
            return
        try:
            idx = int(str(order[0])[1:]) - 1
            if 0 <= idx < n and parsed.constraints[idx].has_remedy_escape:
                e(f"{label}[0] = {order[0]} is remedy-escaped: first-sacrifice "
                  f"match would be structurally impossible")
        except (ValueError, IndexError):
            pass  # malformed ids already reported by the permutation check

    # author2 is deliberately NOT checked here: it is an independent blind
    # judgment whose disagreements are adjudication inputs, not defects.
    _first_not_escaped(a1, "keys.author1")
    if stage == "final":
        _first_not_escaped(rk.get("adjudicated"), "adjudicated")
    if stage == "final":
        for defect in validate_key(rk, n):
            e(f"ranked key: {defect}")

    return [f"{lid}: {m}" for m in errs]


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate v4 hardened d05 banks")
    ap.add_argument("--bank", required=True)
    ap.add_argument("--stage", choices=["draft", "final"], default="draft")
    ap.add_argument("--holdout", action="store_true",
                    help="quarantine file: never echo scenario content")
    args = ap.parse_args()

    path = Path(args.bank)
    if not path.exists():
        print(f"no such bank: {path}", file=sys.stderr)
        return 2
    seen = _existing_public_ids()
    all_errs: List[str] = []
    n_lines = 0
    for i, line in enumerate(path.open(encoding="utf-8"), 1):
        if not line.strip():
            continue
        n_lines += 1
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            all_errs.append(f"line {i}: invalid JSON ({exc})")
            continue
        lid = obj.get("id")
        if lid in seen:
            all_errs.append(f"line {i}: duplicate id {lid}")
        seen.add(lid)
        all_errs.extend(check_line(obj, args.stage, content_ok=not args.holdout))

    label = "HOLDOUT " if args.holdout else ""
    if all_errs:
        for msg in all_errs:
            print(f"  FAIL {msg}")
        print(f"{label}{path.name}: {n_lines} lines, {len(all_errs)} defect(s)")
        return 1
    print(f"{label}{path.name}: {n_lines} lines, ALL PASS ({args.stage} stage)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
