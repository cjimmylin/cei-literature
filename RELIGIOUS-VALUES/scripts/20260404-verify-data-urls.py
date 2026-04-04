#!/usr/bin/env python3
"""Verify DATA_URL accessibility for gate-passing religious benchmark candidates.

Agent 7: DATA_URL Verification.
Checks HTTP accessibility of all DATA_URLs in the v2 feature matrix,
classifies each as VERIFIED_ACCESSIBLE / AUTH_REQUIRED / NOT_FOUND / etc.,
and scores the O1 (data actually accessible) feature.

Output: RELIGIOUS-VALUES/data/20260404-data-availability-verification.json
"""
from __future__ import annotations

import json
import time
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
from requests.exceptions import (
    ConnectionError,
    Timeout,
    TooManyRedirects,
    RequestException,
)

# ---------- paths ----------
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
INPUT_FILE = DATA_DIR / "20260404-religious-benchmark-feature-matrix-v2.json"
OUTPUT_FILE = DATA_DIR / "20260404-data-availability-verification.json"

TIMEOUT_SEC = 15
DELAY_SEC = 2  # polite crawl delay

# User-Agent so sites don't block us as a bare script
HEADERS = {
    "User-Agent": "Mozilla/5.0 (CEI-Literature-Vault academic research link checker)"
}


# ---------- helpers ----------
def classify_status(status_code: int | None, error_type: str | None) -> str:
    """Map HTTP status / error to accessibility category."""
    if error_type == "TIMEOUT":
        return "TIMEOUT"
    if error_type == "INVALID_URL":
        return "INVALID_URL"
    if error_type:
        return "SERVER_ERROR"  # connection error etc.
    if status_code is None:
        return "SERVER_ERROR"
    if status_code in (200, 202):
        # 202 Accepted is used by Harvard Dataverse for citation pages
        return "VERIFIED_ACCESSIBLE"
    if status_code in (301, 302, 303, 307, 308):
        # We follow redirects, so if final status is still 3xx something is odd
        return "REDIRECT_ACCESSIBLE"
    if status_code in (401, 403):
        return "AUTH_REQUIRED"
    if status_code == 404:
        return "NOT_FOUND"
    if 500 <= status_code < 600:
        return "SERVER_ERROR"
    # Other codes (e.g. 429 rate-limit)
    if 400 <= status_code < 500:
        return "AUTH_REQUIRED"  # treat 4xx as access issue
    return "SERVER_ERROR"


