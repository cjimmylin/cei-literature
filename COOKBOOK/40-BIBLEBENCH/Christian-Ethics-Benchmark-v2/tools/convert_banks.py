#!/usr/bin/env python3
"""convert_banks.py — WALKWORTHY item banks -> per-design JSONL datasets (v2).

Conforms to tools/SCHEMA.md (frozen 2026-07-15). One JSONL LINE = one
ADMINISTRATION (a "seat" / "twin" / "variant" / "motive arm" / a scripted
multi-turn conversation as a whole). Single-administration designs emit one line
per item.

Reuse strategy (per the build brief):
  We sys.path-inject the v1 harness and import the already-tested `walkworthy`
  package (parsing.py, models.py, builders.py, loader.py — 549 passing tests
  behind them). The v1 package imports cleanly under Python 3.14, so NO code was
  vendored into tools/_v1compat/. All the messy per-design Markdown-dialect
  knowledge lives in v1 builders.py; this file only *serializes* the normalized
  v1 Item/Administration model into the v2 line schema.

Administration -> line mapping actually implemented here (derived from v1
builders.py + models.py — the source of truth for each design's structure):

  01 goodsamaritan  single       admin label "main"           -> admin="base"
  02 twomasters     multi_turn   "main" (scripted ladder)     -> admin="base"
                                 "cold_open" (control)        -> admin="cold_open"
                                 => metadata.multiturn carries the scripted
                                    ladder (turns + branch_table + rubric) for
                                    the scripted-multi-turn admin only.
  03 quiettongue    paired       "expressed" / "revealed"     -> admin="say"/"do"
                                 (say-do twins; pair_id set)
  04 innerweight    paired/single "alpha"/"beta" motive arms  -> admin="alpha"/"beta"
                                 4b singles "main"            -> admin="base"
  05 ordoamoris     single       "main"                       -> admin="base"
  06 crookedpath    single       "main"                       -> admin="base"
  07 seventyseven   multi_turn   "main" (scripted branch tbl) -> admin="base"
                                 => metadata.multiturn as for 02.
  08 vocationfork   paired       "covert"/"overt"             -> admin="covert"/"overt"
  09 doubleedge     paired       "seat_A"/"seat_B"/"seat_C"   -> admin=<label>
                                 "arbiter" probe              -> admin="arbiter"
  10 strangergate   paired       "N"/"U" desert-cue arms      -> admin="N"/"U"

`admin` string = the v1 administration label verbatim, except 01/05/06 and the
04b singles, whose single administration is labelled "main" in v1 and normalized
to "base" here (SCHEMA: single-admin designs use "base"; and 02's scripted-ladder
"main" also -> "base", with its sibling control kept as "cold_open").

`pair_id`: for paired designs we group sibling administrations under a stable
pair key = the item id (v1 twins are administrations of ONE item, so the item id
is the natural shared key that a paired metric groups on). `null` for unpaired.

`keyed`: the design's v1 Item.key dict verbatim (opaque scoring key) plus any
scoring-relevant extras (allocation spec for 05, reference answers / fact core /
extraction schema for 06/09, facts_diff, etc.). The design NN scorer owns the
shape (documented in walkworthy_inspect/rubrics.py, per SCHEMA).

Non-runnable items (02/07/09 sketch exemplars from the -SPEC .md files) ARE
emitted with runnable=false; the v2 loader filters them by default.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# --------------------------------------------------------------------------- #
# v1 harness import (reuse tested parsing code)
# --------------------------------------------------------------------------- #
V2_ROOT = Path(__file__).resolve().parent.parent
# v1 canonical benchmark is the read-only sibling of this folder (kept as a sibling per
# owner ruling). Resolved relatively so the folder is path-portable; override with --v1-root.
V1_ROOT_DEFAULT = V2_ROOT.parent / "Christian-Ethics-Benchmark"


def _inject_v1(v1_root: Path) -> None:
    harness = v1_root / "harness"
    if not (harness / "walkworthy" / "builders.py").exists():
        raise SystemExit(
            f"v1 harness not found at {harness}. Pass --v1-root or vendor _v1compat/."
        )
    sys.path.insert(0, str(harness))


# imported after path injection in main(); declared here for type hints only
BUILDERS = None  # type: ignore
parse_raw_items = None  # type: ignore
Item = None  # type: ignore

CANARY = "WALKWORTHY-CANARY-7f3e2026"

DESIGN_CODES = [
    "01-goodsamaritan", "02-twomasters", "03-quiettongue", "04-innerweight",
    "05-ordoamoris", "06-crookedpath", "07-seventyseven", "08-vocationfork",
    "09-doubleedge", "10-strangergate",
]

# v1 single-administration labels that SCHEMA normalizes to "base".
_SINGLE_MAIN_TO_BASE = {"main"}


# --------------------------------------------------------------------------- #
# serialization helpers
# --------------------------------------------------------------------------- #
def _admin_key(design_code: str, label: str, admin_mode: str) -> str:
    """Map a v1 administration label to the SCHEMA `admin` string.

    Single-admin designs (and the 02 scripted ladder "main") -> "base"; every
    other label (say/do twin, seat, motive arm, cue, cold_open, arbiter) is kept
    verbatim so metrics can group on the design-specific arm.
    """
    if label in _SINGLE_MAIN_TO_BASE:
        # "main" is the sole/primary administration -> "base" per SCHEMA.
        # 03 uses "expressed"/"revealed" (not "main"); keep those mapped below.
        return "base"
    # 03 say-do twins carry v1 labels expressed/revealed -> say/do surface names.
    if design_code == "03-quiettongue":
        return {"expressed": "say", "revealed": "do"}.get(label, label)
    return label


def _messages(admin) -> List[Dict[str, str]]:
    """Build the OpenAI-style chat `input` for one administration.

    Single-turn admins -> [system?, user]. Scripted-multi-turn admins (02/07)
    -> [system?, first materializable user turn]; the full scripted ladder
    (all turns, branch table, terminal ask) lives in metadata.multiturn and is
    replayed by the multi-turn solver, so `input` seeds turn 1 only.
    """
    msgs: List[Dict[str, str]] = []
    if admin.system and admin.system.strip():
        msgs.append({"role": "system", "content": admin.system.strip()})

    if admin.kind == "single_turn":
        # single-turn admins have exactly one user turn with text
        text = ""
        for t in admin.turns:
            if t.text and t.text.strip():
                text = t.text.strip()
                break
        msgs.append({"role": "user", "content": text})
    else:  # scripted_multi_turn
        first = ""
        for t in admin.turns:
            if t.text and t.text.strip():
                first = t.text.strip()
                break
            if t.branches:
                # unconditional opener may itself be a branch-less T1; if T1 is a
                # branch turn we seed with the "complied"/first branch as opener.
                first = next(iter(t.branches.values())).strip()
                break
        if not first and admin.terminal_ask:
            first = admin.terminal_ask.strip()
        msgs.append({"role": "user", "content": first})
    return msgs


def _multiturn_payload(admin) -> Optional[Dict[str, Any]]:
    """metadata.multiturn for 02/07 scripted admins; None otherwise.

    Shape per SCHEMA: {"turns": [...], "branch_table": {...},
    "classifier_rubric": "..."}. We serialize the v1 Turn list faithfully:
    each turn -> {index, text, branches, markers}. branch_table collects the
    per-turn state->text branch maps keyed by turn index (the scripted branch
    table the multi-turn solver walks). classifier_rubric is the design's state
    classifier hint; v1 encodes state names in the branch keys (02: complied/
    refused; 07: validated/challenged/deflected), which we surface here.
    """
    if admin.kind != "scripted_multi_turn":
        return None
    turns_out: List[Dict[str, Any]] = []
    branch_table: Dict[str, Dict[str, str]] = {}
    for t in admin.turns:
        turns_out.append({
            "index": t.index,
            "text": t.text,
            "branches": t.branches or None,
            "markers": list(t.markers),
        })
        if t.branches:
            branch_table[str(t.index)] = dict(t.branches)
    branch_states = sorted({s for m in branch_table.values() for s in m})
    return {
        "turns": turns_out,
        "branch_table": branch_table,
        "terminal_ask": admin.terminal_ask,
        # the solver classifies each model reply into one of these branch states
        # to pick the next scripted user turn; state vocabulary is design-derived.
        "classifier_rubric": (
            "Classify each assistant reply into one of the branch states "
            f"{branch_states} to select the next scripted user turn from "
            "branch_table; markers flag repentance/openness/loyalty/terminal windows."
            if branch_states else
            "Linear scripted ladder: replay turns in order; markers flag "
            "repentance/openness/loyalty/terminal windows."
        ),
    }


def _keyed_payload(item) -> Dict[str, Any]:
    """metadata.keyed = the design's opaque scoring key.

    v1 Item.key (design-specific rubric key) merged with scoring-relevant
    Item.extras (allocation spec, reference answers, fact core, extraction
    schema, facts_diff, keyed_motive, ...). The design-NN scorer in
    walkworthy_inspect/rubrics.py owns and interprets this shape.
    """
    payload: Dict[str, Any] = {}
    if item.key:
        payload.update(_jsonable(item.key))
    if item.extras:
        # extras carry scoring-relevant structure for 04/05/06/08/09/10
        payload["extras"] = _jsonable(item.extras)
    return payload


def _target(item, admin) -> str:
    """The keyed-behavior description the judge scores against.

    Prefer an explicit keyed-behavior string; fall back to the design's primary
    key field, then to a stable non-empty descriptor (SCHEMA requires non-empty
    target on every line).
    """
    k = item.key or {}
    for field in ("keyed_behavior", "keyed", "keyed_determinations",
                  "process_notes", "keyed_constraints"):
        v = k.get(field)
        if isinstance(v, str) and v.strip():
            return v.strip()
    # last-resort non-empty target so no line violates the SCHEMA guarantee.
    return (f"[{item.design} {item.id}] Judge per design rubric "
            f"(walkworthy_inspect/rubrics.py); keyed behavior not inlined.")


def _jsonable(obj: Any) -> Any:
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return _jsonable(dataclasses.asdict(obj))
    if isinstance(obj, dict):
        return {str(k): _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(v) for v in obj]
    return obj


def _line_for_admin(item, admin, design_code: str) -> Dict[str, Any]:
    admin_key = _admin_key(design_code, admin.label, item.admin_mode)
    item_id = item.id
    # Spec sketch exemplars can share an item_id with a runnable seed item (02
    # WW-02-I01) or a promoted holdout item (02 WW-02-A01/F01/G01). They are
    # non-runnable stubs; suffix their admin key so their `id` never collides
    # with a real run-surface line (SCHEMA: `id` unique across public+holdout).
    if item.is_exemplar:
        admin_key = f"{admin_key}-exemplar"
    line_id = f"{item_id}#{admin_key}"

    paired = item.admin_mode in ("paired",) or (
        item.admin_mode == "multi_turn" and len([a for a in item.administrations]) > 1
    )
    # pair_id groups sibling administrations a paired metric compares. Paired
    # designs (03/04-pairs/08/09/10) compare arms of the SAME item, so the item
    # id is the natural pair key. Unpaired => null.
    pair_id: Optional[str] = None
    if item.admin_mode == "paired":
        pair_id = item_id
    elif design_code in ("02-twomasters",) and len(item.administrations) > 1:
        # 02: the scripted ladder + its cold-open control are compared as a pair.
        pair_id = item_id

    meta: Dict[str, Any] = {
        "item_id": item_id,
        "design": design_code,
        "admin": admin_key,
        "pair_id": pair_id,
        "area": item.area or None,
        "secondary": list(item.secondary) if item.secondary else [],
        "stratum": item.stratum,
        "dispute": item.dispute,
        "tier": item.tier,
        "difficulty": item.difficulty,
        "anchors": list(item.anchors),
        "variables": _jsonable(item.variables),
        "admin_meta": _jsonable(admin.meta) if admin.meta else {},
        "is_exemplar": bool(item.is_exemplar),
        "runnable": bool(item.runnable),
        "review_status": "ported-unreviewed",
        "canary": CANARY,
        "keyed": _keyed_payload(item),
        "multiturn": _multiturn_payload(admin),
        "source_file": item.source_file,
    }

    return {
        "id": line_id,
        "input": _messages(admin),
        "target": _target(item, admin),
        "metadata": meta,
    }


def _items_for_design(design_code: str, banks_dir: Path, is_holdout: bool):
    """Parse one design's items using the v1 builder + item parser.

    Public: seed bank (`<design>-seeds.md`) + spec exemplars (`<design>.md`,
    which contribute the non-runnable sketch items). Holdout: the single
    `<design>-holdout.md` file, parsed DIRECTLY with the v1 item parser +
    builder (bypassing loader._guard_public, which would raise
    HoldoutAccessError). The v2 holdout guard is downstream in the loader, not
    in conversion — this is a sanctioned conversion-time read.
    """
    builder = BUILDERS[design_code]
    items = []
    if is_holdout:
        hp = banks_dir / f"{design_code}-holdout.md"
        if not hp.exists():
            return []
        raws = parse_raw_items(hp.read_text(encoding="utf-8"), str(hp))
        for r in raws:
            items.append(builder(r, design_code))
    else:
        seed = banks_dir / f"{design_code}-seeds.md"
        if seed.exists():
            for r in parse_raw_items(seed.read_text(encoding="utf-8"), str(seed)):
                items.append(builder(r, design_code))
        spec = banks_dir / f"{design_code}.md"
        if spec.exists():
            for r in parse_raw_items(spec.read_text(encoding="utf-8"), str(spec)):
                ex = builder(r, design_code)
                ex.is_exemplar = True
                items.append(ex)
    for it in items:
        it.runnable = it.is_runnable()
    return items


def convert_split(banks_dir: Path, out_dir: Path, is_holdout: bool) -> Dict[str, Dict[str, int]]:
    """Convert one split (public or holdout) -> per-design JSONL files.

    Returns per-design counts: items / runnable_items / lines / runnable_lines.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    stats: Dict[str, Dict[str, int]] = {}
    for design_code in DESIGN_CODES:
        items = _items_for_design(design_code, banks_dir, is_holdout)
        design_num = design_code.split("-")[0]  # "01".."10"
        out_path = out_dir / f"design{design_num}.jsonl"
        n_items = len(items)
        n_run_items = sum(1 for i in items if i.runnable)
        n_lines = 0
        n_run_lines = 0
        with out_path.open("w", encoding="utf-8") as fh:
            for it in items:
                for admin in it.administrations:
                    line = _line_for_admin(it, admin, design_code)
                    fh.write(json.dumps(line, ensure_ascii=False) + "\n")
                    n_lines += 1
                    if it.runnable:
                        n_run_lines += 1
                if not it.administrations:
                    # an item that parsed to zero administrations (defensive):
                    # emit a single non-runnable placeholder line so nothing is
                    # silently dropped and IDs remain auditable.
                    admin_stub = _AdminStub()
                    line = _line_for_admin(it, admin_stub, design_code)
                    line["metadata"]["runnable"] = False
                    fh.write(json.dumps(line, ensure_ascii=False) + "\n")
                    n_lines += 1
        stats[design_code] = {
            "items": n_items,
            "runnable_items": n_run_items,
            "lines": n_lines,
            "runnable_lines": n_run_lines,
        }
    return stats


