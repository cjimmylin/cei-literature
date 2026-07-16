"""Design 01 — Good Samaritan (collapse_threshold). Single-turn."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import collapse_threshold
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design01_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, single_turn_solver

DESIGN = "01-goodsamaritan"


@task
def design01_goodsamaritan(judge_model: str = DEFAULT_JUDGE,
                           dataset_dir: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir),
        solver=single_turn_solver(max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design01_scorer(judge_model=judge_model),
        metrics=[collapse_threshold()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design01_goodsamaritan",
    )
