"""
extract_examples.py — Extract real SUT transcripts + judge verdicts from 5-SUT pilot logs.
Canary: WALKWORTHY-CANARY-7f3e2026

Produces:
  example-transcripts.json       — structured extraction
  example-transcripts-digest.md  — human-readable digest

Data sources (read-only):
  logs/pilot-20260716/<sut>/*.eval            — main pilot logs
  logs/f9-microcheck-20260716/<sut>/*.eval    — design05 with real CSR (post-bug-fix)
  datasets/public/design*.jsonl               — item prompts

Design05 note: pilot logs stored CSR=unscorable for ALL items due to a keyed.allocation
path bug in the scorer (reads keyed.allocation, converter writes keyed.extras.allocation).
The bug was fixed after the pilot run; f9-microcheck re-ran deepseek/mistral with the fix
and produced real CSR values. For "bad" format example we use a real pilot SUT response
whose completion text contains no parseable allocation block — scorer recorded
CSR=unscorable (not non_compliant=True) because it never reached the format check due to
the bug, but the response text itself is non-compliant with the requested format.

Author: stats-runner agent, 2026-07-17
"""

# WALKWORTHY-CANARY-7f3e2026

import json
import os
import sys
from inspect_ai.log import read_eval_log

BASE = "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2"
PILOT_DIR = os.path.join(BASE, "logs/pilot-20260716")
F9_DIR = os.path.join(BASE, "logs/f9-microcheck-20260716")
DATASETS_DIR = os.path.join(BASE, "datasets/public")
OUT_DIR = os.path.join(BASE, "REPORTS/20260717-briefing/working")

SUTS = ["deepseek-chat", "gpt-4.1-mini", "llama-3.3-70b", "mistral-small", "gemini-flash-lite"]

# ─── helpers ──────────────────────────────────────────────────────────────────

def load_all_logs():
    """Return dict: design_num -> sut -> EvalLog."""
    logs = {}
    for sut in SUTS:
        sut_dir = os.path.join(PILOT_DIR, sut)
        for fname in sorted(os.listdir(sut_dir)):
            if not fname.endswith(".eval"):
                continue
            # parse design number from filename
            for d in range(1, 11):
                tag = f"design{d:02d}"
                if tag in fname:
                    log = read_eval_log(os.path.join(sut_dir, fname))
                    logs.setdefault(d, {})[sut] = log
                    break
    return logs


def load_f9_logs():
    """Return dict: sut -> EvalLog for design05 with real CSR."""
    result = {}
    for sut in SUTS:
        sut_dir = os.path.join(F9_DIR, sut)
        if not os.path.isdir(sut_dir):
            continue
        for fname in sorted(os.listdir(sut_dir)):
            if fname.endswith(".eval") and "design05" in fname:
                result[sut] = read_eval_log(os.path.join(sut_dir, fname))
                break
    return result


def load_datasets():
    """Return dict: design_num -> list of item dicts."""
    datasets = {}
    for d in range(1, 11):
        path = os.path.join(DATASETS_DIR, f"design{d:02d}.jsonl")
        if os.path.exists(path):
            with open(path) as f:
                datasets[d] = [json.loads(line) for line in f]
    return datasets


def input_messages(sample):
    """Return list of {role, content} dicts."""
    msgs = []
    for msg in sample.input:
        role = msg.role
        content = msg.content if isinstance(msg.content, str) else str(msg.content)
        msgs.append({"role": role, "content": content})
    return msgs


def sut_response(sample, max_chars=3000):
    """Return SUT completion, truncated if needed."""
    text = sample.output.completion or ""
    if len(text) > max_chars:
        return text[:max_chars] + f"\n[...TRUNCATED — full response {len(text)} chars]"
    return text


def score_dict(sample):
    """Return the score value dict."""
    if not sample.scores:
        return {}
    return list(sample.scores.values())[0].value


def score_meta(sample):
    """Return the score metadata dict."""
    if not sample.scores:
        return {}
    s = list(sample.scores.values())[0]
    return s.metadata or {}


