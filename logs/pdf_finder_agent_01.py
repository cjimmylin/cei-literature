#!/usr/bin/env python3
"""PDF Discovery Agent 01 - Find downloadable PDF URLs for missing papers."""

import json
import time
import urllib.parse
import subprocess
import re
import sys
import os

INPUT_FILE = "logs/20260216-missing_pdfs_batch_01.json"
OUTPUT_FILE = "logs/20260216-missing_pdfs_agent_01.json"

def load_papers():
    with open(INPUT_FILE) as f:
        return json.load(f)

def save_results(results):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def curl_json(url, timeout=30):
    """Run curl and return parsed JSON, or None on failure."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "--max-time", str(timeout), url],
            capture_output=True, text=True, timeout=timeout+5
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
    except (json.JSONDecodeError, subprocess.TimeoutExpired, Exception) as e:
        print(f"  curl error for {url[:80]}: {e}", flush=True)
    return None

def curl_head_check(url, timeout=15):
    """Check if URL returns a valid PDF (200 status, content-type application/pdf)."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-I", "--max-time", str(timeout), url],
            capture_output=True, text=True, timeout=timeout+5
        )
        output = result.stdout.lower()
        has_200 = "200" in output.split("\n")[0] if output else False
        has_pdf = "application/pdf" in output
        return has_200 and has_pdf
    except Exception:
        return False

def extract_arxiv_id(url):
    """Extract arXiv ID from URL."""
    if not url:
        return None
    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    if m:
        return m.group(1)
    return None

def try_arxiv(paper):
    """Try to find PDF via arXiv."""
    for field in ['url', 'external_pdf']:
        val = paper.get(field, '')
        if val and 'arxiv.org' in val:
            aid = extract_arxiv_id(val)
            if aid:
                pdf_url = f"https://arxiv.org/pdf/{aid}.pdf"
                return pdf_url
    return None

def try_acl(paper):
    """Try ACL Anthology."""
    url = paper.get('url', '')
    if url and 'aclanthology.org' in url:
        if not url.endswith('.pdf'):
            pdf_url = url.rstrip('/') + '.pdf'
        else:
            pdf_url = url
        return pdf_url
    return None

def try_direct_pdf_url(paper):
    """Check if external_pdf or url is already a direct PDF link."""
    for field in ['external_pdf', 'url']:
        val = paper.get(field, '')
        if val and val not in ['', 'N/A']:
            if val.lower().endswith('.pdf'):
                return val
            # Some known PDF patterns
            if 'nlm.nih.gov' in val and '/pdf/' in val:
                return val
            if 'iospress.nl/pdf/' in val:
                return val
            if 'techrxiv.org/doi/pdf/' in val:
                return val
            if 'ieeexplore.ieee.org/ielx' in val and '.pdf' in val:
                return val
            if 'ieee.org/ielx' in val and '.pdf' in val:
                return val
    return None

def try_mdpi_open_access(paper):
    """MDPI papers are open access - construct PDF URL."""
    url = paper.get('url', '')
    if url and 'mdpi.com' in url:
        # MDPI pattern: https://www.mdpi.com/JOURNAL/VOL/ISSUE/ARTICLE -> add /pdf
        if '/pdf' not in url:
            pdf_url = url.rstrip('/') + '/pdf'
            return pdf_url
    return None

def try_unpaywall(paper):
    """Try Unpaywall API."""
    doi = paper.get('doi', '')
    if not doi:
        return None
    encoded_doi = urllib.parse.quote(doi, safe='')
    api_url = f"https://api.unpaywall.org/v2/{encoded_doi}?email=research@cei-literature.org"
    data = curl_json(api_url)
    if data:
        # Check best_oa_location first
        best = data.get('best_oa_location', {})
        if best and best.get('url_for_pdf'):
            return best['url_for_pdf']
        # Check all oa_locations
        for loc in data.get('oa_locations', []):
            if loc.get('url_for_pdf'):
                return loc['url_for_pdf']
    return None

def try_semantic_scholar(paper):
    """Try Semantic Scholar API."""
    title = paper.get('short_title', '')
    if not title or len(title) < 10:
        return None
    encoded_title = urllib.parse.quote(title)
    api_url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded_title}&fields=openAccessPdf&limit=1"
    data = curl_json(api_url)
    if data and data.get('data'):
        for item in data['data']:
            oap = item.get('openAccessPdf')
            if oap and oap.get('url'):
                return oap['url']
    return None

