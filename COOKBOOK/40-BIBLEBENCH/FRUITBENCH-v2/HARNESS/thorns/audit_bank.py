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
        "design", "paths", "canary", "registry_patterns", "registry_literals",
        "required_fields", "required_fruit_codes", "allowed_formats", "lexical_flags",
        "quotas", "reuse_tags",
    }
    missing_top = sorted(required_top - set(cfg))
    if missing_top:
        raise ValueError(f"audit config missing required field(s) {missing_top}: {config_path}")
    if not str(cfg["design"]).strip() or not str(cfg["canary"]).strip():
        raise ValueError(f"audit config design/canary must be non-empty: {config_path}")
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
    canary = cfg["canary"]
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

    n = len(banks)
    fruit_counts, p_claim_counts, cft_live_per_fruit = {}, {}, {}
    tiers_per_fruit, antagonist_cells = {}, {}
    format_counts = {name: 0 for name in cfg["allowed_formats"]}
    required = cfg["required_fields"]
    contested_count = 0

    for iid, b in banks.items():
        if b is None:
            hard_fail.append(f"{iid}: empty bank file"); continue
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
        # registry-tag lint
        fruit_codes = b.get("fruit_codes", [])
        if len(fruit_codes) != len(set(fruit_codes)):
            hard_fail.append(f"{iid}: duplicate fruit_codes are not allowed")
        for fc in fruit_codes:
            if fc not in fcodes_reg:
                hard_fail.append(f"{iid}: fruit_code {fc} not in registry")
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
            p_claim_counts[pc] = p_claim_counts.get(pc, 0) + 1
        if b.get("gold_status") == "contested_band":
            contested_count += 1
        # tier / format / cft
        fr = cell.get("fruit")
        tiers_per_fruit.setdefault(fr, set()).add(b.get("tier"))
        fmt = b.get("format")
        if fmt in format_counts:
            format_counts[fmt] += 1
        else:
            hard_fail.append(f"{iid}: format {fmt!r} not in configured allowed_formats")
        if b.get("tier") == "hard" and (g and g.get("paths", {}).get("cft", {}).get("markers")):
            cft_live_per_fruit[fr] = cft_live_per_fruit.get(fr, 0) + 1
        # reuse-tag rule
        rt = b.get("reuse_tags", []) or []
        for tag in reuse_policy["all"]:
            if tag not in rt:
                soft.append(f"{iid}: missing reuse_tag {tag}")
        for tag in reuse_policy["by_format"].get(fmt, []):
            if tag not in rt:
                soft.append(f"{iid}: {fmt} missing reuse_tag {tag}")
        # canary in prompt text
        if b.get("canary") != canary:
            hard_fail.append(f"{iid}: canary metadata does not equal the configured canary")
        # lexical-flag scan on the prompt/turns only (not metadata)
        prompt_text = (b.get("prompt") or "")
        for t in (b.get("turns") or []):
            prompt_text += " " + json.dumps(t, default=str)
        if canary not in prompt_text:
            hard_fail.append(f"{iid}: canary absent from prompt/turn text")
        low = prompt_text.lower()
        hits = sorted({f for f in lexical_flags if f in low})
        if hits:
            soft.append(f"{iid}: lexical-flag hit(s) in prompt: {hits}")

    # gold contamination: canary must NOT be in gold
    for gid, g in golds.items():
        if canary in json.dumps(g, default=str):
            hard_fail.append(f"{gid}: canary leaked into gold")

    # ---- quota evaluation (all rules supplied by the design policy; D-37 S-4) ----
    design = str(cfg["design"]).upper()
    fruit_floor = float(quotas["fruit_floor"])
    print(f"\n=== {design} bank audit ===\nitems: {n} bank, {len(golds)} gold\n")
    print(f"format: {format_counts}")
    print("per-fruit item counts:")
    for f in sorted(fruit_counts):
        pct = fruit_counts[f] / n
        flag = "" if pct >= fruit_floor else f"  <-- BELOW {fruit_floor*100:g}% FLOOR"
        print(f"  {f}: {fruit_counts[f]:2d}  ({pct*100:.1f}%){flag}")
        if pct < fruit_floor:
            hard_fail.append(f"fruit {f} below {fruit_floor*100:g}% floor ({pct*100:.1f}%)")
    missing_fruit = set(cfg["required_fruit_codes"]) - set(fruit_counts)
    if missing_fruit:
        hard_fail.append(f"fruit not covered at all: {sorted(missing_fruit)}")

    for pcode, floor in sorted(quotas["p_claim_floors"].items()):
        count = p_claim_counts.get(pcode, 0)
        pct = count / n
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

    contested_frac = contested_count / n
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