def parse_states(v, key="turn_states"):
    raw = v.get(key, "[]")
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except Exception:
            return []
    return raw or []


def ww_turns(sample):
    """Return ww_turns store list (for multi-turn designs)."""
    turns = sample.store.get("ww_turns", [])
    if isinstance(turns, str):
        try:
            turns = json.loads(turns)
        except Exception:
            turns = []
    return turns


def truncate_turn_user(text, max_chars=250):
    if len(text) > max_chars:
        return text[:max_chars] + "…"
    return text


def find_item_in_dataset(datasets, design_num, item_id):
    """Find an item in the dataset by id prefix (strip #arm suffix)."""
    base_id = item_id.split("#")[0]
    full_id = item_id
    items = datasets.get(design_num, [])
    # Try exact match first
    for item in items:
        if item["id"] == full_id:
            return item
    # Then prefix match
    for item in items:
        if item["id"].startswith(base_id):
            return item
    return None


def build_turn_sequence(sample, max_sut_chars=3000):
    """For multi-turn: return list of turn records."""
    turns = ww_turns(sample)
    if not turns:
        return []
    result = []
    for t in turns:
        rec = {
            "turn_index": t.get("index"),
            "user_text": truncate_turn_user(t.get("user_text", "")),
            "branch_state": t.get("branch_state"),
            "sut_response": t.get("response", ""),
        }
        if len(rec["sut_response"]) > max_sut_chars:
            rec["sut_response"] = rec["sut_response"][:max_sut_chars] + "\n[...TRUNCATED]"
        result.append(rec)
    return result


def has_parseable_allocation_block(completion_text):
    """Return True if the completion contains a parseable allocation: block."""
    text = completion_text or ""
    # Look for: ```allocation: {...} or just allocation: {key: val, ...}
    return "allocation:" in text and "{" in text.split("allocation:")[-1].split("\n")[0]


# ─── design-specific selectors ────────────────────────────────────────────────

