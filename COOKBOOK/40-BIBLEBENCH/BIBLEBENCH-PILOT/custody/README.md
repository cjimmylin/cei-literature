# Private cue/evidence custody

This directory is for authenticated private custody manifests. A manifest binds
each frozen C0/C1/C2 primary logical call to the one probe relationship derived
from the frozen `Schedule`, plus the supplied exact evidence artifact identifier
and evidence-bundle SHA-256.

The geometry is deliberately **144 pair-scoped rows**, not 48 schedule-bundle
rows. Each of the 48 scheduler `bundle_id` values groups three distinct
C0/C1/C2 primary/probe pairs, and each pair has its own evidence object and
custody row. A scheduler bundle is grouping metadata; it is not one shared
evidence object.

## Hard surface boundary

`PRIVATE_CUSTODY_ONLY_PROHIBITED_FROM_MODEL_AND_JUDGE_SURFACES` is an access and
data-flow rule, not descriptive metadata. Never place a custody manifest, a
custody row, its receipt, or any extracted custody field into:

- a tested-model request or response envelope;
- a forecast, primary, or probe payload;
- a human or model judge packet, prompt, rubric, or evidence envelope; or
- any public result surface that could reveal actor, cue, or pairing metadata.

Keep manifests in a private operator-only location. Downstream analysis may use
them only after model execution and judging surfaces are isolated from the
manifest.

Every authenticated manifest also carries top-level `private: true`. The shared
actor/model and judge envelope firewalls both forbid that key, so attempting to
embed the manifest at either boundary fails mechanically.

## Exact inventory contract

Call
`build_cue_custody_manifest(schedule, evidence_inventory, evidence_root=root)`
with the frozen `Schedule`, one explicit private evidence-root `Path`, and a
tuple containing exactly one strict inventory object per primary/probe evidence
bundle. Each object contains:

- `bundle_id`, `actor_id`, `module`, `episode_id`, `role`, and `cue`;
- `primary_logical_call_id` and `probe_logical_call_id`;
- `primary_canonical_request_sha256` and
  `probe_canonical_request_sha256`;
- `evidence_artifact`, a safe relative artifact path or identifier; and
- `evidence_bundle_sha256`, the exact lowercase SHA-256 from the frozen
  evidence bundle.

The caller-supplied relationship fields and evidence hash are assertions, not
pairing or hash authority. The builder validates the frozen schedule, derives
every primary-to-probe relationship from it, and recomputes both canonical
request hashes. It then opens only the 144 declared relative artifact paths
under `evidence_root`, without following symlinks or scanning the root. The root
and traversed directories must be owner-private; evidence files must be private,
regular, single-link files. Each file must contain exactly one strict canonical
JSON object plus its final newline. The builder hashes the canonical object
bytes and requires the inventory's `evidence_bundle_sha256` to match.

Missing, extra, duplicate, nonexistent, noncanonical, symlinked, cross-bundle,
cross-actor, cross-episode, wrong-primary, cue, request-hash, or evidence-hash
changes fail closed. Verification reopens and rehashes every artifact, so
underlying content drift after manifest creation also fails closed.

## Authentication and export

The manifest contains the canonical schedule SHA-256, 144 pair-scoped custody rows,
`manifest_sha256`, and a separately hashed `custody_receipt` that repeats the
manifest hash, schedule hash, row count, private-surface policy, and verified
status. `verify_cue_custody_manifest` recomputes the expected manifest from the
frozen schedule and exact inventory and requires canonical byte equality.

Use
`export_cue_custody_manifest(destination, schedule, evidence_inventory,
evidence_root=root)` for publication. The destination parent must already be a
trusted private directory. Export is canonical JSON, mode `0600`, atomic, and
exclusive-create; an existing target is never overwritten.

## Analysis integration contract

The narrow supported verifier API is:

```python
verify_cue_custody_manifest(
    schedule,
    evidence_inventory,
    manifest,
    evidence_root=root,
) -> VerifiedCueCustody
```

It deterministically revalidates the schedule, exact inventory, authenticated
manifest and receipt, and all evidence objects under the explicit root.
`VerifiedCueCustody` is an immutable summary returned by that verification run.
Its normal constructor is disabled, and there is no public or module-sentinel
construction path. The result binds:

- `manifest_sha256` and `receipt_sha256`;
- `canonical_schedule_sha256`;
- domain-separated `evidence_inventory_sha256`;
- `custody_rows_sha256`, computed from the exact 144 manifest rows; and
- `row_count`.

`VerifiedCueCustody` is **not** a provenance or authorization token. Python
cannot establish object provenance against hostile same-process fabrication.
Consumers MUST rerun `verify_cue_custody_manifest` themselves from the primary
schedule, inventory, manifest/receipt, and evidence root, then use the returned
summary in that same validation flow. Accepting an externally supplied instance,
checking only its type/status, or trusting a caller-asserted `verified` flag is
prohibited.

After rerunning verification, an analysis consumer compares
`custody_rows_sha256` with the canonical hash of the manifest rows and binds its
observation set to those exact logical-call rows. The summary grants no
filesystem access and contains no evidence content.

`tests/fixtures/cue-custody-synthetic.json` is
`SYNTHETIC_VALIDATION_ONLY`. It contains no provider/model output and no
secrets. It must never be cited as pilot evidence.

## Deferred nonblocking issue

P2, deferred: the JSON Schema's Unicode length accounting and the runtime's
UTF-8 byte limits are not identical for some non-ASCII identifiers. Registered
pilot identifiers and artifact paths are ASCII, so this does not alter the
pairing, hashes, evidence custody, or paper claim. Do not expand the pre-live P1
repair to Unicode-compatibility hardening without a separate owner decision.
