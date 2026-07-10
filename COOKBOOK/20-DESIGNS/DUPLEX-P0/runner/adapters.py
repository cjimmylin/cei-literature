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


# --------------------------------------------------------------------------- administration errors (F-1 / SA-5)

class AdministrationError(RuntimeError):
    """A model administration FAILED (auth, network, rate-limit, CLI crash, timeout) rather than
    the model refusing.

    SA-5 (F-1): an administration error is bounded-retried with exponential backoff and then RAISED
    fail-loud. It is NEVER coerced into a refusal, and the orchestrator never checkpoints its cell
    as complete — so a transient failure is retried on resume instead of being recorded permanently
    as an "explicit_refusal" (the corruption the OVERTURNED returncode!=0 -> refusal path caused).
    """

    def __init__(self, message: str, vendor: Optional[str] = None, attempts: Optional[int] = None):
        super().__init__(message)
        self.vendor = vendor
        self.attempts = attempts


class _CodexTransient(RuntimeError):
    """Internal: a single Codex administration attempt failed transiently (non-zero return or
    subprocess timeout) and should be retried."""


# Transient Anthropic API errors eligible for bounded retry (rate-limit / overloaded / network /
# timeout / 5xx). Matched by class NAME so the test suite need not import the SDK, and so an
# authentication or bad-request error (a different class) is NOT retried but raised at once
# (SA-5 addendum: "fail loud only when the first call errors with an authentication error").
_TRANSIENT_ANTHROPIC_ERROR_NAMES = frozenset(
    {"RateLimitError", "InternalServerError", "OverloadedError",
     "APIConnectionError", "APITimeoutError", "APIConnectionTimeoutError"}
)


def _is_transient_anthropic_error(exc: BaseException) -> bool:
    return type(exc).__name__ in _TRANSIENT_ANTHROPIC_ERROR_NAMES


def _retry(fn, *, max_retries, backoff_base, sleep, is_transient, vendor):
    """Run `fn`, retrying transient administration failures with exponential backoff, then RAISE
    an AdministrationError once the retries are exhausted (SA-5: bounded retry -> fail loud).
    Non-transient exceptions propagate immediately (unretried)."""
    attempt = 0
    while True:
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 — classified below, re-raised if not transient
            if not is_transient(e):
                raise
            attempt += 1
            if attempt > max_retries:
                raise AdministrationError(
                    f"{vendor} administration failed after {attempt} attempt(s): {e!r}",
                    vendor=vendor, attempts=attempt,
                ) from e
            sleep(backoff_base * (2 ** (attempt - 1)))


