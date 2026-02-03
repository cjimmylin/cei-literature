#!/usr/bin/env python3
"""
Download PDFs for the new consequentialist/utilitarian ethics papers.
"""

import os
import subprocess
import time
from pathlib import Path

from vault_config import PDFS_DIR

# PDF download targets
pdfs = [
    {
        "filename": "2025-Hui-Decoding Moral Responses in AI.pdf",
        "url": "https://www.sciencedirect.com/science/article/pii/S2451958825002696/pdfft",
        "alt_urls": [],
    },
    {
        "filename": "2025-Dillion-AI Language Model Rivals Expert Ethicist.pdf",
        "url": "https://www.nature.com/articles/s41598-025-86510-0.pdf",
        "alt_urls": [],
    },
    {
        "filename": "2024-Stenseke-Computational Complexity of Ethics.pdf",
        "url": "https://arxiv.org/pdf/2302.04218.pdf",
        "alt_urls": ["https://link.springer.com/content/pdf/10.1007/s10462-024-10732-3.pdf"],
    },
    {
        "filename": "2024-Zhi-Xuan-Beyond Preferences in AI Alignment.pdf",
        "url": "https://arxiv.org/pdf/2408.16984.pdf",
        "alt_urls": ["https://dspace.mit.edu/bitstream/handle/1721.1/157530/11098_2024_Article_2249.pdf"],
    },
    {
        "filename": "2025-Barman-RLHF Whose Culture Whose Values.pdf",
        "url": "https://arxiv.org/pdf/2407.17482.pdf",
        "alt_urls": ["https://link.springer.com/content/pdf/10.1007/s13347-025-00861-0.pdf"],
    },
    {
        "filename": "2025-Chaudhari-RLHF Deciphered.pdf",
        "url": "https://dl.acm.org/doi/pdf/10.1145/3743127",
        "alt_urls": [],
    },
    {
        "filename": "2023-Dai-Safe RLHF.pdf",
        "url": "https://arxiv.org/pdf/2310.12773.pdf",
        "alt_urls": [],
    },
    {
        "filename": "2025-Tennant-Moral Intrinsic Rewards for Alignment.pdf",
        "url": "https://openreview.net/pdf?id=ZFk4eh0WcL",
        "alt_urls": [],
    },
    {
        "filename": "2025-Baum-Aggregation Problems Machine Ethics.pdf",
        "url": "https://ojs.aaai.org/index.php/AIES/article/download/36554/38692",
        "alt_urls": [],
    },
    {
        "filename": "2025-Kneer-Hard Problem AI Alignment Value Forks.pdf",
        "url": "https://philarchive.org/archive/KNETHP",
        "alt_urls": ["https://dl.acm.org/doi/pdf/10.1145/3715275.3732174"],
    },
    {
        "filename": "2025-Sun-Axiology AI Ethics MCDA.pdf",
        "url": "https://www.mdpi.com/2504-3900/126/1/17/pdf",
        "alt_urls": [],
    },
    {
        "filename": "2019-Aliman-Requisite Variety Ethical Utility Functions.pdf",
        "url": "https://arxiv.org/pdf/1907.00430.pdf",
        "alt_urls": [],
    },
    {
        "filename": "2023-Boddington-Normative Ethical Theory AI Ethics.pdf",
        "url": "https://link.springer.com/content/pdf/10.1007/978-981-19-9382-4_6.pdf",
        "alt_urls": [],
    },
    {
        "filename": "2025-Vishwanath-Machine Ethics or AI Alignment.pdf",
        "url": "https://ceur-ws.org/Vol-3975/paper9.pdf",
        "alt_urls": [],
    },
    {
        "filename": "2023-Stenseke-Use and Abuse Normative Ethics Moral Machines.pdf",
        "url": "https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA220614",
        "alt_urls": [],
    },
    {
        "filename": "2020-Della Foresta-Consequentialism Machine Ethics.pdf",
        "url": "https://montrealethics.ai/consequentialism-and-machine-ethics-towards-a-foundational-machine-ethic-to-ensure-the-ethical-conduct-of-artificial-moral-agents/",
        "alt_urls": [],
        "note": "This may not have a direct PDF - it's a web article"
    },
    {
        "filename": "2025-Benavoli-AI Safety Uncertainty Incomplete Preferences.pdf",
        "url": "https://arxiv.org/pdf/2512.23508.pdf",
        "alt_urls": [],
    },
]


def download_pdf(url, output_path, timeout=30):
    """Download a PDF using curl."""
    try:
        result = subprocess.run(
            [
                "curl", "-L", "-o", str(output_path),
                "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "-H", "Accept: application/pdf,*/*",
                "--max-time", str(timeout),
                "-s", "-w", "%{http_code}",
                url
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 10
        )
        http_code = result.stdout.strip()
        return http_code in ["200", "302", "301"]
    except Exception as e:
        print(f"  Error: {e}")
        return False


def is_valid_pdf(filepath):
    """Check if file is a valid PDF."""
    if not filepath.exists():
        return False
    if filepath.stat().st_size < 1000:  # Less than 1KB
        return False
    with open(filepath, 'rb') as f:
        header = f.read(5)
        return header == b'%PDF-'


def main():
    PDFS_DIR.mkdir(exist_ok=True)

    downloaded = []
    failed = []
    skipped = []

    for pdf in pdfs:
        filepath = PDFS_DIR / pdf["filename"]

        # Skip if already exists and valid
        if filepath.exists() and is_valid_pdf(filepath):
            skipped.append(pdf["filename"])
            print(f"SKIP (exists): {pdf['filename']}")
            continue

        print(f"Downloading: {pdf['filename']}")

        # Try primary URL
        success = download_pdf(pdf["url"], filepath)
        if success and is_valid_pdf(filepath):
            downloaded.append(pdf["filename"])
            print(f"  SUCCESS: {pdf['filename']}")
            time.sleep(0.5)  # Rate limiting
            continue

        # Try alternate URLs
        for alt_url in pdf.get("alt_urls", []):
            print(f"  Trying alt URL: {alt_url}")
            success = download_pdf(alt_url, filepath)
            if success and is_valid_pdf(filepath):
                downloaded.append(pdf["filename"])
                print(f"  SUCCESS (alt): {pdf['filename']}")
                break
            time.sleep(0.5)
        else:
            # All URLs failed
            if filepath.exists() and not is_valid_pdf(filepath):
                filepath.unlink()  # Remove invalid file
            failed.append(pdf["filename"])
            print(f"  FAILED: {pdf['filename']}")

        time.sleep(0.5)  # Rate limiting

    print(f"\n=== Download Summary ===")
    print(f"Downloaded: {len(downloaded)}")
    print(f"Skipped (already exist): {len(skipped)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print(f"\nFailed downloads (may need manual download):")
        for f in failed:
            print(f"  - {f}")

    return downloaded, failed


if __name__ == "__main__":
    main()
