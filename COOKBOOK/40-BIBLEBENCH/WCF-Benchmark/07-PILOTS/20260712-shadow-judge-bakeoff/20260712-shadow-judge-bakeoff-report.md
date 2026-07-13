# WCF-Bench — Shadow Judge Bakeoff

**SHADOW / NOT A QUALIFICATION MANIFEST**

Run status: **PARTIAL**

This descriptive report has no effect on T4, the panel, the manifest, the closed candidate ladder, or any score of record.

## Scope

Surface denominators: `{'open_award': 8, 'coherence': 8, 'disclosure': 6, 'settled_core': 6}`; seed 1647.
Comparator-specific denominators:
```json
[
  {
    "available": 8,
    "comparator": "gemini-flash",
    "persisted_comparator_records": 8,
    "planned": 8,
    "required_comparator_records": 8,
    "surface": "open_award"
  },
  {
    "available": 8,
    "comparator": "grok-4.20",
    "persisted_comparator_records": 8,
    "planned": 8,
    "required_comparator_records": 8,
    "surface": "open_award"
  },
  {
    "available": 8,
    "comparator": "gemini-flash",
    "persisted_comparator_records": 8,
    "planned": 8,
    "required_comparator_records": 8,
    "surface": "coherence"
  },
  {
    "available": 8,
    "comparator": "grok-4.20",
    "persisted_comparator_records": 8,
    "planned": 8,
    "required_comparator_records": 8,
    "surface": "coherence"
  },
  {
    "available": 6,
    "comparator": "gemini-flash",
    "persisted_comparator_records": 6,
    "planned": 6,
    "required_comparator_records": 6,
    "surface": "disclosure"
  },
  {
    "available": 2,
    "comparator": "grok-4.20",
    "persisted_comparator_records": 2,
    "planned": 6,
    "required_comparator_records": 2,
    "surface": "disclosure"
  },
  {
    "available": 6,
    "comparator": "gemini-flash",
    "persisted_comparator_records": 6,
    "planned": 6,
    "required_comparator_records": 6,
    "surface": "settled_core"
  },
  {
    "available": 2,
    "comparator": "grok-4.20",
    "persisted_comparator_records": 2,
    "planned": 6,
    "required_comparator_records": 2,
    "surface": "settled_core"
  }
]
```

## Qualification

```json
{
  "deepseek-v4-pro": {
    "eligible_surfaces": [
      "coherence",
      "disclosure",
      "settled_core"
    ],
    "probes": {
      "award_consistency": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "disclosure_inversion": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "discrimination": {
        "cause_tally": {
          "fail_transport_after_retry": 7,
          "pass": 1
        },
        "k": 8,
        "n_pass": 1
      },
      "g4": {
        "cause_tally": {
          "fail_format": 1,
          "pass": 7
        },
        "k": 8,
        "n_pass": 7
      },
      "negative_disclosure": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "settled_core": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      }
    }
  },
  "glm-5.2": {
    "eligible_surfaces": [
      "coherence",
      "disclosure",
      "open_award",
      "settled_core"
    ],
    "probes": {
      "award_consistency": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "disclosure_inversion": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "discrimination": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "g4": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "negative_disclosure": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      },
      "settled_core": {
        "cause_tally": {
          "pass": 8
        },
        "k": 8,
        "n_pass": 8
      }
    }
  }
}
```

- glm-5.2: surfaces=['coherence', 'disclosure', 'open_award', 'settled_core']; labels=['SHADOW-ELIGIBLE FOR open_award', 'SHADOW-ELIGIBLE FOR coherence', 'SHADOW-ELIGIBLE FOR disclosure', 'SHADOW-ELIGIBLE FOR settled_core', 'INDEPENDENCE-CONFLICTED', 'INSUFFICIENT EVIDENCE']
- deepseek-v4-pro: surfaces=['coherence', 'disclosure', 'settled_core']; labels=['SHADOW-INELIGIBLE FOR open_award', 'SHADOW-ELIGIBLE FOR coherence', 'SHADOW-ELIGIBLE FOR disclosure', 'SHADOW-ELIGIBLE FOR settled_core', 'INDEPENDENCE-CONFLICTED', 'INSUFFICIENT EVIDENCE']

## Real-response agreement

Incumbent agreement is descriptive and the incumbents are not human labels.

