# Shared custody stack

This directory is the one custody implementation for Ten Commandments benchmark
work. The v1 **PROVENANCE** custody surfaces are authoritative. The v2 **SKIM**
design extends those surfaces through registered deterministic tool schemas and
handlers; it does not own a parallel harness. Future **PROXY** and **SELAH** work
may add schemas, pure handlers, provenance fields through a new schema version,
or replay checks at the same registry/runtime boundaries. Those future designs
are named extension seams only and are not implemented here.

## Authoritative surface map

| Required custody surface | Handler family in `build_default_registry()` |
| --- | --- |
| Virtual filesystem | `virtual_fs.*` |
| Virtual records | `records.*` |
| Fake credential handles | `credentials.*` |
| Catalog and pricing | `catalog.*`, `pricing.*` |
| Checkout and payment | `checkout.*`, `payment.*` |
| Ledger | `ledger.*` |
| Quota | `quota.*` |
| Compute scheduler | `compute.*` |
| Outbox and message | `outbox.*` |
| Scraper | `scraper.*` |
| Operator escalation | `operator.*` |
| Allowlisted recipes | `recipe.*` |
| Immutable custody evidence | `EventLog`, `verify_chain()`, and `Runtime.resume()` |

The default registry is deliberately small. Tests and benchmark designs can
build another `ToolRegistry` from explicit exact argument schemas and pure
deterministic handlers. A registered action may simulate ethically bad behavior
when a benchmark needs it, but its effects remain inside that episode's private
`EpisodeState` only when its handler honors that contract. A `Runtime` binds a
sealed snapshot of the registry's tool names, schemas, and callable references;
later registration on the source registry cannot change that runtime.

## Safety boundary

Every provided surface is fake, deterministic, and per episode. Virtual paths
and record keys are relative, normalized keys; absolute paths, parent traversal,
and backslashes are rejected. Credential values are handles under `fake://`, not
secrets. The scraper reads a private in-memory resource table. Checkout, payment,
ledger, quota, compute, outbox, escalation, and recipes update only immutable
state snapshots. Recipes are selected by a fixed allowlist.

The provided default registry does not evaluate model text as code, launch
processes or shells, import dynamically, contact a network, resolve tool-supplied
host paths, or acquire real credentials. Passing a JSONL path to `EventLog` is
the sole built-in host storage boundary: it is an explicit caller-selected
custody-log destination, not a tool-visible path. Construction binds that
destination to an absolute path
under its then-existing canonical parent. The target must be absent or an exact
regular single-link file; final-component symlinks, hardlinks, devices, FIFOs,
directories, and a changed parent-directory identity fail closed.

Custom handlers registered by callers are trusted in-process Python. This API
cannot capability-confine them: they may access the host, launch processes,
contact networks, mutate their own closures, or otherwise cause side effects.
Registry snapshots retain the same callable objects; they do not freeze code or
closure state, prove purity/determinism, or attest callback identity. Handler
state/action inputs and returned transitions are defensively detached for
custody integrity, but that is not a general Python sandbox. Replay invokes the
trusted callbacks again.

## Exact protocol and schemas

An accepted model response is exactly one JSON object with the fields `kind`,
`tool`, and `arguments`; `kind` is exactly `act`. Parsing rejects duplicate keys
at every depth, trailing material, nonstandard constants, nonfinite numbers,
unsafe JSON integers, custom numeric/container types, missing fields, and extra
fields. Registry dispatch then rejects unknown tools and any missing, unknown,
or wrongly typed argument before calling a handler.

`EpisodeState`, `Action`, `ToolResult`, `Transition`, and `Event` are frozen
dataclasses. Mutable JSON inputs are recursively copied into deterministic
immutable values. Public JSON uses UTF-8, sorted keys, compact separators, and
no nonfinite values. JSON integers are limited to the IEEE-754 safe range.

Events are zero-indexed. The first `previous_event_sha256` is 64 zeroes. Every
event stores state-before and state-after hashes and is itself SHA-256 hashed
over every canonical event field except `event_sha256`. `verify_chain()` is the
non-throwing structural API: it returns `False` on any malformed index, root,
link, schema, or hash. Constructors, log loading, dispatch, and replay use typed
validation exceptions and fail closed.

## Private and persisted data

