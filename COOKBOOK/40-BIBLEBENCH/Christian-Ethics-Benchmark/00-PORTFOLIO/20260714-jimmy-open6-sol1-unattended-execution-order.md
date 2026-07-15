# Jimmy order — WALKWORTHY OPEN6-SOL1 unattended execution

**Date:** 2026-07-14

**Owner:** Jimmy Lin

**Status:** AUTHORIZED in direct chat

## Execution order

Proceed unattended through the entire registered OPEN6-SOL1 pilot in this order:

1. finish all offline tests and independent P1 reviews;
2. freeze the immutable manifest and same-roster/same-ceiling catalog snapshot;
3. run the complete free fake-backend dry run;
4. run promoted live canaries;
5. if all required canaries pass, run the full runnable-PUBLIC SUT surface;
6. complete only missing Sol routing and single-judge work;
7. produce descriptive analysis, the standalone supplement/PDF, and the
   claims-conformance checks;
8. update the dashboard and write a dated handoff;
9. run final verification, commit explicit WALKWORTHY paths, fast-forward
   integrate, and push.

## Spend controls

- Expected OpenRouter spend: approximately **$11.10**.
- Soft checkpoint: **$15.00** booked spend.
- At and after the soft checkpoint, continue automatically only when booked spend
  plus a conservative registered-ceiling projection for every remaining nominal
  call and remaining replay reserve is at most **$23.00**.
- Absolute hard NTE: **$25.00**. No request may start if booked plus in-flight
  reservation plus the next request's registered reservation could exceed it.

The conservative soft-checkpoint projection is mechanical: for every remaining
nominal call, use that exact model's registered 24,000-input-token envelope and
2,048-output-token cap at its registered provider price ceilings; add the same
registered maximum for each unused replay-reserve slot. This deliberately
overestimates rather than infers future response length.

## Resume, missingness, and stops

Never rerun valid substantive output. After temporary provider or OAuth recovery,
resume only missing work. After one logical key exhausts its one byte-identical
replay, record permanent explicit missingness under the original denominator and
continue unaffected registered keys, models, and batches.

Stop the affected execution and document once on:

- projected or reserved OpenRouter spend above the authorized limits;
- call- or turn-cap breach;
- required offline or canary failure;
- exact-model unavailability under the existing ceiling;
- OAuth quota exhaustion;
- a second custody, returned-model, reported-cost, hash, or schema failure;
- any unregistered behavior.

The stop checkpoint must list completed and missing logical keys, spend/reserve and
call/turn counts, exact stop reason, and safest next command.

## Boundaries retained

Exact roster, exact `gpt-5.6-sol` OAuth roles, concurrency at most two, payloads,
prompts, output caps, price ceilings, replay/call/turn limits, PUBLIC denominators,
and custody requirements remain unchanged. No substitution, extra replay,
concurrency increase, prompt/item/key/denominator edit, HOLDOUT access, scale-up,
credit purchase, frozen-O5 change, O5 verdict, public release, or workaround is
authorized.

This order supplements the three earlier 2026-07-14 Jimmy authorization memos and
does not change their descriptive-only claims boundary.