def check_url(url: str) -> dict:
    """Check a single URL. Returns dict with status info."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return {
            "http_status": None,
            "content_type": None,
            "content_length": None,
            "accessibility": "INVALID_URL",
            "notes": f"Malformed URL: {url}",
        }

    # Try HEAD first (lighter)
    try:
        resp = requests.head(
            url,
            timeout=TIMEOUT_SEC,
            headers=HEADERS,
            allow_redirects=True,
        )
        status = resp.status_code
        ctype = resp.headers.get("Content-Type", "")
        clength = resp.headers.get("Content-Length")

        # Some servers return 405 for HEAD — fall through to GET
        if status in (405, 501):
            raise RequestException("HEAD not allowed, trying GET")

        # HuggingFace sometimes returns 200 on HEAD but actual page has
        # "gated" or "private" — we'll accept 200 at face value unless
        # we know the pattern
        accessibility = classify_status(status, None)
        notes = _make_notes(url, status, ctype)
        return {
            "http_status": status,
            "content_type": ctype,
            "content_length": clength,
            "accessibility": accessibility,
            "notes": notes,
        }

    except Timeout:
        pass  # fall through to GET
    except (ConnectionError, TooManyRedirects) as e:
        # Try GET before giving up
        pass
    except RequestException:
        pass  # 405 etc — try GET

    # Try GET with stream=True (download only headers)
    try:
        resp = requests.get(
            url,
            timeout=TIMEOUT_SEC,
            headers=HEADERS,
            allow_redirects=True,
            stream=True,
        )
        status = resp.status_code
        ctype = resp.headers.get("Content-Type", "")
        clength = resp.headers.get("Content-Length")

        # For HuggingFace dataset pages, check if the response body
        # contains "gated" or "private" indicators
        body_snippet = ""
        if "huggingface.co" in url and status == 200:
            # Read first 5KB to check for gating
            chunk = resp.raw.read(5000)
            body_snippet = chunk.decode("utf-8", errors="replace")
            if "Access to this resource is restricted" in body_snippet:
                resp.close()
                return {
                    "http_status": status,
                    "content_type": ctype,
                    "content_length": clength,
                    "accessibility": "AUTH_REQUIRED",
                    "notes": "HuggingFace gated dataset — access restricted",
                }
        resp.close()

        accessibility = classify_status(status, None)
        notes = _make_notes(url, status, ctype)
        return {
            "http_status": status,
            "content_type": ctype,
            "content_length": clength,
            "accessibility": accessibility,
            "notes": notes,
        }

    except Timeout:
        return {
            "http_status": None,
            "content_type": None,
            "content_length": None,
            "accessibility": "TIMEOUT",
            "notes": f"No response within {TIMEOUT_SEC}s",
        }
    except (ConnectionError, TooManyRedirects) as e:
        return {
            "http_status": None,
            "content_type": None,
            "content_length": None,
            "accessibility": "SERVER_ERROR",
            "notes": f"Connection error: {type(e).__name__}: {str(e)[:100]}",
        }
    except RequestException as e:
        return {
            "http_status": None,
            "content_type": None,
            "content_length": None,
            "accessibility": "SERVER_ERROR",
            "notes": f"Request error: {type(e).__name__}: {str(e)[:100]}",
        }


def _make_notes(url: str, status: int, ctype: str) -> str:
    """Generate human-readable notes about the check."""
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    parts = []

    if "github.com" in host:
        parts.append("GitHub repo")
    elif "huggingface.co" in host:
        if "/datasets/" in url:
            parts.append("HuggingFace dataset")
        else:
            parts.append("HuggingFace model/org page")
    elif "kaggle.com" in host:
        parts.append("Kaggle dataset")
    elif "mendeley.com" in host:
        parts.append("Mendeley Data repository")
    elif "doi.org" in host:
        parts.append("DOI redirect")
    else:
        parts.append(f"Website ({host})")

    if status != 200:
        parts.append(f"HTTP {status}")

    if ctype:
        ct_short = ctype.split(";")[0].strip()
        if ct_short:
            parts.append(ct_short)

    return " — ".join(parts)


def split_urls(raw_url: str) -> list[str]:
    """Split compound URL fields (some entries have multiple URLs separated by
    comma, semicolon, or space)."""
    if not raw_url:
        return []
    # Normalize separators
    for sep in [" ; ", " , ", ";", ","]:
        if sep in raw_url:
            return [u.strip() for u in raw_url.split(sep) if u.strip()]
    return [raw_url.strip()]


# ---------- main ----------
def main():
    print("Loading feature matrix...", flush=True)
    with open(INPUT_FILE) as f:
        data = json.load(f)

    entries = data["entries"]
    gate_passers = [e for e in entries if e.get("passes_gates")]
    print(f"Total entries: {len(entries)}, gate passers: {len(gate_passers)}", flush=True)

    results = []
    summary = {
        "VERIFIED_ACCESSIBLE": 0,
        "REDIRECT_ACCESSIBLE": 0,
        "AUTH_REQUIRED": 0,
        "NOT_FOUND": 0,
        "SERVER_ERROR": 0,
        "TIMEOUT": 0,
        "NO_URL": 0,
        "INVALID_URL": 0,
    }

    for i, entry in enumerate(gate_passers):
        eid = entry["id"]
        stitle = entry.get("short_title", "")
        data_url = entry.get("DATA_URL", "") or ""
        p3_avail = entry.get("P3_data_availability", "")
        p3_url = entry.get("P3_url", "")

        if not data_url.strip():
            result = {
                "id": eid,
                "short_title": stitle,
                "data_url": data_url,
                "p3_availability": p3_avail,
                "http_status": None,
                "content_type": None,
                "accessibility": "NO_URL",
                "O1_accessible": False,
                "notes": "No DATA_URL in feature matrix",
            }
            results.append(result)
            summary["NO_URL"] += 1
            print(f"  [{i+1}/{len(gate_passers)}] id={eid:3d} NO_URL  {stitle[:50]}", flush=True)
            continue

        # Some entries have multiple URLs — check all, use best result
        urls = split_urls(data_url)
        best_result = None
        all_checks = []

        for url in urls:
            print(f"  [{i+1}/{len(gate_passers)}] id={eid:3d} checking {url[:70]}...", flush=True)
            check = check_url(url)
            all_checks.append({"url": url, **check})

            # Keep the best (most accessible) result
            if best_result is None:
                best_result = check
                best_result["checked_url"] = url
            elif (
                check["accessibility"] in ("VERIFIED_ACCESSIBLE", "REDIRECT_ACCESSIBLE")
                and best_result["accessibility"] not in ("VERIFIED_ACCESSIBLE", "REDIRECT_ACCESSIBLE")
            ):
                best_result = check
                best_result["checked_url"] = url

            # Polite delay
            time.sleep(DELAY_SEC)

        accessibility = best_result["accessibility"]
        o1 = accessibility in ("VERIFIED_ACCESSIBLE", "REDIRECT_ACCESSIBLE")

        result = {
            "id": eid,
            "short_title": stitle,
            "data_url": data_url,
            "p3_availability": p3_avail,
            "http_status": best_result.get("http_status"),
            "content_type": best_result.get("content_type"),
            "accessibility": accessibility,
            "O1_accessible": o1,
            "notes": best_result.get("notes", ""),
        }
        if len(urls) > 1:
            result["all_url_checks"] = all_checks

        results.append(result)
        summary[accessibility] += 1
        status_str = f"HTTP {best_result.get('http_status', '?')}"
        print(f"       -> {accessibility} ({status_str})  {stitle[:50]}", flush=True)

    # Compute gate impact
    current_passers = len(gate_passers)
    would_fail = [r for r in results if not r["O1_accessible"]]
    would_fail_ids = [
        {"id": r["id"], "short_title": r["short_title"], "accessibility": r["accessibility"]}
        for r in would_fail
    ]

    output = {
        "generated": "20260404",
        "total_checked": len(results),
        "summary": summary,
        "results": results,
        "gate_impact": {
            "current_gate_passers": current_passers,
            "verified_accessible": sum(1 for r in results if r["O1_accessible"]),
            "would_fail_data_gate_after_verification": len(would_fail),
            "affected_entries": would_fail_ids,
        },
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}", flush=True)
    print(f"DATA_URL Verification Complete", flush=True)
    print(f"{'='*60}", flush=True)
    print(f"Total checked: {len(results)}", flush=True)
    for cat, count in summary.items():
        if count > 0:
            print(f"  {cat}: {count}", flush=True)
    print(f"\nGate impact:", flush=True)
    print(f"  Current gate passers: {current_passers}", flush=True)
    print(f"  Verified accessible:  {output['gate_impact']['verified_accessible']}", flush=True)
    print(f"  Would FAIL data gate: {len(would_fail)}", flush=True)
    if would_fail:
        print(f"\n  Affected entries:", flush=True)
        for w in would_fail_ids:
            print(f"    id={w['id']:3d} [{w['accessibility']}] {w['short_title'][:50]}", flush=True)
    print(f"\nOutput: {OUTPUT_FILE}", flush=True)


if __name__ == "__main__":
    main()
