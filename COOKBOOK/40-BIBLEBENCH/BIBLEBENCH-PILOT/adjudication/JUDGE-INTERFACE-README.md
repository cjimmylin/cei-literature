# BibleBench Pass-One Judge Interface

`judge-interface.html` is a deterministic, self-contained interface for the
frozen 48-record provisional-gold packet. It opens directly from local disk and
does not need a server. Its Content Security Policy denies network connections,
external media and code, form submission, and embedding.

The interface is a draft-authoring aid only. It cannot finalize gold, write the
authoritative YAML packet, expose the blinded repeat, access credentials, or
make provider calls.

## Open and review

1. Open `judge-interface.html` in a modern browser from the local filesystem.
2. Confirm the displayed source SHA-256 is
   `289228c05900e520ccd361e4d605670f34992a853402c2cd8052f90e0b854166`.
3. Review one episode at a time. Module and role filters change navigation only;
   they do not change the 48-record draft.
4. Enter both track decisions and rationales, confidence, contestability, the
   stable judge ID, a UTC review time, and the issue array. Enter `[]` only after
   explicitly determining that the record has no issue entries.
5. Treat the displayed record decision as a mechanical roll-up of the two owner
   track entries. It is not a recommendation.
6. Resolve mechanical warnings. Warnings identify missing, invalid, or
   contradictory fields without recommending a substantive judgment.

Use Previous/Next or, when focus is outside an editor, Left/Right Arrow or
`k`/`j`. The record-index box jumps to an overall packet position.

## Draft custody

The page autosaves under a browser-local key namespaced by the exact packet
SHA-256. Browser storage is convenience state, not authoritative custody. Use
**Export JSON** regularly and retain exported files according to the project's
owner-review custody procedure.

**Import JSON** accepts only the closed draft shape, the same source hash, and
exactly the same 48 unique episode IDs. Import/export is lossless after JSON
normalization. An import never changes the frozen source content embedded in
the page. Imported records are canonicalized to frozen source order by episode
ID before display. Partial issue-editor keystrokes are stored verbatim through
navigation, reload, export, and import while the record remains
`DRAFT_INCOMPLETE`.

- `DRAFT_INCOMPLETE` means at least one record is missing a required field or
  has a mechanical contradiction.
- `DRAFT_COMPLETE` means all 48 draft records pass the interface's mechanical
  checks. It does not mean approval, finalization, multi-judge validation, or
  Christian consensus.

The exported draft contains only its source binding, episode IDs, derived draft
status, and owner fields. Its closed schema is
`../schemas/judge-draft.schema.json`.

## Existing finalizer boundary

The Python module can normalize an exported draft and merge a mechanically
complete draft into an in-memory copy of the frozen packet. That copy is then
checked by `validate_review_packet(...)`, including the registered roll-up,
confidence, contestability, issue-priority, routing, provenance, and payload
hash rules. The interface module does not write the merged packet.

Freezing the reviewed packet remains a separate authorized custodian step under
`PROVISIONAL-GOLD-JUDGE-GUIDE.md` and the existing fail-closed finalizer. The
later blinded repeat remains separate and hidden until pass one is frozen.

## Custodian-only bridge

After the browser export reaches `DRAFT_COMPLETE`, an authorized custodian may
emit the reviewed-packet input expected by the existing finalizer:

```bash
PYTHONPATH=src /opt/homebrew/bin/python3 -m biblebench_pilot.judge_ui \
  --draft-json /absolute/path/to/exported-owner-draft.json \
  --reviewed-packet-output /absolute/path/to/custodian-reviewed-input.yaml
```

The bridge reloads the exact pending source packet, binds its byte-level SHA-256,
canonicalizes records to source order by episode ID, validates the closed draft,
merges owner fields in memory, and runs `validate_review_packet(...)`. It then
writes a new mode-`0600` reviewed-packet input using exclusive-create semantics.
It refuses incomplete or contradictory drafts and refuses to overwrite any
existing output.

This bridge does not finalize gold and does not modify
`provisional-gold-review.yaml`. The browser contains no bridge or filesystem
write path. Finalization remains a separate custodian action using the existing
`finalize_review_packet(...)` procedure, including its judge object, completion
timestamp, immutable output, and manifest checks.

## Deterministic rebuild

From `BIBLEBENCH-PILOT/`:

```bash
PYTHONPATH=src /opt/homebrew/bin/python3 -m biblebench_pilot.judge_ui
```

The builder validates the frozen packet against the authored banks, refuses any
packet containing precompleted owner state, escapes embedded JSON against
script termination, and rewrites only `adjudication/judge-interface.html`.
Given identical packet, schema, and builder bytes, repeated builds are
byte-identical.
