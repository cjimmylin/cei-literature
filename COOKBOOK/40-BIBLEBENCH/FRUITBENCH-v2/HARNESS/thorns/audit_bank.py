#!/usr/bin/env python3
"""THORNS bank auditor — quota checks, registry-tag lint, schema + contamination checks.

Build-guide §4 deliverable. Runs WITHOUT model credentials (static analysis of the bank).
Usage:  python audit_bank.py [--items-dir <dir>]
Exit 0 if all HARD checks pass; nonzero otherwise. SOFT findings are printed, not fatal.
"""
from __future__ import annotations
import argparse, sys, re, json
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: install it with the active environment's `python -m pip install pyyaml`")

HERE = Path(__file__).resolve().parent
DEFAULT_CONFIG = HERE / "audit_config.json"


def load_audit_config(path: str | Path = DEFAULT_CONFIG) -> dict:
    """Load a design audit policy and resolve its paths relative to the policy file."""
    config_path = Path(path).resolve()
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    required_top = {
        "design", "paths", "registry_patterns", "registry_literals",
        "required_fields", "required_fruit_codes", "allowed_formats", "lexical_flags",
        "quotas", "reuse_tags",
    }
    missing_top = sorted(required_top - set(cfg))
    if missing_top:
        raise ValueError(f"audit config missing required field(s) {missing_top}: {config_path}")
    if not str(cfg["design"]).strip():
        raise ValueError(f"audit config design must be non-empty: {config_path}")
    canary_modes = [name for name in ("canary", "canary_policy") if name in cfg]
    if len(canary_modes) != 1:
        raise ValueError(
            "audit config must define exactly one of canary or canary_policy: "
            f"{config_path}"
        )
    if "canary" in cfg:
        if not isinstance(cfg["canary"], str) or not cfg["canary"].strip():
            raise ValueError(f"audit config canary must be a non-empty string: {config_path}")
    else:
        policy = cfg["canary_policy"]
        if not isinstance(policy, dict):
            raise ValueError(f"audit config canary_policy must be an object: {config_path}")
        required_canary = {"pattern", "require_unique", "forbidden_tokens"}
        missing_canary = sorted(required_canary - set(policy))
        if missing_canary:
            raise ValueError(
                f"audit config canary_policy missing {missing_canary}: {config_path}"
            )
        try:
            re.compile(policy["pattern"])
        except (TypeError, re.error) as exc:
            raise ValueError(f"audit config canary_policy.pattern is invalid: {exc}") from exc
        if policy["require_unique"] is not True:
            raise ValueError(
                "audit config canary_policy.require_unique must be true for live-valid banks"
            )
        forbidden = policy["forbidden_tokens"]
        if (
            not isinstance(forbidden, list)
            or not forbidden
            or any(not isinstance(token, str) or not token.strip() for token in forbidden)
        ):
            raise ValueError(
                "audit config canary_policy.forbidden_tokens must be a non-empty string list"
            )
    pattern_keys = {"fruit", "vice", "claim"}
    missing_patterns = sorted(pattern_keys - set(cfg["registry_patterns"]))
    if missing_patterns:
        raise ValueError(
            f"audit config registry_patterns missing {missing_patterns}: {config_path}"
        )
    for name, pattern in cfg["registry_patterns"].items():
        try:
            re.compile(pattern)
        except (TypeError, re.error) as exc:
            raise ValueError(
                f"audit config registry_patterns.{name} is invalid: {exc}"
            ) from exc
    quota_keys = {
        "fruit_floor", "p_claim_floors", "social_factional",
        "required_tiers_per_fruit", "cft_live_per_fruit_min",
        "contested_fraction_max",
    }
    missing_quotas = sorted(quota_keys - set(cfg["quotas"]))
    if missing_quotas:
        raise ValueError(f"audit config quotas missing {missing_quotas}: {config_path}")
    social_keys = {"enabled", "codes", "floor"}
    missing_social = sorted(social_keys - set(cfg["quotas"]["social_factional"]))
    if missing_social:
        raise ValueError(
            f"audit config quotas.social_factional missing {missing_social}: {config_path}"
        )
    reuse_keys = {"all", "by_format"}
    missing_reuse = sorted(reuse_keys - set(cfg["reuse_tags"]))
    if missing_reuse:
        raise ValueError(f"audit config reuse_tags missing {missing_reuse}: {config_path}")
    if not cfg["allowed_formats"]:
        raise ValueError(f"audit config allowed_formats must be non-empty: {config_path}")
    fraction_fields = {
        "fruit_floor": cfg["quotas"]["fruit_floor"],
        "social_factional.floor": cfg["quotas"]["social_factional"]["floor"],
        "contested_fraction_max": cfg["quotas"]["contested_fraction_max"],
        **{
            f"p_claim_floors.{name}": value
            for name, value in cfg["quotas"]["p_claim_floors"].items()
        },
    }
    for name, value in fraction_fields.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise ValueError(f"audit config quotas.{name} must be numeric in [0,1]")
    cft_min = cfg["quotas"]["cft_live_per_fruit_min"]
    if isinstance(cft_min, bool) or not isinstance(cft_min, int) or cft_min < 0:
        raise ValueError(
            "audit config quotas.cft_live_per_fruit_min must be a nonnegative integer"
        )
    base = config_path.parent
    paths = {}
    for key, value in (cfg.get("paths") or {}).items():
        p = Path(value)
        paths[key] = str((base / p).resolve() if not p.is_absolute() else p.resolve())
    cfg["paths"] = paths
    for key in ("items", "registry"):
        if not paths.get(key):
            raise ValueError(f"audit config missing paths.{key}: {config_path}")
    return cfg


