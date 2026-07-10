"""Safety + corpus-accounting guarantees for the public-split loader.

The HOLDOUT guard (charter §6.6) and the 356-item public-split total are both
load-bearing: a leak or a miscount corrupts every downstream claim.
"""
from pathlib import Path

import pytest

from walkworthy.loader import (
    HoldoutAccessError,
    load_design,
    load_public_split,
)


def test_public_split_totals_356(benchmark_root):
    items = load_public_split(benchmark_root, include_exemplars=True)
    seeds = [it for it in items if not it.is_exemplar]
    exemplars = [it for it in items if it.is_exemplar]
    assert len(seeds) == 315
    assert len(exemplars) == 41
    assert len(items) == 356


def test_holdout_guard_refuses_holdout_path():
    from walkworthy.loader import _guard_public
    holdout = Path("Christian-Ethics-Benchmark/HOLDOUT/01-goodsamaritan-holdout.md")
    with pytest.raises(HoldoutAccessError):
        _guard_public(holdout)


def test_loader_never_reads_holdout_dir(benchmark_root):
    # Even the full public load must not touch any file under HOLDOUT/.
    items = load_public_split(benchmark_root, include_exemplars=True)
    for it in items:
        assert "HOLDOUT" not in Path(it.source_file).parts


def test_runnable_accounting(benchmark_root):
    # 315 seeds are fully scripted; 12 spec exemplars (02/07/09 x4) are prose
    # sketches -> non-runnable. 356 total, 344 runnable.
    items = load_public_split(benchmark_root, include_exemplars=True)
    runnable = [it for it in items if it.runnable]
    nonrun = [it for it in items if not it.runnable]
    assert len(runnable) == 344
    assert {it.design for it in nonrun} == {
        "02-twomasters", "07-seventyseven", "09-doubleedge"
    }
    assert all(it.is_exemplar for it in nonrun)


def test_every_runnable_seed_has_key(benchmark_root):
    items = load_public_split(benchmark_root, include_exemplars=False)
    for it in items:
        assert it.key, f"{it.id}: empty key/rubric"
