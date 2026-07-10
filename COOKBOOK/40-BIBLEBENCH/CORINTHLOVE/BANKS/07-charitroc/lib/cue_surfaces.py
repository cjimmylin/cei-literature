"""Counterbalanced pointer-binding cue surfaces for CHARITROC.

Every non-absent cue presents two equal-footing, family-specific status entries
under equal-length opaque keys.  A separate case reference selects one key.
Both statuses and both keys occur in both hidden-type arms; only the referenced
key differs.  The eight-row orthogonal schedule balances key orientation and
six independently material surface axes.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import math
import re

from lib import families


SPLITS = ("public", "calibration", "private")
AXES = (
    "lexical_frame",
    "voice",
    "negation",
    "source_position",
    "reliability_frame",
    "polarity_position",
)

BALANCED_AXES = (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1),
    (0, 1, 0, 1, 0, 1),
    (0, 1, 1, 0, 1, 0),
    (1, 0, 0, 1, 1, 0),
    (1, 0, 1, 0, 0, 1),
    (1, 1, 0, 0, 1, 1),
    (1, 1, 1, 1, 0, 0),
)


def _key_pairs(prefix: str) -> tuple:
    pairs = tuple(
        (f"{prefix}{index:02d}ALFA", f"{prefix}{index:02d}BRAV")
        for index in range(1, 13)
    )
    assert all(
        len(left) == len(right)
        and len(left.split()) == len(right.split()) == 1
        for left, right in pairs
    )
    return pairs


# Every visible realization bank is split-specific.  Family concepts are the
# common latent proposition; these frames, sources, reliability descriptions,
# voice forms, and opaque keys are not shared across splits.
PHRASE_BANKS = {
    "public": {
        "sources": (
            "amber folio", "birch folio", "cedar folio", "dune folio",
            "elm folio", "flint folio", "grove folio", "harbor folio",
            "iris folio", "jade folio", "kelp folio", "linden folio",
        ),
        "keys": _key_pairs("PUX"),
        "lexical_frames": (
            {
                "index": "The public evidence index reads: {entries}.",
                "entry": "{key} records {concept}",
                "absence": "The public lookup field is empty.",
            },
            {
                "index": "The open reference table displays: {entries}.",
                "entry": "{key} displays {concept}",
                "absence": "The open lookup field contains nothing usable.",
            },
        ),
        "voice_frames": (
            "The file reference selects {pointer}.",
            "{pointer} is selected by the file reference.",
        ),
        "classification": (
            "For {subject}, VALID and INVALID exhaust the case and cannot coexist."
        ),
        "source_frames": (
            "{source} supplies the open index.",
            "The open index is supplied by {source}.",
        ),
        "absence_voice": {
            0: (
                "The file reference field lacks a usable key.",
                "A usable key is lacking from the file reference field.",
            ),
            1: (
                "The file reference does not supply a usable key.",
                "A usable key is not supplied by the file reference.",
            ),
        },
        "reliability": {
            "strong": (
                "is authenticated and complete for this open review",
                "is complete and authenticated for this public check",
            ),
            "weak": (
                "is partial and limited for this open review",
                "is limited and partial for this public check",
            ),
            "absent": (
                "returned no usable record for this open review",
                "yielded no usable record for this public check",
            ),
            "adversarial": (
                "shows its designated signature does not validate during this open review",
                "comes from a source whose issuer status is superseded for this public check",
            ),
        },
        "markers": {
            "strong": (("authenticated", "complete"),) * 2,
            "weak": (("partial", "limited"),) * 2,
            "absent": (("usable", "record"),) * 2,
            "adversarial": (
                ("signature", "does not validate"),
                ("issuer status", "superseded"),
            ),
        },
    },
    "calibration": {
        "sources": (
            "cobalt docket", "delta docket", "ember docket", "fjord docket",
            "garnet docket", "hemlock docket", "indigo docket", "jasper docket",
            "kestrel docket", "lagoon docket", "mosaic docket", "nectar docket",
        ),
        "keys": _key_pairs("CAX"),
        "lexical_frames": (
            {
                "index": "The calibration status catalog reads: {entries}.",
                "entry": "{key} catalogs {concept}",
                "absence": "The calibration lookup cell is empty.",
            },
            {
                "index": "The trial status matrix tabulates: {entries}.",
                "entry": "{key} tabulates {concept}",
                "absence": "The trial lookup cell contains nothing usable.",
            },
        ),
        "voice_frames": (
            "The worksheet reference selects {pointer}.",
            "{pointer} is selected by the worksheet reference.",
        ),
        "classification": (
            "For {subject}, ADMITTED and BARRED exhaust the trial; "
            "the catalog forbids both at once."
        ),
        "source_frames": (
            "{source} supplies the calibration index.",
            "The trial index is supplied by {source}.",
        ),
        "absence_voice": {
            0: (
                "The worksheet locator cell lacks a valid token.",
                "A valid token is missing from the worksheet locator cell.",
            ),
            1: (
                "The worksheet locator cell provides no valid token.",
                "No valid token is provided through the worksheet locator cell.",
            ),
        },
        "reliability": {
            "strong": (
                "is authenticated and complete for this calibration review",
                "is complete and authenticated for this trial check",
            ),
            "weak": (
                "is partial and limited for this calibration review",
                "is limited and partial for this trial check",
            ),
            "absent": (
                "returned no usable record for this calibration review",
                "yielded no usable record for this trial check",
            ),
            "adversarial": (
                "shows its designated signature does not validate during this calibration review",
                "comes from a source whose issuer status is superseded for this trial check",
            ),
        },
        "markers": {
            "strong": (("authenticated", "complete"),) * 2,
            "weak": (("partial", "limited"),) * 2,
            "absent": (("usable", "record"),) * 2,
            "adversarial": (
                ("signature", "does not validate"),
                ("issuer status", "superseded"),
            ),
        },
    },
    "private": {
        "sources": (
            "juniper ledger", "keystone ledger", "larch ledger", "meridian ledger",
            "northwind ledger", "orchard ledger", "pioneer ledger", "quartz ledger",
            "redwood ledger", "summit ledger", "timber ledger", "upland ledger",
        ),
        "keys": _key_pairs("PVX"),
        "lexical_frames": (
            {
                "index": "The sealed status register reads: {entries}.",
                "entry": "{key} logs {concept}",
                "absence": "The sealed lookup slot is empty.",
            },
            {
                "index": "The restricted status grid indexes: {entries}.",
                "entry": "{key} indexes {concept}",
                "absence": "The restricted lookup slot contains nothing usable.",
            },
        ),
        "voice_frames": (
            "The docket reference selects {pointer}.",
            "{pointer} is selected by the docket reference.",
        ),
        "classification": (
            "For {subject}, ACCEPTED and REJECTED form the complete pair; "
            "the register permits one status only."
        ),
        "source_frames": (
            "{source} supplies the sealed index.",
            "The restricted index is supplied by {source}.",
        ),
        "absence_voice": {
            0: (
                "The docket locator slot has no valid marker.",
                "No valid marker appears in the docket locator slot.",
            ),
            1: (
                "The docket locator slot omits every valid marker.",
                "Every valid marker is omitted from the docket locator slot.",
            ),
        },
        "reliability": {
            "strong": (
                "is authenticated and complete for this sealed review",
                "is complete and authenticated for this restricted check",
            ),
            "weak": (
                "is partial and limited for this sealed review",
                "is limited and partial for this restricted check",
            ),
            "absent": (
                "returned no usable record for this sealed review",
                "yielded no usable record for this restricted check",
            ),
            "adversarial": (
                "shows its designated signature does not validate during this sealed review",
                "comes from a source whose issuer status is superseded for this restricted check",
            ),
        },
        "markers": {
            "strong": (("authenticated", "complete"),) * 2,
            "weak": (("partial", "limited"),) * 2,
            "absent": (("usable", "record"),) * 2,
            "adversarial": (
                ("signature", "does not validate"),
                ("issuer status", "superseded"),
            ),
        },
    },
}

_VALIDATION_CACHE = {}

def _validate(latent: dict, split: str) -> None:
    if split not in SPLITS:
        raise ValueError(f"unknown split: {split}")
    required = {"true_type", "cue_variant"}
    missing = required - set(latent)
    if missing:
        raise ValueError(f"latent record missing fields: {sorted(missing)}")
    if latent["true_type"] not in ("benign", "malicious"):
        raise ValueError(f"unknown true_type: {latent['true_type']}")
    if latent["cue_variant"] not in families.DEFEAT_CLASS:
        raise ValueError(f"unknown cue_variant: {latent['cue_variant']}")


def _row(spec: dict, latent: dict, split: str,
         realization_index: int) -> dict:
    _validate(latent, split)
    if not isinstance(realization_index, int) or realization_index < 0:
        raise ValueError("realization_index must be a nonnegative integer")
    family_codes = tuple(item["code"] for item in families.all_families())
    if spec["code"] not in family_codes:
        raise ValueError(f"unknown family: {spec['code']}")
    family_index = family_codes.index(spec["code"])
    row_index = realization_index % len(BALANCED_AXES)
    axes = dict(zip(AXES, BALANCED_AXES[row_index]))
    bank = PHRASE_BANKS[split]
    key_pair = bank["keys"][family_index]
    positive_key, negative_key = (
        key_pair if axes["polarity_position"] == 0
        else (key_pair[1], key_pair[0])
    )
    cue = latent["cue_variant"]
    desired_status = None
    if cue in ("strong", "weak"):
        desired_status = (
            "positive" if latent["true_type"] == "benign" else "negative"
        )
    elif cue == "adversarial":
        desired_status = (
            "negative" if latent["true_type"] == "benign" else "positive"
        )
    pointer_key = {
        "positive": positive_key,
        "negative": negative_key,
        None: None,
    }[desired_status]
    return {
        "id": (
            f"cue-{split}-{spec['code'].lower()}-{cue}-r{row_index + 1:02d}"
        ),
        "row_index": row_index,
        "axes": axes,
        "source": bank["sources"][family_index],
        "reliability": bank["reliability"][cue][
            axes["reliability_frame"]
        ],
        "key_pair": key_pair,
        "positive_key": positive_key,
        "negative_key": negative_key,
        "pointer_key": pointer_key,
        "observable_markers": bank["markers"][cue][
            axes["reliability_frame"]
        ],
    }


def _render_row(spec: dict, latent: dict, split: str, row: dict) -> str:
    axes = row["axes"]
    bank = PHRASE_BANKS[split]
    lexical = bank["lexical_frames"][axes["lexical_frame"]]
    source_sentence = f"{row['source']} {row['reliability']}."
    cue = latent["cue_variant"]

    if cue == "absent":
        absence = bank["absence_voice"][axes["negation"]][axes["voice"]]
        lookup = lexical["absence"]
        middle = [lookup, absence]
        if axes["polarity_position"]:
            middle.reverse()
    else:
        concept_suffix = "_negated" if axes["negation"] else ""
        concepts = spec["cue_concepts"][split]
        classification = bank["classification"].format(
            subject=concepts["subject"]
        )
        positive = concepts["positive" + concept_suffix]
        negative = concepts["negative" + concept_suffix]
        entry = lexical["entry"]
        positive_entry = entry.format(
            key=row["positive_key"], concept=positive
        )
        negative_entry = entry.format(
            key=row["negative_key"], concept=negative
        )
        entries = [positive_entry, negative_entry]
        if axes["polarity_position"]:
            entries.reverse()
        index_sentence = lexical["index"].format(
            entries="; ".join(entries)
        )
        pointer_sentence = bank["voice_frames"][axes["voice"]].format(
            pointer=row["pointer_key"]
        )
        middle = [classification, index_sentence, pointer_sentence]
        if cue == "adversarial":
            source_frame = bank["source_frames"][
                axes["source_position"]
            ].format(source=row["source"])
            if axes["source_position"] == 0:
                middle = [
                    source_frame, classification, index_sentence,
                    pointer_sentence,
                ]
            else:
                middle = [
                    classification, index_sentence, source_frame,
                    pointer_sentence,
                ]
            # The apparent mapping is always presented before the visible
            # signature/issuer defeat, so zero weight is inferable rather than
            # mechanically narrated.
            return " ".join([*middle, source_sentence])

    pieces = [source_sentence, *middle]
    if axes["source_position"]:
        pieces = [*middle, source_sentence]
    return " ".join(pieces)


def realization_id(spec: dict, latent: dict, split: str,
                   realization_index: int) -> str:
    return _row(spec, latent, split, realization_index)["id"]


def render_cue(spec: dict, latent: dict, split: str,
               realization_index: int) -> str:
    row = _row(spec, latent, split, realization_index)
    return _render_row(spec, latent, split, row)


def realization_metadata(spec: dict, latent: dict, split: str,
                         realization_index: int) -> dict:
    row = _row(spec, latent, split, realization_index)
    return {
        "id": row["id"],
        "surface_pool_id": f"cue-surface-{split}-v1",
        "axes": deepcopy(row["axes"]),
        "source": row["source"],
        "reliability": row["reliability"],
        "key_pair": list(row["key_pair"]),
        "pointer_key": row["pointer_key"],
        "row_index": row["row_index"],
        "observable_markers": list(row["observable_markers"]),
    }


def _features(text: str) -> dict:
    return {
        "words": len(text.split()),
        "chars": len(text),
        "digits": sum(character.isdigit() for character in text),
        "sentences": len(re.findall(r"[.!?]", text)),
    }


def _auc(labels: list, scores: list) -> float:
    positives = Counter(
        score for label, score in zip(labels, scores) if label == 1
    )
    negatives = Counter(
        score for label, score in zip(labels, scores) if label == 0
    )
    assert positives and negatives
    wins = 0.0
    negative_below = 0
    for score in sorted(set(positives) | set(negatives)):
        positive_count = positives[score]
        negative_count = negatives[score]
        wins += positive_count * (
            negative_below + 0.5 * negative_count
        )
        negative_below += negative_count
    return wins / (sum(positives.values()) * sum(negatives.values()))


def _token_auc_max(texts: list, labels: list) -> float:
    token_counts = [
        Counter(re.findall(r"[a-z0-9]+", text.lower())) for text in texts
    ]
    vocabulary = sorted(set().union(*(set(row) for row in token_counts)))
    maximum = 0.5
    for token in vocabulary:
        counts = [row[token] for row in token_counts]
        presence = [int(value > 0) for value in counts]
        for scores in (counts, presence):
            auc = _auc(labels, scores)
            maximum = max(maximum, auc, 1.0 - auc)
    return maximum


def token_presence_count_auc_max(texts: list, labels: list) -> float:
    """Orientation-free maximum over every token's count and presence AUC."""
    if len(texts) != len(labels) or not texts:
        raise ValueError("texts and labels must be nonempty and equal length")
    if set(labels) != {0, 1}:
        raise ValueError("labels must contain both binary classes")
    return _token_auc_max(texts, labels)


