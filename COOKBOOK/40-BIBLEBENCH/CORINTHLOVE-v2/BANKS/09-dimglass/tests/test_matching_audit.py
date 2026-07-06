"""C3: matched-arm symmetry audit passes on the shipped bank."""
import os

import matching_audit

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_matching_audit_passes():
    res = matching_audit.run(bank_dir=BANK, assert_ok=True)
    assert res["failures"] == []
    assert res["n_pairs"] >= 200
