from __future__ import annotations

import json
from pathlib import Path
import shutil
from time import monotonic, sleep

import pytest


selenium = pytest.importorskip("selenium")
from selenium import webdriver  # noqa: E402
from selenium.common.exceptions import WebDriverException  # noqa: E402
from selenium.webdriver.chrome.options import Options  # noqa: E402
from selenium.webdriver.common.by import By  # noqa: E402


PACKAGE_ROOT = Path(__file__).parents[1]
INTERFACE = PACKAGE_ROOT / "adjudication" / "judge-interface.html"
MAC_CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def _chrome_binary() -> str | None:
    if MAC_CHROME.is_file():
        return str(MAC_CHROME)
    return next(
        (
            value
            for name in ("google-chrome", "google-chrome-stable", "chromium")
            if (value := shutil.which(name))
        ),
        None,
    )


def _open_interface(download_dir: Path, prelude: str | None = None):
    binary = _chrome_binary()
    if binary is None:
        pytest.skip("Chrome/Chromium is not installed")
    options = Options()
    options.binary_location = binary
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(download_dir.resolve()),
            "download.prompt_for_download": False,
        },
    )
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as error:
        pytest.skip(f"Chrome WebDriver is unavailable: {error.msg}")
    if prelude is not None:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {"source": prelude}
        )
    driver.get(INTERFACE.resolve().as_uri())
    return driver


def _wait_for_export(download_dir: Path) -> Path:
    deadline = monotonic() + 5
    while monotonic() < deadline:
        exports = list(download_dir.glob("biblebench-pass-one-draft-*.json"))
        if exports:
            return exports[0]
        sleep(0.05)
    raise AssertionError("browser export did not complete")


def test_real_browser_marks_impossible_utc_date_invalid(tmp_path: Path) -> None:
    driver = _open_interface(tmp_path)
    try:
        reviewed_at = driver.find_element(By.ID, "reviewed-at")
        reviewed_at.send_keys("2026-02-30T17:00:00Z")

        warnings = driver.find_element(By.ID, "warnings").text
        assert "owner_reviewed_at is invalid" in warnings
    finally:
        driver.quit()


@pytest.mark.parametrize(
    ("prelude", "error_name"),
    [
        (
            "Object.defineProperty(window,'localStorage',{configurable:true,"
            "get(){return {getItem(){throw new DOMException('blocked','SecurityError');},"
            "setItem(){throw new DOMException('blocked','SecurityError');}};}});",
            "SecurityError",
        ),
        (
            "Object.defineProperty(window,'localStorage',{configurable:true,"
            "get(){return {getItem(){return null;},setItem(){throw new DOMException("
            "'full','QuotaExceededError');}};}});",
            "QuotaExceededError",
        ),
    ],
)
def test_real_browser_exports_when_local_storage_fails(
    tmp_path: Path, prelude: str, error_name: str
) -> None:
    driver = _open_interface(tmp_path, prelude)
    try:
        driver.find_element(By.ID, "export-draft").click()

        status = driver.find_element(By.ID, "storage-status")
        assert status.text == "Storage unavailable; using in-memory draft only."
        assert status.get_attribute("title") == error_name
        exported = json.loads(_wait_for_export(tmp_path).read_text(encoding="utf-8"))
        assert exported["draft_version"] == "biblebench-pass-one-judge-draft-v1"
        assert len(exported["records"]) == 48
    finally:
        driver.quit()
