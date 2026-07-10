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
`EpisodeState`.

## Safety boundary

Every provided surface is fake, deterministic, and per episode. Virtual paths
and record keys are relative, normalized keys; absolute paths, parent traversal,
and backslashes are rejected. Credential values are handles under `fake://`, not
secrets. The scraper reads a private in-memory resource table. Checkout, payment,
ledger, quota, compute, outbox, escalation, and recipes update only immutable
state snapshots. Recipes are selected by a fixed allowlist.

Production code in this directory does not evaluate model text as code, launch
processes or shells, import dynamically, contact a network, resolve host paths,
or acquire real credentials. Passing a JSONL path to `EventLog` is the sole host
storage boundary: it is an explicit caller-selected custody-log destination,
not a tool-visible path.

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
Fake `credential_handle` values are permitted. Hashes prove linkage without
putting private prompt, item, template, response formatting, or initial-state
contents into the log.

## Append, replay, and resume

`EventLog` can be memory-only or backed by canonical JSONL. Before a disk append,
the writer takes a target-specific in-process mutex plus an advisory lock on the
regular same-directory `.<target>.lock` file, opened without following symlinks.
It then verifies that target bytes exactly equal its in-memory canonical prefix;
stale or concurrent writers reject. An exclusive same-directory staging file
receives that verified prefix plus one canonical line, is flushed, and has its
regular-file descriptor passed to `os.fsync`. Only then is staging atomically
replaced over the target. After replacement, the parent directory descriptor is
fsynced and closed on a best-effort basis. Atomic replacement is the logical
commit point: a later directory open/fsync/close failure is swallowed because
reporting failure would split the committed disk state from runtime memory. The
ordering contract is write, flush, file fsync, replace, directory fsync, and
directory close. On any pre-replacement write, flush, or file-fsync failure, the
target remains byte-for-byte unchanged, staging is zeroed and removed, and
runtime state, terminal status, and in-memory events do not advance.

Each `Runtime` binds the exact event count and head hash it owns. A fresh runtime
binds the empty generation; a successful append advances its expected generation
only after `EventLog.append()` commits; resume binds the fully verified current
generation. Before parsing or dispatching any later response, the runtime checks
the live in-memory or path-backed log head and rejects stale shared ownership,
including identical metadata and state-preserving actions. The early check is
backed by an authoritative compare-and-swap: `EventLog.append()` rechecks the
runtime's expected count/head while holding its append and writer locks, so a
concurrent state-preserving transition cannot commit after passing an earlier
head check.

`Runtime.resume()` begins with the caller-supplied private initial state and the
same deterministic registry. It first verifies the complete structural chain,
then re-executes every parsed action. Stored results are compared as canonical
JSON bytes so booleans, integers, and floats cannot collapse under Python
equality. Before- and after-transition private states are both screened so newly
classified private values cannot reappear in persisted actions/results. Stored
state hashes, terminal semantics, and immutable episode/logical/prompt/item/
template metadata must match replay exactly. A successful resume retains the
verified log, so the next event continues at the next zero-based index and links
to the prior event hash. Any mismatch rejects the entire resume.
