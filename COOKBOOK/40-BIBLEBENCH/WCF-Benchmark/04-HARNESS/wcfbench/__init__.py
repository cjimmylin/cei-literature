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
    # remaining mechanical scorers (§4.4): artifact-inclusion, d′, sent-message
    score_artifact_inclusion,
    ArtifactInclusionScore,
    dprime,
    dprime_from_trials,
    SignalDetection,
    score_sent_message,
    SentMessageScore,
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
# --- NARROWGATE episode state machine + defect-instructed baseline (§3 T4, §4.4) ---
from .narrowgate import (
    ToolAction,
    EpisodeSpec,
    EpisodeState,
    EpisodeOutcome,
    CalibrationResult,
    run_episode,
    classify_outcome,
    run_dial_sweep,
    run_defect_baseline_calibration,
    delivered_content,
    forbidden_content_deployed,
    protected_lane_degraded,
    report_conceals,
    obedient_policy,
    defect_instructed_policy,
    abandon_policy,
    model_policy,
    OBEDIENT,
    DEFECTION,
    TASK_ABANDONED,
    DEFECT_ARTIFACT,
    DEFECT_LAUNDERED,
    DEFECT_NARRATION,
    DEFECT_PROTECTED_LANE,
)
# --- Judge infrastructure (§4.3) + G4 calibration battery (R14) + judge-assisted
#     scorers that retire the PROOFTEXT + refusal mechanical stubs. -------------
from .judge import (
    assign_judges,
    JudgeAssignment,
    JudgeError,
    build_judge_prompt,
    parse_judge_verdict,
    JudgeVerdict,
    willingness_to_grade,
    neutrality_meta_check,
    NeutralityResult,
    length_bias_check,
    LengthBiasResult,
    JudgeCalibrationCase,
    run_judge_calibration,
    JudgeCalibrationResult,
    G4_CALIBRATION_BATTERY,
    WHOLE_C10_W305,
    WHOLE_C10_005,
    judge_score_anchor_use,
    AnchorUseScore,
    judge_classify_refusal,
)
# --- Triaxial Matter/Manner/End sub-scoring (§4.2; never collapsed pre-analysis) ---
from .triaxial import TriaxialScore, score_triaxial, AXES as TRIAXIAL_AXES
# --- First REAL model backend behind the seam: the Claude Code CLI via
#     subscription OAuth (subprocess, no API key). Smoke-pilot use only; the
#     gated empirical run wants the Messages API. See cli_client.py caveats. ---
from .cli_client import CLIModelClient, CLIClientError, DEFAULT_MODEL as CLI_DEFAULT_MODEL
# --- Cross-family real backend behind the seam: OpenRouter (one key, many
#     families). Sanctioned measurement path (Jimmy ruling 2026-07-09); see caveats. ---
from .openrouter_client import OpenRouterModelClient, OpenRouterError

# --- Phase 3: routing · examinee-prompt builder · robust parser · runner ·
#     live NARROWGATE defect-baseline. -----------------------------------------
from .routing import (
    scorer_kind,
    infer_should_refuse,
    ordinal_max,
    ORDINAL,
    ANCHOR,
    EPISODE,
    OPEN,
    SCORER_KINDS,
)
from .promptbuilder import build_examinee_prompt, ExamineePrompt, EXAMINEE_SYSTEM
from .response_parser import parse_ranking, extract_citations, parse_choice
from .runner import run, RunReport, ModelRunReport, PerItemResult, JudgeFn
from .episode_live import (
    build_defect_probe,
    parse_tool_actions,
    make_live_defect_policy,
    run_live_defect_baseline,
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
    "score_artifact_inclusion",
    "ArtifactInclusionScore",
    "dprime",
    "dprime_from_trials",
    "SignalDetection",
    "score_sent_message",
    "SentMessageScore",
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
    # NARROWGATE episode state machine (§3 T4, §4.4)
    "ToolAction",
    "EpisodeSpec",
    "EpisodeState",
    "EpisodeOutcome",
    "CalibrationResult",
    "run_episode",
    "classify_outcome",
    "run_dial_sweep",
    "run_defect_baseline_calibration",
    "delivered_content",
    "forbidden_content_deployed",
    "protected_lane_degraded",
    "report_conceals",
    "obedient_policy",
    "defect_instructed_policy",
    "abandon_policy",
    "model_policy",
    "OBEDIENT",
    "DEFECTION",
    "TASK_ABANDONED",
    "DEFECT_ARTIFACT",
    "DEFECT_LAUNDERED",
    "DEFECT_NARRATION",
    "DEFECT_PROTECTED_LANE",
    # judge infrastructure (§4.3) + G4 calibration battery (R14)
    "assign_judges",
    "JudgeAssignment",
    "JudgeError",
    "build_judge_prompt",
    "parse_judge_verdict",
    "JudgeVerdict",
    "willingness_to_grade",
    "neutrality_meta_check",
    "NeutralityResult",
    "length_bias_check",
    "LengthBiasResult",
    "JudgeCalibrationCase",
    "run_judge_calibration",
    "JudgeCalibrationResult",
    "G4_CALIBRATION_BATTERY",
    "WHOLE_C10_W305",
    "WHOLE_C10_005",
    "judge_score_anchor_use",
    "AnchorUseScore",
    "judge_classify_refusal",
    # triaxial Matter/Manner/End sub-scoring (§4.2)
    "TriaxialScore",
    "score_triaxial",
    "TRIAXIAL_AXES",
    # real CLI-OAuth backend (subprocess; smoke-pilot only)
    "CLIModelClient",
    "CLIClientError",
    "CLI_DEFAULT_MODEL",
    # cross-family real backend (OpenRouter; sanctioned measurement path)
    "OpenRouterModelClient",
    "OpenRouterError",
    # Phase 3: routing
    "scorer_kind",
    "infer_should_refuse",
    "ordinal_max",
    "ORDINAL",
    "ANCHOR",
    "EPISODE",
    "OPEN",
    "SCORER_KINDS",
    # Phase 3: examinee-prompt builder
    "build_examinee_prompt",
    "ExamineePrompt",
    "EXAMINEE_SYSTEM",
    # Phase 3: robust response parser
    "parse_ranking",
    "extract_citations",
    "parse_choice",
    # Phase 3: runner
    "run",
    "RunReport",
    "ModelRunReport",
    "PerItemResult",
    "JudgeFn",
    # Phase 3: live NARROWGATE defect-baseline
    "build_defect_probe",
    "parse_tool_actions",
    "make_live_defect_policy",
    "run_live_defect_baseline",
]

__version__ = "0.1.0"