def headline_items(banks: dict) -> dict:
    """Return the locked headline stratum without deleting exploratory provenance rows."""
    return {
        item_id: item
        for item_id, item in banks.items()
        if isinstance(item, dict) and item.get("status") != "exploratory"
    }


def cft_ids(cft: dict | None) -> tuple[str, ...]:
    """Read a CFT path while preserving backward compatibility with scalar cft_id."""
    if not cft:
        return ()
    if "cft_ids" in cft:
        values = cft["cft_ids"]
        if not isinstance(values, list) or not values:
            raise ValueError("cft_ids must be a non-empty list")
        if any(not isinstance(value, str) or not value.strip() for value in values):
            raise ValueError("cft_ids entries must be non-empty strings")
        if len(values) != len(set(values)):
            raise ValueError("cft_ids must not contain duplicates")
        return tuple(values)
    value = cft.get("cft_id")
    if value is None:
        return ()
    if not isinstance(value, str) or not value.strip():
        raise ValueError("cft_id must be a non-empty string")
    return (value,)


def _model_visible_text(bank: dict) -> str:
    prompt_text = str(bank.get("prompt") or "")
    for turn in bank.get("turns") or []:
        prompt_text += " " + json.dumps(turn, default=str)
    return prompt_text


def audit_canaries(banks: dict, golds: dict, policy: dict) -> list[str]:
    """Validate per-item canary opacity, uniqueness, visibility, and gold isolation."""
    failures: list[str] = []
    exact = policy.get("exact")
    pattern = policy.get("pattern")
    require_unique = bool(policy.get("require_unique"))
    forbidden = tuple(str(token).casefold() for token in policy.get("forbidden_tokens", []))
    observed: dict[str, list[str]] = {}

    for item_id, bank in banks.items():
        if not isinstance(bank, dict):
            continue
        canary = bank.get("canary")
        if not isinstance(canary, str) or not canary:
            failures.append(f"{item_id}: canary metadata must be a non-empty string")
            continue
        observed.setdefault(canary, []).append(item_id)
        if exact is not None and canary != exact:
            failures.append(f"{item_id}: canary metadata does not equal the configured canary")
        if pattern is not None and re.fullmatch(pattern, canary) is None:
            failures.append(f"{item_id}: canary {canary!r} does not match configured pattern")
        low_canary = canary.casefold()
        hits = sorted(token for token in forbidden if token in low_canary)
        if hits:
            failures.append(f"{item_id}: canary contains forbidden token(s) {hits}")
        if canary not in _model_visible_text(bank):
            failures.append(f"{item_id}: canary absent from prompt/turn text")

    if require_unique:
        for canary, item_ids in sorted(observed.items()):
            if len(item_ids) > 1:
                failures.append(
                    f"duplicate canary {canary!r} is shared by items {sorted(item_ids)}"
                )

    all_canaries = tuple(observed)
    for item_id, bank in banks.items():
        if not isinstance(bank, dict):
            continue
        visible = _model_visible_text(bank)
        own = bank.get("canary")
        foreign = sorted(
            canary for canary in all_canaries if canary != own and canary in visible
        )
        if foreign:
            failures.append(f"{item_id}: prompt/turn text contains foreign canary {foreign}")

    for gold_id, gold in golds.items():
        gold_text = json.dumps(gold, default=str)
        leaked = sorted(canary for canary in all_canaries if canary in gold_text)
        if leaked:
            failures.append(f"{gold_id}: canary leaked into gold {leaked}")
    return failures


