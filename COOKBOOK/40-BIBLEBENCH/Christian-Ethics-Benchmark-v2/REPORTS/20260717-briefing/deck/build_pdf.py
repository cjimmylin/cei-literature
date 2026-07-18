#!/usr/bin/env python3
"""Render deck.html -> deck.pdf for the WALKWORTHY v2 briefing deck.

WALKWORTHY-CANARY-7f3e2026 · no holdout content · writing/rendering-only.

Approach: serve the briefing directory over a short-lived localhost HTTP server
and print deck.html to PDF with headless Google Chrome. Chrome's print path
honors the deck's print CSS (`@page { size: 1280px 720px }`, one `.slide` per
page), producing an 18-page 16:9 PDF (960x540 pt == 1280x720 px at 72pt/96px).

Why HTTP and not file://: the relative figure paths (../figures/figN-*.png)
load cleanly over HTTP, and this mirrors the vault's Playwright convention
(file:// is blocked for browser automation). Chrome itself is fine with either;
HTTP is the robust choice.

Run from anywhere:  python3 build_pdf.py
Fallback (loses styling): pandoc deck.md -o deck.pdf --pdf-engine=typst \\
    -f gfm+pipe_tables-tex_math_dollars
"""
import functools
import http.server
import socketserver
import subprocess
import threading
from pathlib import Path

DECK_DIR = Path(__file__).resolve().parent                 # .../deck
BRIEFING_DIR = DECK_DIR.parent                             # .../20260717-briefing (server root)
PORT = 8765
URL = f"http://localhost:{PORT}/deck/deck.html"
OUT = DECK_DIR / "deck.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def serve(root: Path, port: int) -> socketserver.TCPServer:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main() -> None:
    httpd = serve(BRIEFING_DIR, PORT)
    try:
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--virtual-time-budget=8000",   # let the figures load before printing
                f"--print-to-pdf={OUT}",
                URL,
            ],
            check=True,
        )
        print(f"wrote {OUT}")
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
