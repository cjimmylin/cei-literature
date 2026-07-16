# WCF-Bench Pilot 2 Session-66 quality relative/absolute lease stop

**Date:** 2026-07-15

**Permanent label:** **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Outcome

Jimmy authorized the exact LEASE IDENTITY FIX. Fresh-agent TDD changed the lease identity
from symlink-resolving `Path.resolve()` to the normalized absolute lexical run path and added
the exact two-process symlink-parent regression. The regression moved from RED (contender
acquired) to GREEN; the full custody file passed 13/13. Fresh named specification review
passed. Fresh quality review then found one new P1 within its registered relative-versus-
absolute normalization check. The automatic stop fired before credential/private-balance
access, OAuth, inference, empirical run-directory creation, or spend.

## New P1 — macOS `/var` and `/private/var` spellings split the lease

`os.path.abspath()` does not canonicalize the normal macOS `/var` → `/private/var` filesystem
alias. The quality reviewer reproduced:

1. a holder launched from a `/var/tmp/...` fixture cwd with relative `late-link/run` before
   the parent existed, yielding a `/private/var/tmp/...` lexical absolute path;
2. the parent appearing as a symlink; and
3. a contender using the equivalent absolute `/var/tmp/.../late-link/run` spelling.

The two spellings produced different lease hashes, and the contender acquired while the
holder remained active. This defeats the process-exclusive boundary protecting the strict
cumulative `$28.13` cap and append-only evidence custody.

## Smallest bounded correction

An exact **TOP-LEVEL ALIAS FIX** would canonicalize only the stable top-level filesystem
component (for example `/var` → `/private/var`) before hashing, while leaving all deeper
run-path components lexical so later ordinary-directory or symlink creation cannot move the
identity. Add the exact relative-holder/equivalent-absolute-contender regression, then run
fresh named-only specification and quality reviews. No live/private step may begin before
both PASS.

## Owner gate

Jimmy chooses exact **TOP-LEVEL ALIAS FIX** or **DEFER**. The existing strict cumulative
`$28.13` authority remains recorded, paused, unconsumed, and amount-sufficient. If the exact
bounded correction and both named reviews pass, it resumes automatically at the private-
balance gate without a new amount-specific ruling. Any further new P1 or failed registered
gate stops.

Session live calls/spend: zero / `$0.00`. Empirical execution remains 0%.

## Verification note

The exact lease gate passed 3/3 and the complete custody test file passed 13/13. A fresh
901-test full-suite attempt was not green because the host temporary volume exhausted its
remaining space: pytest finished with 839 passed, 2 failed, and 60 setup errors, all under
`OSError: [Errno 28] No space left on device` or the resulting inability to create a
temporary directory. The isolated first failing live-seam test passed when rerun. This is
recorded as an environmental verification block, not represented as a code PASS.
