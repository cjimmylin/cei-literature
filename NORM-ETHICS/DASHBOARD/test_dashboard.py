#!/usr/bin/env python3
"""NormEval Dashboard — automated screenshot test runner.

Uses Playwright's bundled Chromium to avoid conflicts with system Chrome.
Starts a local HTTP server, captures screenshots of all 10 tabs, then cleans up.

Usage:
    cd CEI-Lit-WS/NORM-ETHICS/DASHBOARD
    python3 test_dashboard.py              # all tabs
    python3 test_dashboard.py 9            # Tab 10 (Cross-Vendor) only (0-indexed)
    python3 test_dashboard.py --port 9000  # custom port

Requirements:
    pip install playwright
    playwright install chromium
"""
from __future__ import annotations

import argparse
import http.server
import os
import signal
import sys
import threading
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)

DASHBOARD_DIR = Path(__file__).parent
SCREENSHOT_DIR = DASHBOARD_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

TAB_SELECTORS = [
    ("tab-overview",     "00-overview"),
    ("tab-papers",       "01-papers"),
    ("tab-features",     "02-features"),
    ("tab-traditions",   "03-traditions"),
    ("tab-composite",    "04-composite"),
    ("tab-trials",       "05-trials"),
    ("tab-data",         "06-data"),
    ("tab-crossmodel",   "07-crossmodel"),
    ("tab-gaps",         "08-gaps"),
    ("tab-crossvendor",  "09-crossvendor"),
]


def start_server(port: int) -> http.server.HTTPServer:
    """Start a local HTTP server in a daemon thread."""
    os.chdir(DASHBOARD_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def capture_tabs(port: int, tabs: list[int] | None = None) -> list[Path]:
    """Capture screenshots of specified tabs (or all) using bundled Chromium."""
    screenshots: list[Path] = []
    url = f"http://127.0.0.1:{port}/"

    with sync_playwright() as p:
        # Use Playwright's bundled Chromium — no system Chrome conflict
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        # Disable cache to avoid stale CSS/JS
        context.route("**/*", lambda route: route.continue_(headers={
            **route.request.headers,
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }))
        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        # Wait for initial render
        time.sleep(1)

        selected = tabs if tabs is not None else list(range(len(TAB_SELECTORS)))

        for idx in selected:
            if idx < 0 or idx >= len(TAB_SELECTORS):
                print(f"  SKIP: tab index {idx} out of range (0-{len(TAB_SELECTORS)-1})")
                continue

            tab_id, filename = TAB_SELECTORS[idx]
            print(f"  Capturing Tab {idx}: {tab_id}...", end=" ", flush=True)

            # Click the tab link
            tab_link = page.query_selector(f'a[href="#{tab_id}"]')
            if not tab_link:
                print("NOT FOUND")
                continue
            tab_link.click()

            # Wait for lazy chart rendering (setTimeout 50ms + ECharts init)
            time.sleep(1.5)

            # Scroll to top of tab content
            page.evaluate(f'document.getElementById("{tab_id}").scrollIntoView()')
            time.sleep(0.3)

            # Full-page screenshot
            out = SCREENSHOT_DIR / f"{filename}.png"
            page.screenshot(path=str(out), full_page=True)
            screenshots.append(out)
            print(f"OK → {out.name}")

        browser.close()

    return screenshots


def main():
    parser = argparse.ArgumentParser(description="NormEval Dashboard screenshot tester")
    parser.add_argument("tabs", nargs="*", type=int,
                        help="Tab indices to capture (0-9). Default: all.")
    parser.add_argument("--port", type=int, default=8765,
                        help="HTTP server port (default: 8765)")
    args = parser.parse_args()

    tabs = args.tabs if args.tabs else None

    print(f"Starting HTTP server on port {args.port}...")
    server = start_server(args.port)

    try:
        print(f"Capturing {'all tabs' if tabs is None else f'tabs {tabs}'}...")
        shots = capture_tabs(args.port, tabs)
        print(f"\nDone — {len(shots)} screenshot(s) saved to {SCREENSHOT_DIR}/")
    finally:
        server.shutdown()
        print("Server stopped.")


if __name__ == "__main__":
    main()