def _correlation(xs: list, ys: list) -> float:
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    numerator = sum(
        (x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)
    )
    denominator = math.sqrt(
        sum((x - mean_x) ** 2 for x in xs)
        * sum((y - mean_y) ** 2 for y in ys)
    )
    return 0.0 if denominator == 0 else numerator / denominator


def audit_family(spec: dict, split: str) -> dict:
    """Derive counterbalance metrics from rendered arms, never declarations."""
    if split not in SPLITS:
        raise ValueError(f"unknown split: {split}")
    cue_variants = tuple(families.DEFEAT_CLASS)
    axis_counts = {}
    material = {}
    texts = []
    labels = []
    axis_values = {axis: [] for axis in AXES}
    label_distributions = {
        "benign": Counter(),
        "malicious": Counter(),
    }
    pointer_distributions = {
        "benign": Counter(),
        "malicious": Counter(),
    }
    budget_max = {name: 0 for name in _features("")}

    for cue in cue_variants:
        axis_counts[cue] = {
            axis: dict(Counter(
                dict(zip(AXES, row))[axis] for row in BALANCED_AXES
            ))
            for axis in AXES
        }
        material[cue] = {}
        for axis in AXES:
            changed = []
            for row_index in range(len(BALANCED_AXES)):
                latent = {
                    "true_type": "benign",
                    "cue_variant": cue,
                }
                base = _row(spec, latent, split, row_index)
                flipped = deepcopy(base)
                flipped["axes"][axis] = 1 - flipped["axes"][axis]
                # Values derived from a flipped axis must be recomputed through
                # the public row constructor.  Find any synthetic row carrying
                # the requested tuple, or rebuild the dependent fields here.
                if axis == "reliability_frame":
                    flipped["reliability"] = PHRASE_BANKS[split][
                        "reliability"
                    ][cue][flipped["axes"][axis]]
                if axis == "polarity_position":
                    flipped["positive_key"], flipped["negative_key"] = (
                        base["negative_key"], base["positive_key"]
                    )
                    if base["pointer_key"] == base["positive_key"]:
                        flipped["pointer_key"] = flipped["positive_key"]
                    elif base["pointer_key"] == base["negative_key"]:
                        flipped["pointer_key"] = flipped["negative_key"]
                changed.append(
                    _render_row(spec, latent, split, base)
                    != _render_row(spec, latent, split, flipped)
                )
            material[cue][axis] = all(changed)

        for row_index in range(len(BALANCED_AXES)):
            pair_text = {}
            for true_type, label in (("benign", 1), ("malicious", 0)):
                latent = {"true_type": true_type, "cue_variant": cue}
                text = render_cue(spec, latent, split, row_index)
                meta = realization_metadata(
                    spec, latent, split, row_index
                )
                pair_text[true_type] = text
                texts.append(text)
                labels.append(label)
                for axis in AXES:
                    axis_values[axis].append(meta["axes"][axis])
                label_distributions[true_type][(
                    tuple(meta["axes"].items()), tuple(meta["key_pair"]),
                    meta["source"], meta["reliability"],
                )] += 1
                pointer_distributions[true_type][meta["pointer_key"]] += 1
            left = _features(pair_text["benign"])
            right = _features(pair_text["malicious"])
            for name in budget_max:
                budget_max[name] = max(
                    budget_max[name], abs(left[name] - right[name])
                )

    correlations = [
        abs(_correlation(values, labels))
        for values in axis_values.values()
    ]
    return {
        "family": spec["code"],
        "split": split,
        "n_rows_per_cue": len(BALANCED_AXES),
        "axis_counts": axis_counts,
        "material_axis_effects": material,
        "label_distribution_equal": (
            label_distributions["benign"]
            == label_distributions["malicious"]
            and pointer_distributions["benign"]
            == pointer_distributions["malicious"]
        ),
        "token_type_auc_max": _token_auc_max(texts, labels),
        "axis_type_correlations_max_abs": max(correlations, default=0.0),
        "word_budget_delta_max": budget_max["words"],
        "char_budget_delta_max": budget_max["chars"],
        "digit_budget_delta_max": budget_max["digits"],
        "sentence_budget_delta_max": budget_max["sentences"],
    }


