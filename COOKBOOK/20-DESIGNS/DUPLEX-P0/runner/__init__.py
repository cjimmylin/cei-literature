"""DUPLEX P0 runner — vendor-neutral administration, cross-family judging, orchestration.

Live API access is confined to the adapters (runner.adapters). Everything else operates on
plain dicts and injected callables so the whole runner is testable with mocked adapters and
NO live calls.
"""

from .adapters import (
    AdapterResult,
    BaseAdapter,
    AnthropicAdapter,
    OpenAICodexAdapter,
    OpenAIAPIAdapter,
    GeminiAdapter,
    detect_refusal,
    classify_refusal,
    build_adapter,
)
from .roster import load_roster, enabled_models, vendor_of
from .judges import assign_judges, judge_neutrality_check
from .items import load_item_bank, normalize_item, DEFAULT_BANK_PATH
from .orchestrator import (
    Orchestrator,
    Checkpoint,
    condition_config,
    per_condition_sd,
    load_results,
    cell_key,
    code_load_compliance,
)

__all__ = [
    "AdapterResult",
    "BaseAdapter",
    "AnthropicAdapter",
    "OpenAICodexAdapter",
    "OpenAIAPIAdapter",
    "GeminiAdapter",
    "detect_refusal",
    "classify_refusal",
    "build_adapter",
    "load_roster",
    "enabled_models",
    "vendor_of",
    "assign_judges",
    "judge_neutrality_check",
    "load_item_bank",
    "normalize_item",
    "DEFAULT_BANK_PATH",
    "Orchestrator",
    "Checkpoint",
    "condition_config",
    "per_condition_sd",
    "load_results",
    "cell_key",
    "code_load_compliance",
]
