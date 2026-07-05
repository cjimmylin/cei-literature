---
stem: "2018-Behzadan-TrolleyMod v1.0"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, agentic-multiturn, moral-psychology]
task_format: "interactive"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Platform built on CARLA simulator (Unreal Engine 4) for high-fidelity AV trolley problem experiments (p.1)"
  - "Three types of spawnable objects: pedestrians (Walker), vehicles (CarlaWheeledVehicle), props (StaticActor) (p.5)"
---
## 1. Gist
TrolleyMod v1.0 is an open-source simulation platform built as a modification of the CARLA autonomous driving simulator (Unreal Engine 4) for collecting ethical decision-making data in the context of autonomous vehicles. Rather than web-based click surveys like the Moral Machine, TrolleyMod places human subjects in first-person driving simulations where they must physically steer a vehicle facing unavoidable collisions — trolley-problem variants with realistic physics, 3D graphics, and real-time decision pressure. The paper introduces the system architecture, configuration workflow, and data collection pipeline, and positions TrolleyMod as addressing three gaps in prior work: lack of real-time human performance baselines, low-fidelity simulation environments, and closed or inflexible platforms. For values-alignment benchmarking, the paper is relevant as infrastructure — it demonstrates a high-fidelity interactive paradigm for eliciting embodied moral decisions, which could be adapted for testing AI agents as well as humans.

## 2. Benchmark/eval design features
TrolleyMod is an infrastructure/platform paper, not a benchmark with reported empirical results. Its core design features are:

- **Scenario structure**: Each "scenario" is a trolley-problem episode in which one or more victim groups are placed on each side of a road. The subject drives a vehicle that auto-accelerates; only swerve left/right controls are available. Invisible barriers ensure the subject must collide with at least one group.
- **Configurable characters**: Pedestrian actors store age, gender, group ID, group size, and special traits (e.g., pregnant, disabled). This mirrors the Moral Machine's character taxonomy but in 3D embodied form.
- **Session structure**: A simulation is a sequence of scenarios. Results are written to a text file or network socket upon scenario completion.
- **AI integration**: TrolleyMod provides a Python API to CARLA, enabling reinforcement learning agents (e.g., via TensorFlow, PyTorch) to be substituted for human subjects — this is the key agentic feature.
- **Extensibility**: The platform supports custom maps (urban, suburban, highway, custom), custom scenario configurations via input text files, and custom controller implementations.

The authors argue that compared to the Moral Machine, TrolleyMod: (a) uses higher-fidelity simulation; (b) provides real-time human performance baselines; (c) is open-source and reconfigurable; and (d) can account for temporal dynamics and environmental nudges.

## 3. Task format & example item
Interactive first-person driving simulation. From the paper (p.3): "In each episode of the experiment, the subject is put in the driver's seat of a vehicle that accelerates automatically. The only control actions available to the subject are swerving left or right. Furthermore, the conditions of dilemma can be reinforced via invisible barriers to ensure that the only available options to the driver are to collide with at least one group of victims or other objects."

No verbatim example scenario item is provided in the paper; the format is a real-time 3D action, not a text prompt.

## 4. Scoring / grading methodology
Data collection is behavioral: when the subject's vehicle collides with a victim actor, the CollisionHandler function records the collision data (which actor/group was hit, all actor metadata including age, gender, special traits) and writes results to a text file or network socket. The paper does not describe any scoring or aggregation methodology for the collected data — analysis of results (e.g., sociological analysis, IRL-based value inference) is described as future work. No scoring rubric or aggregate metric is defined in v1.0.

