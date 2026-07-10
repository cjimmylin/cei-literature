"""WALKWORTHY run harness (Session O2).

Manifest-driven runner for the WALKWORTHY family of 10 Christian-ethics
values-alignment benchmarks. Mock-first: no live model calls until Session O3.

Authority: 00-PORTFOLIO/20260706-master-plan.md §2 (build spec), §3 (frozen gates);
normative charter (construct + strata + reporting spine); item playbook (refusal
taxonomy). Loads the PUBLIC split only — never HOLDOUT/ (charter §6.6).
"""

CANARY = "WALKWORTHY-CANARY-7f3e2026"

__all__ = ["CANARY"]
