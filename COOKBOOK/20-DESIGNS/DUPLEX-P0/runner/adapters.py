"""Vendor-neutral model adapters.

Every adapter implements the same interface:

    administer(prompt, model_id, temperature, seed, **gen) -> AdapterResult
        AdapterResult(text, raw, refusal_flag, latency)

Adapters are the ONLY place live API/subprocess access happens. Both the Anthropic SDK client
and the Codex subprocess runner are injectable so tests mock them — there are NO live calls in
the test suite.

  - AnthropicAdapter    : installed `anthropic` SDK (v0.84), key from env ANTHROPIC_API_KEY.
                          Models per §3.5: Opus 4.6 / Sonnet 4.6 / Haiku 3.5.
  - OpenAICodexAdapter  : subprocess wrapper around the OAuth Codex CLI (`codex exec`).
                          Models per §3.5: GPT-5 Codex / GPT Mini.
  - GeminiAdapter       : DEFERRED — raises NotImplementedError.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


# --------------------------------------------------------------------------- result type

@dataclass
class AdapterResult:
    text: str
    raw: Any
    refusal_flag: bool
    latency: float


# --------------------------------------------------------------------------- refusal detection (§4)

# Explicit refusal category (§4 / KB07 L65): a refusing model must NOT silently score as
# maximally reason-(un)responsive. Detection here just flags; the orchestrator codes the category
# and drops the cell from the scored distribution.
_REFUSAL_PATTERNS = [
    r"\bi can(?:'|’)?t\b",
    r"\bi cannot\b",
    r"\bi can not\b",
    r"\bi won(?:'|’)?t\b",
    r"\bi will not\b",
    r"\bi(?:'|’)?m not able\b",
    r"\bi am not able\b",
    r"\bi(?:'|’)?m unable\b",
    r"\bi am unable\b",
    r"\bi must decline\b",
    r"\bi(?:'|’)?d rather not\b",
    r"\bi do not feel comfortable\b",
    r"\bi don(?:'|’)?t feel comfortable\b",
    r"\bi refuse\b",
    r"\bunable to (?:help|assist|answer|comply)\b",
    r"\bcan(?:'|’)?t (?:help|assist) with (?:that|this)\b",
]
_REFUSAL_RE = re.compile("|".join(_REFUSAL_PATTERNS), re.IGNORECASE)


def detect_refusal(text: Optional[str]) -> bool:
    if not text:
        return False
    return bool(_REFUSAL_RE.search(text))


def classify_refusal(text: Optional[str]) -> Optional[str]:
    """Return the explicit refusal category, or None if not a refusal.

    P0 uses a single 'explicit_refusal' category (co-reported per §4). The matched surface
    is preserved for the over-refusal audit.
    """
    if not detect_refusal(text):
        return None
    m = _REFUSAL_RE.search(text or "")
    return "explicit_refusal"


# --------------------------------------------------------------------------- base

class BaseAdapter:
    vendor = "base"

    def administer(
        self,
        prompt: str,
        model_id: str,
        temperature: float,
        seed: int,
        **gen: Any,
    ) -> AdapterResult:
        raise NotImplementedError


# --------------------------------------------------------------------------- Anthropic

class AnthropicAdapter(BaseAdapter):
    """Anthropic subjects via the installed `anthropic` SDK.

    `client` is injectable for testing; in production it is constructed lazily from
    ANTHROPIC_API_KEY. `gen` accepts per-resource-condition params from
    orchestrator.condition_config: `max_tokens`, `thinking` (dict or None), `system`.
    """

    vendor = "anthropic"

    def __init__(self, client: Optional[Any] = None, api_key_env: str = "ANTHROPIC_API_KEY"):
        self._client = client
        self._api_key_env = api_key_env

    @property
    def client(self) -> Any:
        if self._client is None:
            import anthropic  # deferred import; only when a live call is actually made

            key = os.environ.get(self._api_key_env)
            if not key:
                raise RuntimeError(
                    f"{self._api_key_env} not set — cannot construct live Anthropic client."
                )
            self._client = anthropic.Anthropic(api_key=key)
        return self._client

    def administer(
        self,
        prompt: str,
        model_id: str,
        temperature: float,
        seed: int,
        max_tokens: int = 1024,
        thinking: Optional[Dict[str, Any]] = None,
        system: Optional[str] = None,
        **_: Any,
    ) -> AdapterResult:
        # NOTE(seed): the Anthropic Messages API exposes no `seed` parameter. `seed` is retained
        # for checkpoint identity / bookkeeping only; the API is non-deterministic even at fixed
        # temperature. Do not treat repeated seeds as reproducible on this vendor.
        params: Dict[str, Any] = {
            "model": model_id,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            params["system"] = system
        if thinking:
            # extended_thinking condition -> adaptive thinking on Opus 4.6 / Sonnet 4.6.
            # TODO(live): 4.x historically constrained `temperature` when thinking is on
            # (required temperature=1). Verify against the installed SDK/model; if the API
            # rejects temperature+thinking, drop temperature here for the thinking condition.
            params["thinking"] = thinking

        t0 = time.monotonic()
        resp = self.client.messages.create(**params)
        latency = time.monotonic() - t0

        text = _extract_text(resp)
        stop_reason = getattr(resp, "stop_reason", None)
        refusal = stop_reason == "refusal" or detect_refusal(text)
        return AdapterResult(text=text, raw=_raw(resp), refusal_flag=refusal, latency=latency)


def _extract_text(resp: Any) -> str:
    content = getattr(resp, "content", None)
    if content is None:
        return ""
    parts: List[str] = []
    for block in content:
        if getattr(block, "type", None) == "text":
            parts.append(getattr(block, "text", "") or "")
    return "".join(parts)


def _raw(resp: Any) -> Any:
    for attr in ("to_dict", "model_dump"):
        fn = getattr(resp, attr, None)
        if callable(fn):
            try:
                return fn()
            except Exception:
                pass
    return repr(resp)


# --------------------------------------------------------------------------- OpenAI (Codex CLI)

class OpenAICodexAdapter(BaseAdapter):
    """OpenAI subjects via the OAuth Codex CLI (`codex exec`) — no API key.

    Command template (codex-cli 0.134.0, verified `--help`):

        codex exec -m <model_id> --skip-git-repo-check --ephemeral --color never \
            -o <last_message_file> -              # prompt on stdin

    `-o/--output-last-message` writes just the agent's final message to a file, which we read
    back as the response text. `runner` is injectable (a callable with subprocess.run's shape)
    so tests mock the subprocess — NO live calls in tests.

    OPEN ITEMS for a live run (documented in runner/README.md):
      * codex must be on PATH AND authenticated (OAuth via `codex login`; check `codex login`
        status). shutil.which alone does not prove auth.
      * `codex exec` is an AGENTIC coding runner, not a chat completion. For a pure
        moral-judgment probe it should be constrained to a single answer (read-only sandbox,
        no tool use). TODO(live): confirm the flag/-c config that yields a clean single-turn
        answer, and confirm `-m gpt-5-codex` / `-m gpt-5-mini` resolve on the installed codex.
      * codex exposes no temperature/seed flags today; `temperature`/`seed` are recorded for
        bookkeeping. TODO(live): check whether `-c` overrides can set them.
    """

    vendor = "openai"

    def __init__(
        self,
        codex_bin: Optional[str] = None,
        runner: Optional[Callable[..., Any]] = None,
        timeout: float = 180.0,
    ):
        # `runner` defaults to subprocess.run; tests inject a fake.
        self._runner = runner or subprocess.run
        self._explicit_bin = codex_bin
        self._timeout = timeout

    def available(self) -> bool:
        return self.codex_bin is not None

    @property
    def codex_bin(self) -> Optional[str]:
        if self._explicit_bin:
            return self._explicit_bin
        return shutil.which("codex")

    def build_command(self, model_id: str, out_path: str) -> List[str]:
        return [
            self.codex_bin or "codex",
            "exec",
            "-m",
            model_id,
            "--skip-git-repo-check",
            "--ephemeral",
            "--color",
            "never",
            "-o",
            out_path,
            "-",  # read prompt from stdin
        ]

    def administer(
        self,
        prompt: str,
        model_id: str,
        temperature: float,
        seed: int,
        max_tokens: int = 1024,
        thinking: Optional[Dict[str, Any]] = None,
        system: Optional[str] = None,
        **_: Any,
    ) -> AdapterResult:
        if not self.available():
            raise RuntimeError(
                "codex CLI not found on PATH — OpenAI adapter unavailable. "
                "Install/authenticate the OAuth Codex CLI before a live run."
            )
        full_prompt = prompt if not system else (system + "\n\n" + prompt)
        with tempfile.NamedTemporaryFile(
            "w+", suffix=".txt", delete=False
        ) as tf:
            out_path = tf.name
        cmd = self.build_command(model_id, out_path)
        t0 = time.monotonic()
        proc = self._runner(
            cmd,
            input=full_prompt,
            capture_output=True,
            text=True,
            timeout=self._timeout,
        )
        latency = time.monotonic() - t0

        text = _read_last_message(out_path)
        if not text:
            # fall back to stdout if the -o file was not produced (older/newer codex)
            text = getattr(proc, "stdout", "") or ""
        returncode = getattr(proc, "returncode", 0)
        refusal = detect_refusal(text)
        raw = {
            "cmd": cmd,
            "returncode": returncode,
            "stderr": getattr(proc, "stderr", ""),
            "out_path": out_path,
        }
        return AdapterResult(text=text, raw=raw, refusal_flag=refusal, latency=latency)


def _read_last_message(path: str) -> str:
    try:
        with open(path, "r") as fh:
            return fh.read().strip()
    except (OSError, IOError):
        return ""


# --------------------------------------------------------------------------- Gemini (DEFERRED)

class GeminiAdapter(BaseAdapter):
    """Google/Gemini subjects — DEFERRED (scope decision). Do not enable in P0."""

    vendor = "google"

    def administer(
        self,
        prompt: str,
        model_id: str,
        temperature: float,
        seed: int,
        **gen: Any,
    ) -> AdapterResult:
        raise NotImplementedError(
            "GeminiAdapter is deferred. TODO(gemini): implement via the google-genai SDK "
            "(GEMINI_API_KEY) or Vertex, wire generation params (temperature, thinking), then "
            "flip vendors.google.enabled=true + per-model enabled flags in config/p0-roster.yaml."
        )


# --------------------------------------------------------------------------- factory

def build_adapter(vendor: str, **kwargs: Any) -> BaseAdapter:
    v = vendor.lower()
    if v == "anthropic":
        return AnthropicAdapter(**kwargs)
    if v == "openai":
        return OpenAICodexAdapter(**kwargs)
    if v in ("google", "gemini"):
        return GeminiAdapter()
    raise ValueError(f"unknown vendor: {vendor!r}")
