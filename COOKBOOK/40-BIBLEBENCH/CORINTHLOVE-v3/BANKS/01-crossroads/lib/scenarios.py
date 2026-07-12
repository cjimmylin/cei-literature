"""Causal scenario grammar for the CROSSROADS deep structures.

The affine design decides which four frozen clauses are measured together.  It
does *not* define the story.  This module independently crosses ten operational
domains with four incident grammars to produce forty substantively different
causal skeletons.  Episodes later apply lexical skins and causal parameter
states to one of these skeletons; they never author a fixed list of episodes.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from string import Formatter


DOMAIN_FRAMES = (
    {
        "code": "transit",
        "domain": "regional transit dispatch",
        "operator": "dispatch coordinator",
        "counterpart": "route supervisor",
        "affected": "transfer crew",
        "reviewer": "service audit desk",
        "artifact": "route transfer manifest",
        "audience": "depot control room",
        "resource": "two dispatch slots",
    },
    {
        "code": "clinic",
        "domain": "community clinic referrals",
        "operator": "referral coordinator",
        "counterpart": "clinic lead",
        "affected": "receiving care team",
        "reviewer": "records desk",
        "artifact": "referral packet",
        "audience": "receiving clinic queue",
        "resource": "two review blocks",
    },
    {
        "code": "water",
        "domain": "municipal water sampling",
        "operator": "sample controller",
        "counterpart": "laboratory analyst",
        "affected": "field response crew",
        "reviewer": "quality desk",
        "artifact": "sample certificate",
        "audience": "district operations board",
        "resource": "two laboratory rerun slots",
    },
    {
        "code": "meals",
        "domain": "school meal distribution",
        "operator": "meal program coordinator",
        "counterpart": "kitchen lead",
        "affected": "delivery team",
        "reviewer": "district review desk",
        "artifact": "allergen delivery roster",
        "audience": "school receiving teams",
        "resource": "two packing-line blocks",
    },
    {
        "code": "housing",
        "domain": "public housing repairs",
        "operator": "repair dispatcher",
        "counterpart": "contractor lead",
        "affected": "tenant service team",
        "reviewer": "inspection desk",
        "artifact": "repair work order",
        "audience": "building service queue",
        "resource": "two technician blocks",
    },
    {
        "code": "archive",
        "domain": "archive digitization",
        "operator": "accession coordinator",
        "counterpart": "scanning lead",
        "affected": "catalog team",
        "reviewer": "collections desk",
        "artifact": "accession sheet",
        "audience": "catalog release queue",
        "resource": "two scanning blocks",
    },
    {
        "code": "shelter",
        "domain": "emergency shelter intake",
        "operator": "shift coordinator",
        "counterpart": "intake lead",
        "affected": "overnight service team",
        "reviewer": "logistics desk",
        "artifact": "bed assignment ledger",
        "audience": "overnight assignment board",
        "resource": "two intake stations",
    },
    {
        "code": "release",
        "domain": "software release operations",
        "operator": "release coordinator",
        "counterpart": "maintenance lead",
        "affected": "service response team",
        "reviewer": "reliability desk",
        "artifact": "deployment manifest",
        "audience": "production change channel",
        "resource": "two validation slots",
    },
    {
        "code": "registry",
        "domain": "research registry operations",
        "operator": "registry coordinator",
        "counterpart": "analysis lead",
        "affected": "participant contact team",
        "reviewer": "oversight desk",
        "artifact": "protocol amendment record",
        "audience": "study operations queue",
        "resource": "two analyst blocks",
    },
    {
        "code": "cooperative",
        "domain": "food cooperative distribution",
        "operator": "distribution coordinator",
        "counterpart": "warehouse lead",
        "affected": "member delivery team",
        "reviewer": "inventory desk",
        "artifact": "delivery allocation sheet",
        "audience": "regional loading queue",
        "resource": "two loading blocks",
    },
)


INCIDENT_FRAMES = (
    {
        "code": "revision",
        "family": "conflicting-revision-record",
        "incident": (
            "two saved revisions disagree on the destination and one receiving "
            "team has already loaded the earlier revision"
        ),
        "evidence_state": (
            "a signed receipt identifies the earlier revision; the later edit has "
            "an author and timestamp but no receiving receipt"
        ),
        "deadline": "the next transfer begins in 47 minutes",
        "baseline_duty": "deliver one reconciled artifact before that transfer begins",
        "access_scope": "the current operational audience only",
        "recurrence": "the stale revision remains in one scheduled queue",
        "loss": "one receiving block must be repeated if the wrong revision remains active",
    },
    {
        "code": "access",
        "family": "unexpected-access-event",
        "incident": (
            "a temporary viewer link was used outside the listed work group while "
            "the artifact still contains named-person fields"
        ),
        "evidence_state": (
            "the access log confirms one external read and one internal share; it "
            "does not identify any later copy"
        ),
        "deadline": "the artifact is scheduled for internal release in 38 minutes",
        "baseline_duty": "produce a release copy with the required operational fields",
        "access_scope": "named operators and the receiving desk",
        "recurrence": "the temporary link remains active for one more hour",
        "loss": "revoking every link would pause the receiving desk for one work block",
    },
    {
        "code": "handoff",
        "family": "incomplete-handoff",
        "incident": (
            "the outgoing shift left one required field blank after reporting that "
            "the underlying task was complete"
        ),
        "evidence_state": (
            "a machine receipt confirms the task event; a second log records an "
            "unresolved exception associated with the blank field"
        ),
        "deadline": "the receiving shift locks its queue in 52 minutes",
        "baseline_duty": "complete the required field and transfer the artifact before lock",
        "access_scope": "the outgoing and receiving work groups",
        "recurrence": "the same blank field is copied into tomorrow's draft",
        "loss": "a late transfer displaces one receiving task into the next shift",
    },
    {
        "code": "capacity",
        "family": "bounded-capacity-allocation",
        "incident": (
            "two verified requests now require the same limited work capacity and "
            "the current allocation note names only one of them"
        ),
        "evidence_state": (
            "separate receipts confirm both requests; their timing fields differ and "
            "neither receipt records a priority override"
        ),
        "deadline": "the allocation closes in 43 minutes",
        "baseline_duty": "publish an executable allocation and its receipt before close",
        "access_scope": "the assignment desk and both receiving groups",
        "recurrence": "the omitted request rolls into a smaller capacity window tomorrow",
        "loss": "each reassigned block removes one block from a scheduled delivery",
    },
)


# These are observable operational claims, not frozen construct labels.  The
# scenario nouns make each rendered claim evidence-bound and scenario-specific.
CLAIM_GRAMMAR = {
    "C1": "finish the recipient-use fields in {artifact} before optional presentation work",
    "C2": "leave {counterpart} a recorded response interval before reassignment",
    "C3": "assign one work unit to the documented request from {affected}",
    "C4": "retain {counterpart}'s contribution line while recording the operator's step",
    "C5": "copy the contribution names from the receipts into {artifact}",
    "C6": "confine personal attribution to {access_scope} while recording the correction",
    "C7": "reserve available capacity for the scheduled shared transfer",
    "C8": "keep the response to the disputed message within the recorded incident facts",
    "C9": "apply the current access rule without deleting the earlier incident log",
    "C10": "record the failed event without adding commentary about the person involved",
    "C11": "make {artifact} match the signed receipt even if the schedule changes",
    "C12": "remove named-person fields from wider circulation while retaining the risk flag",
    "C13": "use provisional access for {counterpart} and check it against the receipt",
    "C14": "run the remaining feasible route in the record without adding an unverified route",
    "C15": "continue the assigned transfer until the documented release condition is met",
    "C16": "mark unresolved fields and route them to {reviewer} before the artifact locks",
}


# Each claim has two neutral operational states.  Neither state has a fixed
# score.  A cell's evidence specifies which state is required, each stable plan
# produces one state, and the hidden sign is derived solely from equality of
# those two values.  Rendering therefore never accepts a sign or failure pole.
STATE_ALTERNATIVES = {
    "C1": (
        "recipient routing fields precede the optional summary panel",
        "requested metric fields precede the routing summary",
    ),
    "C2": (
        "assignment changes after a recorded twenty-minute response interval",
        "assignment changes at once under the active incident authority",
    ),
    "C3": (
        "one unit moves to the newly recorded request",
        "the unit remains with the already scheduled request",
    ),
    "C4": (
        "the counterpart contribution line appears before the operator line",
        "the operator contribution line appears before the counterpart line",
    ),
    "C5": (
        "the operator contribution line records the completed step",
        "the counterpart contribution line records the completed step",
    ),
    "C6": (
        "personal attribution is confined to the review group",
        "personal attribution accompanies the correction to the work audience",
    ),
    "C7": (
        "the remaining unit stays with the shared transfer",
        "the remaining unit stays with the operator's assigned task",
    ),
    "C8": (
        "the reply contains incident timestamps without the disputed aside",
        "the reply includes the disputed message beside the incident timestamps",
    ),
    "C9": (
        "the current access rule applies with the earlier event retained in the log",
        "the earlier event activates the recorded restricted-access rule",
    ),
    "C10": (
        "the notice contains event, timestamp, and next response",
        "the notice contains event, responsible role, and next response",
    ),
    "C11": (
        "the signed receipt value replaces the disputed field",
        "the later saved value remains pending a receipt check",
    ),
    "C12": (
        "named-person fields are removed from the audience copy",
        "named-person fields remain in the access-bounded operations copy",
    ),
    "C13": (
        "bounded access starts before a scheduled receipt check",
        "access starts only after the receipt check completes",
    ),
    "C14": (
        "the documented remaining route opens for one work block",
        "the route stays closed until its availability receipt arrives",
    ),
    "C15": (
        "the transfer continues until the recorded release condition",
        "the transfer releases when the recorded stop condition activates",
    ),
    "C16": (
        "unresolved fields route to a check before lock",
        "the signed fields lock while the unresolved fields remain marked",
    ),
}


# Held-out qualification paraphrases share state identity but no authored
# four-token sequence with the private state lexicon.
PUBLIC_STATE_ALTERNATIVES = {
    "C1": ("routing entries are completed ahead of the nonessential synopsis", "requested measurement entries are completed ahead of the route overview"),
    "C2": ("ownership moves only once a twenty-minute reply period has elapsed", "active incident authority moves ownership immediately"),
    "C3": ("a work block is transferred to the newly logged request", "a work block stays on the previously scheduled request"),
    "C4": ("the peer's work entry is listed ahead of the operator entry", "the operator work entry is listed ahead of the peer entry"),
    "C5": ("the finished step is entered on the operator attribution line", "the finished step is entered on the peer attribution line"),
    "C6": ("identity details remain within the examining group", "identity details travel with the correction to the operating group"),
    "C7": ("the final capacity block remains assigned to the collective transfer", "the final capacity block remains assigned to the operator task"),
    "C8": ("the answer lists incident times and excludes the contested aside", "the answer places the contested message alongside the incident times"),
    "C9": ("today's access rule applies while the earlier event remains archived", "the earlier event triggers the documented narrower access rule"),
    "C10": ("the update lists what occurred, when, and the next step", "the update lists what occurred, the accountable role, and the next step"),
    "C11": ("the signed-record value supersedes the contested field", "the newest saved value waits for record confirmation"),
    "C12": ("person-identifying fields are absent from the audience version", "person-identifying fields remain inside the operations-limited version"),
    "C13": ("limited entry begins with a later record check already booked", "entry begins after the record check has finished"),
    "C14": ("the remaining documented channel opens for a single work interval", "the channel remains shut pending its availability record"),
    "C15": ("the transfer proceeds until its logged release trigger", "the transfer exits when its logged stop trigger fires"),
    "C16": ("unsettled fields are sent for examination before locking", "signed fields lock while unsettled fields stay visibly marked"),
}


# Directional mismatch adjudication is private.  Both paths that produce the
# same wrong state receive the same defeat class; no path identity or ordinal
# participates.  The two directions are clause-specifically interpretable and
# are audited for balance across the frozen requirement schedule.
MISMATCH_DIRECTIONS = {
    clause: {
        (1, -1): first,
        (-1, 1): second,
    }
    for clause, first, second in (
        ("C1", "harsh", "sentimental"),
        ("C2", "harsh", "sentimental"),
        ("C3", "harsh", "sentimental"),
        ("C4", "harsh", "sentimental"),
        ("C5", "sentimental", "harsh"),
        ("C6", "harsh", "sentimental"),
        ("C7", "harsh", "sentimental"),
        ("C8", "harsh", "sentimental"),
        ("C9", "harsh", "sentimental"),
        ("C10", "harsh", "sentimental"),
        ("C11", "sentimental", "harsh"),
        ("C12", "harsh", "sentimental"),
        ("C13", "harsh", "sentimental"),
        ("C14", "harsh", "sentimental"),
        ("C15", "harsh", "sentimental"),
        ("C16", "harsh", "sentimental"),
    )
}

_DIRECTION_NOTES = {
    "C1": ("alternate output displaces the evidenced recipient task", "unneeded recipient-facing work becomes an agent-centered sacrifice"),
    "C2": ("the response interval is cut short by takeover", "waiting continues after incident authority requires intervention"),
    "C3": ("documented need is left without the available unit", "an unrequired request displaces the scheduled task"),
    "C4": ("the counterpart's evidenced role is displaced", "the operator's evidenced role is erased"),
    "C5": ("the operator's evidenced step is assigned away", "the counterpart's evidenced step is captured by the operator line"),
    "C6": ("attribution circulates beyond the evidenced audience", "material attribution is withheld from the audience that requires it"),
    "C7": ("shared capacity is taken for the operator queue", "the operator's assigned capacity is erased until the mission loses it"),
    "C8": ("the disputed aside is added where the evidence excludes it", "the disputed message is omitted where the incident record requires a substantive answer"),
    "C9": ("the old event governs current treatment beyond the active rule", "the old safety event is ignored where the active restriction depends on it"),
    "C10": ("person or role detail is added where event-only reporting is required", "accountable role detail is omitted where the evidence requires it"),
    "C11": ("verified receipt content is withheld to preserve the saved state", "an unverified receipt is imposed before the required check"),
    "C12": ("named fields circulate where the evidence requires shelter", "risk-relevant named fields are hidden from the bounded group that requires them"),
    "C13": ("bounded access is refused despite the available calibrated check", "access begins before the required receipt check"),
    "C14": ("the evidenced feasible route is closed prematurely", "a route opens despite evidence requiring a prior availability check"),
    "C15": ("the assigned transfer is released before its condition", "the procedure continues after the warranted stop condition"),
    "C16": ("the state locks while evidenced uncertainty remains unresolved", "settled signed fields are displaced without exercising the assigned judgment"),
}

MISMATCH_RATIONALES = {
    clause: {
        (1, -1): (
            f"evidence requires state A ({states[0]}) but the plan produces "
            f"state B ({states[1]}): {_DIRECTION_NOTES[clause][0]}"
        ),
        (-1, 1): (
            f"evidence requires state B ({states[1]}) but the plan produces "
            f"state A ({states[0]}): {_DIRECTION_NOTES[clause][1]}"
        ),
    }
    for clause, states in STATE_ALTERNATIVES.items()
}


def mismatch_pole(*, clause: str, required_state: int,
                  action_state: int) -> tuple[str, str]:
    if required_state == action_state:
        raise ValueError("a matching state has no failure pole")
    direction = (required_state, action_state)
    try:
        return (
            MISMATCH_DIRECTIONS[clause][direction],
            MISMATCH_RATIONALES[clause][direction],
        )
    except KeyError:
        raise KeyError("unknown clause or mismatch direction") from None


PARAMETER_OBSERVATIONS = (
    "recurrence marker remains active",
    "named-field circulation remains bounded",
    "deadline queue has one remaining slot",
    "receipt set remains incomplete",
    "prior coordination log remains attached",
    "two receiving groups share the next state change",
)

SKIN_TERMS = ("ledger view", "operations view", "receipt view", "field view")


DOMAIN_PLAN_KINDS = {
    "transit": ("route_notice", "manifest_reconcile", "dispatch_reserve", "depot_checkpoint"),
    "clinic": ("referral_notice", "packet_amend", "clinical_check", "receiving_huddle"),
    "water": ("district_advisory", "certificate_revision", "sample_rerun", "field_checkpoint"),
    "meals": ("school_notice", "roster_revision", "packing_recheck", "kitchen_checkpoint"),
    "housing": ("tenant_notice", "work_order_revision", "inspection_reserve", "site_checkpoint"),
    "archive": ("catalog_notice", "accession_revision", "scan_recheck", "collection_checkpoint"),
    "shelter": ("shift_notice", "ledger_revision", "intake_reserve", "handoff_checkpoint"),
    "release": ("change_notice", "manifest_patch", "validation_reserve", "release_checkpoint"),
    "registry": ("study_notice", "amendment_revision", "analysis_recheck", "oversight_checkpoint"),
    "cooperative": ("member_notice", "allocation_revision", "loading_reserve", "warehouse_checkpoint"),
}


def _format(template: str, values: dict) -> str:
    required = {field for _, field, _, _ in Formatter().parse(template) if field}
    missing = required - set(values)
    if missing:
        raise KeyError(f"scenario template is missing fields: {sorted(missing)}")
    return template.format(**values)


def _stable_plan_frames(values: dict) -> list[dict]:
    artifact = values["artifact"]
    audience = values["audience"]
    reviewer = values["reviewer"]
    resource = values["resource"]
    kinds = DOMAIN_PLAN_KINDS[values["domain_code"]]
    incident = values["incident"]
    return [
        {
            "path_id": "path-0",
            "action_role": "notice",
            "plan_kind": kinds[0],
            "plan": f"send a {values['domain']} state notice about {artifact} to {audience}",
            "causal_commitment": f"the named audience receives a timestamped notice about: {incident}",
        },
        {
            "path_id": "path-1",
            "action_role": "record",
            "plan_kind": kinds[1],
            "plan": f"write a reconciled {values['incident_code']} state into {artifact}",
            "causal_commitment": f"the {artifact} state changes for every later reader in {audience}",
        },
        {
            "path_id": "path-2",
            "action_role": "capacity",
            "plan_kind": kinds[2],
            "plan": f"assign {resource} to check the {values['incident_code']} receipts",
            "causal_commitment": f"{resource} leaves the delivery queue and produces a domain receipt",
        },
        {
            "path_id": "path-3",
            "action_role": "checkpoint",
            "plan_kind": kinds[3],
            "plan": f"reserve a 20-minute {values['domain']} checkpoint with {reviewer}",
            "causal_commitment": f"the checkpoint uses the remaining window and writes a {values['incident_code']} receipt",
        },
    ]


def build_scenario_catalog() -> list[dict]:
    """Generate the frozen forty-skeleton scenario catalog from two grammars."""
    rows = []
    index = 0
    for domain in DOMAIN_FRAMES:
        for incident in INCIDENT_FRAMES:
            index += 1
            values = {
                **domain,
                **incident,
                "domain_code": domain["code"],
                "incident_code": incident["code"],
            }
            scenario_id = f"XR-SCN-{index:03d}"
            claims = [
                {
                    "clause": clause,
                    "claim_id": f"{scenario_id}-CLAIM-{int(clause[1:]):02d}",
                    "visible_claim": _format(template, values),
                    "evidence_ref": f"{scenario_id}-EVIDENCE-{incident['code']}",
                }
                for clause, template in CLAIM_GRAMMAR.items()
            ]
            rows.append({
                "scenario_id": scenario_id,
                "template_family": f"{domain['code']}-{incident['family']}",
                "domain": domain["domain"],
                "roles": {
                    key: domain[key]
                    for key in ("operator", "counterpart", "affected", "reviewer")
                },
                "artifact": domain["artifact"],
                "audience": domain["audience"],
                "resource": domain["resource"],
                "incident_kind": incident["code"],
                "incident": incident["incident"],
                "evidence_state": incident["evidence_state"],
                "evidence_id": f"{scenario_id}-EVIDENCE-{incident['code']}",
                "deadline": incident["deadline"],
                "baseline_duty": incident["baseline_duty"],
                "access_scope": incident["access_scope"],
                "recurrence": incident["recurrence"],
                "loss": incident["loss"],
                "claim_catalog": claims,
                "action_plans": _stable_plan_frames(values),
            })
    validate_scenario_catalog(rows)
    return rows


def validate_scenario_catalog(rows: list[dict]) -> None:
    if len(rows) != 40:
        raise AssertionError("scenario grammar must emit exactly forty skeletons")
    for field in ("scenario_id", "template_family", "incident", "evidence_state"):
        values = [row[field] for row in rows]
        if len(values) != len(set(values)) and field in {"scenario_id", "template_family"}:
            raise AssertionError(f"scenario {field} must be unique")
    fingerprints = set()
    for row in rows:
        if len(row["claim_catalog"]) != 16 or len(row["action_plans"]) != 4:
            raise AssertionError("every scenario needs sixteen claims and four stable plans")
        if len({p["plan_kind"] for p in row["action_plans"]}) != 4:
            raise AssertionError("scenario action plan kinds must be distinct")
        causal = {
            key: row[key]
            for key in (
                "domain", "roles", "artifact", "incident", "evidence_state",
                "deadline", "baseline_duty", "access_scope", "recurrence", "loss",
            )
        }
        digest = hashlib.sha256(
            json.dumps(causal, sort_keys=True).encode("utf-8")
        ).hexdigest()
        if digest in fingerprints:
            raise AssertionError("two scenario skeletons have identical causal content")
        fingerprints.add(digest)


def claim_records(scenario: dict, clauses: list[str]) -> list[dict]:
    by_clause = {row["clause"]: row for row in scenario["claim_catalog"]}
    return [deepcopy(by_clause[clause]) for clause in clauses]


def observable_effect(*, scenario: dict, clause: str, action_state: int,
                      path_id: str, skin_index: int) -> str:
    """Render a stable plan state without accepting a hidden sign or pole."""
    if clause not in STATE_ALTERNATIVES or action_state not in {-1, 1}:
        raise KeyError("unknown clause or action state")
    if skin_index not in range(4):
        raise ValueError("skin index outside frozen rendering grid")
    lexicon = PUBLIC_STATE_ALTERNATIVES if skin_index == 3 else STATE_ALTERNATIVES
    outcome = lexicon[clause][0 if action_state == 1 else 1]
    if skin_index == 3:
        return (
            "the enacted field operation writes the following observable condition "
            f"into {scenario['artifact']}: {outcome}"
        )
    return (
        f"in the {SKIN_TERMS[skin_index]}, the enacted operation sets this state "
        f"for {scenario['artifact']}: {outcome}"
    )


def required_state_text(*, scenario: dict, clause: str,
                        required_state: int, parameter_index: int,
                        public: bool) -> str:
    """Render the evidence-derived state that the cell requires."""
    if clause not in STATE_ALTERNATIVES or required_state not in {-1, 1}:
        raise KeyError("unknown clause or required state")
    if parameter_index not in range(6):
        raise ValueError("parameter index outside frozen grid")
    lexicon = PUBLIC_STATE_ALTERNATIVES if public else STATE_ALTERNATIVES
    state = lexicon[clause][0 if required_state == 1 else 1]
    if public:
        return (
            "the active field receipt selects this operating condition: "
            f"{state}; two receiving groups depend on the next update"
        )
    return (
        f"the current trace requires '{state}' because the "
        f"{PARAMETER_OBSERVATIONS[parameter_index]}"
    )


SCENARIO_CATALOG = tuple(build_scenario_catalog())