def resolve_auth_mode(env: Optional[Dict[str, str]] = None) -> str:
    """Report which credential the anthropic SDK chain will use, for run metadata (SA-5 addendum).

    Precedence mirrors the SDK: a NON-EMPTY ``ANTHROPIC_API_KEY``, else ``ANTHROPIC_AUTH_TOKEN``,
    else the ``ant auth login`` profile. Sharp edge encoded here: an EMPTY ``ANTHROPIC_API_KEY=""``
    is treated as unset (it falls through to the token / profile), matching the entrypoint's env
    sanity-check — an exported empty key still outranks the profile at the SDK level, which is why
    the entrypoint must fail loud on it, but for *reporting* we describe the intended resolution.
    """
    env = env if env is not None else os.environ
    if env.get("ANTHROPIC_API_KEY"):
        return "api_key"
    if env.get("ANTHROPIC_AUTH_TOKEN"):
        return "auth_token"
    return "profile"


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

    def __init__(
        self,
        client: Optional[Any] = None,
        api_key_env: str = "ANTHROPIC_API_KEY",
        max_retries: int = 4,
        backoff_base: float = 0.5,
        sleep: Optional[Callable[[float], None]] = None,
    ):
        self._client = client
        self._api_key_env = api_key_env
        self._max_retries = max_retries
        self._backoff_base = backoff_base
        self._sleep = sleep or time.sleep
        # Credential mode used for run metadata (SA-5 addendum). "injected" for a test client;
        # otherwise resolved from the SDK credential chain when the live client is constructed.
        self.auth_mode: Optional[str] = "injected" if client is not None else None

    @property
    def client(self) -> Any:
        if self._client is None:
            import anthropic  # deferred import; only when a live call is actually made

            # SA-5 addendum (OAuth credential path): do NOT hard-require ANTHROPIC_API_KEY.
            # Construct a bare client and let the SDK credential chain resolve
            # (ANTHROPIC_API_KEY -> ANTHROPIC_AUTH_TOKEN -> `ant auth login` profile). An
            # authentication error surfaces on the FIRST call, not at construction — which is
            # what lets `ant auth login` (org-billed OAuth, auto-refreshing profile) work without
            # a static key. Prefer profile resolution over an exported token for long runs.
            self._client = anthropic.Anthropic()
            self.auth_mode = resolve_auth_mode()
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
        omit_sampling_params: bool = False,
        **_: Any,
    ) -> AdapterResult:
        # NOTE(seed): the Anthropic Messages API exposes no `seed` parameter. `seed` is retained
        # for checkpoint identity / bookkeeping only; the API is non-deterministic even at fixed
        # temperature. Do not treat repeated seeds as reproducible on this vendor.
        params: Dict[str, Any] = {
            "model": model_id,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        # F-2 / SA-6: omit the sampling param entirely on a V-4 (or model-capability) drop. Sending
        # `temperature` with extended thinking — or on any Opus 4.7+/Fable subject — is a 400.
        if not omit_sampling_params:
            params["temperature"] = temperature
        if system:
            params["system"] = system
        if thinking:
            # extended_thinking condition -> adaptive thinking on Opus 4.6 / Sonnet 4.6.
            # F-2 owns the V-4 temperature drop for this condition (the orchestrator omits the
            # sampling param before this call); this adapter only forwards what it is given.
            params["thinking"] = thinking

        t0 = time.monotonic()
        # SA-5 (F-1): bounded retry with exponential backoff for TRANSIENT API errors
        # (rate-limit/overloaded/network); persistent transient errors raise AdministrationError;
        # non-transient errors (auth/bad-request) propagate immediately.
        resp = _retry(
            lambda: self.client.messages.create(**params),
            max_retries=self._max_retries, backoff_base=self._backoff_base,
            sleep=self._sleep, is_transient=_is_transient_anthropic_error, vendor=self.vendor,
        )
        latency = time.monotonic() - t0

        text = _extract_text(resp)
        stop_reason = getattr(resp, "stop_reason", None)
        # WS-1 D10 / SA-5: refusal_flag carries ONLY the structured API signal. A content refusal
        # ("I cannot ...") is decided downstream by the scorer returning no stance, never by a
        # substring match on the answer (which would delete substantive stance-1 answers).
        refusal = stop_reason == "refusal"
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
        max_retries: int = 4,
        backoff_base: float = 0.5,
        sleep: Optional[Callable[[float], None]] = None,
    ):
        # `runner` defaults to subprocess.run; tests inject a fake.
        self._runner = runner or subprocess.run
        self._explicit_bin = codex_bin
        self._timeout = timeout
        self._max_retries = max_retries
        self._backoff_base = backoff_base
        self._sleep = sleep or time.sleep

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

        def _attempt() -> AdapterResult:
            with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False) as tf:
                out_path = tf.name
            cmd = self.build_command(model_id, out_path)
            try:
                proc = self._runner(
                    cmd, input=full_prompt, capture_output=True, text=True, timeout=self._timeout,
                )
            except subprocess.TimeoutExpired as e:
                # A timeout is an administration failure, not a refusal — retry it.
                raise _CodexTransient(f"codex exec timed out after {self._timeout}s") from e

            text = _read_last_message(out_path)
            if not text:
                # fall back to stdout if the -o file was not produced (older/newer codex)
                text = getattr(proc, "stdout", "") or ""
            returncode = getattr(proc, "returncode", 0)
            if returncode != 0:
                # SA-5 (OVERTURNED): a non-zero return is an ADMINISTRATION error (auth, network,
                # rate limit, CLI crash), NOT a model refusal. It conflates admin failures with
                # refusals and, once checkpointed, becomes a permanent fabricated "explicit_refusal".
                # Retry it; on persistent failure _retry raises AdministrationError (fail loud).
                raise _CodexTransient(
                    f"codex exec returncode={returncode}: "
                    f"{(getattr(proc, 'stderr', '') or '')[:500]}"
                )
            raw = {
                "cmd": cmd,
                "returncode": returncode,
                "stderr": getattr(proc, "stderr", ""),
                "out_path": out_path,
            }
            # SA-5: Codex has NO structured refusal signal, so refusal_flag is ALWAYS False.
            # A content refusal is decided downstream by the scorer returning no stance (no_stance).
            return AdapterResult(text=text, raw=raw, refusal_flag=False, latency=0.0)

        t0 = time.monotonic()
        result = _retry(
            _attempt, max_retries=self._max_retries, backoff_base=self._backoff_base,
            sleep=self._sleep, is_transient=lambda e: isinstance(e, _CodexTransient),
            vendor=self.vendor,
        )
        result.latency = time.monotonic() - t0
        return result


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