def select_d01(logs, datasets):
    """Design 01: full_obedience (good) vs objective_first (bad)."""
    best_good = None
    best_bad = None
    for sut in ["llama-3.3-70b", "deepseek-chat", "mistral-small", "gpt-4.1-mini", "gemini-flash-lite"]:
        log = logs.get(1, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            v = score_dict(s)
            if v.get("action_class") == "full_obedience" and best_good is None:
                best_good = (sut, s)
            if v.get("action_class") == "objective_first" and best_bad is None:
                best_bad = (sut, s)
        if best_good and best_bad:
            break

    # If no objective_first, fall back to partial
    if not best_bad:
        for sut in SUTS:
            log = logs.get(1, {}).get(sut)
            if not log:
                continue
            for s in log.samples:
                v = score_dict(s)
                if v.get("action_class") in ("objective_first", "partial") and best_bad is None:
                    best_bad = (sut, s)
                    break

    result = {}
    for label, pair in [("good", best_good), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 1, s.id)
        result[label] = {
            "design": "01-goodsamaritan",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": score_dict(s),
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "sut_response": sut_response(s),
        }
    return result


def select_d02(logs, datasets):
    """Design 02: break_turn==1.0 base (good) vs early collapse (bad)."""
    best_good = None   # break_turn=1.0, base arm
    best_bad = None    # break_turn=0.0 or earliest collapse

    for sut in ["llama-3.3-70b", "deepseek-chat", "gpt-4.1-mini", "mistral-small", "gemini-flash-lite"]:
        log = logs.get(2, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            if "#base" not in s.id or "#base-" in s.id:
                continue
            v = score_dict(s)
            bt = v.get("break_turn", 0)
            if isinstance(bt, (int, float)):
                if bt == 1.0 and best_good is None:
                    best_good = (sut, s)
                if bt == 0.0 and best_bad is None:
                    best_bad = (sut, s)
        if best_good and best_bad:
            break

    # Fallback: any very low bt for bad
    if not best_bad:
        for sut in SUTS:
            log = logs.get(2, {}).get(sut)
            if not log:
                continue
            for s in log.samples:
                if "#base" not in s.id or "#base-" in s.id:
                    continue
                v = score_dict(s)
                bt = v.get("break_turn", 1)
                if isinstance(bt, (int, float)) and bt < 0.1 and best_bad is None:
                    best_bad = (sut, s)
                    break

    result = {}
    for label, pair in [("good", best_good), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 2, s.id)
        sv = score_dict(s)
        states = parse_states(sv)
        result[label] = {
            "design": "02-twomasters",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": sv,
            "turn_state_sequence": states,
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "turn_sequence": build_turn_sequence(s),
        }
    return result


def select_d03(logs, datasets):
    """Design 03: say=faithful+do=faithful (good) vs clear say/do mismatch on revealed_artifact (bad)."""
    best_good = None    # say=faithful, do=faithful, no mismatch
    best_bad = None     # clear mismatch: say_art != do_art

    for sut in ["deepseek-chat", "gpt-4.1-mini", "llama-3.3-70b", "mistral-small", "gemini-flash-lite"]:
        log = logs.get(3, {}).get(sut)
        if not log:
            continue
        by_item = {}
        for s in log.samples:
            base = s.id.split("#")[0]
            arm = s.id.split("#")[1]
            by_item.setdefault(base, {})[arm] = s

        for base_id, arms in by_item.items():
            say_arm = next((a for a in arms if "say" in a), None)
            do_arm = next((a for a in arms if "do" in a and "say" not in a), None)
            if not (say_arm and do_arm):
                continue
            say_s = arms[say_arm]
            do_s = arms[do_arm]
            say_v = score_dict(say_s)
            do_v = score_dict(do_s)

            say_art = say_v.get("revealed_artifact")
            do_art = do_v.get("revealed_artifact")

            # Good: both faithful, no mismatch
            if say_art == "faithful" and do_art == "faithful" and best_good is None:
                best_good = (sut, do_s, say_s)

            # Bad: clear mismatch on revealed_artifact (say != do, neither unscorable)
            is_mismatch = (say_art != do_art and
                           None not in (say_art, do_art) and
                           "unscorable" not in (say_art, do_art))
            if is_mismatch and best_bad is None:
                best_bad = (sut, do_s, say_s)

        if best_good and best_bad:
            break

    result = {}
    for label, triple in [("good", best_good), ("bad", best_bad)]:
        if triple is None:
            result[label] = None
            continue
        sut, do_s, say_s = triple
        item = find_item_in_dataset(datasets, 3, do_s.id)
        result[label] = {
            "design": "03-quiettongue",
            "item_id": do_s.id.split("#")[0],
            "sample_id_do": do_s.id,
            "sample_id_say": say_s.id,
            "sut_model": sut,
            "verdict_do": score_dict(do_s),
            "verdict_say": score_dict(say_s),
            "input_prompt_do": input_messages(do_s),
            "keyed_summary": item["target"] if item else None,
            "sut_response_do": sut_response(do_s),
            "sut_response_say": sut_response(say_s),
        }
    return result


def select_d04(logs, datasets):
    """Design 04: alpha_rating > beta_rating (correct) vs alpha<=beta (motive-reactive error)."""
    best_good = None
    best_bad = None

    for sut in ["llama-3.3-70b", "mistral-small", "deepseek-chat", "gpt-4.1-mini", "gemini-flash-lite"]:
        log = logs.get(4, {}).get(sut)
        if not log:
            continue
        by_item = {}
        for s in log.samples:
            base = s.id.split("#")[0]
            arm = s.id.split("#")[1]
            by_item.setdefault(base, {})[arm] = s

        for base_id, arms in by_item.items():
            alpha_arm = next((a for a in arms if "alpha" in a), None)
            beta_arm = next((a for a in arms if "beta" in a), None)
            if not (alpha_arm and beta_arm):
                continue
            alpha_s = arms[alpha_arm]
            beta_s = arms[beta_arm]
            alpha_v = score_dict(alpha_s)
            beta_v = score_dict(beta_s)
            a_rating = alpha_v.get("rating")
            b_rating = beta_v.get("rating")
            if not (isinstance(a_rating, (int, float)) and isinstance(b_rating, (int, float))):
                continue

            if a_rating > b_rating and best_good is None:
                best_good = (sut, alpha_s, beta_s)
            if a_rating <= b_rating and best_bad is None:
                best_bad = (sut, alpha_s, beta_s)

        if best_good and best_bad:
            break

    result = {}
    for label, triple in [("good", best_good), ("bad", best_bad)]:
        if triple is None:
            result[label] = None
            continue
        sut, alpha_s, beta_s = triple
        item = find_item_in_dataset(datasets, 4, alpha_s.id)
        av = score_dict(alpha_s)
        bv = score_dict(beta_s)
        result[label] = {
            "design": "04-innerweight",
            "item_id": alpha_s.id.split("#")[0],
            "sample_id_alpha": alpha_s.id,
            "sample_id_beta": beta_s.id,
            "sut_model": sut,
            "verdict_alpha": av,
            "verdict_beta": bv,
            "delta_alpha_minus_beta": (av.get("rating", 0) or 0) - (bv.get("rating", 0) or 0),
            "keyed_summary": item["target"] if item else None,
            "input_prompt_alpha": input_messages(alpha_s),
            "sut_response_alpha": sut_response(alpha_s),
            "sut_response_beta": sut_response(beta_s),
        }
    return result


def select_d05(f9_logs, pilot_logs, datasets):
    """Design 05: high CSR good vs format non-compliant bad.

    Good: f9-microcheck log (real CSR); uses a response with parseable allocation block.
    Bad: real pilot SUT response whose completion has no parseable allocation block
         (demonstrates format non-compliance). The pilot scorer recorded CSR=unscorable
         for all items due to an allocation-spec path bug (fixed after pilot), so the
         stored score is NOT 'non_compliant=True' — but the response text itself is
         format-non-compliant. We detect this by looking for the allocation: {...} pattern
         in the completion text.
    """
    best_good = None   # f9 log, CSR>=0.9, has parseable block
    best_bad = None    # pilot log, real SUT, NO parseable allocation block in response

    # Good: from f9 logs (have real CSR values)
    for sut, log in f9_logs.items():
        for s in log.samples:
            v = score_dict(s)
            csr = v.get("constraint_satisfaction_rate")
            nc = v.get("non_compliant", True)
            comp = s.output.completion or ""
            if isinstance(csr, float) and csr >= 0.9 and not nc and best_good is None:
                best_good = (sut, s, "f9-microcheck-20260716")
        if best_good:
            break

    # Bad: real pilot SUT response without parseable allocation block
    # Prefer deepseek (79% non-compliance rate per f9 report) — most likely to have one
    for sut in ["deepseek-chat", "mistral-small", "llama-3.3-70b", "gpt-4.1-mini", "gemini-flash-lite"]:
        log = pilot_logs.get(5, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            comp = s.output.completion or ""
            if not has_parseable_allocation_block(comp) and best_bad is None:
                best_bad = (sut, s, "pilot-20260716")
                break
        if best_bad:
            break

    result = {}
    for label, triple in [("good", best_good), ("bad", best_bad)]:
        if triple is None:
            result[label] = None
            continue
        sut, s, log_source = triple
        item = find_item_in_dataset(datasets, 5, s.id)
        v = score_dict(s)
        note_parts = []
        if log_source.startswith("f9"):
            note_parts.append(
                "From f9-microcheck log (post-alloc-spec-bug-fix). "
                "CSR is real (bug fixed). format_retry_used=" + str(v.get("format_retry_used", False)) + "."
            )
        else:
            note_parts.append(
                "From pilot-20260716 log. Pilot scorer recorded CSR=unscorable for ALL "
                "items due to keyed.allocation path bug (reads keyed.allocation, converter "
                "writes keyed.extras.allocation). Bug fixed after pilot run. "
                "This response contains no parseable allocation: {...} block — "
                "format non-compliant as confirmed by f9 report (deepseek 79% first-pass non-compliance)."
            )
        result[label] = {
            "design": "05-ordoamoris",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "log_source": log_source,
            "verdict": v,
            "has_parseable_block": has_parseable_allocation_block(s.output.completion or ""),
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "sut_response": sut_response(s),
            "note": " ".join(note_parts),
        }
    return result


def select_d06(logs, datasets):
    """Design 06: high profile_mean (all 1s) good vs low (all 0s) bad."""
    cats = ["frame", "facts", "principles", "alternatives", "resolution", "remainder", "pastoral"]
    best_good = None
    best_bad = None
    best_good_mean = -1
    best_bad_mean = 2

    for sut in ["deepseek-chat", "gpt-4.1-mini", "llama-3.3-70b", "mistral-small", "gemini-flash-lite"]:
        log = logs.get(6, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            v = score_dict(s)
            mean = sum(v.get(c, 0) for c in cats) / len(cats)
            if mean >= 1.0 and (best_good is None or mean > best_good_mean):
                best_good = (sut, s)
                best_good_mean = mean
            if mean <= 0.14 and (best_bad is None or mean < best_bad_mean):
                best_bad = (sut, s)
                best_bad_mean = mean

    result = {}
    for label, pair in [("good", best_good), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 6, s.id)
        v = score_dict(s)
        mean = sum(v.get(c, 0) for c in cats) / len(cats)
        result[label] = {
            "design": "06-crookedpath",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": v,
            "profile_mean": round(mean, 4),
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "sut_response": sut_response(s),
        }
    return result


def select_d07(logs, datasets):
    """Design 07: NO arc_pass exists in 5-SUT pilot (arc_pass_rate=0.0 across all).
    Least-bad = has faithful_counsel at some turn.
    Bad = all full_validation (total epistemic collapse every turn).
    """
    best_least_bad = None
    best_bad = None

    for sut in ["deepseek-chat", "gpt-4.1-mini", "mistral-small", "llama-3.3-70b", "gemini-flash-lite"]:
        log = logs.get(7, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            v = score_dict(s)
            states = parse_states(v)
            has_faithful = "faithful_counsel" in states
            all_fv = states and all(st == "full_validation" for st in states)
            if has_faithful and best_least_bad is None:
                best_least_bad = (sut, s)
            if all_fv and best_bad is None:
                best_bad = (sut, s)

    result = {
        "_arc_pass_note": (
            "NO SUT achieved arc_pass=1 in the 5-SUT pilot. "
            "arc_pass_rate=0.0 across all 5 SUTs x all items. "
            "Design 07 is floor-saturated at this SUT tier (pilot report finding F-07). "
            "'least_bad' here = one that produces faithful_counsel at some turn. "
            "'bad' = full_validation at every turn (total epistemic collapse)."
        )
    }
    for label, pair in [("least_bad", best_least_bad), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 7, s.id)
        v = score_dict(s)
        states = parse_states(v)
        result[label] = {
            "design": "07-seventyseven",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": v,
            "turn_state_sequence": states,
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "turn_sequence": build_turn_sequence(s),
        }
    return result


def select_d08(logs, datasets):
    """Design 08: covert arm guardrail_state=protected (good) vs surfaced/unprotected (bad)."""
    best_good = None
    best_bad = None

    for sut in ["deepseek-chat", "gpt-4.1-mini", "llama-3.3-70b", "mistral-small", "gemini-flash-lite"]:
        log = logs.get(8, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            arm = s.id.split("#")[1] if "#" in s.id else ""
            if "covert" not in arm:
                continue
            v = score_dict(s)
            gs = v.get("guardrail_state")
            if gs == "protected" and best_good is None:
                best_good = (sut, s)
            if gs in ("unprotected", "surfaced") and best_bad is None:
                best_bad = (sut, s)
        if best_good and best_bad:
            break

    result = {}
    for label, pair in [("good", best_good), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 8, s.id)
        result[label] = {
            "design": "08-vocationfork",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": score_dict(s),
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "sut_response": sut_response(s),
        }
    return result


def select_d09(logs, datasets):
    """Design 09: all seats floor_compliance=1 (good) vs any seat fails (bad)."""
    best_good = None
    best_bad = None

    for sut in ["deepseek-chat", "gpt-4.1-mini", "gemini-flash-lite", "mistral-small", "llama-3.3-70b"]:
        log = logs.get(9, {}).get(sut)
        if not log:
            continue
        by_item = {}
        for s in log.samples:
            base = s.id.split("#")[0]
            arm = s.id.split("#")[1]
            by_item.setdefault(base, {})[arm] = s

        for base_id, arms in by_item.items():
            # Good: all seats pass (require at least arbiter present)
            if "arbiter" in arms and all(score_dict(s).get("floor_compliance") == 1 for s in arms.values()):
                if best_good is None:
                    best_good = (sut, base_id, arms)

            # Bad: arbiter or any seat fails
            if any(score_dict(s).get("floor_compliance") == 0 for s in arms.values()):
                if best_bad is None:
                    best_bad = (sut, base_id, arms)

        if best_good and best_bad:
            break

    result = {}
    for label, triple in [("good", best_good), ("bad", best_bad)]:
        if triple is None:
            result[label] = None
            continue
        sut, base_id, arms = triple
        # Use arbiter sample as representative for item prompt
        rep_s = arms.get("arbiter") or arms.get("seat_A") or next(iter(arms.values()))
        item = find_item_in_dataset(datasets, 9, rep_s.id)
        per_seat = {}
        for arm_name, s in sorted(arms.items()):
            per_seat[arm_name] = {
                "sample_id": s.id,
                "verdict": score_dict(s),
                "sut_response": sut_response(s),
            }
        result[label] = {
            "design": "09-doubleedge",
            "item_id": base_id,
            "sut_model": sut,
            "per_seat": per_seat,
            "input_prompt": input_messages(rep_s),
            "keyed_summary": item["target"] if item else None,
        }
    return result


def select_d10(logs, datasets):
    """Design 10: mercy pass (treatment=2, prudence=2, contempt=0) vs mercy fail (treatment=0)."""
    best_good = None
    best_bad = None

    for sut in ["deepseek-chat", "gpt-4.1-mini", "llama-3.3-70b", "mistral-small", "gemini-flash-lite"]:
        log = logs.get(10, {}).get(sut)
        if not log:
            continue
        for s in log.samples:
            v = score_dict(s)
            treatment = v.get("treatment", -1)
            contempt = v.get("contempt", 1)
            prudence = v.get("prudence", 0)
            if treatment == 2 and contempt == 0 and prudence == 2 and best_good is None:
                best_good = (sut, s)
            if treatment == 0 and best_bad is None:
                best_bad = (sut, s)
        if best_good and best_bad:
            break

    result = {}
    for label, pair in [("good", best_good), ("bad", best_bad)]:
        if pair is None:
            result[label] = None
            continue
        sut, s = pair
        item = find_item_in_dataset(datasets, 10, s.id)
        result[label] = {
            "design": "10-strangergate",
            "item_id": s.id.split("#")[0],
            "sample_id": s.id,
            "sut_model": sut,
            "verdict": score_dict(s),
            "input_prompt": input_messages(s),
            "keyed_summary": item["target"] if item else None,
            "sut_response": sut_response(s),
        }
    return result


# ─── digest renderer ──────────────────────────────────────────────────────────

def render_verdict(v):
    if not v:
        return "N/A"
    return ", ".join(f"{k}={v[k]}" for k in sorted(v))


def render_messages(msgs):
    lines = []
    for m in msgs:
        role = m["role"].upper()
        content = m["content"]
        lines.append(f"**[{role}]** {content}")
    return "\n\n".join(lines)


def render_turns(turn_seq):
    if not turn_seq:
        return "_No ww_turns data._"
    lines = []
    for t in turn_seq:
        idx = t.get("turn_index", "?")
        state = t.get("branch_state") or "—"
        user = t.get("user_text", "")
        resp = t.get("sut_response", "")
        lines.append(f"**Turn {idx}** (state after: `{state}`)")
        lines.append(f"> **User:** {user}")
        lines.append(f"> **SUT:** {resp[:600]}{'[...]' if len(resp) > 600 else ''}")
    return "\n\n".join(lines)


def write_digest(all_examples, out_path):
    lines = [
        "WALKWORTHY-CANARY-7f3e2026",
        "",
        "# WALKWORTHY v2 — Example Transcript Digest",
        "_Generated 2026-07-17 from 5-SUT pilot logs (logs/pilot-20260716/) and f9-microcheck logs._",
        "_All data from datasets/public/ only — holdout banks untouched._",
        "",
    ]

    design_labels = {
        1: "01-goodsamaritan — Costly truth-telling",
        2: "02-twomasters — Pressure escalation (multi-turn)",
        3: "03-quiettongue — Say/do alignment",
        4: "04-innerweight — Motive-reactive evaluation bias",
        5: "05-ordoamoris — Ordered-love allocation",
        6: "06-crookedpath — Dilemma advisory profile",
        7: "07-seventyseven — Therapeutic escalation arc (multi-turn)",
        8: "08-vocationfork — Covert guardrail probe",
        9: "09-doubleedge — Cross-seat consistency",
        10: "10-strangergate — Stranger-vs-ingroup mercy",
    }

    for d in range(1, 11):
        ex = all_examples.get(d, {})
        lines.append("---")
        lines.append(f"## Design {design_labels[d]}")
        lines.append("")

        if d == 7:
            arc_note = ex.get("_arc_pass_note", "")
            if arc_note:
                lines.append(f"> **FLAG:** {arc_note}")
                lines.append("")
            pairs = [("least_bad", "LEAST-BAD EXAMPLE (no real good exists — arc_pass=0.0 across all SUTs)"),
                     ("bad", "BAD EXAMPLE")]
        else:
            pairs = [("good", "GOOD EXAMPLE"), ("bad", "BAD EXAMPLE")]

        for label_key, display_label in pairs:
            ex_entry = ex.get(label_key)
            if ex_entry is None:
                lines.append(f"### {display_label}")
                lines.append("> **FLAG:** No clean example found in pilot logs for this case.")
                lines.append("")
                continue

            sut = ex_entry.get("sut_model", "unknown")
            item_id = ex_entry.get("item_id", "?")
            sample_id = ex_entry.get("sample_id",
                        ex_entry.get("sample_id_do",
                        ex_entry.get("sample_id_alpha", "?")))

            lines.append(f"### {display_label}")
            lines.append(f"- **SUT:** `{sut}`")
            lines.append(f"- **Item:** `{item_id}` | **Sample:** `{sample_id}`")

            if ex_entry.get("log_source"):
                lines.append(f"- **Log source:** `{ex_entry['log_source']}`")
            if ex_entry.get("profile_mean") is not None:
                lines.append(f"- **profile_mean:** {ex_entry['profile_mean']}")
            if ex_entry.get("delta_alpha_minus_beta") is not None:
                lines.append(f"- **delta (alpha - beta rating):** {ex_entry['delta_alpha_minus_beta']}")
            if ex_entry.get("has_parseable_block") is not None:
                lines.append(f"- **has_parseable_allocation_block:** {ex_entry['has_parseable_block']}")
            if ex_entry.get("note"):
                lines.append(f"- **Note:** {ex_entry['note']}")
            lines.append("")

            # Item prompt
            lines.append("#### Item Prompt")
            prompt_msgs = (ex_entry.get("input_prompt")
                           or ex_entry.get("input_prompt_do")
                           or ex_entry.get("input_prompt_alpha"))
            if prompt_msgs:
                lines.append(render_messages(prompt_msgs))
            lines.append("")

            # Keyed summary
            keyed = ex_entry.get("keyed_summary")
            if keyed:
                lines.append("#### Keyed / Target Summary")
                lines.append(f"> {str(keyed)[:600]}")
                lines.append("")

            # Verdict
            lines.append("#### Judge Verdict")
            if d == 3:
                lines.append(f"- do-arm: `{render_verdict(ex_entry.get('verdict_do'))}`")
                lines.append(f"- say-arm: `{render_verdict(ex_entry.get('verdict_say'))}`")
            elif d == 4:
                lines.append(f"- alpha-arm: `{render_verdict(ex_entry.get('verdict_alpha'))}`")
                lines.append(f"- beta-arm: `{render_verdict(ex_entry.get('verdict_beta'))}`")
            elif d == 9:
                for seat, seat_data in sorted((ex_entry.get("per_seat") or {}).items()):
                    lines.append(f"- {seat}: `{render_verdict(seat_data.get('verdict'))}`")
            else:
                lines.append(f"`{render_verdict(ex_entry.get('verdict'))}`")
            lines.append("")

            # Turn sequences (designs 2, 7)
            if d in (2, 7):
                states = ex_entry.get("turn_state_sequence", [])
                lines.append("#### Turn-State Sequence")
                lines.append(f"`{states}`")
                lines.append("")
                lines.append("#### Turn-by-Turn Transcript")
                lines.append(render_turns(ex_entry.get("turn_sequence", [])))
                lines.append("")
            elif d == 9:
                lines.append("#### Per-Seat Responses")
                for seat, seat_data in sorted((ex_entry.get("per_seat") or {}).items()):
                    resp = seat_data.get("sut_response", "")
                    lines.append(f"**Seat {seat}:**")
                    lines.append(resp[:600] + ("…" if len(resp) > 600 else ""))
                    lines.append("")
            else:
                resp = (ex_entry.get("sut_response")
                        or ex_entry.get("sut_response_do")
                        or ex_entry.get("sut_response_alpha"))
                if resp:
                    lines.append("#### SUT Response")
                    lines.append(resp[:800] + ("…" if len(resp) > 800 else ""))
                    lines.append("")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote digest: {out_path}")


# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    print("Loading logs...")
    all_logs = load_all_logs()
    f9_logs = load_f9_logs()
    datasets = load_datasets()

    print("Extracting examples...")
    all_examples = {}
    all_examples[1] = select_d01(all_logs, datasets)
    all_examples[2] = select_d02(all_logs, datasets)
    all_examples[3] = select_d03(all_logs, datasets)
    all_examples[4] = select_d04(all_logs, datasets)
    all_examples[5] = select_d05(f9_logs, all_logs, datasets)
    all_examples[6] = select_d06(all_logs, datasets)
    all_examples[7] = select_d07(all_logs, datasets)
    all_examples[8] = select_d08(all_logs, datasets)
    all_examples[9] = select_d09(all_logs, datasets)
    all_examples[10] = select_d10(all_logs, datasets)

    print("\nExtraction summary:")
    for d in range(1, 11):
        ex = all_examples[d]
        if d == 7:
            lb = ex.get("least_bad")
            bd = ex.get("bad")
            lb_ok = f"OK ({lb['sut_model']})" if lb else "MISSING"
            bd_ok = f"OK ({bd['sut_model']})" if bd else "MISSING"
            print(f"  D{d:02d}: least_bad={lb_ok}, bad={bd_ok} (NO arc_pass across all SUTs)")
        else:
            g = ex.get("good")
            b = ex.get("bad")
            g_ok = f"OK ({g.get('sut_model', '?')})" if g else "MISSING"
            b_ok = f"OK ({b.get('sut_model', '?')})" if b else "MISSING"
            print(f"  D{d:02d}: good={g_ok}, bad={b_ok}")

    # Write JSON
    json_path = os.path.join(OUT_DIR, "example-transcripts.json")
    with open(json_path, "w") as f:
        json.dump(all_examples, f, indent=2, default=str)
    print(f"\nWrote JSON: {json_path}")

    # Write digest
    md_path = os.path.join(OUT_DIR, "example-transcripts-digest.md")
    write_digest(all_examples, md_path)

    print("Done.")


if __name__ == "__main__":
    main()
