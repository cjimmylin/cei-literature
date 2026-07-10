"""OpenRouterModelClient — the cross-family real backend behind the mock seam.

OpenRouter (https://openrouter.ai) is an OpenAI-compatible **Chat Completions**
endpoint that fronts many model families (OpenAI, Anthropic, Google, Meta, …)
behind a SINGLE API key. That makes it the natural substrate for this benchmark's
spine requirements: ≥2 judges from **different families** (generator-family
excluded) and ≥3 frontier families for the capability battery — all reachable
without juggling three vendor accounts.

This client implements the exact same seam every scorer/runner calls —
``.complete(prompt, item_id=None) -> str`` — so swapping it in for
``MockModelClient`` is a one-line change at the runner boundary. It uses stdlib
``urllib`` (no new dependency, import-clean, hermetically testable by
monkeypatching ``urllib.request.urlopen``); nothing here streams.

Provenance / ToS note (mirrors ``cli_client.py``'s honesty): OpenRouter is a
**proxy** in front of the vendors. Whether it is the *sanctioned path for the
gated G1–G7 run* (vs a smoke/bring-up backend) is a project ruling, not this
module's call — the reproducibility and per-vendor-ToS questions the spine's
"sanctioned Messages-API path" language raises apply to a proxy too. Default to
smoke/pilot scale until that ruling lands; ``MockModelClient`` stays the test
default and the suite stays hermetic.

Usage:
    client = OpenRouterModelClient(model="openai/gpt-4o-mini")   # key from env
    text = client.complete("Rank these ...", item_id="AGG-C6-W301")
    print(client.total_tokens)   # cost/usage accounting for large runs
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

DEFAULT_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
ENV_KEY = "OPENROUTER_API_KEY"


class OpenRouterError(RuntimeError):
    """Raised on a missing key, an HTTP/connection failure, or a malformed reply."""


class OpenRouterModelClient:
    """A single-turn OpenRouter chat client implementing the ``.complete`` seam."""

    def __init__(
        self,
        model: str,
        *,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        system: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 2048,
        timeout: int = 60,
        referer: str = "https://github.com/cjimmylin/cei-literature",
        title: str = "WCF-Bench",
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self.model = model
        self.api_key = api_key or os.environ.get(ENV_KEY)
        if not self.api_key:
            raise OpenRouterError(
                f"no OpenRouter API key: pass api_key=... or set ${ENV_KEY} "
                f"(e.g. `source ~/.codex/secrets/openrouter.env`)."
            )
        self.base_url = base_url
        self.system = system
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.referer = referer
        self.title = title
        self.extra_headers = dict(extra_headers or {})
        # accounting for large runs
        self.call_count = 0
        self.usage_log: List[Dict[str, Any]] = []
        # truncation surfacing (the pilot's lesson): a verbose response cut off at
        # max_tokens (finish_reason == "length") must be flagged as truncation, not
        # mistaken for a silent non-answer. Per-call `last_*` + a cumulative list.
        self.last_finish_reason: Optional[str] = None
        self.last_truncated: bool = False
        self.truncated_item_ids: List[Optional[str]] = []

    # -- accounting -------------------------------------------------------
    @property
    def total_tokens(self) -> int:
        return sum(int(e["usage"].get("total_tokens", 0)) for e in self.usage_log if e.get("usage"))

    # -- the seam ---------------------------------------------------------
    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        """POST one chat completion and return the assistant text. Fails loud."""
        messages: List[Dict[str, str]] = []
        if self.system:
            messages.append({"role": "system", "content": self.system})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            # OpenRouter attribution headers (optional but recommended)
            "HTTP-Referer": self.referer,
            "X-Title": self.title,
        }
        headers.update(self.extra_headers)

        req = urllib.request.Request(self.base_url, data=body, method="POST", headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", errors="replace")[:500]
            except Exception:  # pragma: no cover - best-effort detail
                pass
            raise OpenRouterError(f"OpenRouter HTTP {e.code} ({e.reason}) for model {self.model!r}: {detail}") from e
        except urllib.error.URLError as e:
            raise OpenRouterError(f"OpenRouter connection error for model {self.model!r}: {e.reason}") from e

        self.call_count += 1

        # OpenRouter surfaces upstream errors in the body too.
        if isinstance(data, dict) and data.get("error"):
            raise OpenRouterError(f"OpenRouter returned error for {self.model!r}: {json.dumps(data['error'])[:300]}")

        try:
            choice = data["choices"][0]
            content = choice["message"]["content"]
        except (KeyError, IndexError, TypeError) as e:
            raise OpenRouterError(
                f"malformed OpenRouter response for {self.model!r}: {json.dumps(data)[:300]}"
            ) from e
        if content is None:
            raise OpenRouterError(f"OpenRouter returned null content for {self.model!r} (item {item_id})")

        # Truncation surfacing: finish_reason == "length" means the response was cut
        # off at max_tokens — the partial content is still returned (it may hold a
        # parseable RANKING line) but the caller must know it was truncated.
        finish_reason = choice.get("finish_reason") if isinstance(choice, dict) else None
        self.last_finish_reason = finish_reason
        self.last_truncated = finish_reason == "length"
        if self.last_truncated:
            self.truncated_item_ids.append(item_id)
        if isinstance(data, dict) and "usage" in data:
            self.usage_log.append({"item_id": item_id, "model": data.get("model", self.model),
                                   "usage": data["usage"], "finish_reason": finish_reason})
        return content
