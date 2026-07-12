# v3 shared-artifact ownership

This table prevents copy-drift. Reuse is by reference through a documented
adapter; shared artifacts have one owner.

| Artifact | Owner | Consumers | Change rule |
|---|---|---|---|
| Frozen C1–C16 registry | v3 portfolio | every v3 bank | Portfolio authority only; banks verify IDs/definitions |
| Global `canary_registry.txt` | v3 bank root | every v3 bank | Append-only; marker/item mappings never reassigned |
| CROSSROADS deep structures | `01-crossroads` | approved later adapters | Owner edits; consumers pin source hash |
| CROSSROADS public tool/simulant interfaces | `01-crossroads` | public harness clients | Versioned interface; private decision logic excluded |
| CROSSROADS private path keys and simulants | `01-crossroads` | trusted scorer only | Sealed split; never copied or rendered |
| CROSSROADS episode export/A3/A4 map | `01-crossroads` | portfolio analysis | Frozen before pilot; amendments append-only |

No shared file may contain a second bank's private split, judge map, access
evidence, or decision logic. A consumer needing a different surface writes an
adapter and records the source hash; it does not fork the owned structure.
