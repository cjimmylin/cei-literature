"""Honest status for the deferred empirical fine-tune probe."""


def finetune_status():
    return {
        "status": "NOT_RUN",
        "evidence_origin": None,
        "synthetic_surrogate_run": False,
        "empirical_eligible": False,
        "reason": "the preregistered 10%-fine-tune probe requires a later real training run",
    }


__all__ = ["finetune_status"]