def load_registry_codes(cfg: dict):
    txt = Path(cfg["paths"]["registry"]).read_text(encoding="utf-8")
    patterns = cfg["registry_patterns"]
    fcodes = set(re.findall(patterns["fruit"], txt))
    wcodes = set(re.findall(patterns["vice"], txt))
    pcodes = set(re.findall(patterns["claim"], txt))
    literals = cfg["registry_literals"]
    fcodes.update(literals.get("fruit", []))
    wcodes.update(literals.get("vice", []))
    pcodes.update(literals.get("claim", []))
    return fcodes, wcodes, pcodes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(DEFAULT_CONFIG))
    ap.add_argument("--items-dir", help="optional explicit override of config paths.items")
    args = ap.parse_args()
    cfg = load_audit_config(args.config)
    items = Path(args.items_dir).resolve() if args.items_dir else Path(cfg["paths"]["items"])
    bank_dir, gold_dir = items / "bank", items / "gold"
    canary_policy = cfg.get("canary_policy") or {
        "exact": cfg["canary"],
        "require_unique": False,
        "forbidden_tokens": [],
    }
    lexical_flags = cfg["lexical_flags"]
    quotas = cfg["quotas"]
    reuse_policy = cfg["reuse_tags"]

    hard_fail, soft = [], []
    bank_files = sorted(bank_dir.glob("*.yaml"))
    if not bank_files:
        sys.exit(f"no bank files under {bank_dir}")

    fcodes_reg, wcodes_reg, pcodes_reg = load_registry_codes(cfg)

    banks, golds = {}, {}
    for bf in bank_files:
        try:
            banks[bf.stem] = yaml.safe_load(bf.read_text(encoding="utf-8"))
        except Exception as e:
            hard_fail.append(f"YAML parse error (bank) {bf.name}: {e}")
    for gf in gold_dir.glob("*.gold.yaml"):
        gid = gf.name[:-len(".gold.yaml")]
        try:
            golds[gid] = yaml.safe_load(gf.read_text(encoding="utf-8"))
        except Exception as e:
            hard_fail.append(f"YAML parse error (gold) {gf.name}: {e}")
    orphan_gold = sorted(set(golds) - set(banks))
    if orphan_gold:
        hard_fail.append(f"orphan gold files without bank items: {orphan_gold}")

    headline = headline_items(banks)
    exploratory_ids = sorted(set(banks) - set(headline))
    n_total = len(banks)
    n = len(headline)
    if n == 0:
        hard_fail.append("headline stratum is empty after exploratory exclusions")
    headline_denominator = max(n, 1)
    fruit_counts, p_claim_counts, cft_live_per_fruit = {}, {}, {}
    tiers_per_fruit, antagonist_cells = {}, {}
    format_counts = {name: 0 for name in cfg["allowed_formats"]}
    format_counts_all = {name: 0 for name in cfg["allowed_formats"]}
    required = cfg["required_fields"]
    contested_count = 0

    for iid, b in banks.items():
        if b is None:
            hard_fail.append(f"{iid}: empty bank file"); continue
        in_headline = iid in headline
        if b.get("id") != iid:
            hard_fail.append(f"{iid}: bank id {b.get('id')!r} does not match filename stem")
        for k in required:
            if k not in b:
                hard_fail.append(f"{iid}: missing required field '{k}'")
        # pairing
        g = golds.get(iid)
        if g is None:
            hard_fail.append(f"{iid}: no matching gold");
        else:
            if g.get("id") != iid:
                hard_fail.append(f"{iid}: gold id {g.get('id')!r} does not match filename stem")
            if g.get("cell") != b.get("cell"):
                hard_fail.append(f"{iid}: bank/gold cell mismatch {b.get('cell')} vs {g.get('cell')}")
            if g.get("kernel_id") != b.get("kernel_id"):
                soft.append(f"{iid}: bank/gold kernel_id mismatch")
            cft = (g.get("paths") or {}).get("cft") or {}
            try:
                observed_cft_ids = cft_ids(cft)
            except ValueError as exc:
                hard_fail.append(f"{iid}: {exc}")
                observed_cft_ids = ()
            if len(observed_cft_ids) > 1:
                markers_by_cft = cft.get("markers_by_cft")
                if not isinstance(markers_by_cft, dict):
                    hard_fail.append(f"{iid}: multi-CFT gold requires markers_by_cft")
                elif set(markers_by_cft) != set(observed_cft_ids):
                    hard_fail.append(
                        f"{iid}: markers_by_cft keys do not equal cft_ids"
                    )
        # registry-tag lint
        fruit_codes = b.get("fruit_codes", [])
        if len(fruit_codes) != len(set(fruit_codes)):
            hard_fail.append(f"{iid}: duplicate fruit_codes are not allowed")
        for fc in fruit_codes:
            if fc not in fcodes_reg:
                hard_fail.append(f"{iid}: fruit_code {fc} not in registry")
            if in_headline:
                fruit_counts[fc] = fruit_counts.get(fc, 0) + 1
        vc = b.get("vice_code")
        cell = b.get("cell", {}) or {}
        if cell.get("fruit") not in fruit_codes:
            hard_fail.append(
                f"{iid}: cell.fruit {cell.get('fruit')!r} is absent from fruit_codes"
            )
        if vc is not None:
            if vc not in wcodes_reg:
                hard_fail.append(f"{iid}: vice_code {vc} not in registry")
            if in_headline:
                antagonist_cells.setdefault((cell.get("fruit"), vc), []).append(iid)
            if cell.get("vice") != vc:
                hard_fail.append(
                    f"{iid}: cell.vice {cell.get('vice')!r} does not match vice_code {vc!r}"
                )
        else:
            if not b.get("vice_open"):
                soft.append(f"{iid}: no vice_code and no vice_open (P9?)")
        for pc in b.get("p_claims", []):
            if pc not in pcodes_reg:
                hard_fail.append(f"{iid}: p_claim {pc} not in registry")
            if in_headline:
                p_claim_counts[pc] = p_claim_counts.get(pc, 0) + 1
        if in_headline and b.get("gold_status") == "contested_band":
            contested_count += 1
        # tier / format / cft
        fr = cell.get("fruit")
        if in_headline:
            tiers_per_fruit.setdefault(fr, set()).add(b.get("tier"))
        fmt = b.get("format")
        if fmt in format_counts_all:
            format_counts_all[fmt] += 1
            if in_headline:
                format_counts[fmt] += 1
        else:
            hard_fail.append(f"{iid}: format {fmt!r} not in configured allowed_formats")
        cft_path = (g.get("paths") or {}).get("cft") if g else None
        cft_has_markers = bool(cft_path and cft_path.get("markers"))
        if cft_path and isinstance(cft_path.get("markers_by_cft"), dict):
            cft_has_markers = cft_has_markers or any(cft_path["markers_by_cft"].values())
        if in_headline and b.get("tier") == "hard" and cft_has_markers:
            cft_live_per_fruit[fr] = cft_live_per_fruit.get(fr, 0) + 1
        # reuse-tag rule
        rt = b.get("reuse_tags", []) or []
        for tag in reuse_policy["all"]:
            if tag not in rt:
                soft.append(f"{iid}: missing reuse_tag {tag}")
        for tag in reuse_policy["by_format"].get(fmt, []):
            if tag not in rt:
                soft.append(f"{iid}: {fmt} missing reuse_tag {tag}")
        # lexical-flag scan on the prompt/turns only (not metadata)
        prompt_text = _model_visible_text(b)
        low = prompt_text.lower()
        hits = sorted({f for f in lexical_flags if f in low})
        if hits:
            soft.append(f"{iid}: lexical-flag hit(s) in prompt: {hits}")

    hard_fail.extend(audit_canaries(banks, golds, canary_policy))

    # ---- quota evaluation (all rules supplied by the design policy; D-37 S-4) ----
    design = str(cfg["design"]).upper()
    fruit_floor = float(quotas["fruit_floor"])
    print(
        f"\n=== {design} bank audit ===\n"
        f"items: {n_total} bank total, {n} headline, {len(exploratory_ids)} exploratory, "
        f"{len(golds)} gold\n"
    )
    if exploratory_ids:
        print(f"exploratory provenance rows: {exploratory_ids}")
    print(f"format (all): {format_counts_all}")
    print(f"format (headline quotas): {format_counts}")
    print("per-fruit item counts:")
    for f in sorted(fruit_counts):
        pct = fruit_counts[f] / headline_denominator
        flag = "" if pct >= fruit_floor else f"  <-- BELOW {fruit_floor*100:g}% FLOOR"
        print(f"  {f}: {fruit_counts[f]:2d}  ({pct*100:.1f}%){flag}")
        if pct < fruit_floor:
            hard_fail.append(f"fruit {f} below {fruit_floor*100:g}% floor ({pct*100:.1f}%)")
    missing_fruit = set(cfg["required_fruit_codes"]) - set(fruit_counts)
    if missing_fruit:
        hard_fail.append(f"fruit not covered at all: {sorted(missing_fruit)}")

    for pcode, floor in sorted(quotas["p_claim_floors"].items()):
        count = p_claim_counts.get(pcode, 0)
        pct = count / headline_denominator
        print(f"\n{pcode} items: {count} ({pct*100:.1f}%)  floor {floor*100:g}%")
        if pct < floor:
            hard_fail.append(f"{pcode} below {floor*100:g}% floor ({pct*100:.1f}%)")

    social = quotas["social_factional"]
    if social["enabled"]:
        codes = set(social["codes"])
        floor = float(social["floor"])
        ant_cells = list(antagonist_cells)
        sf = [c for c in ant_cells if c[1] in codes]
        sf_frac = len(sf) / len(ant_cells) if ant_cells else 0
        print(f"\nantagonist cells: {len(ant_cells)}; configured social-factional: "
              f"{len(sf)} ({sf_frac*100:.0f}%)  floor {floor*100:g}%")
        if sf_frac < floor:
            hard_fail.append(f"social-factional cells {sf_frac*100:.0f}% < {floor*100:g}%")

    required_tiers = set(quotas["required_tiers_per_fruit"])
    if required_tiers:
        print(f"\ntier coverage (each fruit needs {sorted(required_tiers)}):")
        for f in sorted(cfg["required_fruit_codes"]):
            observed_tiers = tiers_per_fruit.get(f, set())
            ok = required_tiers <= observed_tiers
            print(f"  {f}: {sorted(observed_tiers)}{'' if ok else '  <-- MISSING A TIER'}")
            if not ok:
                hard_fail.append(f"fruit {f} missing a tier: has {sorted(observed_tiers)}")

    cft_min = int(quotas["cft_live_per_fruit_min"])
    if cft_min:
        print(f"\nCFT-live items per fruit (need >={cft_min}):")
        for f in sorted(cfg["required_fruit_codes"]):
            count = cft_live_per_fruit.get(f, 0)
            print(f"  {f}: {count}{'' if count >= cft_min else f'  <-- BELOW {cft_min}'}")
            if count < cft_min:
                hard_fail.append(f"fruit {f} has <{cft_min} CFT-live items ({count})")

    contested_frac = contested_count / headline_denominator
    contested_max = float(quotas["contested_fraction_max"])
    print(f"\ncontested-band items: {contested_count} ({contested_frac*100:.1f}%)  "
          f"stop threshold >{contested_max*100:g}%")
    if contested_frac > contested_max:
        hard_fail.append(
            f"contested fraction {contested_frac*100:.1f}% > {contested_max*100:g}% (FO-6 stop)"
        )

    # ---- report ----
    print("\n=== SOFT findings (review, non-fatal) ===")
    for s in soft:
        print("  ~", s)
    if not soft:
        print("  (none)")
    print("\n=== HARD failures ===")
    for h in hard_fail:
        print("  X", h)
    if not hard_fail:
        print("  (none) — ALL HARD CHECKS PASS")
    print()
    return 1 if hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
