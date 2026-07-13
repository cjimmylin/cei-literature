"""Hermetic contract tests for the zero-paid T4 metadata preflight."""

from __future__ import annotations

import json
import os
import sys
from types import SimpleNamespace

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

import t4_preflight as t4  # noqa: E402
from wcfbench import load_items  # noqa: E402
from wcfbench.mvp import PricingError  # noqa: E402


def _bomb(*_args, **_kwargs):
    raise AssertionError("dry plan touched metadata, artifacts, or a paid client")


def _catalog_entry(slug, prompt="0.000001", completion="0.000002", **extra):
    entry = {
        "id": slug,
        "name": slug,
        "architecture": {
            "input_modalities": ["text"],
            "output_modalities": ["text"],
        },
        "pricing": {"prompt": prompt, "completion": completion},
    }
    entry.update(extra)
    return entry


def _arena(slug, rating):
    return {"model": slug, "slug": slug, "rating": rating, "exact_match": True}


def _token_profiles():
    names = (
        "base_sut", "base_judge", "variant_p3_sut", "variant_p3_judge",
        "variant_p4_sut", "variant_p4_judge", "variant_p6_sut",
        "variant_p6_judge", "g5b_judge", "g5c_sut", "g5c_judge",
    )
    return {name: {
        "prompt_tokens": 100 + index,
        "completion_tokens": 2048,
        "source": "rendered_prompt_fixed_completion_ceiling",
        "derivation": {
            "request_class": name,
            "prompt_method": "max_rendered_utf8_bytes",
            "prompt_scope": f"offline rendered prompts for {name}",
            "prompt_provenance": f"sha256:{index:064x}",
            "max_rendered_prompt_bytes": 100 + index,
            "completion_method": "fixed_max_tokens",
            "completion_provenance": "OpenRouterModelClient max_tokens=2048",
            "fixed_completion_cap": 2048,
        },
    } for index, name in enumerate(names, 1)}


def _source_registry(arena_rows):
    families = {}
    for row in arena_rows:
        family = t4._family_of_slug(row["slug"])
        if family not in set(t4.PRIMARY_FAMILIES) | set(t4.FALLBACK_FAMILIES):
            continue
        families.setdefault(family, {"complete": True, "candidates": []})["candidates"].append({
            "arena_name": row["model"], "openrouter_slug": row["slug"],
            "rating": row["rating"],
        })
    return {
        "source_url": "https://official.example/arena",
        "retrieved_at": "2026-07-13T12:00:00Z",
        "source_revision": "rev-1",
        "source_hash": "a" * 64,
        "families": families,
    }


def _integrated_inputs():
    roster_candidates = (
        "openai/o3", "deepseek/deepseek-chat", "qwen/qwen3-max",
        "moonshotai/kimi-k2", "meta-llama/llama-3.3-70b-instruct",
        "z-ai/glm-4.5", "mistralai/mistral-large-2512",
        "meta-llama/llama-3.1-8b-instruct", "cohere/command-a",
        "amazon/nova-pro-v1",
    )
    arena_rows = [_arena(slug, 1000 + index) for index, slug in enumerate(roster_candidates)]
    next(row for row in arena_rows
         if row["slug"] == "meta-llama/llama-3.3-70b-instruct")["rating"] = 2000
    source_rows = []
    for index, slug in enumerate(roster_candidates):
        for metric_index, metric in enumerate(t4.CAPABILITY_METRICS):
            source_rows.append({
                "model": slug, "metric": metric, "value": 10 * index + metric_index,
                "source_url": f"https://official.example/{metric}",
                "retrieved_at": "2026-07-13T12:00:00Z", "source_revision": "rev-1",
                "source_hash": f"hash-{metric}", "exact_match": True,
            })
    return {
        "arena_rows": arena_rows,
        "alias_rows": [],
        "roster_source_registry": _source_registry(arena_rows),
        "capability_source_rows": source_rows,
        "token_profiles": _token_profiles(),
        "retrieved_at": "2026-07-13T12:00:00Z",
    }


