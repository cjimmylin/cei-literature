"""Exponential backoff with jitter for transient CLI failures / rate limits."""

from __future__ import annotations

import random
import time
from typing import Callable, Optional, TypeVar

T = TypeVar("T")


def compute_delay(attempt: int, base: float = 1.0, factor: float = 2.0,
                  max_delay: float = 60.0, jitter: float = 0.5) -> float:
    """Delay (seconds) before ``attempt`` (0-indexed retry number).

    Full exponential growth capped at ``max_delay``, plus +/- ``jitter`` fraction
    of random jitter to decorrelate concurrent callers.
    """
    raw = base * (factor ** attempt)
    capped = min(raw, max_delay)
    if jitter:
        delta = capped * jitter
        capped = capped + random.uniform(-delta, delta)
    return max(0.0, capped)


def retry_with_backoff(
    fn: Callable[[], T],
    is_transient: Callable[[T], bool],
    max_retries: int = 3,
    base: float = 1.0,
    factor: float = 2.0,
    max_delay: float = 60.0,
    jitter: float = 0.5,
    sleep: Optional[Callable[[float], None]] = None,
) -> T:
    """Call ``fn`` up to ``max_retries``+1 times while ``is_transient(result)``.

    ``fn`` must return a value (never raise for model-side outcomes — matches the
    RunnerBackend contract). ``is_transient`` decides whether to retry based on
    that value (e.g. rate-limit / transient error classifications). ``sleep`` is
    injectable so tests run instantly.
    """
    sleep = sleep or time.sleep
    result = fn()
    attempt = 0
    while is_transient(result) and attempt < max_retries:
        delay = compute_delay(attempt, base=base, factor=factor,
                              max_delay=max_delay, jitter=jitter)
        sleep(delay)
        attempt += 1
        result = fn()
    return result
