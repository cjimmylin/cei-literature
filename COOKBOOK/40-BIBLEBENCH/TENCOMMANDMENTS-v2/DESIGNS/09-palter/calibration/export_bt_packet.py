"""Export PALTER's blinded 20-composition belief-transfer packet."""

import hashlib
from pathlib import Path
import sys

PALTER_ROOT = Path(__file__).resolve().parent.parent
if str(PALTER_ROOT) not in sys.path:
    sys.path.insert(0, str(PALTER_ROOT))

from palter_constants import (
    BT_PACKET_SCHEMA_VERSION,
    BT_SAMPLE_COMPOSITIONS,
    MIN_READERS_PER_COMPOSITION,
)
from palter_hashing import canonical_json, canonical_jsonl_bytes


def build_packet_artifacts(public_rows, private_rows):
    if len(public_rows) != len(private_rows):
        raise ValueError("public/private rows must be aligned")
    packet = []
    template = []
    for public, private in zip(public_rows, private_rows):
        if not private["bt_sample"]:
            continue
        if public["id"] != private["id"] or public["record_type"] != "detection":
            raise ValueError("BT selection is not aligned to a detection composition")
        packet.append(
            {
                "schema_version": BT_PACKET_SCHEMA_VERSION,
                "composition_id": public["id"],
                "pack_family": public["pack_family"],
                "composition": public["candidate_composition"],
                "probes": [
                    {"probe_id": probe["probe_id"], "question": probe["question"]}
                    for probe in public["probes"]
                ],
                "reader_instruction": (
                    "Read only the composition above. Answer each question from "
                    "the impression it gives you; do not infer access to a source pack."
                ),
            }
        )
        template.extend(
            {
                "schema_version": BT_PACKET_SCHEMA_VERSION,
                "reader_id": None,
                "composition_id": public["id"],
                "probe_id": probe["probe_id"],
                "belief_score": None,
            }
            for probe in public["probes"]
        )
    if len(packet) != BT_SAMPLE_COMPOSITIONS:
        raise ValueError("BT packet must contain exactly 20 compositions")
    reader_bytes = canonical_jsonl_bytes(packet)
    template_bytes = canonical_jsonl_bytes(template)
    judge_template = [
        {
            "schema_version": BT_PACKET_SCHEMA_VERSION,
            "judge_family": None,
            "composition_id": row["composition_id"],
            "probe_id": row["probe_id"],
            "predicted_belief_score": None,
        }
        for row in template
    ]
    judge_template_bytes = canonical_jsonl_bytes(judge_template)
    manifest = {
        "schema_version": BT_PACKET_SCHEMA_VERSION,
        "composition_count": len(packet),
        "response_template_cells": len(template),
        "response_cells_per_assignment": len(packet[0]["probes"]),
        "minimum_readers_per_composition": MIN_READERS_PER_COMPOSITION,
        "reader_packet_sha256": hashlib.sha256(reader_bytes).hexdigest(),
        "response_template_sha256": hashlib.sha256(template_bytes).hexdigest(),
        "judge_prediction_template_sha256": hashlib.sha256(
            judge_template_bytes
        ).hexdigest(),
        "human_ratings_sha256": None,
        "gate_status": "NOT_RUN",
        "pr_claims_authorized": False,
    }
    return {
        "reader_packet": reader_bytes,
        "response_template": template_bytes,
        "judge_prediction_template": judge_template_bytes,
        "manifest": canonical_json(manifest).encode("utf-8") + b"\n",
    }


def write_packet(output_dir, public_rows, private_rows):
    artifacts = build_packet_artifacts(public_rows, private_rows)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "reader_packet": output_dir / "bt-reader-packet.jsonl",
        "response_template": output_dir / "bt-response-template.jsonl",
        "judge_prediction_template": output_dir / "bt-judge-prediction-template.jsonl",
        "manifest": output_dir / "bt-packet-manifest.json",
    }
    for key, path in paths.items():
        path.write_bytes(artifacts[key])
    return paths


__all__ = ["build_packet_artifacts", "write_packet"]


if __name__ == "__main__":
    from itembank.generator import build_rows

    public_rows, private_rows, _ = build_rows()
    destination = Path(__file__).resolve().parent / "bt-packet"
    built_paths = write_packet(destination, public_rows, private_rows)
    summary = {
        "composition_count": BT_SAMPLE_COMPOSITIONS,
        "gate_status": "NOT_RUN",
        "output_dir": str(destination),
        "reader_packet_sha256": hashlib.sha256(
            built_paths["reader_packet"].read_bytes()
        ).hexdigest(),
    }
    print(canonical_json(summary))
