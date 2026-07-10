"""OpenRouter model backend — the MEASUREMENT-path client (real developer API).

One `ModelClient` that reaches every vendor's models through a single OpenRouter key
(OpenAI-compatible `/chat/completions`). Unlike the O3 subscription-CLI backends
(smoke-only by ToS), OpenRouter is a legitimate paid API, so it is the runner for the
large-scale cross-vendor panel:

  - **Native multi-turn** — the executor's `Message` list maps straight to the
    `messages` array, fixing the CLI transcript-flattening (O3 finding M-4).
  - **Cross-family for free** — `anthropic/…`, `openai/…`, `google/…`, `meta-llama/…`
    etc. through one key; `family_from_slug` gives the family the charter's cross-family
    judge rule needs.
  - **No sampling params** — temperature/top_p/top_k are never sent (reasoning models
    400 on them); decoding is pinned via the prompt.

Security: the key is read from `OPENROUTER_API_KEY` or a local (gitignored) secrets
file and is NEVER placed in `ModelResponse.raw`, the manifest, or any artifact.

The HTTP transport is injected (`transport=`) so the whole thing is unit-tested against
recorded responses with no live call.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Callable, List, Optional, Tuple

from .cli_backends import ModelCallError
from .clients import Message, ModelClient, ModelResponse

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_SECRETS_FILE = "~/.codex/secrets/openrouter.env"
_RETRY_STATUS = {429, 500, 502, 503, 504}


def family_from_slug(model: str) -> str:
    """`anthropic/claude-sonnet-5` -> `anthropic` (the OpenRouter vendor prefix)."""
    return model.split("/", 1)[0] if "/" in model else model


def load_openrouter_key(secrets_file: str = DEFAULT_SECRETS_FILE) -> Optional[str]:
    """Resolve the key: env var first, then a local file (KEY=VALUE / export KEY=VALUE
    / raw token). Returns None if nothing is found. Never logs the value."""
    env = os.environ.get("OPENROUTER_API_KEY")
    if env:
        return env.strip()
    path = os.path.expanduser(secrets_file)
    if not os.path.isfile(path):
        return None
    raw = open(path, encoding="utf-8").read().strip()
    if not raw:
        return None
    if "=" in raw and not raw.startswith("sk-"):
        raw = raw.split("=", 1)[1].strip()
    return raw.strip().strip('"').strip("'")


Transport = Callable[..., Tuple[int, dict]]


def _default_transport(url: str, headers: dict, payload: dict,
                       timeout: Optional[float] = None) -> Tuple[int, dict]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.getcode(), json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            data = json.loads(e.read().decode("utf-8"))
        except Exception:
            data = {"error": str(e)}
        return e.code, data


def _extract_text(data: dict) -> str:
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return ""
    if isinstance(content, list):  # content-parts form
        return "".join(p.get("text", "") for p in content if isinstance(p, dict))
    return content or ""


class OpenRouterClient(ModelClient):
    """A single-model OpenRouter client. `family` derives from the slug prefix."""

    def __init__(self, name: str, model: str, api_key: Optional[str] = None,
                 family: Optional[str] = None, timeout: float = 120.0,
                 max_retries: int = 4, base_backoff: float = 1.0,
                 url: str = OPENROUTER_URL, transport: Optional[Transport] = None,
                 sleep: Optional[Callable] = None, extra_headers: Optional[dict] = None):
        super().__init__(name)
        self.model = model
        self.family = family or family_from_slug(model)
        self.api_key = api_key or load_openrouter_key()
        self.timeout = timeout
        self.max_retries = max_retries
        self.base_backoff = base_backoff
        self.url = url
        self._transport = transport or _default_transport
        self._sleep = sleep or time.sleep
        self.extra_headers = extra_headers or {}
        if not self.api_key:
            raise ModelCallError(
                "OpenRouterClient: no API key (set OPENROUTER_API_KEY or provide the "
                "secrets file). Live calls are disabled without a credential.")

    def build_payload(self, messages: List[Message], system: Optional[str]) -> dict:
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        for m in messages:
            msgs.append({"role": m.role, "content": m.content})
        # deliberately NO temperature / top_p / top_k
        return {"model": self.model, "messages": msgs}

    def _headers(self) -> dict:
        h = {"Authorization": f"Bearer {self.api_key}",
             "Content-Type": "application/json",
             # OpenRouter attribution headers (optional, non-secret)
             "HTTP-Referer": "https://github.com/cjimmylin/cei-literature",
             "X-Title": "WALKWORTHY-benchmark"}
        h.update(self.extra_headers)
        return h

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        payload = self.build_payload(messages, system)
        headers = self._headers()
        last_status, last_data = None, None
        for attempt in range(self.max_retries + 1):
            status, data = self._transport(self.url, headers, payload, timeout=self.timeout)
            last_status, last_data = status, data
            if status == 200:
                text = _extract_text(data)
                if not text.strip():
                    raise ModelCallError(
                        f"OpenRouter {self.model}: empty content "
                        f"(finish={data.get('choices',[{}])[0].get('finish_reason')})")
                return ModelResponse(
                    text=text, model=data.get("model", self.model), family=self.family,
                    usage=data.get("usage", {}) or {},
                    raw={"backend": "openrouter", "model": self.model})  # NO key
            if status in _RETRY_STATUS and attempt < self.max_retries:
                self._sleep(min(self.base_backoff * (2 ** attempt), 30.0))
                continue
            break
        err = ""
        if isinstance(last_data, dict):
            err = str(last_data.get("error", last_data))[:300]
        raise ModelCallError(f"OpenRouter {self.model} failed: HTTP {last_status}: {err}")