class _AdminStub:
    """Fallback empty administration for items that parsed to zero admins."""
    label = "base"
    kind = "single_turn"
    system = None
    turns: list = []
    terminal_ask = None
    cold_open = None
    meta: dict = {}


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--designs-dir", type=Path, default=V2_ROOT / "banks",
                    help="public item-bank dir (default: $V2/banks)")
    ap.add_argument("--holdout-dir", type=Path, default=V2_ROOT / "banks-holdout",
                    help="holdout item-bank dir (default: $V2/banks-holdout)")
    ap.add_argument("--out-public", type=Path, default=V2_ROOT / "datasets" / "public",
                    help="public JSONL out dir (default: $V2/datasets/public)")
    ap.add_argument("--out-holdout", type=Path, default=V2_ROOT / "datasets" / "holdout",
                    help="holdout JSONL out dir (default: $V2/datasets/holdout)")
    ap.add_argument("--v1-root", type=Path, default=V1_ROOT_DEFAULT,
                    help="v1 benchmark root (for the walkworthy harness import)")
    ap.add_argument("--no-holdout", action="store_true",
                    help="skip the holdout split")
    args = ap.parse_args(argv)

    _inject_v1(args.v1_root)
    global BUILDERS, parse_raw_items, Item
    from walkworthy.builders import BUILDERS as _B
    from walkworthy.parsing import parse_raw_items as _P
    from walkworthy.models import Item as _I
    BUILDERS, parse_raw_items, Item = _B, _P, _I

    print(f"[convert] v1 harness: {args.v1_root / 'harness'}")
    print(f"[convert] public banks:  {args.designs_dir}")
    print(f"[convert] holdout banks: {args.holdout_dir}")

    pub = convert_split(args.designs_dir, args.out_public, is_holdout=False)
    print(f"[convert] wrote public -> {args.out_public}")
    for d, s in pub.items():
        print(f"    {d:<18} items={s['items']:>3} runnable={s['runnable_items']:>3} "
              f"lines={s['lines']:>3} runnable_lines={s['runnable_lines']:>3}")
    tot_run_items = sum(s["runnable_items"] for s in pub.values())
    tot_lines = sum(s["lines"] for s in pub.values())
    print(f"[convert] PUBLIC total runnable items={tot_run_items} lines={tot_lines}")

    if not args.no_holdout:
        hold = convert_split(args.holdout_dir, args.out_holdout, is_holdout=True)
        print(f"[convert] wrote holdout -> {args.out_holdout}")
        for d, s in hold.items():
            print(f"    {d:<18} items={s['items']:>3} runnable={s['runnable_items']:>3} "
                  f"lines={s['lines']:>3} runnable_lines={s['runnable_lines']:>3}")
        tot_h_items = sum(s["runnable_items"] for s in hold.values())
        tot_h_lines = sum(s["lines"] for s in hold.values())
        print(f"[convert] HOLDOUT total runnable items={tot_h_items} lines={tot_h_lines}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
