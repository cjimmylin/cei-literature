import skim_common as common
import skim_constants as constants
import skim_evidence as evidence
import skim_hashing as hashing
import skim_schemas as schemas
import skim_statistics as statistics


EXPECTED_COMMON_EXPORTS = (
    'ACTION_CLASSIFICATIONS',
    'ACTION_VALUE_FIELDS',
    'BENEFICIARIES',
    'BOOTSTRAP_REPLICATES',
    'CAPABILITY_REFERENCE_FIELDS',
    'CONDITIONAL_CHECK_CORES',
    'CONSTRUCTION_PROOF_FIELDS',
    'COVER_STORY_LEVELS',
    'DIAGNOSTIC_BLOCKERS',
    'DIAGNOSTIC_ELIGIBLE_FOR_EMPIRICAL_DECISION',
    'DIAGNOSTIC_REQUESTS',
    'DIAGNOSTIC_STATUS',
    'DIFFICULTY_STRATA',
    'DOMAINS',
    'EvidenceBasis',
    'FALLBACK_PROFILE_CELLS',
    'FAMILIES',
    'FAMILY_ANALYSIS_STATUS',
    'FAMILY_CODES',
    'FAMILY_CORE_COUNTS',
    'FROZEN_ARTIFACT_HASH_FIELDS',
    'GATE_THRESHOLDS',
    'GLOBAL_MAGNITUDE_FREQUENCIES',
    'ITEM_RETENTION_RULES',
    'ITEM_RETENTION_ACTIONS',
    'LOGICAL_BANK_RECORDS',
    'LOGICAL_RECORD_COUNTS',
    'MAGNITUDE_TIERS',
    'MAGNITUDE_ORDER',
    'MAGNITUDE_WINDOWS',
    'MANDATE_CLARITY',
    'MAX_PAID_MODEL_CALLS',
    'OFFICIAL_REQUESTS',
    'POINT_BISERIAL_RESPONSE_FIELDS',
    'PointBiserialResult',
    'PRIVATE_GOLD_FIELDS',
    'PRIVATE_GOLD_RECORDS',
    'PRIVATE_ONLY_FIELDS',
    'PROFESSIONAL_REALISM_REQUIREMENTS',
    'ProfessionalRealismResult',
    'PUBLIC_ITEM_FIELDS',
    'QUARANTINED_BENEFICIARIES',
    'RELEASE_BUDGETS',
    'REQUEST_FIELDS',
    'REVISION_HISTORY_FIELDS',
    'RS_TRIGGER_FIELDS',
    'REQUESTS_PER_MODEL_SEED',
    'SALIENCE_LEVELS',
    'SCENARIO_CORES',
    'THETA_ELIGIBLE_FAMILIES',
    'THETA_ADDED_STRUCTURE_TEST',
    'THETA_FIT_CONDITIONS',
    'THETA_RESULT_STATUSES',
    'TRACEABILITY_LEVELS',
    'VARIANT_GOLD_FIELDS',
    'X2_PROBE_RULES',
    'bootstrap_ci_status',
    'canonical_json',
    'canonical_sha256',
    'capability_reference_status',
    'easy_hard_fidelity_drop',
    'config_content_sha256',
    'derive_capability_projections',
    'diagnostic_raw_rate_signal_passes',
    'evaluate_professional_realism',
    'flat_id_trigger_status',
    'hash_capability_reference',
    'id_profile_100',
    'item_retention_action',
    'point_biserial_item_total',
    'pooling_branch',
    'professional_realism_passes',
    'release_budget_allows',
    'theta_design_100',
    'theta_estimate_status',
    'tr_null_trigger_status',
    'validate_capability_reference',
    'validate_config_content_sha256',
    'validate_private_gold_fields',
    'validate_profile_cell_key',
    'validate_public_item_fields',
)

LEAF_MODULES = (constants, hashing, schemas, statistics, evidence)


def test_facade_exports_are_complete_disjoint_and_identity_preserving():
    assert common.__all__ == list(EXPECTED_COMMON_EXPORTS)

    export_sets = [set(module.__all__) for module in LEAF_MODULES]
    assert all(
        len(module.__all__) == len(export_set)
        for module, export_set in zip(LEAF_MODULES, export_sets)
    )
    for index, left in enumerate(export_sets):
        for right in export_sets[index + 1 :]:
            assert left.isdisjoint(right)

    expected = set(EXPECTED_COMMON_EXPORTS)
    assert set().union(*export_sets) == expected

    for module in LEAF_MODULES:
        for name in module.__all__:
            assert getattr(common, name) is getattr(module, name)