```json
[
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 8,
    "component_agreement_denominator": 47,
    "component_agreement_fraction": 0.723404255319149,
    "component_agreement_numerator": 34.0,
    "disagreement_count": 7,
    "disagreement_identifiers": [
      {
        "item_id": "WHOLE-C5-W303",
        "response_sha256": "449decde573bf365cd19717da36ddef07a47fec0a8532924e905d4fe0b37624e",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "WHOLE-C7-010",
        "response_sha256": "701acf3ac2a202c76e94e095af97b97d12caa3a2cb4b87e716cd4fd8b8c74bef",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "STED-C9-W305",
        "response_sha256": "f30af4d95b5a66b74f0e460e607edba418eb9639cc0122efc4d707ff2f66d403",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "STED-C9-W304",
        "response_sha256": "eb5ea85572e0f40938da6ab0883096ecc79c31bc780df9f14cebf11e996f4beb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "STED-C1-W306",
        "response_sha256": "28e65f5ec98ae70d62135ea5914fee19117c4fccb56d7af796fdccf94e283307",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "MEND-C9-W307",
        "response_sha256": "97224890453d6454c7acd26fc4d3f8a2b9d4b9e2b1f4530cedc1f395b792667c",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "DUTY-C2-007",
        "response_sha256": "0fc08901a8db9e0ca47c4467f5b1efce9eeb61fb6a32f07a5674d84f625d2feb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      }
    ],
    "exact_agreement_fraction": 0.125,
    "exact_agreement_n": 1,
    "graded_count": 8,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "open_award"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 8,
    "component_agreement_denominator": 47,
    "component_agreement_fraction": 0.6808510638297872,
    "component_agreement_numerator": 32.0,
    "disagreement_count": 7,
    "disagreement_identifiers": [
      {
        "item_id": "STED-C1-009",
        "response_sha256": "3070ece493d282d7cec0727f8c2c58411b737ed075e6595ac8bb01574a94c793",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "WHOLE-C5-W303",
        "response_sha256": "449decde573bf365cd19717da36ddef07a47fec0a8532924e905d4fe0b37624e",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "WHOLE-C7-010",
        "response_sha256": "701acf3ac2a202c76e94e095af97b97d12caa3a2cb4b87e716cd4fd8b8c74bef",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "STED-C9-W305",
        "response_sha256": "f30af4d95b5a66b74f0e460e607edba418eb9639cc0122efc4d707ff2f66d403",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "STED-C9-W304",
        "response_sha256": "eb5ea85572e0f40938da6ab0883096ecc79c31bc780df9f14cebf11e996f4beb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "STED-C1-W306",
        "response_sha256": "28e65f5ec98ae70d62135ea5914fee19117c4fccb56d7af796fdccf94e283307",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "DUTY-C2-007",
        "response_sha256": "0fc08901a8db9e0ca47c4467f5b1efce9eeb61fb6a32f07a5674d84f625d2feb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      }
    ],
    "exact_agreement_fraction": 0.125,
    "exact_agreement_n": 1,
    "graded_count": 8,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "open_award"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 8,
    "component_agreement_denominator": 8,
    "component_agreement_fraction": 0.125,
    "component_agreement_numerator": 1.0,
    "disagreement_count": 7,
    "disagreement_identifiers": [
      {
        "item_id": "MEND-A-010",
        "response_sha256": "dbb7282948aae1ae77e24bdee72539a81a7ad0eda294829c1263611ee03995a8",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "MEND-C2-W302",
        "response_sha256": "962968d9bcd832174bc1b582b06371bb593ea08317f78aaad627a26ef562357d",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C5-W303",
        "response_sha256": "1fe5b2fe199eaa82d622159afe64a0e659ac5e17e886deb26e0853fb0b0c2fcc",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C4-W301",
        "response_sha256": "58dd38097b9e84e272941b2f77d37ac7f40bb8aabd7b68fbef1fa63ab38f938f",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "LIB-C4-W301",
        "response_sha256": "55d0b1d7ff419982397fac2718b4eca51de50fadfe1bd3110227e5a31c3467d2",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C10-009",
        "response_sha256": "135667c65e52064af444199c0a3a037c0bb130cf0afdad77ed4f8a9cbbbeffca",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "WHOLE-C10-005",
        "response_sha256": "a38bb7b801ac888c545f6a55cb7e60fb200af99a5752eca8f3139cccbcb05f2f",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      }
    ],
    "exact_agreement_fraction": 0.125,
    "exact_agreement_n": 1,
    "graded_count": 8,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "coherence"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 8,
    "component_agreement_denominator": 8,
    "component_agreement_fraction": 0.375,
    "component_agreement_numerator": 3.0,
    "disagreement_count": 5,
    "disagreement_identifiers": [
      {
        "item_id": "LIB-C2-W307",
        "response_sha256": "3557af4ac57eed30f9b13a45419be2bde874a33da73aff7fbddd879b4cba9bb5",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "LIB-C5-W303",
        "response_sha256": "1fe5b2fe199eaa82d622159afe64a0e659ac5e17e886deb26e0853fb0b0c2fcc",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C4-W301",
        "response_sha256": "58dd38097b9e84e272941b2f77d37ac7f40bb8aabd7b68fbef1fa63ab38f938f",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "LIB-C4-W301",
        "response_sha256": "55d0b1d7ff419982397fac2718b4eca51de50fadfe1bd3110227e5a31c3467d2",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C10-009",
        "response_sha256": "135667c65e52064af444199c0a3a037c0bb130cf0afdad77ed4f8a9cbbbeffca",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      }
    ],
    "exact_agreement_fraction": 0.375,
    "exact_agreement_n": 3,
    "graded_count": 8,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "coherence"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 6,
    "component_agreement_denominator": 6,
    "component_agreement_fraction": 0.5,
    "component_agreement_numerator": 3.0,
    "disagreement_count": 3,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "cf8555ee3023d72d8f31eade3a660e0d47111af514f89d2465fe5242e1aca2d1",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "f2d5560d43f595b8e4e08f156a512389bc077a171b8f85990499bc82b14f89f7",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "7de5b4bc1b166a50f65c79b37a609ca5a917044a537fdbc89bb7764b3c116633",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.5,
    "exact_agreement_n": 3,
    "graded_count": 6,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "disclosure"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 2,
    "component_agreement_denominator": 2,
    "component_agreement_fraction": 0.0,
    "component_agreement_numerator": 0.0,
    "disagreement_count": 2,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "8ae5238107ade44be6b508a3033d37d46c0fe0463f8da739c35682bbaac39290",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.0,
    "exact_agreement_n": 0,
    "graded_count": 6,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "disclosure"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 6,
    "component_agreement_denominator": 10,
    "component_agreement_fraction": 0.1,
    "component_agreement_numerator": 1.0,
    "disagreement_count": 5,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "cf8555ee3023d72d8f31eade3a660e0d47111af514f89d2465fe5242e1aca2d1",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "820b58cb2f72a2de24866c515833ee54995ffcad5b2eb41bfd06619526ef1b3c",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "f2d5560d43f595b8e4e08f156a512389bc077a171b8f85990499bc82b14f89f7",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "7de5b4bc1b166a50f65c79b37a609ca5a917044a537fdbc89bb7764b3c116633",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.16666666666666666,
    "exact_agreement_n": 1,
    "graded_count": 6,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "settled_core"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 2,
    "component_agreement_denominator": 3,
    "component_agreement_fraction": 0.6666666666666666,
    "component_agreement_numerator": 2.0,
    "disagreement_count": 1,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.5,
    "exact_agreement_n": 1,
    "graded_count": 6,
    "judge": "glm-5.2",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "settled_core"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 8,
    "component_agreement_denominator": 42,
    "component_agreement_fraction": 0.8571428571428571,
    "component_agreement_numerator": 36.0,
    "disagreement_count": 5,
    "disagreement_identifiers": [
      {
        "item_id": "WHOLE-C5-W303",
        "response_sha256": "449decde573bf365cd19717da36ddef07a47fec0a8532924e905d4fe0b37624e",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "WHOLE-C7-010",
        "response_sha256": "701acf3ac2a202c76e94e095af97b97d12caa3a2cb4b87e716cd4fd8b8c74bef",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "STED-C9-W304",
        "response_sha256": "eb5ea85572e0f40938da6ab0883096ecc79c31bc780df9f14cebf11e996f4beb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "STED-C1-W306",
        "response_sha256": "28e65f5ec98ae70d62135ea5914fee19117c4fccb56d7af796fdccf94e283307",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "MEND-C9-W307",
        "response_sha256": "97224890453d6454c7acd26fc4d3f8a2b9d4b9e2b1f4530cedc1f395b792667c",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      }
    ],
    "exact_agreement_fraction": 0.2857142857142857,
    "exact_agreement_n": 2,
    "graded_count": 7,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 0.875,
    "planned": 8,
    "surface": "open_award"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 8,
    "component_agreement_denominator": 42,
    "component_agreement_fraction": 0.7380952380952381,
    "component_agreement_numerator": 31.0,
    "disagreement_count": 6,
    "disagreement_identifiers": [
      {
        "item_id": "STED-C1-009",
        "response_sha256": "3070ece493d282d7cec0727f8c2c58411b737ed075e6595ac8bb01574a94c793",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "WHOLE-C5-W303",
        "response_sha256": "449decde573bf365cd19717da36ddef07a47fec0a8532924e905d4fe0b37624e",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "WHOLE-C7-010",
        "response_sha256": "701acf3ac2a202c76e94e095af97b97d12caa3a2cb4b87e716cd4fd8b8c74bef",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      },
      {
        "item_id": "STED-C9-W305",
        "response_sha256": "f30af4d95b5a66b74f0e460e607edba418eb9639cc0122efc4d707ff2f66d403",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "STED-C9-W304",
        "response_sha256": "eb5ea85572e0f40938da6ab0883096ecc79c31bc780df9f14cebf11e996f4beb",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "STED-C1-W306",
        "response_sha256": "28e65f5ec98ae70d62135ea5914fee19117c4fccb56d7af796fdccf94e283307",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "mistralai/mistral-large-2512"
      }
    ],
    "exact_agreement_fraction": 0.14285714285714285,
    "exact_agreement_n": 1,
    "graded_count": 7,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 0.875,
    "planned": 8,
    "surface": "open_award"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 8,
    "component_agreement_denominator": 8,
    "component_agreement_fraction": 0.625,
    "component_agreement_numerator": 5.0,
    "disagreement_count": 3,
    "disagreement_identifiers": [
      {
        "item_id": "MEND-A-010",
        "response_sha256": "dbb7282948aae1ae77e24bdee72539a81a7ad0eda294829c1263611ee03995a8",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "MEND-C2-W302",
        "response_sha256": "962968d9bcd832174bc1b582b06371bb593ea08317f78aaad627a26ef562357d",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "LIB-C10-009",
        "response_sha256": "135667c65e52064af444199c0a3a037c0bb130cf0afdad77ed4f8a9cbbbeffca",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      }
    ],
    "exact_agreement_fraction": 0.625,
    "exact_agreement_n": 5,
    "graded_count": 8,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "coherence"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 8,
    "component_agreement_denominator": 8,
    "component_agreement_fraction": 0.625,
    "component_agreement_numerator": 5.0,
    "disagreement_count": 3,
    "disagreement_identifiers": [
      {
        "item_id": "LIB-C2-W307",
        "response_sha256": "3557af4ac57eed30f9b13a45419be2bde874a33da73aff7fbddd879b4cba9bb5",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "LIB-C10-009",
        "response_sha256": "135667c65e52064af444199c0a3a037c0bb130cf0afdad77ed4f8a9cbbbeffca",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "anthropic/claude-haiku-4.5"
      },
      {
        "item_id": "WHOLE-C10-005",
        "response_sha256": "a38bb7b801ac888c545f6a55cb7e60fb200af99a5752eca8f3139cccbcb05f2f",
        "source_run": "corrected-mvp-open-reparse",
        "sut_slug": "deepseek/deepseek-chat"
      }
    ],
    "exact_agreement_fraction": 0.625,
    "exact_agreement_n": 5,
    "graded_count": 8,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 8,
    "surface": "coherence"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 6,
    "component_agreement_denominator": 6,
    "component_agreement_fraction": 0.5,
    "component_agreement_numerator": 3.0,
    "disagreement_count": 3,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "cf8555ee3023d72d8f31eade3a660e0d47111af514f89d2465fe5242e1aca2d1",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "f2d5560d43f595b8e4e08f156a512389bc077a171b8f85990499bc82b14f89f7",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      }
    ],
    "exact_agreement_fraction": 0.5,
    "exact_agreement_n": 3,
    "graded_count": 6,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "disclosure"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 2,
    "component_agreement_denominator": 2,
    "component_agreement_fraction": 0.5,
    "component_agreement_numerator": 1.0,
    "disagreement_count": 1,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "8ae5238107ade44be6b508a3033d37d46c0fe0463f8da739c35682bbaac39290",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.5,
    "exact_agreement_n": 1,
    "graded_count": 6,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "disclosure"
  },
  {
    "comparator": "gemini-flash",
    "comparator_available_count": 6,
    "component_agreement_denominator": 10,
    "component_agreement_fraction": 0.2,
    "component_agreement_numerator": 2.0,
    "disagreement_count": 5,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C3-W302",
        "response_sha256": "cf8555ee3023d72d8f31eade3a660e0d47111af514f89d2465fe5242e1aca2d1",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "820b58cb2f72a2de24866c515833ee54995ffcad5b2eb41bfd06619526ef1b3c",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "f2d5560d43f595b8e4e08f156a512389bc077a171b8f85990499bc82b14f89f7",
        "source_run": "r33-3judge",
        "sut_slug": "deepseek/deepseek-chat"
      },
      {
        "item_id": "AGG-C8-W305",
        "response_sha256": "7de5b4bc1b166a50f65c79b37a609ca5a917044a537fdbc89bb7764b3c116633",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.16666666666666666,
    "exact_agreement_n": 1,
    "graded_count": 6,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "settled_core"
  },
  {
    "comparator": "grok-4.20",
    "comparator_available_count": 2,
    "component_agreement_denominator": 3,
    "component_agreement_fraction": 0.6666666666666666,
    "component_agreement_numerator": 2.0,
    "disagreement_count": 1,
    "disagreement_identifiers": [
      {
        "item_id": "AGG-C5-W304",
        "response_sha256": "11d78d0e67438db3ca3b5b93733c570a1e891ceeb0f3796ccea6a890b9a84945",
        "source_run": "floor-rerun",
        "sut_slug": "meta-llama/llama-3.1-8b-instruct"
      }
    ],
    "exact_agreement_fraction": 0.5,
    "exact_agreement_n": 1,
    "graded_count": 6,
    "judge": "deepseek-v4-pro",
    "parseable_fraction": 1.0,
    "planned": 6,
    "surface": "settled_core"
  }
]
```

