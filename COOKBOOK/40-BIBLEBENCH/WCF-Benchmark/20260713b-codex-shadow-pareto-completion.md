# WCF-Bench — Shadow Pareto Completion

**Label:** **COMPANION OFFLINE COMPLETION / SHADOW ONLY / NOT A QUALIFICATION MANIFEST**

**Authority:** The binding Jimmy disposition recorded in
`20260713a-jimmy-shadow-reconciliation-ratification-record.md` authorizes this offline
completion from persisted evidence.

The immutable run directory and artifacts were not edited. This completion made no model,
network, OpenRouter, or paid calls.

## Mechanical Pareto application

The pre-registered Pareto contract in
`20260712n-shadow-judge-bakeoff-design.md` section 4 was applied mechanically to the
persisted qualification and operational metadata using the existing
`04-HARNESS/shadow_judge_bakeoff.py` `dominates` and `pareto_names` functions.

| Shadow candidate | Eligible surfaces | Parse fraction | Attributed cost | Independence conflicts |
|---|---:|---:|---:|---:|
| `glm-5.2` | 4 | `1.0` (28/28) | `$0.31201990142` | 1 |
| `deepseek-v4-pro` | 3 | `0.9642857142857143` (27/28) | `$0.38574403701` | 1 |

GLM is at least as good as DeepSeek on every registered dimension. It is strictly better
on eligible-surface count, parse fraction, and cost, while the two candidates are equal on
independence conflicts. Therefore GLM dominates DeepSeek.

The Pareto set is exactly `["glm-5.2"]`.

The only recommendation label applied is **`PARETO-PREFERRED SHADOW CANDIDATE`** for
`glm-5.2`.

## Shadow surface labels and caveats

- `glm-5.2`: `SHADOW-ELIGIBLE FOR open_award`, `SHADOW-ELIGIBLE FOR coherence`,
  `SHADOW-ELIGIBLE FOR disclosure`, and `SHADOW-ELIGIBLE FOR settled_core`.
- `deepseek-v4-pro`: `SHADOW-INELIGIBLE FOR open_award`, `SHADOW-ELIGIBLE FOR
  coherence`, `SHADOW-ELIGIBLE FOR disclosure`, and `SHADOW-ELIGIBLE FOR settled_core`.
- Both candidates retain the **`INDEPENDENCE-CONFLICTED`** caveat under the pre-registered
  design.

Incumbent agreement remains descriptive. It is not accuracy, human truth, or a human-label
substitute.

## Verification

A network-free invocation of the actual implementation functions from `04-HARNESS/`
against the exact table above returned:

```text
glm_dominates_deepseek= True
deepseek_dominates_glm= False
pareto_names= ['glm-5.2']
```

## Strong non-effect statement

This companion completion grants no production authorization and changes no panel,
manifest, candidate ladder, T4 plan, benchmark score, paper, or release state. It does not
authorize T3 or T4, and it authorizes no paid calls. Any production effect requires a
subsequent explicit Jimmy ruling.

## Sources

- Binding disposition:
  `20260713a-jimmy-shadow-reconciliation-ratification-record.md`.
- Immutable metadata:
  `07-PILOTS/20260712-shadow-judge-bakeoff/shadow-run-metadata.json`.
- Immutable execution-time report:
  `07-PILOTS/20260712-shadow-judge-bakeoff/20260712-shadow-judge-bakeoff-report.md`.
- Pre-registered analysis contract: `20260712n-shadow-judge-bakeoff-design.md` section 4.
- Mechanical implementation: `04-HARNESS/shadow_judge_bakeoff.py`, functions `dominates`
  and `pareto_names`.
