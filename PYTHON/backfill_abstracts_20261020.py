#!/usr/bin/env python3
"""Fill the empty `abstract` of 24 scholarly notes from OpenAlex, Crossref and Semantic Scholar.

Written 2026-10-20 for the owner's machine. The cloud session that made the 2026-10-19 vault fixes
could not reach OpenAlex or Semantic Scholar (rate-limited), so these 24 notes kept an empty
abstract. The list is in logs/20261019d-low14-scores-metadata-abstracts.md
("Scholarly works still without an abstract"); one entry there was retired since and is left out.

For each note it looks up, in this order:
  1. OpenAlex by the note's DOI, then Crossref by DOI, then Semantic Scholar by DOI;
  2. if there is no DOI or no abstract was found, a title search in OpenAlex, Crossref and Semantic
     Scholar.
A candidate is ACCEPTED only when:
  - its DOI equals the note's DOI, or
  - its title matches the note's title exactly once both are lower-cased and stripped of
    punctuation (or the note's title, which is often cut short, is a prefix of at least 40
    characters), AND either the note's first-author surname appears among the candidate's
    authors (a different year is then only recorded, since many notes carry the year they were
    added), or, when the note names no real author, the year is within 1 of the note's year.
The abstract must be at least 150 characters. HTML/JATS tags are removed.

Nothing is written unless --apply is given. Each write is a single-line edit of `abstract:` with
the vault's safe editor (.agent/lib/paper_utils.update_paper_field). Every decision, accepted or
not, is written to logs/abstract-backfill/20261020-results.json so the change can be reviewed.

Usage (from the vault root, on a new branch):
    git checkout -b abstracts-20261020
    python3 PYTHON/backfill_abstracts_20261020.py           # dry run: show what it would write
    python3 PYTHON/backfill_abstracts_20261020.py --apply   # write the accepted abstracts
Polite: about one request per second; takes 2-4 minutes. Needs only the Python standard library.
"""
import argparse
import difflib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".agent"))
os.environ.setdefault("VAULT_PDF_PATH", str(ROOT))  # paper_utils needs a PDF path; unused here

NOTES = [
    "2005-Huffer-Governance Corruption and Ethics in the",
    "2005-Teaiwa-Articulated Cultures Militarism and Masculinities in",
    "2012-Kaitani-Bridging The Gap The Changing Reproductive",
    "2012-Konrad-Collaborators collaborating counterparts in anthropological",
    "2016-Purcell-Variation in postharvest processing of sea",
    "2018-Geno-Governance Ethics and Leadership in Papua",
    "2020-Hongladarom-AI for Social Good Buddhist Compassion",
    "2023-Kaganovich-Style Transfer Modern Hebrew Literature Using",
    "2024-Duwairi-A Deep Learning Framework for Automatic Detection of Hate Speech",
    "2024-Kuriyozov-Construction and Evaluation of Sentiment Datasets for Low-Resource",
    "2024-Unknown-A structured sentiment analysis dataset based on public comments from",
    "2025-Ablimit-A multilingual language processing tool for Uyghur Kazak and Kirghiz",
    "2025-Aly-Applying Data Feminism Principles to Assess Bias in English and",
    "2025-Binegde-Exploring cultural commonsense in multilingual large language models",
    "2025-Firmino-Improving hate speech detection using Cross-Lingual Learning -",
    "2025-He-Flood control data push method of",
    "2025-Jim-Recent advancements and challenges of NLP-based sentiment analysis A",
    "2025-Lim-How Do Users Identify and Perceive Stereotypes Understanding User",
    "2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics",
    "2025-Pretrained-Research on the Training and Application Methods of a Lightweight",
    "2025-Shi-Benchmarking four large language models’ performance of addressing",
    "2025-Unknown-Is ChatGPT A Good Translator A Preliminary Study",
    "2025-Xiang-Diagnosing the bias iceberg in large language models A three-level",
    "2025-Xiangfeng-A dataset of Mongolian Tibetan and Uyghur speech fragments based on",
]
NOT_AUTHORS = {"unknown", "pretrained", "translation", "authors", "n/a", "na", ""}
UA = "cei-literature-vault/1.0 (abstract backfill; python urllib)"
RESULTS = ROOT / "logs" / "abstract-backfill" / "20261020-results.json"  # logs/*.json is gitignored