def test_default_mode_has_no_network_and_no_writes(capsys):
    code = t4.main([], metadata_fetch=_bomb, artifact_writer=_bomb)

    assert code == 0
    assert "DRY RUN" in capsys.readouterr().out


def test_openrouter_metadata_boundary_only_uses_authorized_get_endpoints():
    calls = []

    def opener(url, api_key):
        calls.append((url, api_key))
        if url == t4.AUTH_KEY_URL:
            return {"data": {"usage": 2, "limit": 10, "limit_remaining": 8}}
        if url == t4.MODELS_URL:
            return {"data": [_catalog_entry("openai/test-model")]}
        raise AssertionError(f"unauthorized endpoint: {url}")

    metadata = t4.fetch_openrouter_metadata(
        "runtime-secret", opener=opener, now=lambda: "2026-07-13T18:00:01Z")

    assert [url for url, _key in calls] == [t4.AUTH_KEY_URL, t4.MODELS_URL]
    assert metadata["key_snapshot"]["limit_remaining"] == 8.0
    assert set(metadata["catalog"]) == {"openai/test-model"}
    assert metadata["catalog_retrieved_at"] == "2026-07-13T18:00:01Z"
    assert "runtime-secret" not in json.dumps(metadata)
    assert "chat/completions" not in " ".join(url for url, _key in calls)


def test_metadata_cli_requires_inputs_json_and_freezes_all_five_payloads(
        tmp_path, monkeypatch):
    inputs_path = tmp_path / "inputs.json"
    inputs_path.write_text(json.dumps(_integrated_inputs()), encoding="utf-8")
    catalog_slugs = {row["slug"] for row in _integrated_inputs()["arena_rows"]} | set(
        t4.JUDGE_SLUGS)
    catalog = {slug: _catalog_entry(slug) for slug in catalog_slugs}
    captured = {}

    def writer(output_dir, payloads, *, forbidden_values):
        captured.update({"output_dir": str(output_dir), "payloads": payloads,
                         "forbidden_values": forbidden_values})
        return [os.path.join(str(output_dir), name) for name in payloads]

    monkeypatch.setenv("OPENROUTER_API_KEY", "runtime-secret")
    with pytest.raises(SystemExit):
        t4.main(["--metadata-preflight", "--output-dir", str(tmp_path / "missing")])

    code = t4.main(
        ["--metadata-preflight", "--output-dir", str(tmp_path / "frozen"),
         "--inputs-json", str(inputs_path)],
        metadata_fetch=lambda _key: {
            "key_snapshot": {"usage": 2.0, "limit": 10.0, "limit_remaining": 8.0},
            "catalog": catalog,
            "catalog_retrieved_at": "2026-07-13T18:00:01Z",
        },
        artifact_writer=writer,
    )

    assert code == 0
    assert set(captured["payloads"]) == t4.EXPECTED_ARTIFACTS
    assert captured["forbidden_values"] == ["runtime-secret"]
    manifest = captured["payloads"]["t4-run-manifest.json"]
    assert manifest["call_plan"]["totals"]["full"]["total"] == 16698
    assert len(manifest["five_cheapest_base_shard"]) == 5
    assert manifest["full_cost"]["total_usd"] > 0
    assert manifest["catalog_retrieved_at"] == "2026-07-13T18:00:01Z"
    assert captured["payloads"]["openrouter-catalog-snapshot.json"][
        "retrieved_at"] == "2026-07-13T18:00:01Z"


