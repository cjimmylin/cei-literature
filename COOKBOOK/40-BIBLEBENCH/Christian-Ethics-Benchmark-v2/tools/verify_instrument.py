#!/usr/bin/env python3
"""Verify the working tree against its instrument version stamp (INSTRUMENT.json).

Contract: tools/SCHEMA.md, section "Instrument version stamp (added 2026-07-30, T0-8)".

What this does
--------------
1. Loads <repo root>/INSTRUMENT.json.
2. Recomputes the sha256 of every file listed under `components` and compares.
3. Recounts the public bank surface (items / runnable items / administration lines,
   per design and in total) and compares against `surface`.
4. Checks that every public bank line carries the stamped canary verbatim.
5. Checks the pins block is well formed: every pin with a model slug has a source.
6. Prints a per-component PASS/FAIL table and exits 0 only if everything passed.

What this deliberately does NOT do
----------------------------------
- Never reads `logs/`. Run outputs are not part of the instrument definition.
- Never reads, hashes, lists, or opens `datasets/holdout/`. The holdout is quarantined;
  this stamp certifies the public surface only. A hard guard below refuses any component
  path that points into it, and refuses to honour WALKWORTHY_ALLOW_HOLDOUT.
- Never imports the eval framework and never calls a model. Pure standard library, no
  network, no credentials. Verifying a stamp is free.

Usage: python3 tools/verify_instrument.py   (no arguments; runnable from any directory)
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

# --- repo root, resolved from this file, so cwd never matters -------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STAMP_PATH = os.path.join(ROOT, "INSTRUMENT.json")

FORBIDDEN_PREFIXES = ("datasets/holdout", "logs")

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
OFF = "\033[0m"
COLOR = sys.stdout.isatty()


def _c(text: str, code: str) -> str:
    return f"{code}{text}{OFF}" if COLOR else text


def _norm(rel: str) -> str:
    return rel.replace(os.sep, "/").lstrip("./")


def _is_forbidden(rel: str) -> bool:
    n = _norm(rel)
    return any(n == p or n.startswith(p + "/") for p in FORBIDDEN_PREFIXES)


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Results:
    def __init__(self) -> None:
        self.rows: list[tuple[str, bool, str]] = []

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.rows.append((name, ok, detail))

    @property
    def failed(self) -> list[tuple[str, bool, str]]:
        return [r for r in self.rows if not r[1]]

    def table(self, title: str) -> None:
        if not self.rows:
            return
        width = max(len(r[0]) for r in self.rows)
        print(f"\n{title}")
        print("-" * (width + 8))
        for name, ok, detail in self.rows:
            tag = _c("PASS", GREEN) if ok else _c("FAIL", RED)
            line = f"{name.ljust(width)}  {tag}"
            if detail:
                line += f"  {detail if not ok else _c(detail, DIM)}"
            print(line)


def load_stamp() -> dict:
    if not os.path.exists(STAMP_PATH):
        print(_c(f"FATAL: no instrument stamp at {STAMP_PATH}", RED))
        sys.exit(2)
    with open(STAMP_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def check_components(stamp: dict, res: Results) -> None:
    components = stamp.get("components") or {}
    if not components:
        res.add("components block present", False, "empty or missing")
        return
    for rel in sorted(components):
        spec = components[rel]
        expected = spec.get("sha256", "")
        if _is_forbidden(rel):
            res.add(rel, False, "QUARANTINED PATH - must not be a stamped component")
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            res.add(rel, False, "MISSING from tree")
            continue
        actual = sha256_of(path)
        if actual != expected:
            res.add(rel, False, f"sha256 {actual[:12]}... != stamped {expected[:12]}...")
        else:
            res.add(rel, True, f"sha256 {actual[:12]}...")


def recount_surface(canary: str) -> tuple[dict, list[str]]:
    """Recount the PUBLIC bank only. Returns (counts, canary_problems)."""
    pub = os.path.join(ROOT, "datasets", "public")
    problems: list[str] = []
    items: set[str] = set()
    runnable: set[str] = set()
    admin = 0
    per: dict[str, dict[str, int]] = {}
    for i in range(1, 11):
        name = f"design{i:02d}.jsonl"
        path = os.path.join(pub, name)
        if not os.path.exists(path):
            problems.append(f"{name}: missing")
            continue
        d_items: set[str] = set()
        d_runnable: set[str] = set()
        d_lines = 0
        with open(path, encoding="utf-8") as fh:
            for lineno, raw in enumerate(fh, 1):
                raw = raw.strip()
                if not raw:
                    continue
                obj = json.loads(raw)
                meta = obj.get("metadata") or {}
                d_lines += 1
                admin += 1
                if meta.get("canary") != canary:
                    problems.append(f"{name}:{lineno} canary mismatch")
                item_id = meta.get("item_id")
                if item_id is None:
                    problems.append(f"{name}:{lineno} missing item_id")
                    continue
                items.add(item_id)
                d_items.add(item_id)
                if meta.get("runnable"):
                    runnable.add(item_id)
                    d_runnable.add(item_id)
        per[name] = {
            "items": len(d_items),
            "runnable": len(d_runnable),
            "admin_lines": d_lines,
        }
    counts = {
        "items": len(items),
        "runnable": len(runnable),
        "admin_lines": admin,
        "per_design": per,
    }
    return counts, problems


def check_surface(stamp: dict, res: Results) -> list[str]:
    canary = stamp.get("canary", "")
    stamped = stamp.get("surface") or {}
    actual, canary_problems = recount_surface(canary)

    for key in ("items", "runnable", "admin_lines"):
        want = stamped.get(key)
        got = actual[key]
        res.add(f"surface.{key}", want == got, f"{got} (stamped {want})")

    want_per = stamped.get("per_design") or {}
    for name in sorted(actual["per_design"]):
        got = actual["per_design"][name]
        want = want_per.get(name)
        if want is None:
            res.add(f"surface.per_design.{name}", False, "not in stamp")
            continue
        ok = all(want.get(k) == got[k] for k in ("items", "runnable", "admin_lines"))
        detail = f"{got['items']}i/{got['runnable']}r/{got['admin_lines']}a"
        if not ok:
            detail += (
                f" != stamped {want.get('items')}i/"
                f"{want.get('runnable')}r/{want.get('admin_lines')}a"
            )
        res.add(f"surface.per_design.{name}", ok, detail)

    res.add(
        "canary in every public line",
        not canary_problems,
        "all lines carry the canary" if not canary_problems
        else f"{len(canary_problems)} problem(s): {canary_problems[:3]}",
    )
    return canary_problems


def check_pins(stamp: dict, res: Results) -> None:
    pins = stamp.get("pins") or {}
    if not pins:
        res.add("pins block present", False, "empty or missing")
        return
    for name in sorted(pins):
        entry = pins[name] or {}
        src = entry.get("source")
        ok = bool(src)
        model = entry.get("model")
        detail = model if model else "no model slug (descriptive pin)"
        if not ok:
            detail = "missing required `source` field"
        res.add(f"pins.{name}", ok, detail)


def check_holdout_quarantine(stamp: dict, res: Results) -> None:
    hold = stamp.get("holdout") or {}
    ok = (
        hold.get("quarantined") is True
        and hold.get("hashed_into_stamp") is False
        and hold.get("counted_in_surface") is False
    )
    res.add(
        "holdout quarantine declared",
        ok,
        "declared: not hashed, not counted, not read" if ok
        else "holdout block missing or does not declare quarantine",
    )
    leaked = [r for r in (stamp.get("components") or {}) if _is_forbidden(r)]
    res.add(
        "no quarantined path in components",
        not leaked,
        "clean" if not leaked else f"leaked: {leaked}",
    )
    if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT"):
        res.add(
            "WALKWORTHY_ALLOW_HOLDOUT unset",
            False,
            "set in environment - this checker never verifies holdout content",
        )
    else:
        res.add("WALKWORTHY_ALLOW_HOLDOUT unset", True, "unset")


def main() -> int:
    stamp = load_stamp()
    iid = stamp.get("instrument_id", "<none>")
    print(f"WALKWORTHY instrument verification")
    print(f"  root          {ROOT}")
    print(f"  instrument_id {iid}")
    print(f"  bank_revision {stamp.get('bank_revision', '<none>')}")
    print(f"  stamped       {stamp.get('stamped', '<none>')} "
          f"({stamp.get('stamp_kind', 'unknown')})")
    print(f"  scope         public bank only; holdout quarantined, not verified")

    integrity = Results()
    check_holdout_quarantine(stamp, integrity)
    check_pins(stamp, integrity)

    surface = Results()
    check_surface(stamp, surface)

    comps = Results()
    check_components(stamp, comps)

    integrity.table("INTEGRITY / PINS")
    surface.table("PUBLIC BANK SURFACE")
    comps.table("PINNED COMPONENTS")

    n_fail = len(integrity.failed) + len(surface.failed) + len(comps.failed)
    n_total = len(integrity.rows) + len(surface.rows) + len(comps.rows)
    print()
    if n_fail == 0:
        print(_c(f"ALL PASS - {n_total}/{n_total} checks - tree matches instrument {iid}",
                 GREEN))
        return 0
    print(_c(f"FAILED - {n_fail}/{n_total} checks failed", RED))
    print("A pinned component moved. Per tools/SCHEMA.md, this tree is NOT "
          f"instrument {iid}; a new instrument_id is owed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
