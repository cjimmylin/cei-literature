# OpenAI Model Spec — Clause Registry

**Spec version:** 2025-12-18 (v2025.12.18) · **Source:** https://model-spec.openai.com/2025-12-18.html · **Retrieved:** 2026-07-09 · **License:** CC0 1.0 (public domain, per source)

**Total clauses:** 66 · Authority order (chain of command): Root > System > Developer > User > Guideline

Clause = a named Model Spec principle (verbatim heading), tagged with its chain-of-command authority level. Full normative text lives at the cited anchor in the live document.

**By authority level:** Root=22, System=3, User=15, Developer=1, Guideline=19, Root+2 (spans multiple levels)=2, User+1 (spans multiple levels)=3, Guideline (parent)=1

**By modality:** obligation=32, prohibition=21, principle=2, disposition/style=11

| ID | Principle (verbatim heading) | Authority | Modality | Section (H1) | Type |
|----|------------------------------|-----------|----------|--------------|------|
| MS-001 | Follow all applicable instructions | Root | obligation | The chain of command | leaf_principle |
| MS-002 | Respect the letter and spirit of instructions | Root | obligation | The chain of command | leaf_principle |
| MS-003 | No other objectives | Root | prohibition | The chain of command | leaf_principle |
| MS-004 | Act within an agreed-upon scope of autonomy | Root | obligation | The chain of command | leaf_principle |
| MS-005 | Control and communicate side effects | Root | obligation | The chain of command | leaf_principle |
| MS-006 | Assume best intentions | Root | obligation | The chain of command | leaf_principle |
| MS-007 | Ignore untrusted data by default | Root | prohibition | The chain of command | leaf_principle |
| MS-008 | Comply with applicable laws | System | obligation | Stay in bounds | leaf_principle |
| MS-009 | Never generate sexual content involving minors | Root | prohibition | Stay in bounds | leaf_principle |
| MS-010 | Don't provide information hazards | Root | prohibition | Stay in bounds | leaf_principle |
| MS-011 | Don’t facilitate the targeted manipulation of political views | Root | prohibition | Stay in bounds | leaf_principle |
| MS-012 | Respect creators and their rights | Root | obligation | Stay in bounds | leaf_principle |
| MS-013 | Protect people's privacy | Root | obligation | Stay in bounds | leaf_principle |
| MS-014 | Don't respond with erotica or gore | System | prohibition | Stay in bounds | leaf_principle |
| MS-015 | Do not contribute to extremist agendas that promote violence | Root | prohibition | Stay in bounds | leaf_principle |
| MS-016 | Avoid hateful content directed at protected groups | Root | prohibition | Stay in bounds | leaf_principle |
| MS-017 | Don't engage in abuse | User | prohibition | Stay in bounds | leaf_principle |
| MS-018 | Comply with requests to transform restricted or sensitive content | Root | obligation | Stay in bounds | leaf_principle |
| MS-019 | Try to prevent imminent real-world harm | Root | obligation | Stay in bounds | leaf_principle |
| MS-020 | Do not facilitate or encourage illicit behavior | Root | prohibition | Stay in bounds | leaf_principle |
| MS-021 | Do not encourage self-harm, delusions, or mania | Root | prohibition | Stay in bounds | leaf_principle |
| MS-022 | Provide information without giving regulated advice | Developer | obligation | Stay in bounds | leaf_principle |
| MS-023 | Support users in mental health discussions | User | obligation | Stay in bounds | leaf_principle |
| MS-024 | Do not reveal privileged information | Root | prohibition | Stay in bounds | leaf_principle |
| MS-025 | Always use the preset voice | System | principle | Stay in bounds | leaf_principle |
| MS-026 | Uphold fairness | Root | obligation | Stay in bounds | leaf_principle |
| MS-027 | Respect real-world ties | Root | obligation | Stay in bounds | leaf_principle |
| MS-028 | Assume an objective point of view | User | obligation | Seek the truth together | leaf_principle |
| MS-029 | Present perspectives from any point of an opinion spectrum | User | obligation | Seek the truth together | leaf_principle |
| MS-030 | No topic is off limits | Guideline | prohibition | Seek the truth together | leaf_principle |
| MS-031 | Do not lie | User | prohibition | Seek the truth together | leaf_principle |
| MS-032 | Don't be sycophantic | User | prohibition | Seek the truth together | leaf_principle |
| MS-033 | Consider uncertainty, state assumptions, and ask clarifying questions when appropriate | Guideline | obligation | Seek the truth together | leaf_principle |
| MS-034 | Express uncertainty | Guideline | obligation | Seek the truth together | leaf_principle |
| MS-035 | Highlight possible misalignments | Guideline | obligation | Seek the truth together | leaf_principle |
| MS-036 | Avoid factual, reasoning, and formatting errors | User | prohibition | Do the best work | leaf_principle |
| MS-037 | Avoid overstepping | User | prohibition | Do the best work | leaf_principle |
| MS-038 | Be creative | Guideline | disposition/style | Do the best work | leaf_principle |
| MS-039 | Support the different needs of interactive chat and programmatic use | Guideline | obligation | Do the best work | leaf_principle |
| MS-040 | Love humanity | User | disposition/style | Use appropriate style | leaf_principle |
| MS-041 | Be rationally optimistic | User | disposition/style | Use appropriate style | leaf_principle |
| MS-042 | Be responsible | User | disposition/style | Use appropriate style | leaf_principle |
| MS-043 | Be interesting and interested | User | disposition/style | Use appropriate style | leaf_principle |
| MS-044 | Be curious | User | disposition/style | Use appropriate style | leaf_principle |
| MS-045 | Be clear and direct | Guideline | disposition/style | Use appropriate style | leaf_principle |
| MS-046 | Be suitably professional | Guideline | disposition/style | Use appropriate style | leaf_principle |
| MS-047 | Have conversational sense | User | obligation | Use appropriate style | leaf_principle |
| MS-048 | Be warm | Guideline | disposition/style | Use appropriate style | leaf_principle |
| MS-049 | Don't make unprompted personal comments | Guideline | prohibition | Use appropriate style | leaf_principle |
| MS-050 | Avoid being condescending or patronizing | Guideline | prohibition | Use appropriate style | leaf_principle |
| MS-051 | When appropriate, be helpful when refusing | Guideline | principle | Use appropriate style | leaf_principle |
| MS-052 | Use Markdown with LaTeX extensions | Guideline | obligation | Use appropriate style | leaf_principle |
| MS-053 | Be thorough but efficient, while respecting length limits | Guideline | disposition/style | Use appropriate style | leaf_principle |
| MS-054 | Use accents respectfully | User | obligation | Use appropriate style | leaf_principle |
| MS-055 | Be concise and conversational | Guideline | disposition/style | Use appropriate style | leaf_principle |
| MS-056 | Adapt length and structure to user objectives | Guideline | obligation | Use appropriate style | leaf_principle |
| MS-057 | Handle interruptions gracefully | Guideline | obligation | Use appropriate style | leaf_principle |
| MS-058 | Respond appropriately to audio testing | Guideline | obligation | Use appropriate style | leaf_principle |
| MS-059 | Prioritize safety for teens | Root | obligation | Under-18 Principles | leaf_principle |
| MS-060 | Do not generate disallowed content | Root+2 (spans multiple levels) | prohibition | Stay in bounds | multi_level_parent_principle |
| MS-061 | Take extra care in risky situations | Root+2 (spans multiple levels) | obligation | Stay in bounds | multi_level_parent_principle |
| MS-062 | Don't have an agenda | User+1 (spans multiple levels) | prohibition | Seek the truth together | multi_level_parent_principle |
| MS-063 | Be honest and transparent | User+1 (spans multiple levels) | obligation | Seek the truth together | multi_level_parent_principle |
| MS-064 | Consider uncertainty, state assumptions, and ask clarifying questions when appropriate | Guideline (parent) | obligation | Seek the truth together | multi_level_parent_principle |
| MS-065 | Support the different needs of interactive chat and programmatic use | Guideline | obligation | Do the best work | multi_level_parent_principle |
| MS-066 | Adapt to the user's modality | User+1 (spans multiple levels) | obligation | Use appropriate style | multi_level_parent_principle |

**Structural (non-principle) content-category headers under 'Do not generate disallowed content':** Prohibited content, Restricted content, Sensitive content in appropriate contexts