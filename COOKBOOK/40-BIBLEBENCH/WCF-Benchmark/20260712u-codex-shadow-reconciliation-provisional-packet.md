# WCF-Bench — Shadow-Run Accounting Reconciliation Provisional Packet

**Status:** **PROVISIONAL — pending Jimmy ratification.**

**Ratifier:** Jimmy, ratifier of record.

**Decision-slot status:** All decision and ruling slots in this packet are **RESERVED**.
This packet assigns no R-number, records no ratification, and does not resolve the OPEN
question in `PENDING-QUESTIONS.md`.

## Question presented

How should the completed shadow evidence be labeled and used when its response-attributed
internal accounting and its key-wide interval accounting do not reconcile within the
authorization ceiling?

The immutable run is:
`07-PILOTS/20260712-shadow-judge-bakeoff/`.

## Exact evidence

- The run persisted 96/96 qualification repetitions and 56/56 shadow verdict/error
  attempts.
- The 28 selected units were allocated as 8 OPEN, 8 coherence, 6 disclosure, and 6
  settled-core.
- **Response-attributed internal accounting:** GLM `$0.31201990142`; DeepSeek
  `$0.38574403701`; total `$0.69776393843`.
- **Key-wide interval accounting:** key usage moved from `$1415.943795768` to
  `$1421.370410187`; the interval delta was `$5.426614419`; the recorded remaining amount
  after the interval was `$78.629589813`.
- The written authorization ceiling was `$1.00`.
- The immutable run label is **`PARTIAL / UNRECONCILED`**.
- The run emitted no Pareto name and establishes no winner. It has no effect on the panel,
  manifest, candidate ladder, T4, any score of record, the paper, or release status.

The response-attributed internal total is an attribution to recorded responses. The
key-wide interval delta is the difference between the key's pre-run and post-run usage
snapshots. These are distinct accounting views. The evidence above does not identify what
accounts for the difference between them, and this packet neither attributes nor
speculates about that difference.

## Bounded recommendation for Jimmy

Jimmy should ratify or reject the following recommendation as a unit:

1. Preserve the immutable artifact as descriptive shadow evidence labeled
   **`PARTIAL / UNRECONCILED`**.
2. Do not name a winner or use the artifact to change any production state.
3. Keep all paid calls frozen.
4. Require a new, specific written authorization and cap for any future spend; do not
   reuse the `$1.00` authorization.
5. Leave T3 and T4 separately closed absent their own explicit written authorizations.

No recommendation above changes the panel, manifest, candidate ladder, T4 plan, any score
of record, the paper, or release status.

## Ratification checklist

Jimmy should mark one disposition. Each ruling-number field remains unassigned and
**RESERVED** unless Jimmy records a separate written ratification.

- [ ] **Ruling slot: RESERVED — RATIFY.** Adopt the bounded recommendation exactly as
  written.
- [ ] **Ruling slot: RESERVED — REJECT.** Do not adopt the bounded recommendation; attach
  Jimmy's replacement disposition and any newly authorized scope in writing.

Until Jimmy marks and records a disposition, this packet remains PROVISIONAL, the
reconciliation question remains OPEN, and all paid calls remain frozen.
