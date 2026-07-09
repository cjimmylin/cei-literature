"""MockModelClient — the deterministic, NO-NETWORK model seam.

The vault has no live LLM runner and no API keys (memory:
"vault-no-live-llm-runner"). Every mechanical scorer and dry-run in Phase 2 runs
against canned responses served from an in-memory table. This class is the
**seam** a real client implements later:

    A real client (Phase 3, credential-gated) exposes the same method ---
        def complete(self, prompt: str, item_id: str | None = None) -> str: ...
    --- but calls Anthropic / OpenAI instead of a lookup table. Nothing in the
    scorers or the dry-run may import an SDK or open a socket; they only ever
    call `.complete(...)`. Swapping MockModelClient for `AnthropicModelClient`
    is then a one-line change at the runner boundary.

Usage:
    client = MockModelClient()
    client.register("AGG-C6-W301", "ranking: a < b < c ...")
    text = client.complete(prompt="Rank these...", item_id="AGG-C6-W301")
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple


class MockModelClient:
    """Serves canned responses keyed by item id. Never touches the network."""

    def __init__(self, default_response: str = "") -> None:
        # item_id -> canned response text
        self._responses: Dict[str, str] = {}
        # ordered (prompt, item_id) call log — lets dry-runs / tests inspect calls
        self._calls: List[Tuple[str, Optional[str]]] = []
        self._default_response = default_response

    def register(self, item_id: str, response: str) -> None:
        """Script the response returned for a given item id."""
        self._responses[item_id] = response

    def register_many(self, mapping: Dict[str, str]) -> None:
        """Bulk-register a dict of {item_id: response}."""
        self._responses.update(mapping)

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        """Return the canned response for ``item_id``.

        This is the method a real client overrides. It performs NO I/O; it only
        looks the response up. If nothing is registered for the id, the
        constructor's ``default_response`` is returned (empty string by default),
        which lets scorers exercise the "model said nothing useful" path.
        """
        self._calls.append((prompt, item_id))
        if item_id is not None and item_id in self._responses:
            return self._responses[item_id]
        return self._default_response

    @property
    def call_log(self) -> List[Tuple[str, Optional[str]]]:
        """Ordered list of (prompt, item_id) calls made so far (for tests)."""
        return list(self._calls)

    def reset_log(self) -> None:
        self._calls.clear()