def test_r592_roster_resolves_primary_fallback_pins_dedup_and_anti_leak():
    slugs = {
        "openai/o3",
        "deepseek/deepseek-chat",  # formula/pin collision -> z-ai fallback
        "qwen/qwen3-max",
        "moonshotai/kimi-k2",
        "meta-llama/llama-3.3-70b-instruct",
        "z-ai/glm-4.5",
        "mistralai/mistral-large-2512",
        "meta-llama/llama-3.1-8b-instruct",
        "cohere/command-a",
        "amazon/nova-pro-v1",
        "google/gemini-ultra",  # anti-leak even though its rating is highest
    }
    catalog = {slug: _catalog_entry(slug) for slug in slugs}
    rows = [_arena(slug, index) for index, slug in enumerate(sorted(slugs), 100)]
    next(row for row in rows if row["slug"].startswith("google/"))["rating"] = 9999
    next(row for row in rows if row["slug"] == "deepseek/deepseek-chat")["rating"] = 1000
    next(row for row in rows if row["slug"] == "z-ai/glm-4.5")["rating"] = 500

    result = t4.resolve_roster(catalog, rows)

    assert len(result["roster"]) == 10
    assert len(set(result["roster"])) == 10
    assert "z-ai/glm-4.5" in result["roster"]
    assert "deepseek/deepseek-chat" in result["roster"]
    assert not ({"google", "x-ai", "anthropic"} &
                {slug.split("/", 1)[0] for slug in result["roster"]})
    assert any(row["reason"] == "pinned-collision-fallback" for row in result["trace"])
    assert "rating" in result["arena_ordering_disclosure"]

    traced = t4.resolve_roster(catalog, rows, source_registry=_source_registry(rows))
    deepseek = traced["family_resolution"]["deepseek"]
    assert deepseek["selected"]["selected_family"] == "z-ai"
    assert deepseek["higher_rated_excluded"][0]["reason"] == "pinned-collision"
    assert deepseek["higher_rated_excluded"][0]["provenance"]["source_hash"] == "a" * 64


def test_token_profiles_reject_shared_t3_or_unsupported_derivations():
    profiles = _token_profiles()
    t4.validate_token_profiles(profiles)

    shared = json.loads(json.dumps(profiles))
    shared["base_sut"]["source"] = "T3 immutable p95 shared usage"
    with pytest.raises(ValueError, match="unsupported token profile"):
        t4.validate_token_profiles(shared)

    unsupported = json.loads(json.dumps(profiles))
    unsupported["g5c_sut"]["derivation"]["request_class"] = "base_sut"
    with pytest.raises(ValueError, match="per-request-class"):
        t4.validate_token_profiles(unsupported)


def test_frozen_source_registry_preserves_all_rated_formula_exclusions():
    source_path = os.path.join(
        os.path.dirname(HARNESS), "20260713h-t4-preflight-source-inputs.json")
    with open(source_path, encoding="utf-8") as handle:
        source = json.load(handle)
    candidates = {
        row["arena_name"]: row
        for family in source["roster_source_registry"]["families"].values()
        for row in family["candidates"]
        if row.get("eligible") is False
    }

    assert set(candidates) == {
        "gpt-5.6-sol-xhigh", "gpt-5.5-high", "gpt-5.4-high",
        "gpt-5.2-chat-latest-20260210", "deepseek-v4-pro-thinking",
        "qwen3.7-max-preview", "qwen3.5-max-preview", "qwen3.6-max-preview",
    }
    assert all(row["rating"] > 0 and row["openrouter_slug"] is None
               and row["exclusion_reason"] for row in candidates.values())
    t4.validate_token_profiles(source["token_profiles"])


def test_r592_stops_when_fewer_than_eight_models_survive():
    catalog = {f"openai/m{i}": _catalog_entry(f"openai/m{i}") for i in range(7)}
    rows = [_arena(slug, index) for index, slug in enumerate(catalog)]

    with pytest.raises(t4.RosterResolutionError, match="fewer than 8"):
        t4.resolve_roster(catalog, rows)


