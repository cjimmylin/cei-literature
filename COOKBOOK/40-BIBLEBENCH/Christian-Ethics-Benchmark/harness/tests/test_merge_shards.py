import json

import pytest

from walkworthy.merge_shards import merge_reexecution_shards


def _write(path, records):
    path.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def _record(item_id, model, design="02-twomasters", marker=None):
    record = {"item_id": item_id, "model": model, "design": design}
    if marker is not None:
        record["marker"] = marker
    return record


def test_merge_requires_exact_expected_surface_and_appends_resumably(tmp_path):
    canonical = tmp_path / "canonical.jsonl"
    shard = tmp_path / "shard.jsonl"
    expected = tmp_path / "expected.jsonl"
    first = _record("WW-02-A", "model/a")
    second = _record("WW-07-B", "model/b", design="07-seventyseven")
    ignored = _record("WW-01-C", "model/c", design="01-goodsamaritan")
    _write(canonical, [first])
    _write(shard, [second])
    _write(expected, [first, second, ignored])

    dry = merge_reexecution_shards(
        canonical, [shard], expected,
        designs={"02-twomasters", "07-seventyseven"}, append=False)
    assert dry == {"expected_keys": 2, "canonical_keys": 1,
                   "prospective_keys": 2, "appended": 0, "complete": True}
    assert canonical.read_text(encoding="utf-8").count("\n") == 1

    merged = merge_reexecution_shards(
        canonical, [shard], expected,
        designs={"02-twomasters", "07-seventyseven"}, append=True)
    assert merged["appended"] == 1
    assert merged["prospective_keys"] == 2

    resumed = merge_reexecution_shards(
        canonical, [shard], expected,
        designs={"02-twomasters", "07-seventyseven"}, append=True)
    assert resumed["appended"] == 0
    assert canonical.read_text(encoding="utf-8").count("\n") == 2


def test_merge_rejects_incomplete_unexpected_and_conflicting_surfaces(tmp_path):
    canonical = tmp_path / "canonical.jsonl"
    shard = tmp_path / "shard.jsonl"
    expected = tmp_path / "expected.jsonl"
    first = _record("WW-02-A", "model/a")
    second = _record("WW-07-B", "model/b", design="07-seventyseven")
    _write(canonical, [first])
    _write(expected, [first, second])

    _write(shard, [])
    with pytest.raises(ValueError, match="coverage mismatch: missing=1 extra=0"):
        merge_reexecution_shards(
            canonical, [shard], expected,
            designs={"02-twomasters", "07-seventyseven"})

    _write(shard, [second, _record("WW-02-X", "model/x")])
    with pytest.raises(ValueError, match="coverage mismatch: missing=0 extra=1"):
        merge_reexecution_shards(
            canonical, [shard], expected,
            designs={"02-twomasters", "07-seventyseven"})

    _write(shard, [_record("WW-02-A", "model/a", marker="different"), second])
    with pytest.raises(ValueError, match="conflicting duplicate key"):
        merge_reexecution_shards(
            canonical, [shard], expected,
            designs={"02-twomasters", "07-seventyseven"})


def test_merge_rejects_duplicate_key_within_one_input(tmp_path):
    canonical = tmp_path / "canonical.jsonl"
    shard = tmp_path / "shard.jsonl"
    expected = tmp_path / "expected.jsonl"
    record = _record("WW-02-A", "model/a")
    _write(canonical, [])
    _write(shard, [record, record])
    _write(expected, [record])

    with pytest.raises(ValueError, match="duplicate key within"):
        merge_reexecution_shards(
            canonical, [shard], expected, designs={"02-twomasters"})