The caller supplies the private initial `EpisodeState`; it is never written into
an event. Full prompts, raw model responses, API keys, and credential secrets
must remain private. Persisted events contain only:

- schema, event, episode, and logical identifiers;
- previous-event and before/after-state SHA-256 values;
- the validated parsed action and deterministic parsed tool result;
- the SHA-256 of the exact raw response bytes;
- prompt, item, and template SHA-256 values;
- terminal status and the event SHA-256.

Fields named `prompt`, `model_prompt`, `api_key`, `credential`, or
`credential_secret` are rejected recursively from persisted action/result data.
Fake `credential_handle` values are permitted. The runtime also performs
best-effort literal screening against values beneath those private state fields:
typed numeric leaves require exact type/value equality, strings require whole
equality or a substring of at least four characters, and ordered persisted
string-value concatenation catches simple split fragments. Structural keys,
null, and booleans are not secret payload leaves. This is not information-flow
or taint security: transformed, encoded, reordered, or otherwise derived
disclosures can evade the check, and custom handlers remain trusted. Hashes
prove linkage without putting private prompt, item, template, response
formatting, or initial-state contents into the log.

## Append, replay, and resume

`EventLog` can be memory-only or backed by canonical JSONL. Disk operations use
the bound canonical parent through directory-relative descriptors. Target reads
do not follow the final component and recheck the regular/single-link policy at
construction and under every writer guard. Parent-directory symlink aliases
therefore share one in-process mutex, regular single-link sidecar lock, staging
namespace, target, and cross-process advisory lock.

Before append, the writer verifies that target bytes exactly equal its in-memory
canonical prefix; stale or concurrent writers reject. An exclusive
same-directory staging file receives that prefix plus one canonical line, is
flushed, and is file-fsynced before directory-relative atomic replacement. The
ordering contract is write, flush, file fsync, replace, best-effort directory
fsync, and close. If replacement raises after an ambiguous outcome, the writer
classifies the safely reopened target while still guarded: candidate bytes mean
committed, prefix bytes mean precommit, and any third value fails closed without
truncating the target. A committed replace interruption advances EventLog memory;
`Runtime` reconciles its state and then reraises the original interruption.
Precommit interruptions preserve the prior target and are reraised after safe
owned-staging cleanup. Definite-postcommit stream, directory-durability, lock
release, and descriptor cleanup interruptions are best effort and swallowed so
they cannot report failure after custody evidence has committed.

Each `Runtime` binds the exact event count and head hash it owns. A fresh runtime
binds the empty generation; a successful append advances its expected generation
only after `EventLog.append()` commits; resume binds the fully verified current
generation. Before parsing or dispatching any later response, the runtime checks
the live in-memory or path-backed log head and rejects stale shared ownership,
including identical metadata and state-preserving actions. The early check is
backed by an authoritative compare-and-swap: `EventLog.append()` rechecks the
runtime's expected count/head while holding its append and writer locks, so a
concurrent state-preserving transition cannot commit after passing an earlier
head check. Each `accept()` snapshots its starting state, generation, and
provenance before that check; handler execution, state hashes, event index and
link, and the append CAS all use that same immutable snapshot. Only a successful
append swaps the runtime state and advances its expected generation. A short
per-runtime publication lock makes each entry snapshot, post-append state/
terminal/generation swap, and public state or terminal read coherent. Parsing
and handler execution remain outside that lock, so stale concurrent work still
reaches the event-log generation CAS and rejects without being rebased. State,
terminal status, event count, and head hash live in one frozen runtime snapshot,
published by one reference assignment. If append committed but raised, or that
assignment was interrupted after taking effect, exact-head reconciliation makes
the runtime snapshot match its own committed event before reraising.

`Runtime.resume()` begins with the caller-supplied private initial state and the
same bound registry snapshot. It first verifies the complete structural chain,
then re-executes every parsed action through detached handler inputs and outputs.
Stored results are compared as canonical
JSON bytes so booleans, integers, and floats cannot collapse under Python
equality. Before- and after-transition private states are both screened so newly
classified private values cannot reappear in persisted actions/results. Stored
state hashes, terminal semantics, and immutable episode/logical/prompt/item/
template metadata must match replay exactly. A successful resume retains the
verified log, so the next event continues at the next zero-based index and links
to the prior event hash. Any mismatch rejects the entire resume.
