#!/usr/bin/env python3
"""
Restore frontmatter values damaged by commit 5caae838f (2026-07-09).

That commit ("INNOVATION Cycle-1 CLOSED") rewrote the frontmatter of all 2,385
papers that existed at the time. Collateral damage:
  - ethics_overall: every paper set to `No` (the field is a 0-100 integer since
    2026-03-13, see yaml-standards.md), losing all scores          -> 2,385 papers
  - year: set to `2025` (each previously matched its filename year) -> 1,270 papers
  - abstract: truncated, mostly at the first embedded quote          ->    40 papers
  - authors: block lists emptied                                     ->     4 papers
  - short_title / title: blanked / garbled                           ->     2 papers
(The same commit also dropped stray `"N/A"` continuation lines under local_pdf /
pdf_extract and emptied 17 `tags` lists on purpose; those are left as they are.)

A field is restored only when the paper's current text for it is still exactly
what 5caae838f wrote (nobody has edited it since). Values come from the parent
commit 296fdf0b6:
  - year, ethics_overall, abstract: the exact original line
  - authors: the original names as the corpus-standard one-line string
    `authors: "A; B; C"` (multi-item block lists fail validate_all_papers.py)
  - title, short_title (and a multi-line original abstract): the original text
    as one valid quoted line
Re-running is safe: already-restored fields are counted, not re-written.

YAML safety: only whole single lines inside the frontmatter are replaced
(re.subn count=1, re.MULTILINE); no parse -> rebuild round-trip
(learnings-log 2026-02-07). No deletions.

Usage:
    python3 PYTHON/fix_july9_frontmatter.py            # dry run (default)
    python3 PYTHON/fix_july9_frontmatter.py --apply    # write changes
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

WS_ROOT = Path(__file__).resolve().parent.parent
GOOD_COMMIT = "296fdf0b62e5e86729302aa30e74884564fa2529"  # parent of the bad commit
BAD_COMMIT = "5caae838f9ab92e47abea7360041792ee3c06cfe"   # 2026-07-09 bulk rewrite
EXACT_FIELDS = ("year", "ethics_overall", "abstract")
REBUILT_FIELDS = ("authors", "title", "short_title")
FIELDS = EXACT_FIELDS + REBUILT_FIELDS
FM_RE = re.compile(r"\A---\n(.*?)\n---(?:\n|\Z)", re.DOTALL)
KEY_RE = re.compile(r"^[A-Za-z_][^:\n]*:")


def git(*args):
    return subprocess.run(["git", *args], cwd=WS_ROOT, check=True,
                          capture_output=True, text=True).stdout


class Blobs:
    """Read many files from git history through one `git cat-file --batch` process."""

    def __init__(self):
        self.p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=WS_ROOT,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read(self, commit, path):
        self.p.stdin.write(f"{commit}:{path}\n".encode())
        self.p.stdin.flush()
        header = self.p.stdout.readline().decode()
        if header.endswith("missing\n"):
            return None
        size = int(header.split()[2])
        data = self.p.stdout.read(size)
        self.p.stdout.read(1)  # trailing newline
        return data.decode("utf-8")


def field_block(frontmatter, field):
    """Lines of `field` (its key line plus any continuation lines), or None."""
    lines = frontmatter.split("\n")
    for i, line in enumerate(lines):
        if line.startswith(field + ":"):
            j = i + 1
            while j < len(lines) and not KEY_RE.match(lines[j]):
                j += 1
            return lines[i:j]
    return None


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v.strip()


def list_items(block):
    return [unquote(l.strip()[1:]).strip("[]").strip() for l in block[1:] if l.strip().startswith("-")]


def value(field, block):
    """Field value with quoting/escaping/line-folding ignored (formatting-only edits compare equal)."""
    if field == "authors" and list_items(block):
        return "; ".join(list_items(block))
    text = " ".join([block[0].split(":", 1)[1].strip()] + [l.strip() for l in block[1:]])
    return unquote(text).replace('\\"', '"').replace("''", "'").strip()


def quoted(text):
    if '"' in text:
        return "'" + text.replace("'", "''") + "'"
    return '"' + text + '"'


def rebuilt_line(field, good_block):
    """One-line replacement for a block-list / multi-line / malformed original value."""
    if field == "authors":
        names = list_items(good_block)
        if not names:
            return None
        return f'authors: "{"; ".join(names)}"'
    text = " ".join([good_block[0].split(":", 1)[1].strip()] + [l.strip() for l in good_block[1:]])
    text = unquote(text)
    return f"{field}: {quoted(text)}" if text else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()

    # -z: raw NUL-separated paths, so non-ASCII filenames are not quoted/escaped.
    paths = [p for p in git("ls-tree", "-r", "-z", "--name-only", GOOD_COMMIT, "--", "papers/").split("\0")
             if p.endswith(".md")]
    blobs = Blobs()
    stats = Counter()
    skipped = []
    changes = []

    for rel in paths:
        good = blobs.read(GOOD_COMMIT, rel)
        bad = blobs.read(BAD_COMMIT, rel)
        cur_path = WS_ROOT / rel
        if bad is None or not cur_path.exists():
            stats["not_in_bad_or_head"] += 1
            continue
        cur = cur_path.read_text(encoding="utf-8")
        mg, mb, mc = FM_RE.match(good), FM_RE.match(bad), FM_RE.match(cur)
        if not (mg and mb and mc):
            skipped.append((rel, "*", "frontmatter not found"))
            continue
        fm = mc.group(1)
        new_fm = fm
        for field in FIELDS:
            g, b, c = field_block(mg.group(1), field), field_block(mb.group(1), field), field_block(fm, field)
            if g == b or (g is not None and b is not None and value(field, g) == value(field, b)):
                continue  # not damaged (unchanged, or a formatting-only edit)
            if g is None or b is None or c is None:
                skipped.append((rel, field, "field missing at good/bad/current"))
                continue
            if len(b) != 1:
                skipped.append((rel, field, "damaged value spans several lines"))
                continue
            if field in EXACT_FIELDS and len(g) == 1:
                target = g[0]
            else:
                target = rebuilt_line(field, g)
                if target is None:
                    skipped.append((rel, field, "could not rebuild original value"))
                    continue
            if c == [target]:
                stats[f"already_restored_{field}"] += 1
                continue
            if c != b:
                skipped.append((rel, field, f"edited since bad commit: {c[0][:60]!r}"))
                continue
            new_fm, n = re.subn(rf"^{re.escape(field)}:.*$", lambda _m, t=target: t, new_fm, count=1, flags=re.MULTILINE)
            assert n == 1
            stats[f"restored_{field}"] += 1
            changes.append({"file": rel, "field": field, "from": c[0], "to": target})
        if new_fm != fm:
            new = cur[:mc.start(1)] + new_fm + cur[mc.end(1):]
            # Safety: only single lines of the targeted fields may differ.
            old_lines, new_lines = cur.split("\n"), new.split("\n")
            assert len(old_lines) == len(new_lines), rel
            diff = [(a, z) for a, z in zip(old_lines, new_lines) if a != z]
            assert all(a.split(":", 1)[0] in FIELDS and z.split(":", 1)[0] == a.split(":", 1)[0] for a, z in diff), rel
            stats["files_changed"] += 1
            if args.apply:
                cur_path.write_text(new, encoding="utf-8")

    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Papers at {GOOD_COMMIT[:9]}: {len(paths)}")
    for k, v in sorted(stats.items()):
        print(f"  {k:34s} {v}")
    print(f"  skipped                            {len(skipped)}")
    for s in skipped[:20]:
        print("    ", s)
    for c in changes:
        if c["field"] in REBUILT_FIELDS:
            print(f"  {c['field']}: {c['file'][7:60]} -> {c['to'][:110]}")
    if args.apply and changes:
        out = WS_ROOT / "logs" / "20261018-fix-july9-frontmatter.json"
        out.write_text(json.dumps({"good_commit": GOOD_COMMIT, "bad_commit": BAD_COMMIT,
                                   "stats": stats, "skipped": skipped, "changes": changes},
                                  indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"Change log: {out.relative_to(WS_ROOT)} (gitignored; summary goes in the .md log)")


if __name__ == "__main__":
    sys.exit(main())