# --------------------------------------------------------------------------- network
def get_json(url):
    """GET a JSON URL with up to 3 tries. Falls back to curl if Python's SSL setup fails (macOS)."""
    for attempt in range(3):
        time.sleep(1.0)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            return None
        except urllib.error.URLError as e:
            if "CERTIFICATE" in str(e).upper() and shutil.which("curl"):
                out = subprocess.run(["curl", "-s", "-f", "--max-time", "30", "-A", UA, url],
                                     capture_output=True, text=True)
                if out.returncode == 0 and out.stdout.strip():
                    try:
                        return json.loads(out.stdout)
                    except ValueError:
                        return None
                return None
            time.sleep(3)
        except (TimeoutError, ValueError):
            time.sleep(3)
    return None


# --------------------------------------------------------------------------- text helpers
def norm(t):
    t = html.unescape(t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def clean_abstract(a):
    a = re.sub(r"<[^>]+>", " ", a or "")
    a = html.unescape(a)
    a = re.sub(r"\s+", " ", a).strip()
    return re.sub(r"^(abstract|summary)\s*[:.\-—]*\s*", "", a, flags=re.I)


def openalex_abstract(w):
    inv = (w or {}).get("abstract_inverted_index") or {}
    pos = {i: word for word, idxs in inv.items() for i in idxs}
    return " ".join(pos[i] for i in sorted(pos))


def bare_doi(d):
    d = (d or "").strip().strip('"').lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = d.split("/html")[0].rstrip(".")
    return d if d.startswith("10.") else ""


def read_note(path):
    text = path.read_text(encoding="utf-8")
    fm = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S).group(1)

    def field(name):
        m = re.search(rf"^{re.escape(name)}:[ \t]*(.*)$", fm, re.M)
        return (m.group(1).strip().strip('"') if m else "")
    title = field("short_title") or field("title")
    h1 = re.search(r"^# (.+)$", text[len(fm):], re.M)
    if h1 and len(h1.group(1)) > len(title):
        title = h1.group(1).strip()
    first = re.sub(r"[\[\]]", "", field("first_author"))
    surname = first.split(",")[0].split()[-1] if first.strip() else ""
    year = field("year")
    return {"title": title, "doi": bare_doi(field("doi")), "url": field("url"),
            "year": int(year) if year.isdigit() else None,
            "surname": "" if surname.lower() in NOT_AUTHORS else surname,
            "abstract": field("abstract")}


# --------------------------------------------------------------------------- candidates
def from_openalex(w, src):
    if not w:
        return None
    authors = [a.get("author", {}).get("display_name", "") for a in w.get("authorships", [])]
    return {"source": src, "title": w.get("title") or "", "doi": bare_doi(w.get("doi")),
            "year": w.get("publication_year"), "authors": authors,
            "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
            "abstract": clean_abstract(openalex_abstract(w))}


def from_crossref(m, src):
    if not m:
        return None
    yr = ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0]
    return {"source": src, "title": (m.get("title") or [""])[0], "doi": bare_doi(m.get("DOI")),
            "year": yr, "authors": [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in m.get("author", [])],
            "venue": (m.get("container-title") or [""])[0], "abstract": clean_abstract(m.get("abstract", ""))}


def from_s2(p, src):
    if not p:
        return None
    return {"source": src, "title": p.get("title") or "", "doi": bare_doi((p.get("externalIds") or {}).get("DOI")),
            "year": p.get("year"), "authors": [a.get("name", "") for a in p.get("authors") or []],
            "venue": p.get("venue") or "", "abstract": clean_abstract(p.get("abstract") or "")}


S2_FIELDS = "title,abstract,year,authors,venue,externalIds"


