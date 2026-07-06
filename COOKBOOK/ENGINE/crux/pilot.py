"""Reusable pilot-build entrypoint for the CRUX generator (design 06 §3.1).

This is the shared surface designs 01 (UNMARKED) and 05 (CULTIVATE) consume:

- `publish_spec()` returns the JSON-serializable PUBLISHED spec — the value
  taxonomy, the typed factorial, the screened fractional design, and its
  confounding structure. Per §3.1 the spec is released; only the private
  parameter ranges / live instances are withheld.
- `build_pilot_instances()` compiles one FRESH scenario per screened cell.

`python -m crux.pilot --out DIR` writes both artifacts to disk.
"""
from __future__ import annotations

import argparse
import json
import os
from typing import Any, Dict, List

from crux import factorial, generator, values


def _serialize_cell(cell: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(cell)
    out["value_pair"] = list(cell["value_pair"])  # tuple -> list for JSON
    return out


def scenario_to_dict(s: generator.Scenario) -> Dict[str, Any]:
    return {
        "scenario_id": s.scenario_id,
        "cell": _serialize_cell(s.cell),
        "value_a": s.value_a,
        "value_b": s.value_b,
        "surface": s.surface,
        "commensurable": s.commensurable,
        "causal_graph": s.causal_graph,
        "options": [
            {"label": o.label, "honors": o.honors,
             "sacrifices": o.sacrifices, "text": o.text}
            for o in s.options
        ],
    }


def publish_spec(n_cells: int = 60, seed: int = 0) -> Dict[str, Any]:
    design = factorial.fractional_design(n_cells=n_cells, seed=seed)
    return {
        "values": [
            {"name": v.name, "schwartz_anchor": v.schwartz_anchor,
             "clause": v.clause}
            for v in values.CORE_VALUES
        ],
        "factors": {
            k: ([list(p) for p in lv] if k == "value_pair" else lv)
            for k, lv in factorial.FACTORS.items()
        },
        "fractional_design": [_serialize_cell(c) for c in design.cells],
        "confounding": design.confounding_report(),
    }


def build_pilot_instances(n_cells: int = 60, seed: int = 0,
                          instance_seed: int = 0) -> List[Dict[str, Any]]:
    design = factorial.fractional_design(n_cells=n_cells, seed=seed)
    return [
        scenario_to_dict(generator.generate_scenario(cell, instance_seed=instance_seed))
        for cell in design.cells
    ]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Emit CRUX published spec + pilot instances")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--n-cells", type=int, default=60)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--instance-seed", type=int, default=0)
    args = ap.parse_args(argv)
    os.makedirs(args.out, exist_ok=True)
    spec = publish_spec(args.n_cells, args.seed)
    inst = build_pilot_instances(args.n_cells, args.seed, args.instance_seed)
    with open(os.path.join(args.out, "crux-published-spec.json"), "w") as f:
        json.dump(spec, f, indent=2)
    with open(os.path.join(args.out, "crux-pilot-instances.json"), "w") as f:
        json.dump(inst, f, indent=2)
    print(f"wrote spec ({len(spec['fractional_design'])} cells) + "
          f"{len(inst)} instances to {args.out}")


if __name__ == "__main__":
    main()