def test_capability_normalization_is_exact_missing_safe_and_orients_pc1_to_arena():
    roster = [f"vendor/m{i}" for i in range(1, 7)]
    source_rows = []
    for i, slug in enumerate(roster, 1):
        values = {
            "lmarena_text": 1000 + i * 10,
            "mmlu_pro": 50 + i,
            "gpqa_diamond": 40 + i,
            "livebench_global": 30 + i,
        }
        if slug == "vendor/m5":
            values.pop("gpqa_diamond")
        if slug == "vendor/m6":
            values = {"lmarena_text": values["lmarena_text"]}
        for metric, value in values.items():
            source_rows.append({
                "model": slug,
                "metric": metric,
                "value": value,
                "source_url": f"https://official.example/{metric}",
                "retrieved_at": "2026-07-13T12:00:00Z",
                "source_revision": "rev-1",
                "source_hash": f"hash-{metric}",
                "exact_match": True,
            })
    # Ambiguous duplicates are missing, never averaged or borrowed.
    source_rows.extend([
        {**source_rows[0], "value": 99},
        {**source_rows[0], "value": 100},
    ])

    normalized = t4.normalize_capabilities(roster, source_rows)
    computed = t4.compute_pc1(normalized)
    by_model = {row["model"]: row for row in computed["rows"]}

    assert by_model["vendor/m1"]["lmarena_text"] is None
    assert by_model["vendor/m5"]["gpqa_diamond"] is None
    assert by_model["vendor/m5"]["included"] is True
    assert by_model["vendor/m6"]["included"] is False
    included = [row for row in computed["rows"] if row["included"]]
    assert max(included, key=lambda row: row["lmarena_text"] or -1)["pc1"] > min(
        included, key=lambda row: row["lmarena_text"] or 10**9)["pc1"]
    assert computed["frontier"] == [
        row["model"] for row in sorted(included, key=lambda row: (-row["pc1"], row["model"]))[:5]
    ]
    assert computed["standardized_column_std"] == pytest.approx([1.0, 1.0, 1.0, 1.0])


def test_g5c_sampling_is_design_stratified_deterministic_and_disjoint():
    items = [
        SimpleNamespace(
            id=f"ITEM-{i:03d}",
            design=f"design-{i % 10}",
            extra={},
            kind="open" if i % 3 else "anchor",
        )
        for i in range(180)
    ]

    first = t4.select_g5c_samples(items)
    second = t4.select_g5c_samples(list(reversed(items)))

    assert len(first["priming_ids"]) == 23
    assert len(first["evaluation_ids"]) == 100
    assert set(first["priming_ids"]).isdisjoint(first["evaluation_ids"])
    assert first == second
    assert set(first["priming_allocation"]) == {f"design-{i}" for i in range(10)}


def test_frozen_bank_call_plan_and_ladder_counts_are_exact():
    bank = os.path.join(os.path.dirname(HARNESS), "05-BANK-YAML")
    items = load_items(bank)
    roster = [f"vendor/model-{i}" for i in range(10)]
    g5c = t4.select_g5c_samples(items)

    plan = t4.build_call_plan(items, roster, roster[:5], g5c)

    assert plan["totals"]["base"] == {"sut": 2260, "judge": 6960, "total": 9220}
    assert plan["totals"]["variants"] == {"sut": 1480, "judge": 4510, "total": 5990}
    assert plan["totals"]["g5b"] == {"sut": 0, "judge": 620, "total": 620}
    assert plan["totals"]["g5c"] == {"sut": 200, "judge": 668, "total": 868}
    assert plan["totals"]["full"] == {"sut": 3940, "judge": 12758, "total": 16698}
    assert sum(row["count"] for row in plan["classes"]) == 16698
    assert plan["totals"]["full"]["total"] == sum(
        plan["totals"][phase]["total"] for phase in ("base", "variants", "g5b", "g5c"))
    catalog = {
        slug: _catalog_entry(slug) for slug in set(roster) | set(t4.JUDGE_SLUGS)
    }
    branches = t4.forecast_branches(
        plan, catalog=catalog, token_profiles=_token_profiles(),
        key_snapshot={"limit_remaining": 0.25})
    assert [row["branch"] for row in branches] == [
        "full", "drop_p6", "drop_p3", "drop_p4", "halve_episode_roster"]
    assert [row["logical_calls"] for row in branches] == [16698, 16253, 13333, 10708, 10378]
    assert all(row["forecast_cost_usd"] > 0 for row in branches)
    assert all(row["runtime"]["baseline_minutes"] > 0 for row in branches)
    assert all(row["minimum_ratifiable_cap_usd"] >= row["forecast_cost_usd"]
               for row in branches)
    assert all(row["required_top_up_usd"] >= 0 for row in branches)
    assert branches[-1]["prescribed_call_saving"] == 330
    assert branches[-1]["requires_jimmy_ruling"] is True

    plan8 = t4.build_call_plan(items, roster[:8], roster[:5], g5c)
    assert plan8["totals"]["base"] == {"sut": 1808, "judge": 5568, "total": 7376}
    assert plan8["totals"]["full"]["total"] == 14854


