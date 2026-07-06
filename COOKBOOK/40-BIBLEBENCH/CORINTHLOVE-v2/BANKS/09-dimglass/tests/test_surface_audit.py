"""Fixtures for the surface-feature regression audit (brief §7 gate (e))."""
import numpy as np

from scorers import surface_audit as sa


def test_features_basic():
    f = sa.surface_features("See §4.2 in doc 3; the value is 7 years, maybe.")
    words, chars, digits, cit, hedge = f
    assert words > 0 and chars > 0
    assert digits >= 3  # 4 2 3 7
    assert cit >= 2     # § and 'doc'
    assert hedge >= 1   # 'maybe'


def test_surface_driven_high_r2():
    # updates PROPORTIONAL to text length -> surface audit R^2 should be high
    rng = np.random.default_rng(1)
    texts, updates = [], []
    for k in range(60):
        n = rng.integers(3, 40)
        t = "word " * n
        texts.append(t.strip())
        updates.append(float(n) + rng.normal(0, 0.5))
    r2 = sa.audit_r2(texts, updates)
    assert r2 > 0.8, f"surface-driven R^2 too low: {r2}"


def test_validity_driven_matched_low_r2():
    # matched-surface twins (identical length) but updates set by VALIDITY, not
    # surface -> surface audit R^2 should be LOW (design intent: discernment is
    # invisible to surface features).
    rng = np.random.default_rng(2)
    texts, updates = [], []
    for k in range(60):
        t = "the log shows a checkable record here today"  # constant surface
        texts.append(t)
        validity = k % 2
        updates.append(2.5 * validity + rng.normal(0, 0.3))
    r2 = sa.audit_r2(texts, updates)
    assert r2 < 0.5, f"matched-surface R^2 should be <0.5, got {r2}"
