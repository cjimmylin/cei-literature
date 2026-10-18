#!/usr/bin/env python3
"""Write the v14 dashboard's classifications of the 402 papers added since v13 into their notes.

Dashboard v14 (2026-10-18) classified the papers added after v13 (325 cultural/religious/Global
South papers from 2026-04-04 and 77 alignment papers from July) but kept the results in a build
overlay instead of the notes. This script writes that overlay into `papers/*.md` so the dashboard
can be rebuilt from the vault alone.

Input: DASHBOARDS/cei-dashboard-14/build/overlay_v14.json  ({filename: {field: value}})
  - scores from the vault's own scorers: ethics frameworks (ethics_scoring), mp_* (moral_psych_scoring),
    rv_* (religious_scoring), with the derived moral_psychology / religious_values_list strings
  - per-paper review (DASHBOARDS/cei-dashboard-14/build/new-paper-review/): cultures, languages,
    stated venue, models evaluated
  - first/last author parsed from `authors`, url from arxiv_id/DOI, venue from the vault's
    local venue normaliser (add_conference_field_cc.classify_phase1)

Rules (same as the v14 build, so the rebuilt dashboard matches v14):
  - a field is written only if the note lacks it or its value is empty / N/A / NA / none;
    existing values are never changed
  - an existing empty line is replaced in place (one line); a missing field is appended at the
    end of the frontmatter; nothing else in the file changes
  - formats follow the corpus: scores as unquoted integers, authors as "[[Name]]", lists as one
    comma-separated string (quoted when it is not a single plain token)

Usage:
    python3 PYTHON/apply_v14_classifications.py            # dry run: report only
    python3 PYTHON/apply_v14_classifications.py --apply    # write
Safe to re-run: a second run finds nothing to fill.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
OVERLAY = ROOT / "DASHBOARDS" / "cei-dashboard-14" / "build" / "overlay_v14.json"

FRAMEWORKS = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics", "care_ethics",
              "contractarian_ethics"]
RV = ["rv_islam", "rv_christianity", "rv_buddhism", "rv_judaism", "rv_hinduism", "rv_sikhism",
      "rv_confucianism", "rv_taoism", "rv_shinto", "rv_jainism", "rv_bahai", "rv_zoroastrianism",
      "rv_ubuntu", "rv_indigenous"]
MP = ["mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg", "mp_dual_process", "mp_intuitionist",
      "mp_dyadic", "mp_identity"]
# Order used when a field has to be appended.
ORDER = (["first_author", "last_author", "url", "CONF-CC", "LLM_assessed"] + FRAMEWORKS
         + ["national_ethnic_cultural", "cultures_nationalities_list", "languages_list"]
         + RV + ["religious_values_list"] + MP + ["moral_psychology"])
SCORES = set(FRAMEWORKS + RV + MP)
WIKILINKS = {"first_author", "last_author"}
EMPTY = ("", "n/a", "na", "none")  # what the dashboard generator treats as empty
PLAIN = re.compile(r"[A-Za-z0-9][A-Za-z0-9/_.\-]*")
FM = re.compile(r"\A---\n(.*?)\n---[ \t]*(?=\n|\Z)", re.DOTALL)


def fmt(field, value):
    if field in SCORES:
        return str(int(value))
    if field in WIKILINKS:
        name = str(value).strip()
        if not name or any(ch in name for ch in '"[]|\n'):
            raise ValueError(f"unusable author name {name!r}")
        return f'"[[{name}]]"'
    text = ", ".join(value) if isinstance(value, list) else str(value)
    text = text.strip()
    if "\n" in text:
        raise ValueError(f"multi-line value for {field}")
    if PLAIN.fullmatch(text):
        return text
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def is_empty(raw):
    return raw.strip().strip('"').strip("'").strip().lower() in EMPTY


def plan_paper(content, fields):
    """Return (new_content, filled, appended, kept) or raise ValueError."""
    m = FM.match(content)
    if not m:
        raise ValueError("no frontmatter")
    lines = m.group(1).split("\n")
    unknown = set(fields) - set(ORDER)
    if unknown:
        raise ValueError(f"unexpected fields {sorted(unknown)}")
    filled, appended, kept = [], [], []
    for field in ORDER:
        if field not in fields:
            continue
        idx = [i for i, ln in enumerate(lines) if re.match(rf"{re.escape(field)}[ \t]*:", ln)]
        if len(idx) > 1:
            raise ValueError(f"duplicate key {field}")
        new_line = f"{field}: {fmt(field, fields[field])}"
        if idx:
            i = idx[0]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.startswith((" ", "\t")) or nxt.lstrip().startswith("- "):
                raise ValueError(f"{field} has continuation lines")
            if is_empty(lines[i].split(":", 1)[1]):
                if lines[i] != new_line:
                    lines[i] = new_line
                    filled.append(field)
            else:
                kept.append(field)
        else:
            appended.append(new_line)
    if not filled and not appended:
        return content, filled, appended, kept
    new_fm = "\n".join(lines + appended)
    new_content = content[:m.start(1)] + new_fm + content[m.end(1):]
    # Safety: only the filled lines changed, appended lines come last, the rest is untouched.
    old = m.group(1).split("\n")
    new = new_fm.split("\n")
    if len(new) != len(old) + len(appended) or new[len(old):] != appended:
        raise ValueError("safety check: unexpected line count")
    for o, n in zip(old, new):
        if o != n and not (o.split(":", 1)[0].strip() in filled and is_empty(o.split(":", 1)[1])):
            raise ValueError(f"safety check: line changed unexpectedly: {o!r}")
    if not new_content.endswith(content[m.end(1):]) or not new_content.startswith(content[:m.start(1)]):
        raise ValueError("safety check: text outside the frontmatter changed")
    return new_content, filled, [a.split(":", 1)[0] for a in appended], kept


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()

    overlay = json.loads(OVERLAY.read_text(encoding="utf-8"))
    stats, errors, kept_all = Counter(), [], []
    for fn, fields in sorted(overlay.items()):
        path = PAPERS / fn
        if not path.exists():
            errors.append((fn, "paper not found"))
            continue
        content = path.read_text(encoding="utf-8")
        try:
            new_content, filled, appended, kept = plan_paper(content, fields)
        except (ValueError, AssertionError) as e:
            errors.append((fn, str(e) or "safety check failed"))
            continue
        for f in filled:
            stats["filled:" + f] += 1
        for f in appended:
            stats["added:" + f] += 1
        kept_all += [(fn, f) for f in kept]
        if new_content != content:
            stats["papers changed"] += 1
            if args.apply:
                path.write_text(new_content, encoding="utf-8")

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"[{mode}] overlay papers: {len(overlay)}  changed: {stats.pop('papers changed', 0)}")
    groups = Counter()
    for k, n in stats.items():
        action, field = k.split(":", 1)
        field = "rv_*" if field.startswith("rv_") else "mp_*" if field.startswith("mp_") else field
        groups[(action, field)] += n
    for (action, field), n in sorted(groups.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        print(f"  {action:6} {field:28} {n}")
    print(f"  kept existing value (not overwritten): {len(kept_all)}")
    for fn, f in kept_all:
        print(f"    {f}: {fn}")
    if errors:
        print(f"ERRORS ({len(errors)}): papers skipped")
        for fn, e in errors:
            print(f"    {fn}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
