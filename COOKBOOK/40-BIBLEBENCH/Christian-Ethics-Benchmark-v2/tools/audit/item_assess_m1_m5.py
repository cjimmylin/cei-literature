"""
item_assess_m1_m5.py — WALKWORTHY v2 item assessment: M1 defect scan + M5 coverage.

WALKWORTHY-CANARY-7f3e2026

Usage:
    WALKWORTHY_ALLOW_HOLDOUT=1 python tools/audit/item_assess_m1_m5.py

Reads:
    datasets/public/design01..10.jsonl  (always)
    datasets/holdout/design01..10.jsonl (only if WALKWORTHY_ALLOW_HOLDOUT=="1")

Outputs (all under logs/item-assessment-20260718/):
    m1-defects-public.json
    m1-defects-holdout.json
    m5-coverage-public.json
    m5-coverage-holdout.json
    m1-m5-summary.md
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

CANARY = "WALKWORTHY-CANARY-7f3e2026"
CANARY_COMMENT = "# " + CANARY

V2 = Path(__file__).resolve().parent.parent.parent
PUBLIC_DIR = V2 / "datasets" / "public"
HOLDOUT_DIR = V2 / "datasets" / "holdout"
OUTPUT_DIR = V2 / "logs" / "item-assessment-20260718"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DESIGN_NAMES = [f"{i:02d}" for i in range(1, 11)]

# Required top-level fields
REQUIRED_TOPLEVEL = {"id", "input", "target", "metadata"}

# Required metadata fields
REQUIRED_META = {
    "item_id", "design", "admin", "pair_id", "area", "stratum",
    "tier", "difficulty", "anchors", "runnable", "review_status",
    "canary", "keyed",
}

# id format: WW-DD-LNN#suffix  (DD=2 digits, L=letter, NN=digits, suffix=non-whitespace)
ID_PATTERN = re.compile(r"^WW-\d{2}-[A-Z]\d+(?:-P)?#\S+$")

# Designs with paired admins and their expected admin sets (for runnable items)
# pair_id not null means paired; we check completeness within pair groups
# Design 01: no pair_id (single admin "base" / exemplar "base-exemplar")
# Design 02: pair_id=item_id; admins: base (multiturn), cold_open (single-turn)
# Design 03: pair_id=item_id; admins: say, do
# Design 04: pair_id=item_id; admins: alpha, beta (base is unpaired)
# Design 05: no pair_id (single admin "base")
# Design 06: no pair_id (single admin "base")
# Design 07: no pair_id (single admin "base", multiturn)
# Design 08: pair_id=item_id; admins: covert, overt
# Design 09: pair_id=item_id; admins: seat_A, seat_B (+ arbiter for some, seat_C rare)
# Design 10: pair_id=item_id; admins: N, U

# Designs that require multiturn metadata on runnable items
MULTITURN_DESIGNS = {"02", "07"}

VALID_STRATA = {"a", "c"}


def is_empty_or_whitespace(val: Any) -> bool:
    if val is None:
        return True
    if isinstance(val, str):
        return val.strip() == ""
    return False


def is_empty_keyed(keyed: Any, design: str) -> bool:
    """Check if keyed field is effectively empty (the '(no keyed text)' defect class).

    The defect manifests as keyed == {'keyed': ''} (empty string value).
    For design07 the known defect items are WW-07-L02, WW-07-I04, WW-07-F02.
    """
    if keyed is None:
        return True
    if isinstance(keyed, str) and keyed.strip() == "":
        return True
    if isinstance(keyed, dict):
        # Empty dict
        if len(keyed) == 0:
            return True
        # All string values empty
        all_empty = all(
            isinstance(v, str) and v.strip() == ""
            for v in keyed.values()
        )
        if all_empty:
            return True
    return False


def has_no_keyed_text_literal(line_raw: str) -> bool:
    """Check for the literal '(no keyed text)' string anywhere in the JSON line."""
    return "(no keyed text)" in line_raw.lower()


def audit_input(input_field: Any) -> list[str]:
    """Return list of defect codes for input field.

    Per convert_banks.py (line 123): system message is OPTIONAL (only emitted when
    admin.system is non-empty). Many designs legitimately have user-only input.
    Defect = empty input list OR no user message at all.
    """
    codes = []
    if not isinstance(input_field, list) or len(input_field) == 0:
        codes.append("INPUT_MISSING")
        return codes
    roles = [m.get("role") for m in input_field if isinstance(m, dict)]
    if "user" not in roles:
        codes.append("INPUT_NO_USER")
    return codes


def extract_design_code(design_str: str) -> str:
    """Extract 2-digit design code from design field like '01-goodsamaritan'."""
    if design_str and len(design_str) >= 2:
        return design_str[:2]
    return design_str


def scan_surface(surface: str, data_dir: Path) -> tuple[list[dict], dict]:
    """
    Scan all 10 JSONL files for a surface (public or holdout).

    Returns:
        (all_defect_records, coverage_data)
    """
    all_lines = []        # list of (line_obj, raw_str, filename)
    parse_errors = []

    for dname in DESIGN_NAMES:
        fpath = data_dir / f"design{dname}.jsonl"
        if not fpath.exists():
            # Missing file is a defect at surface level
            parse_errors.append({"file": str(fpath), "error": "FILE_MISSING"})
            continue
        with open(fpath, "r", encoding="utf-8") as fh:
            for lineno, raw in enumerate(fh, 1):
                raw = raw.rstrip("\n")
                if not raw.strip():
                    continue
                try:
                    obj = json.loads(raw)
                    all_lines.append((obj, raw, f"design{dname}.jsonl", lineno))
                except json.JSONDecodeError as e:
                    parse_errors.append({
                        "file": f"design{dname}.jsonl",
                        "lineno": lineno,
                        "error": f"JSON_PARSE_ERROR: {e}",
                    })

    # ---- M1: defect scan ----
    defect_records = []   # per item_id, aggregated
    id_counts: Counter = Counter()
    # Track line-level ids for uniqueness
    seen_ids: dict[str, str] = {}  # id -> filename#lineno

    item_admins: dict[str, list[tuple]] = defaultdict(list)
    # pair_id -> list of (admin, item_id, runnable)
    pair_groups: dict[str, list[tuple]] = defaultdict(list)

    for obj, raw, fname, lineno in all_lines:
        loc = f"{fname}:{lineno}"
        item_defects: list[str] = []
        detail_parts: list[str] = []

        # 1. Required top-level fields
        missing_tl = REQUIRED_TOPLEVEL - set(obj.keys())
        if missing_tl:
            item_defects.append("MISSING_TOPLEVEL")
            detail_parts.append(f"missing_toplevel={sorted(missing_tl)}")

        # 2. Required metadata fields
        meta = obj.get("metadata", {})
        if not isinstance(meta, dict):
            item_defects.append("METADATA_NOT_DICT")
            detail_parts.append("metadata is not a dict")
            meta = {}
        else:
            missing_meta = REQUIRED_META - set(meta.keys())
            if missing_meta:
                item_defects.append("MISSING_META")
                detail_parts.append(f"missing_meta={sorted(missing_meta)}")

        item_id = meta.get("item_id", "UNKNOWN")
        design_full = meta.get("design", "")
        design_code = extract_design_code(design_full)
        admin = meta.get("admin", "")
        pair_id = meta.get("pair_id")
        runnable = meta.get("runnable", None)
        item_admins[item_id].append((admin, fname, lineno, runnable))

        if pair_id is not None:
            pair_groups[pair_id].append((admin, item_id, runnable))

        # 3. Canary check
        line_canary = meta.get("canary")
        if line_canary != CANARY:
            item_defects.append("CANARY_MISMATCH")
            detail_parts.append(f"canary={repr(line_canary)}")

        # 4. ID format
        line_id = obj.get("id", "")
        if not ID_PATTERN.match(str(line_id)):
            item_defects.append("ID_FORMAT")
            detail_parts.append(f"id={repr(line_id)}")

        # 5. ID uniqueness
        if line_id in seen_ids:
            item_defects.append("ID_DUPLICATE")
            detail_parts.append(f"dup_of={seen_ids[line_id]}")
        else:
            seen_ids[line_id] = loc
        id_counts[line_id] += 1

        # 6. Empty target
        target = obj.get("target", "")
        if is_empty_or_whitespace(target):
            item_defects.append("TARGET_EMPTY")

        # 7. Keyed empty / no-keyed-text defect
        keyed = meta.get("keyed")
        if is_empty_keyed(keyed, design_code):
            item_defects.append("KEYED_EMPTY")
            detail_parts.append(f"keyed={repr(keyed)}")

        # 8. Literal "(no keyed text)" anywhere in the raw line
        if has_no_keyed_text_literal(raw):
            item_defects.append("NO_KEYED_TEXT_LITERAL")

        # 9. Empty anchors list
        anchors = meta.get("anchors")
        if isinstance(anchors, list) and len(anchors) == 0:
            item_defects.append("ANCHORS_EMPTY")
        elif not isinstance(anchors, (list, type(None))):
            item_defects.append("ANCHORS_NOT_LIST")

        # 10. Input sanity
        input_codes = audit_input(obj.get("input"))
        item_defects.extend(input_codes)

        # 11. Multiturn: required for designs 02 and 07 on runnable items
        if design_code in MULTITURN_DESIGNS and runnable:
            multiturn = meta.get("multiturn")
            # design02: base admin has multiturn; cold_open does not (single-turn ablation)
            # design07: all runnable items should have multiturn
            if design_code == "07":
                if multiturn is None:
                    item_defects.append("MULTITURN_MISSING")
            elif design_code == "02":
                if admin == "base" and multiturn is None:
                    item_defects.append("MULTITURN_MISSING")

        # 12. Stratum validity
        stratum = meta.get("stratum")
        if stratum not in VALID_STRATA:
            item_defects.append("STRATUM_INVALID")
            detail_parts.append(f"stratum={repr(stratum)}")

        if item_defects:
            defect_records.append({
                "item_id": item_id,
                "id": line_id,
                "design": design_full,
                "admin": admin,
                "runnable": runnable,
                "file": fname,
                "lineno": lineno,
                "defect_codes": item_defects,
                "detail": "; ".join(detail_parts) if detail_parts else "",
            })

    # ---- Pair integrity ----
    pair_defects = []
    # For paired designs, group by pair_id and check completeness
    # Expected pair members per design (runnable admins only):
    #   02: {base, cold_open}
    #   03: {say, do}
    #   04: {alpha, beta}  (base is unpaired - pair_id=null, already handled)
    #   08: {covert, overt}
    #   09: seat_A + seat_B (minimum; arbiter + seat_C are valid additions)
    #   10: {N, U}
    PAIR_REQUIRED = {
        "02": {"base", "cold_open"},
        "03": {"say", "do"},
        "04": {"alpha", "beta"},
        "08": {"covert", "overt"},
        "09": {"seat_A", "seat_B"},  # minimum required
        "10": {"N", "U"},
    }
    # Build pair groups per design code
    pair_by_design: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for obj, raw, fname, lineno in all_lines:
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        pair_id = meta.get("pair_id")
        if pair_id is None:
            continue
        design_full = meta.get("design", "")
        design_code = extract_design_code(design_full)
        admin = meta.get("admin", "")
        runnable = meta.get("runnable", False)
        pair_by_design[design_code][pair_id].append((admin, runnable, fname, lineno))

    for design_code, pair_required in PAIR_REQUIRED.items():
        if design_code not in pair_by_design:
            continue
        for pid, members in pair_by_design[design_code].items():
            runnable_admins = {m[0] for m in members if m[1]}
            # Normalize: strip the "-exemplar" suffix to check base-type completeness.
            # Exemplar-only pairs like {say-exemplar, do-exemplar} are valid complete pairs;
            # normalizing gives {say, do} which satisfies pair_required.
            normalized_admins = {a.removesuffix("-exemplar") for a in runnable_admins}
            # Check that all required admins are present for runnable items
            # If all members are non-runnable, skip (killed items may be incomplete)
            if not runnable_admins:
                continue
            missing_admins = pair_required - normalized_admins
            if missing_admins:
                pair_defects.append({
                    "item_id": pid,
                    "id": pid,
                    "design": design_code,
                    "admin": "PAIR_CHECK",
                    "runnable": True,
                    "file": members[0][2] if members else "unknown",
                    "lineno": members[0][3] if members else 0,
                    "defect_codes": ["PAIR_INCOMPLETE"],
                    "detail": (
                        f"pair_id={pid} design={design_code} "
                        f"present={sorted(runnable_admins)} "
                        f"normalized={sorted(normalized_admins)} "
                        f"missing={sorted(missing_admins)}"
                    ),
                })

    all_defects = defect_records + pair_defects
    if parse_errors:
        for pe in parse_errors:
            all_defects.append({
                "item_id": "PARSE_ERROR",
                "id": "PARSE_ERROR",
                "design": pe.get("file", ""),
                "admin": "",
                "runnable": None,
                "file": pe.get("file", ""),
                "lineno": pe.get("lineno", 0),
                "defect_codes": ["PARSE_ERROR"],
                "detail": pe.get("error", ""),
            })

    # ---- M5: coverage ----
    total_lines = len(all_lines)
    # Unique item_ids
    all_item_ids: set[str] = set()
    runnable_item_ids: set[str] = set()
    design_item_counts: dict[str, set] = defaultdict(set)
    design_line_counts: Counter = Counter()
    design_runnable_lines: Counter = Counter()
    design_area_matrix: dict[str, Counter] = defaultdict(Counter)
    stratum_by_design: dict[str, Counter] = defaultdict(Counter)
    tier_by_design: dict[str, Counter] = defaultdict(Counter)
    difficulty_by_design: dict[str, Counter] = defaultdict(Counter)
    wave_by_design: dict[str, Counter] = defaultdict(Counter)

    for obj, raw, fname, lineno in all_lines:
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        item_id = meta.get("item_id", "UNKNOWN")
        design_full = meta.get("design", "")
        design_code = extract_design_code(design_full)
        runnable = meta.get("runnable", False)
        area = meta.get("area", "UNKNOWN")
        stratum = meta.get("stratum", "UNKNOWN")
        tier = meta.get("tier", "UNKNOWN")
        difficulty = meta.get("difficulty", "UNKNOWN")
        wave = meta.get("wave", None)

        all_item_ids.add(item_id)
        design_item_counts[design_code].add(item_id)
        design_line_counts[design_code] += 1
        design_area_matrix[design_code][area] += 1
        stratum_by_design[design_code][stratum] += 1
        tier_by_design[design_code][tier] += 1
        difficulty_by_design[design_code][difficulty] += 1
        if wave is not None:
            wave_by_design[design_code][str(wave)] += 1

        if runnable:
            runnable_item_ids.add(item_id)
            design_runnable_lines[design_code] += 1

    coverage = {
        "canary": CANARY,
        "surface": surface,
        "total_lines": total_lines,
        "total_items": len(all_item_ids),
        "total_runnable_items": len(runnable_item_ids),
        "total_runnable_lines": sum(design_runnable_lines.values()),
        "per_design": {},
    }

    for dcode in DESIGN_NAMES:
        coverage["per_design"][dcode] = {
            "items": len(design_item_counts.get(dcode, set())),
            "lines": design_line_counts.get(dcode, 0),
            "runnable_lines": design_runnable_lines.get(dcode, 0),
            "area_distribution": dict(sorted(design_area_matrix.get(dcode, {}).items())),
            "stratum_distribution": dict(sorted(stratum_by_design.get(dcode, {}).items())),
            "tier_distribution": dict(sorted(tier_by_design.get(dcode, {}).items())),
            "difficulty_distribution": dict(sorted(difficulty_by_design.get(dcode, {}).items())),
            "wave_distribution": dict(sorted(wave_by_design.get(dcode, {}).items())),
        }

    # stratum-c count across all designs
    stratum_c_total = sum(
        cnt["c"]
        for cnt in stratum_by_design.values()
        if "c" in cnt
    )
    coverage["stratum_c_total"] = stratum_c_total

    return all_defects, coverage


def defect_summary(defects: list[dict]) -> dict[str, int]:
    code_counts: Counter = Counter()
    for rec in defects:
        for code in rec["defect_codes"]:
            code_counts[code] += 1
    return dict(sorted(code_counts.items()))


def write_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    print(f"  wrote {path}")


def main() -> None:
    allow_holdout = os.environ.get("WALKWORTHY_ALLOW_HOLDOUT", "") == "1"

    print("=== WALKWORTHY v2 Item Assessment: M1+M5 ===")
    print(f"  V2={V2}")
    print(f"  allow_holdout={allow_holdout}")

    # ---- PUBLIC surface ----
    print("\n[PUBLIC] scanning...")
    pub_defects, pub_coverage = scan_surface("public", PUBLIC_DIR)
    print(f"  lines={pub_coverage['total_lines']}  items={pub_coverage['total_items']}  runnable_items={pub_coverage['total_runnable_items']}  runnable_lines={pub_coverage['total_runnable_lines']}")
    write_json(OUTPUT_DIR / "m1-defects-public.json", {"canary": CANARY, "surface": "public", "defects": pub_defects})
    write_json(OUTPUT_DIR / "m5-coverage-public.json", pub_coverage)

    # ---- HOLDOUT surface ----
    if allow_holdout:
        print("\n[HOLDOUT] scanning...")
        ho_defects, ho_coverage = scan_surface("holdout", HOLDOUT_DIR)
        print(f"  lines={ho_coverage['total_lines']}  items={ho_coverage['total_items']}  runnable_items={ho_coverage['total_runnable_items']}  runnable_lines={ho_coverage['total_runnable_lines']}")
        write_json(OUTPUT_DIR / "m1-defects-holdout.json", {"canary": CANARY, "surface": "holdout", "defects": ho_defects})
        write_json(OUTPUT_DIR / "m5-coverage-holdout.json", ho_coverage)
    else:
        print("\n[HOLDOUT] skipped (WALKWORTHY_ALLOW_HOLDOUT != 1)")
        ho_defects, ho_coverage = [], {}

    # ---- Acceptance checks ----
    print("\n[ACCEPTANCE CHECKS]")
    expected_pub_lines = 575
    expected_pub_items = 355
    expected_pub_runnable = 344
    checks = {
        "public_lines": (pub_coverage["total_lines"], expected_pub_lines),
        "public_items": (pub_coverage["total_items"], expected_pub_items),
        "public_runnable_items": (pub_coverage["total_runnable_items"], expected_pub_runnable),
    }
    for name, (got, want) in checks.items():
        status = "PASS" if got == want else "FAIL"
        print(f"  {status}: {name} = {got} (expected {want})")

    # Design07 known defect items
    d07_known = {"WW-07-L02", "WW-07-I04", "WW-07-F02"}
    d07_detected = {
        rec["item_id"]
        for rec in pub_defects
        if "KEYED_EMPTY" in rec["defect_codes"] and rec["item_id"] in d07_known
    }
    d07_status = "PASS" if d07_detected == d07_known else "FAIL"
    print(f"  {d07_status}: design07 known defect items detected = {sorted(d07_detected)} (expected {sorted(d07_known)})")

    # ---- Summary markdown ----
    pub_summary = defect_summary(pub_defects)
    ho_summary = defect_summary(ho_defects) if allow_holdout else {}

    md_lines = [
        f"# WALKWORTHY v2 Item Assessment — M1+M5 Summary",
        f"",
        f"**Canary:** {CANARY}",
        f"**Generated:** 2026-07-18",
        f"",
        f"---",
        f"",
        f"## PUBLIC surface",
        f"",
        f"### M5 Coverage",
        f"",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Total lines | {pub_coverage['total_lines']} |",
        f"| Total items (unique item_id) | {pub_coverage['total_items']} |",
        f"| Total runnable items | {pub_coverage['total_runnable_items']} |",
        f"| Total runnable admin-lines | {pub_coverage['total_runnable_lines']} |",
        f"| Stratum-c items (all designs) | {pub_coverage['stratum_c_total']} |",
        f"",
        f"**Acceptance checks (expected: 575 lines / 355 items / 344 runnable):**",
        f"",
    ]
    for name, (got, want) in checks.items():
        status = "PASS" if got == want else "FAIL"
        md_lines.append(f"- {status}: `{name}` = {got} (expected {want})")
    md_lines.append(f"- {d07_status}: design07 known defect items detected = {sorted(d07_detected)}")
    md_lines += [
        f"",
        f"**Per-design (public):**",
        f"",
        f"| Design | Items | Lines | Runnable lines |",
        f"|--------|-------|-------|---------------|",
    ]
    for dcode in DESIGN_NAMES:
        pd = pub_coverage["per_design"].get(dcode, {})
        md_lines.append(
            f"| {dcode} | {pd.get('items',0)} | {pd.get('lines',0)} | {pd.get('runnable_lines',0)} |"
        )

    md_lines += [
        f"",
        f"**Design × area matrix (public, line counts):**",
        f"",
    ]
    all_areas = sorted({
        area
        for dcode in DESIGN_NAMES
        for area in pub_coverage["per_design"].get(dcode, {}).get("area_distribution", {}).keys()
    })
    md_lines.append("| Design | " + " | ".join(all_areas) + " |")
    md_lines.append("|--------|" + "---|" * len(all_areas))
    for dcode in DESIGN_NAMES:
        area_dist = pub_coverage["per_design"].get(dcode, {}).get("area_distribution", {})
        row = " | ".join(str(area_dist.get(a, 0)) for a in all_areas)
        md_lines.append(f"| {dcode} | {row} |")

    md_lines += [
        f"",
        f"### M1 Defects (public)",
        f"",
        f"Total defect records: {len(pub_defects)}",
        f"",
        f"| Defect code | Count |",
        f"|-------------|-------|",
    ]
    for code, cnt in sorted(pub_summary.items()):
        md_lines.append(f"| `{code}` | {cnt} |")

    if pub_defects:
        md_lines += [
            f"",
            f"**Defect items (public):**",
            f"",
        ]
        # Group by item_id
        by_item: dict[str, list] = defaultdict(list)
        for rec in pub_defects:
            by_item[rec["item_id"]].append(rec)
        for item_id in sorted(by_item.keys()):
            recs = by_item[item_id]
            all_codes = sorted({code for r in recs for code in r["defect_codes"]})
            details = "; ".join(r["detail"] for r in recs if r["detail"])
            md_lines.append(f"- `{item_id}` codes={all_codes} {details}")

    # HOLDOUT section
    md_lines += [
        f"",
        f"---",
        f"",
        f"## HOLDOUT surface",
        f"",
    ]
    if allow_holdout and ho_coverage:
        md_lines += [
            f"### M5 Coverage",
            f"",
            f"| Metric | Count |",
            f"|--------|-------|",
            f"| Total lines | {ho_coverage['total_lines']} |",
            f"| Total items (unique item_id) | {ho_coverage['total_items']} |",
            f"| Total runnable items | {ho_coverage['total_runnable_items']} |",
            f"| Total runnable admin-lines | {ho_coverage['total_runnable_lines']} |",
            f"| Stratum-c items (all designs) | {ho_coverage['stratum_c_total']} |",
            f"",
            f"**Per-design (holdout):**",
            f"",
            f"| Design | Items | Lines | Runnable lines |",
            f"|--------|-------|-------|---------------|",
        ]
        for dcode in DESIGN_NAMES:
            hd = ho_coverage["per_design"].get(dcode, {})
            md_lines.append(
                f"| {dcode} | {hd.get('items',0)} | {hd.get('lines',0)} | {hd.get('runnable_lines',0)} |"
            )
        md_lines += [
            f"",
            f"### M1 Defects (holdout)",
            f"",
            f"Total defect records: {len(ho_defects)}",
            f"",
            f"| Defect code | Count |",
            f"|-------------|-------|",
        ]
        for code, cnt in sorted(ho_summary.items()):
            md_lines.append(f"| `{code}` | {cnt} |")
        if ho_defects:
            md_lines += [
                f"",
                f"**Defect items (holdout):**",
                f"",
            ]
            by_item_ho: dict[str, list] = defaultdict(list)
            for rec in ho_defects:
                by_item_ho[rec["item_id"]].append(rec)
            for item_id in sorted(by_item_ho.keys()):
                recs = by_item_ho[item_id]
                all_codes = sorted({code for r in recs for code in r["defect_codes"]})
                details = "; ".join(r["detail"] for r in recs if r["detail"])
                md_lines.append(f"- `{item_id}` codes={all_codes} {details}")
    else:
        md_lines.append("Holdout scan not run (WALKWORTHY_ALLOW_HOLDOUT was not set to 1).")

    md_lines += [
        f"",
        f"---",
        f"",
        f"*{CANARY}*",
    ]

    summary_path = OUTPUT_DIR / "m1-m5-summary.md"
    with open(summary_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md_lines) + "\n")
    print(f"  wrote {summary_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
