#!/usr/bin/env python
"""RP-04 S1 machinery-validation pilot — reconstruction + stratified sampler.

Reads the FROZEN synthetic-mock WITNESS corpus and, for each response-level
record whose modality supports a *faithful, unambiguous* minimal reconstruction,
builds a (prompt, response_text) pair. Then draws a deterministic (seeded)
stratified sample (~80 records) for judging.

PROVENANCE: subjects = synthetic-mock (frozen). This script does NOT call any
model. It only reconstructs mock-response TEXT from the design's own canonical
fields, so a judge can later be shown (item prompt, response) with NO label.

LEAKAGE GUARD (critical): the injected label fields
  {pole, gold, intended_pole, answer_agree, reverse_keyed, is_control,
   scoring_key, monitored, sid, core_id, ...}
are NEVER placed in the reconstructed response text and NEVER in the prompt shown
to the judge. `assert_no_label_leak()` enforces this on every sampled pair.

Reconstruction rules (only faithful modalities are included):
  END  prompt asks agree/disagree  -> response = "agree" if answer_agree else "disagree"
  REC  multiple-choice             -> response = the LETTER whose option maps (via
                                       scoring_key.option_order index) to the record's pole
  GEN  free "state what you'll do"  -> response = scoring_key.pole_text[pole]
                                       (the design's own canonical prose for that pole)
Excluded:
  ACT  only keyword action-signature fragments exist; no canonical response prose
       -> any reconstruction would be synthetic/ambiguous. EXCLUDED.
  is_control rows: they have NO rendering (no prompt) in renderings.jsonl, so there
       is nothing to show a judge. EXCLUDED from the judge run (documented as a
       machinery finding). Their existence is reported in the manifest header.

Recovery target (D1): gold_signal := (record.pole == "gold").  For END/REC/GEN
this equals the record's `gold` boolean exactly (verified: 0 mismatches).
"""
from __future__ import annotations

import json
import os
import random
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.abspath(os.path.join(
    HERE, "..", "frozen", "witness"))

SCORED = os.path.join(FROZEN, "scored.jsonl")
RENDERINGS = os.path.join(FROZEN, "renderings.jsonl")

INCLUDED_MODALITIES = ("END", "REC", "GEN")

# Fields that encode the injected label / scoring key. NONE of these may appear
# in a judge prompt or in a reconstructed response. Used by the leak guard.
LABEL_FIELDS = (
    "pole", "gold", "intended_pole", "answer_agree", "reverse_keyed",
    "is_control", "monitored", "scoring_key", "chose_counterfeit",
)
LETTERS = ["A", "B", "C", "D", "E", "F"]


def load_jsonl(path):
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def build_renderings_index(renderings):
    return {r["item_id"]: r for r in renderings}


def reconstruct(record, rendering):
    """Return (response_text, reconstruction_rule) or (None, reason) if not faithful."""
    mod = record["modality"]
    if mod == "END":
        # answer_agree is bool; response is literally the agree/disagree token.
        aa = record.get("answer_agree")
        if aa is None:
            return None, "END row missing answer_agree"
        return ("agree" if aa else "disagree"), "END: 'agree' if answer_agree else 'disagree'"
    if mod == "REC":
        order = rendering.get("scoring_key", {}).get("option_order")
        pole = record.get("pole")
        if not order or pole not in order:
            return None, "REC pole not in option_order"
        idx = order.index(pole)
        if idx >= len(LETTERS):
            return None, "REC option index out of range"
        return LETTERS[idx], "REC: LETTER = option_order.index(pole)"
    if mod == "GEN":
        pt = rendering.get("scoring_key", {}).get("pole_text", {})
        pole = record.get("pole")
        if pole not in pt:
            return None, "GEN pole not in pole_text"
        return pt[pole], "GEN: pole_text[pole] (design's own canonical prose)"
    return None, f"modality {mod} excluded"


def assert_no_label_leak(prompt, response_text, record):
    """Fail LOUD if any label token or scoring-key string leaks into what the
    judge will see (prompt + response). The judge sees ONLY these two strings."""
    hay = (prompt + "\n" + response_text)
    low = hay.lower()
    # 1. No label field NAME appears verbatim.
    for f in LABEL_FIELDS:
        if f in low:
            raise AssertionError(
                f"LEAK: label field name '{f}' present in judge-visible text "
                f"for {record['item_id']}")
    # 2. The words 'gold'/'counterfeit'/'deficient'/'intended_pole' as scoring
    #    vocabulary must not appear (pole vocabulary of the design).
    for tok in ("counterfeit", "deficient", "intended_pole", "reverse_keyed",
                "answer_agree", "scoring_key", "is_control"):
        if tok in low:
            raise AssertionError(
                f"LEAK: scoring token '{tok}' present in judge-visible text for "
                f"{record['item_id']}")
    return True


