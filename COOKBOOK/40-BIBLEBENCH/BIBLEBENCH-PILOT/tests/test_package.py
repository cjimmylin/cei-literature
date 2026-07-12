def test_package_exposes_version():
    import biblebench_pilot

    assert biblebench_pilot.__version__ == "0.1.0"
