"""WALKWORTHY suite — all 10 designs as one list of Inspect tasks.

Usage:
    inspect eval tasks/walkworthy_suite.py --model <model> -T judge_model=<judge>
    # or run all via eval_set from Python:
    python tasks/walkworthy_suite.py

`walkworthy_suite()` returns the list of 10 @task-decorated Task objects so
`inspect eval` discovers every design; `run_suite()` wraps eval_set for a scripted run.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inspect_ai import eval_set

from walkworthy_inspect.scorers import DEFAULT_JUDGE

from design01_goodsamaritan import design01_goodsamaritan
from design02_twomasters import design02_twomasters
from design03_quiettongue import design03_quiettongue
from design04_innerweight import design04_innerweight
from design05_ordoamoris import design05_ordoamoris
from design06_crookedpath import design06_crookedpath
from design07_seventyseven import design07_seventyseven
from design08_vocationfork import design08_vocationfork
from design09_doubleedge import design09_doubleedge
from design10_strangergate import design10_strangergate

_TASK_FNS = [
    design01_goodsamaritan, design02_twomasters, design03_quiettongue,
    design04_innerweight, design05_ordoamoris, design06_crookedpath,
    design07_seventyseven, design08_vocationfork, design09_doubleedge,
    design10_strangergate,
]


def walkworthy_suite(judge_model: str = DEFAULT_JUDGE, dataset_dir: str | None = None):
    """All 10 WALKWORTHY design tasks (for `inspect eval tasks/walkworthy_suite.py`)."""
    return [fn(judge_model=judge_model, dataset_dir=dataset_dir) for fn in _TASK_FNS]


def run_suite(model: str = "mockllm/model", judge_model: str = "mockllm/model",
              dataset_dir: str | None = None, log_dir: str = "logs/suite",
              limit: int | None = None):
    """Scripted eval_set over all 10 designs."""
    return eval_set(
        tasks=walkworthy_suite(judge_model=judge_model, dataset_dir=dataset_dir),
        model=model,
        log_dir=log_dir,
        limit=limit,
    )


if __name__ == "__main__":
    run_suite(dataset_dir="tools/fixtures", log_dir="logs/mock_suite")
