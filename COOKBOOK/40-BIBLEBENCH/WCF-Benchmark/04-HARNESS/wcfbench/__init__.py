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
    # perturbation-variant materialization (memo item 5)
    materialize_perturbations,
    materialize_pushback,
    materialize_monitoring,
    materialize_persona,
    PerturbationVariant,
    MaterializedPerturbations,
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
    # R24 per-keypoint award scoring + R25 award-consistency probe
    build_award_prompt,
    parse_award_verdict,
    AwardVerdict,
    ProbeResult,
    run_award_consistency_probe,
    # R33.1/.2/.3 reason mandate + evidence quote + truncation robustness
    extract_evidence_quote,
    quote_supported_by,
    award_emission_count,
    complete_with_retry,
    JudgeCall,
    # R33.4 extended acceptance battery
    run_discrimination_probe,
)
# --- Triaxial Matter/Manner/End sub-scoring (§4.2; never collapsed pre-analysis) ---
from .triaxial import TriaxialScore, score_triaxial, AXES as TRIAXIAL_AXES
# --- Contested-item position/coherence scorer (adherence, not correctness;
#     binding ruling 20260709-contested-item-scoring-ruling.md). ----------------
from .contested import (
    score_contested_position,
    ContestedScore,
    settled_core_keypoints,
    position_invariance,
    PositionInvarianceResult,
    steerability_check,
    SteerabilityResult,
    # R28 leveled disclosure + R25 disclosure-inversion probe + R33.4 negative probe
    build_disclosure_prompt,
    DISCLOSURE_ANCHOR,
    run_disclosure_inversion_probe,
    run_negative_disclosure_probe,
)
# --- Live OPEN/CONTESTED judge panel (§4.3): calibrate-and-discard + cross-family
#     assignment + triaxial (OPEN) / position (CONTESTED); retains per-judge raw.
#     R33.4: per-surface acceptance (OPEN award / disclosure / coherence / settled-core). --
from .judge_panel import (
    JudgePanel, OpenVerdict, ContestedVerdict,
    OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE, SURFACES,
    is_retryable_transport_error,
)
# --- R35 judge qualification: retry + majority-of-K gate + the frozen manifest
#     JudgePanel consumes (surface eligibility can no longer flip run-to-run). ------
from .qualification import (
    qualify_judge, JudgeQualification, ProbeReps, run_probe_reps,
    build_manifest, write_manifest, load_manifest, manifest_from_pass_table,
    current_template_hashes, manifest_is_fresh, eligible_surfaces_for,
    SURFACE_PROBES, PROBES as ACCEPTANCE_PROBES,
)
# --- Cross-judge disagreement clusters (the Fable-session input). --------------
from .disagreement import summarize_disagreement, DisagreementCell
# --- R27 transcript persistence (per item×SUT cell: prompt+response+judge texts). --
from .transcripts import template_hash, build_transcript_records, write_run_transcripts
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
    CONTESTED,
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
    "materialize_perturbations",
    "materialize_pushback",
    "materialize_monitoring",
    "materialize_persona",
    "PerturbationVariant",
    "MaterializedPerturbations",
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
    # R24 per-keypoint award scoring + R25 award-consistency probe
    "build_award_prompt",
    "parse_award_verdict",
    "AwardVerdict",
    "ProbeResult",
    "run_award_consistency_probe",
    # R33.1/.2/.3 reason mandate + evidence quote + truncation robustness
    "extract_evidence_quote",
    "quote_supported_by",
    "award_emission_count",
    "complete_with_retry",
    "JudgeCall",
    # R33.4 extended acceptance battery + per-surface acceptance
    "run_discrimination_probe",
    "run_negative_disclosure_probe",
    "OPEN_AWARD",
    "DISCLOSURE",
    "COHERENCE",
    "SETTLED_CORE",
    "SURFACES",
    # triaxial Matter/Manner/End sub-scoring (§4.2)
    "TriaxialScore",
    "score_triaxial",
    "TRIAXIAL_AXES",
    # contested-item position/coherence scorer (adherence, not correctness)
    "score_contested_position",
    "ContestedScore",
    "settled_core_keypoints",
    "position_invariance",
    "PositionInvarianceResult",
    "steerability_check",
    "SteerabilityResult",
    # R28 leveled disclosure + R25 disclosure-inversion probe
    "build_disclosure_prompt",
    "DISCLOSURE_ANCHOR",
    "run_disclosure_inversion_probe",
    # live OPEN/CONTESTED judge panel (§4.3)
    "JudgePanel",
    "OpenVerdict",
    "ContestedVerdict",
    "is_retryable_transport_error",
    # cross-judge disagreement clusters (Fable-session input)
    "summarize_disagreement",
    "DisagreementCell",
    # R27 transcript persistence
    "template_hash",
    "build_transcript_records",
    "write_run_transcripts",
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
    "CONTESTED",
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
