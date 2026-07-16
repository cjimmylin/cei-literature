"""Design 05 — OrdoAmoris (constraint_satisfaction_rate). Single-turn."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from walkworthy_inspect.datasets import load_design
from walkworthy_inspect.metrics import constraint_satisfaction_rate
from walkworthy_inspect.scorers import DEFAULT_JUDGE, design05_scorer
from walkworthy_inspect.solvers import DEFAULT_MAX_TOKENS, design05_format_retry_solver

DESIGN = "05-ordoamoris"


@task
def design05_ordoamoris(judge_model: str = DEFAULT_JUDGE,
                        dataset_dir: str | None = None,
                         item_ids: str | None = None) -> Task:
    return Task(
        dataset=load_design(DESIGN, dataset_dir=dataset_dir, item_ids=item_ids),
        # F9: v1-spirit one-retry format rule at the solver level (live _FORMAT_REMINDER
        # re-prompt when even offline recovery fails; store "ww_format_retry").
        solver=design05_format_retry_solver(max_tokens=DEFAULT_MAX_TOKENS),
        scorer=design05_scorer(judge_model=judge_model),
        metrics=[constraint_satisfaction_rate()],
        config=GenerateConfig(max_tokens=DEFAULT_MAX_TOKENS),
        name="walkworthy_design05_ordoamoris",
    )
