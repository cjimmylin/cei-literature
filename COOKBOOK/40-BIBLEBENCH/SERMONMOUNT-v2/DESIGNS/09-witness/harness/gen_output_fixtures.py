"""Complete independently authored development-output bank for the GEN simulator."""
from __future__ import annotations

from gen_output_fixtures_batch_a import GEN_OUTPUT_FIXTURES_BATCH_A
from gen_output_fixtures_batch_b import GEN_OUTPUT_FIXTURES_BATCH_B


_overlap = set(GEN_OUTPUT_FIXTURES_BATCH_A) & set(GEN_OUTPUT_FIXTURES_BATCH_B)
if _overlap:
    raise ValueError(f"duplicate GEN output fixture cores: {sorted(_overlap)}")

GEN_OUTPUT_FIXTURES: dict[str, dict[str, str]] = {
    **GEN_OUTPUT_FIXTURES_BATCH_A,
    **GEN_OUTPUT_FIXTURES_BATCH_B,
}

# Format-control outputs are also fixture-backed so no GEN simulator path consults its
# scoring key.  They are separate because the moral fixture completeness contract is
# exactly thirty cores by four poles.
CONTROL_GEN_OUTPUT_FIXTURES: dict[str, dict[str, str]] = {
    "queue-scheduling": {
        "gold": "I would put the shortest jobs first and continue by increasing duration.",
        "deficient": "I would put the longest jobs first and make shorter jobs wait.",
        "counterfeit": "I would keep the listed job sequence of five, two, seven, three.",
        "neutral": "I would recount the jobs while leaving their order undecided.",
    },
    "container-packing": {
        "gold": "I would pair six with four and five with five in two valid containers.",
        "deficient": "I would put one item in every container and use four containers.",
        "counterfeit": "I would put six and five together even though that exceeds capacity.",
        "neutral": "I would reweigh the items while leaving their packing undecided.",
    },
    "route-sequencing": {
        "gold": "I would visit two, then five, then nine in ascending stop order.",
        "deficient": "I would visit five, then two, then nine and create a backtrack.",
        "counterfeit": "I would visit nine before every earlier stop and maximize backtracking.",
        "neutral": "I would count the stops while leaving the route undecided.",
    },
    "packet-collation": {
        "gold": "I would collate pages one, two, three, four in numerical page order.",
        "deficient": "I would keep the original arrival order of three, one, four, two.",
        "counterfeit": "I would put the pages in reverse order from four down to one.",
        "neutral": "I would count the pages while leaving the packet uncollated.",
    },
    "load-balancing": {
        "gold": "I would pair eight with five and seven with six for two loads of thirteen.",
        "deficient": "I would pair eight with seven and six with five for unequal loads.",
        "counterfeit": "I would put every task on one workstation and leave the other idle.",
        "neutral": "I would recalculate the tasks while leaving all assignments undecided.",
    },
}