def test_pricing_fails_loud_and_cap_topup_arithmetic_is_exact():
    classes = [
        {"phase": "base", "role": "sut", "model": "vendor/a",
         "request_class": "base_sut", "count": 2},
        {"phase": "base", "role": "judge", "model": "judge/b",
         "request_class": "base_judge", "count": 3},
    ]
    catalog = {
        "vendor/a": _catalog_entry("vendor/a", prompt="0.001", completion="0.002"),
        "judge/b": _catalog_entry("judge/b", prompt="0.003", completion="0.004"),
    }
    profiles = {
        "base_sut": {"prompt_tokens": 10, "completion_tokens": 5, "source": "p95"},
        "base_judge": {"prompt_tokens": 4, "completion_tokens": 6, "source": "p95"},
    }

    cost = t4.estimate_cost(classes, catalog, profiles)

    assert cost["total_usd"] == pytest.approx(0.148)
    assert t4.minimum_ratifiable_cap(cost["total_usd"]) == 0.19
    assert t4.required_top_up(0.19, 0.10) == 0.09
    with pytest.raises(PricingError):
        t4.estimate_cost(classes, {"vendor/a": catalog["vendor/a"]}, profiles)


def test_five_cheapest_base_shard_orders_by_forecast_then_slug():
    roster = ["vendor/z", "vendor/a", "vendor/c", "vendor/b", "vendor/e", "vendor/d"]
    catalog = {
        slug: _catalog_entry(slug, prompt=str(price), completion=str(price * 2))
        for slug, price in zip(roster, (6e-6, 1e-6, 3e-6, 2e-6, 5e-6, 4e-6))
    }
    profile = {"prompt_tokens": 100, "completion_tokens": 50, "source": "p95"}

    shard = t4.select_cheapest_base_shard(roster, catalog, profile, n=5)

    assert [row["model"] for row in shard] == [
        "vendor/a", "vendor/b", "vendor/c", "vendor/d", "vendor/e"]


def test_runtime_uses_immutable_t3_throughput_and_planning_band():
    forecast = t4.forecast_runtime(264)

    assert forecast["calls_per_minute"] == pytest.approx(6.486486486486487)
    assert forecast["baseline_minutes"] == pytest.approx(40.7)
    assert forecast["planning_band_minutes"] == pytest.approx([32.56, 54.2666666667])


def test_artifacts_are_exclusive_canaried_and_secret_free(tmp_path):
    output = tmp_path / "20260713-t4-preflight-test"
    payloads = {
        "capability-battery.csv": [{"model": "vendor/a", "pc1": 1.2}],
        "openrouter-catalog-snapshot.json": {"models": [{"id": "vendor/a"}]},
        "t4-run-manifest.json": {"roster": ["vendor/a"]},
        "t4-cost-plan.csv": [{"model": "vendor/a", "subtotal_usd": 0.1}],
        "t4-preflight-report.md": "# T4 preflight\n",
    }

    with pytest.raises(t4.SecretDisclosureError):
        t4.write_new_artifacts(
            output, {**payloads, "t4-preflight-report.md": "runtime-secret"},
            forbidden_values=["runtime-secret"])
    assert not output.exists()

    paths = t4.write_new_artifacts(output, payloads, forbidden_values=["runtime-secret"])

    assert set(os.path.basename(path) for path in paths) == set(payloads)
    assert all(t4.CANARY in open(path, encoding="utf-8").read() for path in paths)
    assert all("runtime-secret" not in open(path, encoding="utf-8").read() for path in paths)
    with pytest.raises(FileExistsError):
        t4.write_new_artifacts(output, payloads)
