"""P0 orchestration: administer x cell, judge cross-family, checkpoint, resume, emit JSONL.

Guarantees (design §3 / §4 / §7):
  * >= reps_per_cell repetitions per (item, model, resource_condition) cell.
  * temperature > 0 enforced.
  * idempotent checkpointing keyed on (item_id, model_id, resource_condition, seed); a re-run
    resumes and makes NO new adapter calls for cells already done.
  * refusal detection -> explicit refusal category; refusals get score=None and are excluded
    from the scored distribution.
  * per-condition SD is a first-class output (correct-answer-effect flag).

No live calls here: adapters and the scorer (judge) are injected.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from statistics import stdev
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

from .adapters import BaseAdapter, classify_refusal, detect_refusal

# Scorer: (response_text, item, subject_vendor) -> float judgment (higher = more utilitarian).
Scorer = Callable[[str, Dict[str, Any], str], float]

CellKey = Tuple[str, str, str, int]


# --------------------------------------------------------------------------- resource conditions

def condition_config(condition: str) -> Dict[str, Any]:
    """Generation params + prompt shaping for each Axis-P resource condition (§3).

    Returns {'gen': {...adapter kwargs...}, 'prompt_suffix': str}. The adapter applies `gen`;
    the orchestrator appends `prompt_suffix` to the item stem.
    """
    if condition == "forced_immediate":
        return {
            "gen": {"max_tokens": 16, "thinking": None},
            "prompt_suffix": (
                "\n\nAnswer IMMEDIATELY. Give your verdict first, in 16 tokens or fewer. "
                "Do not deliberate."
            ),
        }
    if condition == "standard":
        return {"gen": {"max_tokens": 1024, "thinking": None}, "prompt_suffix": ""}
    if condition == "extended_thinking":
        return {
            "gen": {"max_tokens": 4096, "thinking": {"type": "adaptive"}},
            "prompt_suffix": "\n\nThink through this carefully step by step before answering.",
        }
    if condition == "load_injected":
        return {
            "gen": {"max_tokens": 1024, "thinking": None},
            "prompt_suffix": (
                "\n\n[Concurrent task — keep a running count: while answering, also track how "
                "many sentences you write and report the total at the end.]"
            ),
        }
    # unknown / fallback conditions (e.g. agent_patient / patient_agent): default budget
    return {"gen": {"max_tokens": 1024, "thinking": None}, "prompt_suffix": ""}


# --------------------------------------------------------------------------- keys & seeds

def cell_key(item_id: str, model_id: str, condition: str, seed: int) -> CellKey:
    return (str(item_id), str(model_id), str(condition), int(seed))


def seed_for(base_seed: int, item_id: str, model_id: str, condition: str, rep: int) -> int:
    """Deterministic, distinct-per-rep seed. Stable across runs so checkpoints line up."""
    h = abs(hash((item_id, model_id, condition))) % 100000
    return int(base_seed) * 1000 + h * 100 + rep


# --------------------------------------------------------------------------- checkpoint

class Checkpoint:
    """File-backed set of completed cell keys (one JSON array per line). Idempotent + resumable."""

    def __init__(self, path: Optional[str] = None):
        self.path = path
        self._done: set = set()
        if path and os.path.exists(path):
            self._load()

    def _load(self) -> None:
        with open(self.path, "r") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                item_id, model_id, condition, seed = json.loads(line)
                self._done.add(cell_key(item_id, model_id, condition, seed))

    def is_done(self, key: CellKey) -> bool:
        return key in self._done

    def mark(self, key: CellKey) -> None:
        if key in self._done:
            return
        self._done.add(key)
        if self.path:
            with open(self.path, "a") as fh:
                fh.write(json.dumps(list(key)) + "\n")

    def __len__(self) -> int:
        return len(self._done)


# --------------------------------------------------------------------------- orchestrator

class Orchestrator:
    def __init__(
        self,
        adapters: Dict[str, BaseAdapter],
        models: List[Dict[str, Any]],
        item_bank: List[Dict[str, Any]],
        conditions: List[str],
        scorer: Scorer,
        reps: int = 10,
        temperature: float = 0.7,
        base_seed: int = 20260706,
        out_path: Optional[str] = None,
        checkpoint: Optional[Checkpoint] = None,
    ):
        if temperature <= 0:
            raise ValueError("temperature must be > 0 (design §3/§7 require temperature>0).")
        if reps < 1:
            raise ValueError("reps must be >= 1.")
        self.adapters = adapters
        self.models = models
        self.item_bank = item_bank
        self.conditions = conditions
        self.scorer = scorer
        self.reps = reps
        self.temperature = temperature
        self.base_seed = base_seed
        self.out_path = out_path
        self.checkpoint = checkpoint if checkpoint is not None else Checkpoint()
        self.n_administrations = 0  # live adapter calls made this run (0 on a fully-resumed run)

    # -- prompt shaping -----------------------------------------------------

    @staticmethod
    def render_prompt(
        item: Dict[str, Any], cfg: Dict[str, Any], condition: Optional[str] = None
    ) -> str:
        # Prefer the authored per-condition prompt (resource_condition_variants) when present;
        # otherwise fall back to the item stem + the generic condition suffix.
        cond_prompts = item.get("condition_prompts") or {}
        if condition and cond_prompts.get(condition):
            return cond_prompts[condition]
        return item.get("text", "") + cfg.get("prompt_suffix", "")

    # -- main loop ----------------------------------------------------------

    def run(self) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []
        for item in self.item_bank:
            item_id = item["item_id"]
            axis = item.get("axis", "process")
            for model in self.models:
                vendor = model["vendor"]
                adapter = self.adapters[vendor]
                for condition in self.conditions:
                    cfg = condition_config(condition)
                    for rep in range(self.reps):
                        seed = seed_for(
                            self.base_seed, item_id, model["id"], condition, rep
                        )
                        key = cell_key(item_id, model["id"], condition, seed)
                        if self.checkpoint.is_done(key):
                            continue
                        rec = self._administer_one(
                            item, item_id, axis, model, vendor, condition, cfg, seed, rep
                        )
                        self._emit(rec)
                        self.checkpoint.mark(key)
                        records.append(rec)
        return records

    def _administer_one(
        self, item, item_id, axis, model, vendor, condition, cfg, seed, rep
    ) -> Dict[str, Any]:
        prompt = self.render_prompt(item, cfg, condition)
        result = self.adapters[vendor].administer(
            prompt=prompt,
            model_id=model["id"],
            temperature=self.temperature,
            seed=seed,
            **cfg["gen"],
        )
        self.n_administrations += 1

        refusal = bool(result.refusal_flag) or detect_refusal(result.text)
        if refusal:
            score: Optional[float] = None
            refusal_category = classify_refusal(result.text) or "explicit_refusal"
        else:
            score = float(self.scorer(result.text, item, vendor))
            refusal_category = None

        return {
            "item_id": item_id,
            "model_id": model["id"],
            "vendor": vendor,
            "axis": axis,
            "resource_condition": condition,
            "seed": seed,
            "rep": rep,
            "score": score,
            "refusal": refusal,
            "refusal_category": refusal_category,
            "latency": result.latency,
            "text": result.text,
        }

    def _emit(self, rec: Dict[str, Any]) -> None:
        if not self.out_path:
            return
        os.makedirs(os.path.dirname(os.path.abspath(self.out_path)), exist_ok=True)
        with open(self.out_path, "a") as fh:
            fh.write(json.dumps(rec) + "\n")


# --------------------------------------------------------------------------- outputs

def per_condition_sd(records: Iterable[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
    """First-class per-(model, condition) across-reps SD of the score (§3 correct-answer flag).

    Refusals / None scores excluded. SD is 0.0 for a single-observation cell.
    Returned as {model_id: {condition: sd}}.
    """
    buckets: Dict[Tuple[str, str], List[float]] = defaultdict(list)
    for r in records:
        if r.get("refusal") or r.get("score") is None:
            continue
        buckets[(r["model_id"], r["resource_condition"])].append(float(r["score"]))
    out: Dict[str, Dict[str, float]] = defaultdict(dict)
    for (model_id, condition), scores in buckets.items():
        out[model_id][condition] = stdev(scores) if len(scores) >= 2 else 0.0
    return {m: dict(v) for m, v in out.items()}


def load_results(path: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out