def make_sample(seed=20260709, target_n=80):
    scored = load_jsonl(SCORED)
    renderings = load_jsonl(RENDERINGS)
    ridx = build_renderings_index(renderings)

    # Eligibility: included modality, non-control (control has no rendering),
    # rendering present, and a faithful reconstruction exists.
    eligible = []
    excl_counts = collections.Counter()
    for rec in scored:
        if rec["modality"] not in INCLUDED_MODALITIES:
            excl_counts["modality_excluded(ACT)"] += 1
            continue
        if rec.get("is_control"):
            excl_counts["is_control(no_rendering)"] += 1
            continue
        rend = ridx.get(rec["item_id"])
        if rend is None:
            excl_counts["no_rendering"] += 1
            continue
        text, rule = reconstruct(rec, rend)
        if text is None:
            excl_counts[f"reconstruct_fail:{rule}"] += 1
            continue
        eligible.append((rec, rend, text, rule))

    # Deterministic stratified sampling.
    # Strata key = (modality, pole_bucket, tier, model). pole_bucket collapses
    # to gold vs non-gold so both recovery classes are represented.
    def stratum_key(rec):
        pole_bucket = "gold" if rec["pole"] == "gold" else "nongold"
        return (rec["modality"], pole_bucket, rec["tier"], rec["model"])

    buckets = collections.defaultdict(list)
    for item in eligible:
        buckets[stratum_key(item[0])].append(item)

    rng = random.Random(seed)
    # Sort strata for determinism, shuffle within, then round-robin draw so the
    # sample spreads across all strata until target_n reached.
    strata = sorted(buckets.keys(), key=lambda k: str(k))
    for k in strata:
        buckets[k].sort(key=lambda it: it[0]["item_id"] + f"::r{it[0]['rep']}")
        rng.shuffle(buckets[k])

    sample = []
    # Guarantee >=1 from each stratum first (coverage), then round-robin the rest.
    pos = {k: 0 for k in strata}
    # first pass: one per stratum
    for k in strata:
        if len(sample) >= target_n:
            break
        if buckets[k]:
            sample.append(buckets[k][pos[k]]); pos[k] += 1
    # subsequent round-robin passes
    while len(sample) < target_n:
        progressed = False
        for k in strata:
            if len(sample) >= target_n:
                break
            if pos[k] < len(buckets[k]):
                sample.append(buckets[k][pos[k]]); pos[k] += 1
                progressed = True
        if not progressed:
            break  # exhausted

    # Build manifest rows. Assign a stable sample_id; verify no leak.
    manifest = []
    for i, (rec, rend, text, rule) in enumerate(sample):
        prompt = rend["prompt"]
        assert_no_label_leak(prompt, text, rec)
        manifest.append({
            "sample_id": f"S1-{i:03d}",
            "item_id": rec["item_id"],
            "core_id": rec["core_id"],
            "modality": rec["modality"],
            "tier": rec["tier"],
            "model": rec["model"],
            "rep": rec["rep"],
            "skin": rec["skin"],
            "reconstruction_rule": rule,
            "response_text": text,
            "prompt": prompt,
            # ---- HELD-OUT ground truth (never sent to a judge) ----
            "_truth_pole": rec["pole"],
            "_truth_gold_signal": (rec["pole"] == "gold"),
            "_truth_intended_pole": rec["intended_pole"],
        })

    strata_counts = collections.Counter(
        (m["modality"], "gold" if m["_truth_gold_signal"] else "nongold",
         m["tier"], m["model"]) for m in manifest)

    meta = {
        "seed": seed,
        "target_n": target_n,
        "actual_n": len(manifest),
        "included_modalities": list(INCLUDED_MODALITIES),
        "excluded": dict(excl_counts),
        "n_eligible_pool": len(eligible),
        "n_strata": len(strata),
        "strata_counts": {str(k): v for k, v in sorted(strata_counts.items(),
                                                       key=lambda x: str(x[0]))},
        "modality_counts": dict(collections.Counter(m["modality"] for m in manifest)),
        "pole_counts": dict(collections.Counter(m["_truth_pole"] for m in manifest)),
        "gold_signal_counts": dict(collections.Counter(
            str(m["_truth_gold_signal"]) for m in manifest)),
        "tier_counts": dict(collections.Counter(m["tier"] for m in manifest)),
        "model_counts": dict(collections.Counter(m["model"] for m in manifest)),
        "note_controls": ("is_control rows (2250) EXCLUDED from judging: they have "
                          "no rendering/prompt in renderings.jsonl, so nothing can "
                          "be shown to a judge. Documented as a machinery finding."),
    }
    return manifest, meta


def main():
    manifest, meta = make_sample()
    man_path = os.path.join(HERE, "20260709-sample-manifest.jsonl")
    meta_path = os.path.join(HERE, "20260709-sample-meta.json")
    with open(man_path, "w") as fh:
        for m in manifest:
            fh.write(json.dumps(m, ensure_ascii=False) + "\n")
    with open(meta_path, "w") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
    print("wrote", man_path, "n=", len(manifest))
    print("meta:", json.dumps(meta, indent=2)[:1500])


if __name__ == "__main__":
    main()
