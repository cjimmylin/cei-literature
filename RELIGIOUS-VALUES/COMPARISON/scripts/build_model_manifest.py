#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
OUT = Path(__file__).resolve().parent.parent / "inputs" / "model-manifest.json"

MODELS = [
    {
        "model_id": "claude-opus-4-6",
        "vendor": "Anthropic",
        "family": "Claude",
        "slug": "opus",
        "source_root": str(BASE / "data"),
        "has_existing_rubric": True,
    },
    {
        "model_id": "claude-sonnet-4-20250514",
        "vendor": "Anthropic",
        "family": "Claude",
        "slug": "sonnet",
        "source_root": str(BASE / "data"),
        "has_existing_rubric": True,
    },
    {
        "model_id": "claude-haiku-4-5-20251001",
        "vendor": "Anthropic",
        "family": "Claude",
        "slug": "haiku",
        "source_root": str(BASE / "data"),
        "has_existing_rubric": True,
    },
    {
        "model_id": "gpt-codex",
        "vendor": "OpenAI",
        "family": "Codex",
        "slug": "gpt-codex",
        "source_root": str(BASE / "Codex" / "results"),
        "has_existing_rubric": True,
    },
    {
        "model_id": "gpt-codex-mini",
        "vendor": "OpenAI",
        "family": "Codex",
        "slug": "gpt-codex-mini",
        "source_root": str(BASE / "Codex-Mini" / "results"),
        "has_existing_rubric": True,
    },
    {
        "model_id": "gemini-2.5-flash-lite",
        "vendor": "Gemini",
        "family": "Gemini",
        "slug": "gemini-2.5-flash-lite",
        "source_root": str(BASE / "gemini-2.5-flash-lite"),
        "has_existing_rubric": False,
    },
    {
        "model_id": "gemini-2.5-flash",
        "vendor": "Gemini",
        "family": "Gemini",
        "slug": "gemini-2.5-flash",
        "source_root": str(BASE / "gemini-2.5-flash"),
        "has_existing_rubric": False,
    },
    {
        "model_id": "gemini-2.5-pro",
        "vendor": "Gemini",
        "family": "Gemini",
        "slug": "gemini-2.5-pro",
        "source_root": str(BASE / "gemini-2.5-pro"),
        "has_existing_rubric": False,
    },
    {
        "model_id": "gemini-3.1-pro",
        "vendor": "Gemini",
        "family": "Gemini",
        "slug": "gemini-3.1-pro",
        "source_root": str(BASE / "gemini-3.1-pro"),
        "has_existing_rubric": False,
    },
]


def main() -> int:
    payload = {"generated": "2026-04-04", "models": MODELS}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(payload, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
