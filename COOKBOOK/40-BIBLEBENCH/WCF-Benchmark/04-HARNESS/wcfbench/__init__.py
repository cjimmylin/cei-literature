"""wcfbench — WCF-Bench mock-first harness skeleton (Phase 2, Opus).

A small, runnable, tested spine for the Westminster-Standards benchmark suite.
Scope is deliberately narrow: loader + mock client + two mechanical (judge-free)
scorers + a dry-run. This is NOT the full harness — see README.md "Phase 2 TODO".

NO network / API calls anywhere in this package. The vault has no LLM runner and
no keys; `MockModelClient` is the seam a real Anthropic/OpenAI client later
implements (`.complete(prompt, item_id=None) -> str`).

Governing docs (00-OVERVIEW/):
  - 20260706-build-plan.md   Phase 2 (harness skeleton)
  - 20260706-shared-spine.md §10 (item-record schema), §4 (scoring architecture)
"""

from .loader import ItemRecord, RubricKeypoint, load_item, load_items, LoaderError
from .mock_client import MockModelClient
from .scorers import (
    score_aggravate_ordinal,
    score_prooftext_anchors,
    AggravateScore,
    ProoftextScore,
)

# --- Phase 2 backbone: refusal taxonomy (§4.5) · reporting tensor (§4.6) ·
#     perturbation flip-rate / invariance (§5). ------------------------------
from .refusal import (
    classify_refusal,
    RefusalResult,
    CORRECT_REFUSAL,
    OVER_REFUSAL,
    EVASIVE_NONANSWER,
    ENGAGED,
    REFUSAL_CLASSES,
)
from .tensor import (
    ScoredItem,
    ReportingTensor,
    build_tensor,
)
from .perturbation import (
    run_perturbations,
    FlipResult,
    InvarianceLeagueTable,
    BASE_LABEL,
)

__all__ = [
    "ItemRecord",
    "RubricKeypoint",
    "load_item",
    "load_items",
    "LoaderError",
    "MockModelClient",
    "score_aggravate_ordinal",
    "score_prooftext_anchors",
    "AggravateScore",
    "ProoftextScore",
    # refusal taxonomy (§4.5)
    "classify_refusal",
    "RefusalResult",
    "CORRECT_REFUSAL",
    "OVER_REFUSAL",
    "EVASIVE_NONANSWER",
    "ENGAGED",
    "REFUSAL_CLASSES",
    # reporting tensor (§4.6)
    "ScoredItem",
    "ReportingTensor",
    "build_tensor",
    # perturbation / invariance (§5)
    "run_perturbations",
    "FlipResult",
    "InvarianceLeagueTable",
    "BASE_LABEL",
]

__version__ = "0.1.0"
