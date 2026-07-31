"""Session-19 judge-gap triage: build BLIND raw-materials audit packets for the
90-cell stratified sample in /tmp/wcf-s19-triage-meta/SELECTION.json.

Packets are RAW MATERIALS ONLY (stem + authoritative item key/rubric + full SUT
response) -- NO scores, NO opus/Sol verdicts, NO strict-v2 template, NO GATE-mode
verdict text. The auditor's job is to characterize *why* opus and Sol diverged
on this cell (garnish idiom present? genuine substantive disagreement? ambiguous
key? other?), not to re-grade it. Any exposure to the existing scores or gap
direction would anchor the auditor -- anti-leakage discipline per the
dispatching-parallel-agents skill, mirroring the s16 A1/B3 pattern.

Output: /tmp/wcf-s19-triage/packets/<ITEM>__<sut>__ep<N>.md (repo-external,
per anti-leakage discipline -- may not survive a session boundary, regenerate
from SELECTION.json if needed; deterministic, idempotent, no API calls).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WCF_ROOT / "src"))

from wcf_tasks import render_standard, record_to_sample  # noqa: E402
from wcf_grading import defang_wcf_markers  # noqa: E402

META = Path("/tmp/wcf-s19-triage-meta")
OUT = Path("/tmp/wcf-s19-triage/packets")
RESP_DIR = WCF_ROOT / "logs" / "20260725-session17-fullrun"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    picks = json.loads((META / "SELECTION.json").read_text())["picks"]

    bank = {}
    for line in (WCF_ROOT / "data" / "wcf_main.jsonl").read_text().splitlines():
        r = json.loads(line)
        bank[r["id"]] = r

    # responses are sharded responses-<sut>-ep<N>.jsonl; load only the (sut, epoch)
    # shards actually needed by the sample
    needed_shards = {(p["sut"], p["epoch"]) for p in picks}
    completions = {}  # (item, sut, epoch) -> completion text
    for sut, epoch in needed_shards:
        path = RESP_DIR / f"responses-{sut}-ep{epoch}.jsonl"
        for line in path.read_text().splitlines():
            r = json.loads(line)
            completions[(r["id"], sut, str(epoch))] = r["completion"]

    written = 0
    for p in picks:
        item_id, sut, epoch = p["item"], p["sut"], p["epoch"]
        rec = bank[item_id]
        sample = record_to_sample(rec)
        completion = completions.get((item_id, sut, epoch))
        if completion is None:
            print(f"MISSING completion for {item_id}__{sut}__ep{epoch}", file=sys.stderr)
            continue
        packet = (
            "# Judge-gap triage audit packet\n\n"
            "## THE REQUEST GIVEN TO THE MODEL\n\n"
            f"{sample.input}\n\n"
            "## THE ITEM KEY AND RUBRIC (authoritative)\n\n"
            f"{render_standard(rec)}\n\n"
            "## THE MODEL'S FULL RESPONSE\n\n"
            f"{defang_wcf_markers(completion)}\n"
        )
        out_path = OUT / f"{item_id}__{sut}__ep{epoch}.md"
        out_path.write_text(packet)
        written += 1

    print(f"wrote {written}/{len(picks)} audit packets to {OUT}")


if __name__ == "__main__":
    main()