def try_doi_redirect(paper):
    """For papers with DOI but no PDF found yet, try resolving doi.org and check for open access."""
    doi = paper.get('doi', '')
    if not doi:
        return None
    # Some DOIs resolve to open-access pages
    # Check if it's a known open-access publisher
    if 'dsj-2020' in doi or '10.5334/' in doi:
        # Data Science Journal - open access
        return f"https://datascience.codata.org/articles/{doi}/galley/{doi.split('/')[-1]}/download/"
    return None

def process_papers():
    papers = load_papers()
    results = []

    print(f"Processing {len(papers)} papers...", flush=True)

    # Phase 1: Quick wins (arXiv, ACL, direct PDF, MDPI)
    phase1_remaining = []
    for i, paper in enumerate(papers):
        fn = paper['filename']

        # Try direct PDF URL first
        pdf_url = try_direct_pdf_url(paper)
        if pdf_url:
            print(f"[{i+1}] DIRECT: {fn[:60]}", flush=True)
            results.append({
                "filename": fn,
                "found": True,
                "pdf_url": pdf_url,
                "source": "direct_url"
            })
            continue

        # Try arXiv
        pdf_url = try_arxiv(paper)
        if pdf_url:
            print(f"[{i+1}] ARXIV: {fn[:60]}", flush=True)
            results.append({
                "filename": fn,
                "found": True,
                "pdf_url": pdf_url,
                "source": "arxiv"
            })
            continue

        # Try ACL
        pdf_url = try_acl(paper)
        if pdf_url:
            print(f"[{i+1}] ACL: {fn[:60]}", flush=True)
            results.append({
                "filename": fn,
                "found": True,
                "pdf_url": pdf_url,
                "source": "acl"
            })
            continue

        # Try MDPI
        pdf_url = try_mdpi_open_access(paper)
        if pdf_url:
            print(f"[{i+1}] MDPI: {fn[:60]}", flush=True)
            results.append({
                "filename": fn,
                "found": True,
                "pdf_url": pdf_url,
                "source": "mdpi"
            })
            continue

        # Try direct URL for ANLP proceedings (direct PDF link in URL)
        url = paper.get('url', '')
        if url and url.endswith('.pdf'):
            print(f"[{i+1}] DIRECT_URL: {fn[:60]}", flush=True)
            results.append({
                "filename": fn,
                "found": True,
                "pdf_url": url,
                "source": "direct_url"
            })
            continue

        phase1_remaining.append((i, paper))

    print(f"\nPhase 1 complete: {len(results)} found, {len(phase1_remaining)} remaining", flush=True)
    save_results(results)

    # Phase 2: Unpaywall for papers with DOIs
    phase2_remaining = []
    for i, paper in phase1_remaining:
        fn = paper['filename']
        doi = paper.get('doi', '')

        if doi:
            print(f"[{i+1}] UNPAYWALL: {fn[:60]}...", flush=True)
            pdf_url = try_unpaywall(paper)
            time.sleep(1)

            if pdf_url:
                print(f"  -> FOUND: {pdf_url[:80]}", flush=True)
                results.append({
                    "filename": fn,
                    "found": True,
                    "pdf_url": pdf_url,
                    "source": "unpaywall"
                })
                save_results(results)
                continue

        phase2_remaining.append((i, paper))

    print(f"\nPhase 2 complete: {len(results)} found, {len(phase2_remaining)} remaining", flush=True)
    save_results(results)

    # Phase 3: Semantic Scholar for remaining
    phase3_remaining = []
    for i, paper in phase2_remaining:
        fn = paper['filename']
        title = paper.get('short_title', '')

        if title and len(title) >= 10:
            print(f"[{i+1}] SEMANTIC_SCHOLAR: {fn[:60]}...", flush=True)
            pdf_url = try_semantic_scholar(paper)
            time.sleep(10)

            if pdf_url:
                print(f"  -> FOUND: {pdf_url[:80]}", flush=True)
                results.append({
                    "filename": fn,
                    "found": True,
                    "pdf_url": pdf_url,
                    "source": "semantic_scholar"
                })
                save_results(results)
                continue

        phase3_remaining.append((i, paper))

    print(f"\nPhase 3 complete: {len(results)} found, {len(phase3_remaining)} remaining", flush=True)

    # Phase 4: Mark remaining as not found
    for i, paper in phase3_remaining:
        results.append({
            "filename": paper['filename'],
            "found": False,
            "pdf_url": "",
            "source": ""
        })

    # Sort results by original order
    paper_order = {p['filename']: idx for idx, p in enumerate(papers)}
    results.sort(key=lambda r: paper_order.get(r['filename'], 999))

    save_results(results)

    found_count = sum(1 for r in results if r['found'])
    print(f"\n=== FINAL: {found_count}/{len(results)} PDFs found ===", flush=True)

    return results

if __name__ == "__main__":
    os.chdir("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS")
    process_papers()
