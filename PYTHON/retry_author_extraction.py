#!/usr/bin/env python3
"""Retry author extraction for papers that got Semantic Scholar 429 errors."""
import json, re, sys, time, urllib.request, urllib.parse
from xml.etree import ElementTree
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Load previous results
results = json.loads(Path('logs/20260216-author_extraction_results.json').read_text())
failed = [r for r in results if not r['proposed_authors'] and r['current_authors'] != '[[Unknown]]']

# Also include Unknown papers that are likely academic
unknown_academic = [r for r in results if not r['proposed_authors'] and r['current_authors'] == '[[Unknown]]' and r['url'] and ('arxiv' in r.get('url','') or 'doi' in r.get('url',''))]
failed.extend(unknown_academic)

print(f"Retrying {len(failed)} papers with arXiv/Semantic Scholar...", flush=True)

retried = []
for i, paper in enumerate(failed):
    url = paper.get('url', '')
    title = paper.get('title', '')
    filename = paper['filename']
    print(f"\n[{i+1}/{len(failed)}] {filename[:60]}", flush=True)
    print(f"  URL: {url}", flush=True)

    authors = []
    source = None

    # Try arXiv first if applicable
    if 'arxiv.org' in url:
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
        if match:
            arxiv_id = match.group(1)
            api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
            time.sleep(3)
            try:
                req = urllib.request.Request(api_url, headers={'User-Agent': 'CEI-Vault/1.0'})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    xml = resp.read().decode('utf-8')
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                root = ElementTree.fromstring(xml)
                entry = root.find('atom:entry', ns)
                if entry is not None:
                    for a in entry.findall('atom:author', ns):
                        name = a.find('atom:name', ns)
                        if name is not None and name.text:
                            authors.append(name.text.strip())
                    if authors:
                        source = 'arxiv'
                        print(f"  arXiv -> {len(authors)} authors: {authors[:5]}", flush=True)
            except Exception as e:
                print(f"  arXiv error: {e}", flush=True)

    # Try Semantic Scholar with longer delay
    if not authors and title:
        time.sleep(15)  # 15s delay to avoid 429
        encoded = urllib.parse.quote(title)
        ss_url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit=3&fields=title,authors"
        try:
            req = urllib.request.Request(ss_url, headers={'User-Agent': 'CEI-Vault/1.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            if data.get('data'):
                best = None
                for p in data['data']:
                    if p.get('title','').lower().strip() == title.lower().strip():
                        best = p
                        break
                if not best:
                    best = data['data'][0]
                for a in best.get('authors', []):
                    name = a.get('name', '').strip()
                    if name:
                        authors.append(name)
                if authors:
                    source = 'semantic_scholar'
                    print(f"  Semantic Scholar -> {len(authors)} authors: {authors[:5]}", flush=True)
        except Exception as e:
            print(f"  Semantic Scholar error: {e}", flush=True)

    if authors:
        retried.append({
            'filename': filename,
            'title': title,
            'current_authors': paper['current_authors'],
            'url': url,
            'source': source,
            'proposed_authors': authors,
            'confidence': 'high',
        })
    else:
        print(f"  Still no result", flush=True)

print(f"\n{'='*60}", flush=True)
print(f"RETRY RESULTS: {len(retried)}/{len(failed)} found", flush=True)
for r in retried:
    print(f"  {r['filename'][:50]} -> {len(r['proposed_authors'])} authors ({r['source']})", flush=True)

Path('logs/20260216-author_extraction_retry_results.json').write_text(
    json.dumps(retried, indent=2, ensure_ascii=False))
print(f"\nSaved to logs/20260216-author_extraction_retry_results.json", flush=True)
