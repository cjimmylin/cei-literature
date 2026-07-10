"""Backoff tests — deterministic via injected sleep and jitter=0."""

from t1_runner import compute_delay, retry_with_backoff


def test_compute_delay_exponential_no_jitter():
    assert compute_delay(0, base=1, factor=2, jitter=0) == 1
    assert compute_delay(1, base=1, factor=2, jitter=0) == 2
    assert compute_delay(2, base=1, factor=2, jitter=0) == 4


def test_compute_delay_capped():
    assert compute_delay(10, base=1, factor=2, max_delay=5, jitter=0) == 5


def test_compute_delay_jitter_bounds():
    for _ in range(50):
        d = compute_delay(3, base=1, factor=2, max_delay=100, jitter=0.5)
        # base capped value is 8; +/-50%
        assert 4.0 <= d <= 12.0


def test_retry_stops_when_not_transient():
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        return "ok"
    result = retry_with_backoff(fn, is_transient=lambda r: r != "ok",
                                max_retries=5, sleep=lambda s: None)
    assert result == "ok"
    assert calls["n"] == 1


def test_retry_retries_transient_then_succeeds():
    seq = iter(["rate_limit", "rate_limit", "ok"])
    slept = []

    def fn():
        return next(seq)
    result = retry_with_backoff(fn, is_transient=lambda r: r == "rate_limit",
                                max_retries=5, base=1, jitter=0,
                                sleep=slept.append)
    assert result == "ok"
    assert slept == [1, 2]  # two backoff sleeps before success


def test_retry_exhausts_max_retries():
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        return "rate_limit"
    result = retry_with_backoff(fn, is_transient=lambda r: r == "rate_limit",
                                max_retries=3, sleep=lambda s: None)
    assert result == "rate_limit"
    assert calls["n"] == 4  # 1 initial + 3 retries