## Operations

```json
{
  "deepseek-v4-pro": {
    "actual_cost_usd": 0.38574403701000004,
    "by_phase": {
      "qualification": {
        "actual_cost_usd": 0.22159627581999994,
        "calls": 117,
        "completion_tokens": 85848,
        "errors": 25,
        "mean_call_seconds": 23.541683612179476,
        "prompt_tokens": 80265,
        "retries": 21,
        "truncations": 29
      },
      "real_response": {
        "actual_cost_usd": 0.16414776119000002,
        "calls": 42,
        "completion_tokens": 43937,
        "errors": 12,
        "mean_call_seconds": 30.94094710216673,
        "prompt_tokens": 37454,
        "retries": 11,
        "truncations": 3
      }
    },
    "by_surface": {
      "coherence": {
        "errors": 0,
        "graded": 8,
        "parseable_fraction": 1.0,
        "planned": 8
      },
      "disclosure": {
        "errors": 0,
        "graded": 6,
        "parseable_fraction": 1.0,
        "planned": 6
      },
      "open_award": {
        "errors": 1,
        "graded": 7,
        "parseable_fraction": 0.875,
        "planned": 8
      },
      "settled_core": {
        "errors": 0,
        "graded": 6,
        "parseable_fraction": 1.0,
        "planned": 6
      }
    },
    "calls": 159,
    "completion_tokens": 129785,
    "errors": 1,
    "mean_call_seconds": 25.496206043496862,
    "parse_fraction": 0.9642857142857143,
    "prompt_tokens": 117719,
    "retries": 32,
    "truncations": 32
  },
  "glm-5.2": {
    "actual_cost_usd": 0.31201990141999997,
    "by_phase": {
      "qualification": {
        "actual_cost_usd": 0.17573989137499993,
        "calls": 88,
        "completion_tokens": 45213,
        "errors": 0,
        "mean_call_seconds": 9.100387498624997,
        "prompt_tokens": 71232,
        "retries": 0,
        "truncations": 0
      },
      "real_response": {
        "actual_cost_usd": 0.13628001004499998,
        "calls": 31,
        "completion_tokens": 24880,
        "errors": 3,
        "mean_call_seconds": 20.51820327822581,
        "prompt_tokens": 35115,
        "retries": 3,
        "truncations": 0
      }
    },
    "by_surface": {
      "coherence": {
        "errors": 0,
        "graded": 8,
        "parseable_fraction": 1.0,
        "planned": 8
      },
      "disclosure": {
        "errors": 0,
        "graded": 6,
        "parseable_fraction": 1.0,
        "planned": 6
      },
      "open_award": {
        "errors": 0,
        "graded": 8,
        "parseable_fraction": 1.0,
        "planned": 8
      },
      "settled_core": {
        "errors": 0,
        "graded": 6,
        "parseable_fraction": 1.0,
        "planned": 6
      }
    },
    "calls": 119,
    "completion_tokens": 70093,
    "errors": 0,
    "mean_call_seconds": 12.07477648322689,
    "parse_fraction": 1.0,
    "prompt_tokens": 106347,
    "retries": 3,
    "truncations": 0
  }
}
```

Internal actual/fallback cost: $0.6978.

## PARETO disclosure

No Pareto candidate is emitted.
No weighted composite is used. No label authorizes deployment.

> PARTIAL / STOPPED: reconciliation UNRECONCILED: accounting total exceeded budget
