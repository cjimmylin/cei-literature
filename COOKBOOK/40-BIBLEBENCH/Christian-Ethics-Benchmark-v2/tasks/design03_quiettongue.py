"""Design 03 — QuietTongue (say_do_gap). Single-turn."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import say_do_gap
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design03_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, single_turn_solver

DESIGN = "03-quiettongue"


@task
def design03_quiettongue(judge_model: str = DEFAULT_JUDGE,
                         dataset_dir: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir),
        solver=single_turn_solver(max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design03_scorer(judge_model=judge_model),
        metrics=[say_do_gap()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design03_quiettongue",
    )
