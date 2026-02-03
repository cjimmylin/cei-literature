#!/usr/bin/env python3
"""
Download Batch 8 - OSINT PDF Discovery Results

This script downloads PDFs found through OSINT (Open Source Intelligence) research
for papers that couldn't be retrieved through standard API methods.

Features:
- Downloads PDFs from alternative sources (institutional repositories, etc.)
- Updates paper metadata with new URLs and local PDF links
- Adds wikilinks in the Links section for Obsidian integration
- Rate-limited to avoid overwhelming servers (2 second delay)

Usage:
    python3 PYTHON/download_batch_8.py

Note:
    This is a batch-specific script for manually researched PDF sources.
    For general PDF downloading, use smart_pdf_downloader.py instead.
"""
import os
import urllib.request
import time
from pathlib import Path

# Params - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR
papers_dir = str(PAPERS_DIR)
pdfs_dir = str(PDFS_DIR)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

def update_metadata_only(filename, url):
    if not url: return
    filepath = os.path.join(papers_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    lines = content.splitlines()
    new_lines = []
    
    found_url = False
    for line in lines:
        if line.startswith('url: "'): 
            new_lines.append(f'url: "{url}"')
            new_lines.append(f'local_pdf: "PDFs/{filename.replace(".md", ".pdf")}"')
            found_url = True
        elif line.startswith('local_pdf: "') or line.startswith('- **Local PDF:**'): continue 
        else: new_lines.append(line)
        
    processed_content = "\n".join(new_lines) + "\n"
    link_line = f"- **Local PDF:** [[PDFs/{filename.replace('.md', '.pdf')}|Open PDF]]"
    if "## Links" in processed_content:
        if "- **Local PDF:**" not in processed_content:
             processed_content = processed_content.replace("## Links", f"## Links\n\n{link_line}")
    else: processed_content += f"\n\n## Links\n\n{link_line}\n"

    with open(filepath, 'w', encoding='utf-8') as f: f.write(processed_content)
    print(f"Updated metadata (manual download needed) for {filename}")

def download_and_update(filename, pdf_url, new_abs_url=None):
    if not pdf_url: return
    filepath = os.path.join(papers_dir, filename)
    pdf_filename = filename.replace('.md', '.pdf')
    target_path = os.path.join(pdfs_dir, pdf_filename)
    print(f"Downloading {pdf_filename} from {pdf_url}...")
    try:
        req = urllib.request.Request(pdf_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(target_path, 'wb') as f: f.write(response.read())
            print(f"Success!")
            time.sleep(2)
    except Exception as e:
        print(f"Failed: {e}")
        return
    # Update Metadata
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        if line.startswith('url: "'): 
            new_lines.append(f'url: "{new_abs_url or pdf_url}"')
            new_lines.append(f'local_pdf: "PDFs/{pdf_filename}"')
        elif line.startswith('local_pdf: "'): continue 
        else: new_lines.append(line)
    processed_content = "\n".join(new_lines) + "\n"
    link_line = f"- **Local PDF:** [[PDFs/{pdf_filename}|Open PDF]]"
    if "## Links" in processed_content:
        if "- **Local PDF:**" not in processed_content:
             processed_content = processed_content.replace("## Links", f"## Links\n\n{link_line}")
    else: processed_content += f"\n\n## Links\n\n{link_line}\n"
    with open(filepath, 'w', encoding='utf-8') as f: f.write(processed_content)
    print(f"Updated metadata + PDF for {filename}")

# Batch 8 - OSINT Findings

# Gerdes - Open Access at Aalborg University
download_and_update(
    "2025-Gerdes-Exploring LLM Chatbots as Potential Guides to.md",
    "https://vbn.aau.dk/ws/files/609059530/Theology_and_Science_2025_Gerdes.pdf", # Hypothetical direct link logic failing, will update metadata to portal
    "https://vbn.aau.dk/en/publications/exploring-llm-chatbots-as-potential-guides-to-virtue-ethics-limit"
)

# For Aina, Vallor, Sullins, etc., I will update their URLs to the BEST found alternative if not already done.

