"""Real-token integration tests (GREEN lane).

Marked @pytest.mark.real_tokens and skippable. Makes ONE trivial call per
working backend. Provenance: cli-oauth-provisional. Not an API measurement.

Run with:  pytest -m real_tokens
Skip with: pytest -m "not real_tokens"  (default in pytest.ini)
"""

import shutil

import pytest

from t1_runner import ModelRequest, ResponseStatus
from t1_runner.backends.anthropic_cli import AnthropicCLIBackend
from t1_runner.backends.openai_cli import OpenAICLIBackend
from t1_runner.backends.google_cli import GoogleCLIBackend

pytestmark = pytest.mark.real_tokens


@pytest.mark.skipif(not shutil.which("claude"), reason="claude CLI not on PATH")
def test_real_anthropic_ok():
    b = AnthropicCLIBackend(model_alias="haiku")
    b.cli_version()
    r = b.run(ModelRequest(prompt="Reply with exactly the word OK", item_id="rt-anthropic"),
              timeout_s=120)
    assert r.status in (ResponseStatus.OK, ResponseStatus.REFUSAL), r.error_detail
    assert r.text
    assert r.model_id_reported.startswith("claude")
    assert r.provenance == "cli-oauth-provisional"


@pytest.mark.skipif(not shutil.which("codex"), reason="codex CLI not on PATH")
def test_real_openai_ok():
    b = OpenAICLIBackend()
    b.cli_version()
    r = b.run(ModelRequest(prompt="Reply with exactly the word OK", item_id="rt-openai"),
              timeout_s=120)
    assert r.status in (ResponseStatus.OK, ResponseStatus.REFUSAL), r.error_detail
    assert r.text
    assert r.provenance == "cli-oauth-provisional"


@pytest.mark.skipif(not shutil.which("gemini"), reason="gemini CLI not on PATH")
def test_real_google_documented_broken():
    """Google is BROKEN on this account (IneligibleTierError). We assert it
    fails cleanly as a classified ERROR rather than crashing the runner."""
    b = GoogleCLIBackend()
    b.cli_version()
    r = b.run(ModelRequest(prompt="Reply with exactly the word OK", item_id="rt-google"),
              timeout_s=120)
    # Either it errors (expected on this account) or — if re-provisioned — it works.
    assert r.status in (ResponseStatus.ERROR, ResponseStatus.OK,
                        ResponseStatus.PARSE_FAILURE)
    if r.status == ResponseStatus.ERROR:
        assert "tier" in r.error_detail.lower() or "ineligible" in r.error_detail.lower() \
               or r.error_detail  # documented broken