## 5. Dataset construction & provenance
TrolleyMod v1.0 is a platform release; no dataset is reported in this paper. The platform is designed to enable future data collection. Scenarios are configured via input text files specifying object types, positions, and properties. The system supports custom scenario design by the experiment operator. The GitHub repository (https://github.com/zminton/TrolleyMod/wiki) provides documentation but no pre-built scenario library is described. Dataset size, splits, and licensing are not applicable to this infrastructure paper.

## 6. Validity evidence
No empirical validity evidence is reported — TrolleyMod v1.0 is presented as a platform with no reported experimental results. The authors claim higher ecological validity than web-based surveys (Moral Machine) due to realistic physics, 3D graphics, and embodied decision-making, but do not provide comparative evidence. They note that prior kinetic simulator work (Frison et al. 2016) used a similar paradigm but did not release setup or replication procedures.

## 7. Saturation / discrimination
Not applicable — no results are reported. The platform could potentially produce richer discriminative data than static surveys due to real-time interaction, reaction time measurement, and environmental nudge manipulation, but this is prospective.

## 8. Multiturn / agentic aspects
TrolleyMod is fundamentally an interactive, agentic platform. Key features:
- **Human subjects**: Multi-scenario sequential sessions; each scenario is a real-time control episode with forced collision.
- **AI agents**: The Python API enables RL agents (deep reinforcement learning via TensorFlow/PyTorch) to be substituted for human subjects, enabling automated data collection or AI performance evaluation.
- **Tool use**: The CARLA client-server architecture exposes sensor data (GPS, speed, acceleration, collision data, semantic segmentation, traffic light state) to the agent's policy.
- **Future plans include**: Integration with Inverse Reinforcement Learning (IRL) for automated value inference from behavioral traces.

## 9. Key numbers
- 8 pages total (p.1–8)
- Platform built on CARLA + Unreal Engine 4 (p.4)
- 3 types of spawnable objects (p.5)
- 2 walker-class variables shared with all objects: TestNum, GroupMemberNames (p.5)
- 5 additional variables for pedestrian actors: age, gender, group ID, group size, special traits (p.5)
- 1 Blueprint function library ("FunctionLibrary") containing all simulation functions (p.6)
- Source code at GitHub (https://github.com/zminton/TrolleyMod/wiki) (p.7)

## 10. Pitfalls & limitations
**Author-admitted:** (1) v1.0 is a recently conceived, ongoing project — many extensions are planned. (2) No integration with IRL or other inference techniques yet. (3) Limited to trolley-problem class of dilemmas in current version. (4) No web or smartphone interface for large-scale deployment. (5) No distributed architecture for handling large experiment volumes.

**Additional observations:** (1) No empirical results are reported — the paper is purely a system description. (2) The high-fidelity simulation requirement (Unreal Engine 4, CARLA) creates significant infrastructure barriers compared to web-based surveys. (3) The forced-collision interaction mechanic (auto-acceleration, only swerve controls) is even more abstract than the Moral Machine in some ways — subjects are not actually driving, just steering. (4) No attention to cross-cultural deployment or multilingual support. (5) The platform is designed for human subjects in controlled settings, limiting scalability compared to crowdsourced approaches.

## 11. Novel ideas worth stealing
1. **Embodied real-time moral decision paradigm**: Replacing static images/text with first-person real-time simulation introduces ecological validity, reaction time as a variable, and potential for environmental nudge manipulation. For LLM evaluation, an analogous "active" format — sequential decision steps in a simulated environment — could reveal moral reasoning under time pressure or information uncertainty in ways static MCQ cannot.

2. **AI agent as experimental subject**: The Python API enabling RL agents to be substituted for humans is a direct template for LLM-as-subject evaluation. The same scenario infrastructure that tests humans can test AI, yielding direct human-AI comparison on identical stimuli.

3. **Behavioral trace as data**: Recording full collision events (not just final choices) with actor metadata creates richer datasets for IRL-based value inference. For LLM eval, logging intermediate reasoning steps (chain-of-thought, intermediate tool calls) rather than just final answers enables analogous trajectory-based value inference.

4. **Configurable scenario taxonomy via text files**: Externalizing scenario specification to structured text configuration files (rather than hardcoded scenarios) enables rapid iteration of dilemma designs. Benchmark designers should similarly separate stimulus specification from evaluation infrastructure.

5. **Environmental nudge manipulation**: The paper explicitly mentions accounting for environmental nudges (absent in Moral Machine) — e.g., weather, lighting, road condition — as factors that could modulate moral decisions. LLM benchmarks could analogously manipulate context framing to test robustness of moral responses.

## 12. Notable quotes
- "It can be argued that the low fidelity of the experiments, as well as the inconsideration of temporal and cultural externalities, diminish the feasibility of inferring practical ethical policies that can be implemented in real-world driverless vehicles." (p.3, on the Moral Machine)
- "The results of such experiments can be used for sociological analyses, as well as the training and tuning of value-aligned autonomous vehicles based on social values that are inferred from observations." (p.1)
- "TrolleyMod provides a straightforward interface between the CARLA environment and Python to enable the implementation of custom controllers, such as deep reinforcement learning agents." (p.1)
- "While these prior projects succeeded in providing very valuable insights into the problem of ethical decision-making, there remains a need for an open-source, well-documented, high-fidelity, and highly-flexible simulation platform to further facilitate experimentation and research on crowdsourced ethical models for autonomous vehicles." (p.3)

## 13. UNKNOWN / not in extract
- Any empirical results or pilot data from actual experiments run on TrolleyMod
- Current status or ongoing development beyond v1.0 (paper is from 2018)
- Whether the GitHub repository is still maintained or publicly available
- Specific scenario configurations or pre-built scenario libraries
- Performance benchmarks for the simulation (frame rate, latency)
- Details of how reaction time is recorded alongside collision choices
- Whether the platform has been used in published studies subsequent to this paper
