#!/usr/bin/env python3
"""
Extract structured paper JSON from zero-coverage search agent output files.

Reads the JSONL transcript files, finds the final assistant message containing
a ```json code block, extracts the paper array, and wraps it in the expected
agent report format for consolidate_zero_coverage_search.py.

Output: logs/20260216-zero_coverage_agent_Z{N}.json

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/extract_zero_coverage_agent_results.py
"""

import json
import re
import sys
from pathlib import Path

LOGS_DIR = Path("logs")
DATE_PREFIX = "20260216"

# Agent output files and their metadata
AGENTS = [
    {
        "output_file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a4addbb.output",
        "agent_id": "Z1",
        "traditions": ["Shinto"],
    },
    {
        "output_file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/ab412b8.output",
        "agent_id": "Z2",
        "traditions": ["Baha'i"],
    },
    {
        "output_file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a94fdcf.output",
        "agent_id": "Z3",
        "traditions": ["Zoroastrian"],
    },
    {
        "output_file": "/private/tmp/claude-503/-Users-jimmy-lin-Documents-CEI-Literature-Vault/tasks/a2bf79b.output",
        "agent_id": "Z4",
        "traditions": ["Indigenous (North America)"],
    },
]


def extract_json_array_from_text(text: str) -> list:
    """Extract the last ```json ... ``` code block from text and parse it."""
    # Find all ```json ... ``` blocks
    pattern = r'```json\s*\n(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if not matches:
        return []
    # Use the last match (final results)
    last_json_str = matches[-1].strip()
    try:
        data = json.loads(last_json_str)
        if isinstance(data, list):
            return data
    except json.JSONDecodeError as e:
        print(f"  WARNING: JSON parse error: {e}")
    return []


def process_agent(agent_info: dict) -> dict:
    """Process a single agent's output file."""
    output_file = Path(agent_info["output_file"])
    agent_id = agent_info["agent_id"]
    traditions = agent_info["traditions"]

    print(f"\n  Processing {agent_id} ({', '.join(traditions)})...")

    if not output_file.exists():
        print(f"  ERROR: Output file not found: {output_file}")
        return None

    # Read all lines (JSONL format)
    lines = output_file.read_text(encoding='utf-8').splitlines()
    print(f"  Read {len(lines)} JSONL lines")

    # Find assistant messages with text content containing JSON code blocks
    papers = []
    for line in reversed(lines):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue

        # Look for assistant messages with text content
        msg = obj.get("message", {})
        if msg.get("role") != "assistant":
            continue

        content = msg.get("content", [])
        for block in content:
            if block.get("type") == "text":
                text = block.get("text", "")
                if "```json" in text:
                    extracted = extract_json_array_from_text(text)
                    if extracted:
                        papers = extracted
                        break
        if papers:
            break

    if not papers:
        print(f"  WARNING: No papers extracted for {agent_id}")

    print(f"  Extracted {len(papers)} papers")

    report = {
        "agent_id": agent_id,
        "traditions": traditions,
        "papers": papers,
    }

    # Write to logs
    out_path = LOGS_DIR / f"{DATE_PREFIX}-zero_coverage_agent_{agent_id}.json"
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  Written: {out_path.name}")

    return report


def main():
    print("=" * 60)
    print("EXTRACT ZERO-COVERAGE AGENT RESULTS")
    print("=" * 60)

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    total_papers = 0
    for agent_info in AGENTS:
        report = process_agent(agent_info)
        if report:
            total_papers += len(report["papers"])

    print(f"\n{'=' * 60}")
    print(f"EXTRACTION COMPLETE: {total_papers} total papers across {len(AGENTS)} agents")
    print("=" * 60)


if __name__ == "__main__":
    main()
