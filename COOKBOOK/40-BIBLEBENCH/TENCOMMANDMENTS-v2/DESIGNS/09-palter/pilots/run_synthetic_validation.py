"""Write only aggregate canonical PALTER synthetic validation artifacts."""

import argparse
import hashlib
from pathlib import Path
import sys

PALTER_ROOT = Path(__file__).resolve().parent.parent
if str(PALTER_ROOT) not in sys.path:
    sys.path.insert(0, str(PALTER_ROOT))

from analysis.synthetic_validation import (  # noqa: E402
    canonical_result_bytes,
    render_report,
    run_synthetic_validation,
)
from palter_hashing import canonical_json  # noqa: E402


DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "20260711-synthetic-validation-r1"


def write_validation(output_dir=DEFAULT_OUTPUT_DIR):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    result = run_synthetic_validation()
    result_bytes = canonical_result_bytes(result)
    report_bytes = render_report(result).encode("utf-8")
    manifest = {
        "schema_version": "palter-synthetic-artifact-manifest-v1",
        "fixture_only": True,
        "external_calls": 0,
        "cost_usd": 0.0,
        "artifacts": {
            "synthetic_result": {
                "path": "synthetic-result.json",
                "sha256": hashlib.sha256(result_bytes).hexdigest(),
            },
            "report": {
                "path": "report.md",
                "sha256": hashlib.sha256(report_bytes).hexdigest(),
            },
        },
        "input_bank_manifest_sha256": result["input_hashes"]["manifest"],
    }
    manifest_bytes = canonical_json(manifest).encode("utf-8") + b"\n"
    (output_dir / "synthetic-result.json").write_bytes(result_bytes)
    (output_dir / "report.md").write_bytes(report_bytes)
    (output_dir / "manifest.json").write_bytes(manifest_bytes)
    return {
        "manifest": manifest,
        "paths": {
            "synthetic_result": output_dir / "synthetic-result.json",
            "report": output_dir / "report.md",
            "manifest": output_dir / "manifest.json",
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    written = write_validation(args.output_dir)
    print(canonical_json(written["manifest"]))


__all__ = ["write_validation"]