def candidates(note):
    out = []
    q = urllib.parse.quote
    if note["doi"]:
        d = note["doi"]
        out.append(from_openalex(get_json(f"https://api.openalex.org/works/doi:{q(d)}"), "openalex-doi"))
        cr = get_json(f"https://api.crossref.org/works/{q(d)}")
        out.append(from_crossref((cr or {}).get("message"), "crossref-doi"))
        out.append(from_s2(get_json(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{q(d)}?fields={S2_FIELDS}"), "s2-doi"))
    if not any(c and len(c["abstract"]) >= 150 for c in out) and len(norm(note["title"])) >= 20:
        t = q(note["title"][:200])
        r = get_json(f"https://api.openalex.org/works?per-page=5&search={t}")
        out += [from_openalex(w, "openalex-search") for w in (r or {}).get("results", [])]
        r = get_json(f"https://api.crossref.org/works?rows=5&query.bibliographic={t}")
        out += [from_crossref(m, "crossref-search") for m in ((r or {}).get("message") or {}).get("items", [])]
        r = get_json(f"https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields={S2_FIELDS}&query={t}")
        out += [from_s2(p, "s2-search") for p in (r or {}).get("data", []) or []]
    return [c for c in out if c]


def judge(note, c):
    """Return (accepted, reason)."""
    if len(c["abstract"]) < 150:
        return False, "no abstract (or under 150 characters)"
    if note["doi"] and c["doi"] == note["doi"]:
        return True, "DOI match"
    nt, ct = norm(note["title"]), norm(c["title"])
    title_ok = nt == ct or (len(nt) >= 40 and ct.startswith(nt))
    if not title_ok:
        return False, f"title differs (similarity {difflib.SequenceMatcher(None, nt, ct).ratio():.2f})"
    year_off = bool(note["year"] and c["year"] and abs(int(c["year"]) - note["year"]) > 1)
    if note["surname"]:
        if not any(norm(note["surname"]) in norm(a) for a in c["authors"]):
            return False, f"title matches but first author '{note['surname']}' not among authors"
        if year_off:  # many notes carry the year they were added, not the publication year
            return True, f"exact title match, author consistent; year differs ({c['year']} vs note {note['year']})"
        return True, "exact title match, year and author consistent"
    if year_off:
        return False, f"title matches but year {c['year']} vs note {note['year']} and no author to confirm"
    return True, "exact title match, year consistent (no author on the note to confirm)"


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true", help="write accepted abstracts (default: dry run)")
    args = ap.parse_args()

    from lib import paper_utils as pu

    results, n_ok = [], 0
    for i, name in enumerate(NOTES, 1):
        path = ROOT / "papers" / f"{name}.md"
        rec = {"note": name}
        if not path.exists():
            rec["outcome"] = "note not found (renamed or retired?)"
            print(f"[{i:2}/{len(NOTES)}] SKIP  {name[:60]}: note not found")
            results.append(rec)
            continue
        note = read_note(path)
        if note["abstract"]:
            rec["outcome"] = "already has an abstract"
            print(f"[{i:2}/{len(NOTES)}] SKIP  {name[:60]}: already has an abstract")
            results.append(rec)
            continue
        best, reasons = None, []
        for c in candidates(note):
            ok, why = judge(note, c)
            reasons.append({"source": c["source"], "title": c["title"][:150], "doi": c["doi"],
                            "year": c["year"], "venue": c["venue"][:80], "accepted": ok, "reason": why})
            if ok and (best is None or len(c["abstract"]) > len(best[0]["abstract"])):
                best = (c, why)
        rec.update(note_title=note["title"], note_doi=note["doi"], candidates=reasons)
        if best:
            c, why = best
            rec.update(outcome="accepted", source=c["source"], doi=c["doi"], venue=c["venue"],
                       found_title=c["title"], reason=why, abstract=c["abstract"])
            n_ok += 1
            print(f"[{i:2}/{len(NOTES)}] FOUND {name[:60]}\n        {c['source']}: {why}; "
                  f"'{c['title'][:70]}' ({c['venue'][:40]}, {c['year']}); {len(c['abstract'])} chars")
            if args.apply:
                if not pu.update_paper_field(path, "abstract", c["abstract"]):
                    rec["outcome"] = "accepted but the write failed"
                    print("        WRITE FAILED")
        else:
            rec["outcome"] = "no acceptable match"
            print(f"[{i:2}/{len(NOTES)}] NONE  {name[:60]} ({len(reasons)} candidates checked)")
        results.append(rec)

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps({"applied": args.apply, "accepted": n_ok, "notes": results},
                                  indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n{n_ok} of {len(NOTES)} notes have an accepted abstract. "
          f"{'Written to the notes.' if args.apply else 'Dry run: nothing written.'}")
    print(f"Details: {RESULTS}")


if __name__ == "__main__":
    main()
