"""Design 04 — InnerWeight (motive_sensitivity_index). Single-turn."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import motive_sensitivity_index
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design04_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, single_turn_solver

DESIGN = "04-innerweight"


@task
def design04_innerweight(judge_model: str = DEFAULT_JUDGE,
                         dataset_dir: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir),
        solver=single_turn_solver(max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design04_scorer(judge_model=judge_model),
        metrics=[motive_sensitivity_index()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design04_innerweight",
    )
