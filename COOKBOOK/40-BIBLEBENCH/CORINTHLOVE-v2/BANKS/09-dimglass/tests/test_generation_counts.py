"""Generation integrity: counts, reseed novelty (A1), disjoint pools (B4)."""
import generator as gen
from lib import surfaces


def test_asserts_pass():
    eps, side, stats, pairs, _ = gen.generate(20260706)
    extra = gen.run_asserts(eps, side, stats, pairs)
    assert stats["n_private"] >= 900
    assert stats["n_public"] == 30
    assert extra["frac_valid"] >= 0.40
    assert extra["frac_two_sided"] >= 0.30


def test_generator_not_list_reseed_novel():
    """A1: regenerating with a different seed yields NOVEL items."""
    a, _, _, _, _ = gen.generate(20260706)
    b, _, _, _, _ = gen.generate(999001)
    # same schema/size, but the rendered stage_1 texts should differ substantially
    a_texts = [e["multiturn_script"]["stage_1"] for e in a[:200]]
    b_texts = [e["multiturn_script"]["stage_1"] for e in b[:200]]
    overlap = len(set(a_texts) & set(b_texts))
    assert overlap < 40, f"too many identical items across seeds: {overlap}/200"
    # challenge surfaces also differ
    a_ch = [e["multiturn_script"]["stage_2"] for e in a[:200]]
    b_ch = [e["multiturn_script"]["stage_2"] for e in b[:200]]
    assert len(set(a_ch) & set(b_ch)) < 60


def test_axis_coverage():
    """A2: emitted items span the declared axes (5 domains, 6 doses, 3 personas)."""
    eps, _, _, _, _ = gen.generate(20260706)
    domains = {e["parameters"]["domain"] for e in eps}
    assert domains == {"quant", "corpus_qa", "code", "logic", "reading"}
    doses = {e["parameters"]["round_1"]["dose"] for e in eps}
    assert doses == {"d0", "d1", "d2", "d3", "d4", "d5"}
    personas = {e["parameters"]["round_1"]["persona"] for e in eps}
    assert personas == {"peer", "authority", "novice"}


def test_disjoint_split_pools():
    """B4: public vs private use DISJOINT corpus-variant AND surface pools."""
    eps, _, _, _, _ = gen.generate(20260706)
    pub_cv, priv_cv = set(), set()
    pub_real, priv_real = set(), set()
    for e in eps:
        cv = e["parameters"]["corpus_variant"]
        ridx = e["parameters"]["round_1"]["realization_idx"]
        if e["split"] == "public":
            pub_cv.add(cv)
            pub_real.add(ridx < surfaces.PUBLIC_N)
        else:
            priv_cv.add(cv)
            priv_real.add(ridx < surfaces.PUBLIC_N)
    assert pub_cv & priv_cv == set(), f"corpus-variant pools overlap: {pub_cv & priv_cv}"
    assert pub_cv <= {0, 1} and priv_cv <= {2, 3, 4, 5}
    # public uses only public realizations (idx<PUBLIC_N), private only private
    assert pub_real == {True}
    assert priv_real == {False}


def test_d4d5_valid_only():
    """D-16: no invalid conclusive demonstrations exist anywhere."""
    eps, side, _, _, _ = gen.generate(20260706)
    for e in eps:
        for rnd in ("round_1", "round_2"):
            r = e["parameters"].get(rnd)
            if r and r["dose"] in ("d4", "d5"):
                assert r["validity"] == "valid", f"{e['id']} {rnd} invalid d4/d5"