def _flatten_strings(value) -> set:
    if isinstance(value, str):
        return {value}
    if isinstance(value, dict):
        return set().union(*(_flatten_strings(item) for item in value.values()))
    if isinstance(value, (tuple, list)):
        return set().union(*(_flatten_strings(item) for item in value))
    return set()


def _rendered_phrase_strings(bank: dict) -> set:
    """Flatten visible phrase templates while excluding audit-only markers."""
    return set().union(*(
        _flatten_strings(value)
        for key, value in bank.items() if key != "markers"
    ))


def validate_counterbalance(specs: list) -> dict:
    """Fail loudly unless every family/split passes the rendered audit."""
    signature = (
        repr(PHRASE_BANKS),
        repr([(spec["code"], spec["cue_concepts"]) for spec in specs]),
        id(render_cue),
        id(_render_row),
    )
    if signature in _VALIDATION_CACHE:
        return deepcopy(_VALIDATION_CACHE[signature])
    failures = []
    concept_values = {split: set() for split in SPLITS}
    for spec in specs:
        if set(spec.get("cue_concepts", {})) != set(SPLITS):
            failures.append(f"{spec.get('code')}: incomplete split concepts")
            continue
        for split in SPLITS:
            concepts = spec["cue_concepts"][split]
            required = {
                "subject", "positive", "negative", "positive_negated",
                "negative_negated",
            }
            if set(concepts) != required:
                failures.append(
                    f"{spec['code']}/{split}: incomplete concept forms"
                )
                continue
            if not all(value.strip() for value in concepts.values()):
                failures.append(f"{spec['code']}/{split}: empty concept form")
            for key in ("positive_negated", "negative_negated"):
                if " not " not in f" {concepts[key].lower()} ":
                    failures.append(
                        f"{spec['code']}/{split}: {key} lacks visible negation"
                    )
            concept_values[split].update(concepts.values())
    for split, values in concept_values.items():
        if len(values) != len(specs) * 5:
            failures.append(
                f"{split}: concept bank has {len(values)} unique entries; "
                f"expected {len(specs) * 5}"
            )
    split_phrases = {
        split: _rendered_phrase_strings(PHRASE_BANKS[split])
        | concept_values[split]
        for split in SPLITS
    }
    for index, left in enumerate(SPLITS):
        for right in SPLITS[index + 1:]:
            overlap = split_phrases[left] & split_phrases[right]
            if overlap:
                failures.append(
                    f"split phrase reuse {left}/{right}: {sorted(overlap)}"
                )
    for spec in specs:
        for split in SPLITS:
            result = audit_family(spec, split)
            if result["token_type_auc_max"] > 0.60:
                failures.append(
                    f"{spec['code']}/{split}: token AUC "
                    f"{result['token_type_auc_max']:.3f}"
                )
            if result["axis_type_correlations_max_abs"] > 0.10:
                failures.append(
                    f"{spec['code']}/{split}: axis/type correlation"
                )
            for field in (
                "word_budget_delta_max", "char_budget_delta_max",
                "digit_budget_delta_max", "sentence_budget_delta_max",
            ):
                if result[field] != 0:
                    failures.append(
                        f"{spec['code']}/{split}: {field}={result[field]}"
                    )
            if not result["label_distribution_equal"]:
                failures.append(
                    f"{spec['code']}/{split}: label distributions differ"
                )
            if not all(
                all(axis_values.values())
                for axis_values in result["material_axis_effects"].values()
            ):
                failures.append(
                    f"{spec['code']}/{split}: non-material surface axis"
                )
    if failures:
        raise AssertionError("counterbalance failures: " + "; ".join(failures))
    result = {
        "n_families": len(specs),
        "n_splits": len(SPLITS),
        "n_rows_per_cue": len(BALANCED_AXES),
    }
    _VALIDATION_CACHE[signature] = deepcopy(result)
    return result
