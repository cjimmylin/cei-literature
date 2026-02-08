---
title: "TrolleyMod v1.0 - PDF Extract"
source_pdf: "2018-Behzadan-TrolleyMod v1.0.pdf"
pages: 8
extracted_at: "2026-01-24T17:05:07.102473"
---

# PDF Extract: TrolleyMod v1.0

**Source PDF:** 2018-Behzadan-TrolleyMod v1.0.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

arXiv:1811.05594v1  [cs.AI]  14 Nov 2018
TrolleyMod v1.0: An Open-Source Simulation and
Data-Collection Platform for Ethical Decision Making in
Autonomous Vehicles
Vahid Behzadan1, James Minton1, and Arslan Munir1
Kansas State University, Manhattan, KS 66506, USA
{behzadan,jzm,amunir}@ksu.edu
http://blogs.k-state.edu/aisecurityresearch/
Abstract. This paper presents TrolleyMod v1.0, an open-source platform based
on the CARLA simulator for the collection of ethical decision-making data for
autonomous vehicles. This platform is designed to facilitate experiments aiming
to observe and record human decisions and actions in high-ﬁdelity simulations
of ethical dilemmas that occur in the context of driving. Targeting experiments in
the class of trolley problems, TrolleyMod provides a seamless approach to creat-
ing new experimental settings and environments with the realistic physics-engine
and the high-quality graphical capabilities of CARLA and the Unreal Engine.
Also, TrolleyMod provides a straightforward interface between the CARLA en-
vironment and Python to enable the implementation of custom controllers, such
as deep reinforcement learning agents. The results of such experiments can be
used for sociological analyses, as well as the training and tuning of value-aligned
autonomous vehicles based on social values that are inferred from observations.
1
Introduction
With the rise in technological advancements and investments in autonomous vehicles,
the issue of ethical decision-making in such systems is becoming growingly pronounced
[9]. Similar to human drivers, the Artiﬁcial Intelligence (AI) controllers of driverless
vehicles will inevitably face moral dilemmas, which cannot be solved by adherence to
simple ethical principles [5]. A well-known instance of such dilemmas is the trolley
problem [11], where by some means (e.g., brake malfunction), the vehicle is put in a
situation that forces the driver to decide between hurting bystanders on one side or an-
other. Considering the enhanced computational and observational abilities of AI, it is
expected that autonomous vehicles make better decisions than human drivers in such
circumstances. However, the deﬁnition of better is deeply rooted in complex ethical
principles and policies that are difﬁcult (if not practically impossible) to formally spec-
ify [10]. Furthermore, such principles are often dynamic across cultural, geographical,
and temporal dimensions [3].
While the problem of ethical decision-making in AI has remained an open challenge
for many decades [19], recent studies on data-driven approaches to this problem have
reported promising advances towards practical solutions [12]. Another advancement is
the proposal to model the dynamics of ethical decision-making within the abstraction

--- Page 2 ---

2
V. Behzadan et al.
of value-alignment, which reduces the problem to the identiﬁcation and measurement
of the ethical norms and values of the society, and implementing such values into AI
[2]. The quantiﬁcation and modeling of such norms and values can be performed via
machine learning and parametric techniques, examples of which include those that are
based on Inverse Reinforcement Learning (IRL) [1] and norm inference [12]. A ma-
jor hurdle in such approaches is that of data collection [13]. Modern machine learning
approaches and model-dependent techniques require a large number of samples that
provide a representative dataset of the societal choices and ethical values [17]. In par-
ticular, due to the rarity of representative ethical dilemmas in controlled real-world
observations, the majority of current studies resort to simulation-based experiments.
However, the experimental setups and conﬁgurations utilized by such studies suf-
fer from a number of shortcomings. Firstly, the bulk of such setups do not provide the
means for measuring the performance of human operators in real-time, and thus fail to
present a baseline for benchmarking the performance of AI against humans. Secondly,
the majority of simulation environments used in published experiments (e.g., [3]) pro-
vide a very simple depiction of the conditions in real-world dilemmas, and hence may
fail to account for salient details that are crucial to ethical decision-making. Thirdly,
most of the recent experiments are performed in simulation environments that are either
not open-source, or are very difﬁcult to reconﬁgure and customize for new experiments.
In response to the aforementioned gap, this paper presents TrolleyMod v1.0, an
open-source simulation platform based on the CARLA simulator for autonomous driv-
ing research [4]. Targeting experiments in the class of trolley problems, TrolleyMod
provides a seamless approach to creating new experimental settings and environments
with the realistic physics-engine and the high-quality graphical capabilities of CARLA
and the Unreal Engine [7]. Also, TrolleyMod provides a straightforward interface be-
tween the CARLA environment and Python to enable the implementation of custom
controllers, such as deep reinforcement learning agents in Tensorﬂow (e.g., [16]) or
Pytorch (e.g., [8]). The details of TrolleyMod are presented in the remainder of this
paper, organized as follows: We present an overview of experimental platforms used in
data-driven ethical decision-making studies, followed by the architectural details and
components of TrolleyMod. We conclude the paper with remarks on plans for future
extensions of this project.
2
Previous Work
While the philosophical debate and research on ethical decision-making in AI is decades
old, the engineering work in this area is very recent [12]. In particular, the interest in
creating moral autonomous agents has rapidly grown in the past few years. Speciﬁcally,
advances in imitation learning [18], inverse game theory [20], and IRL [1] have trig-
gered a growing investment into the research on data-driven approaches to the modeling
and transfer of human ethics to autonomous agents. Such approaches rely on collection
of data on ethical decisions and actions of many human subjects to derive a representa-
tive model of the societal ethical principles [17].
In the domain of autonomous vehicles, very few platforms for this purpose are re-
ported, and even fewer are openly available to the research community. Of the best

--- Page 3 ---

TrolleyMod v1.0
3
known ethical data collection platforms for autonomous vehicles is MIT’s Moral Ma-
chine [14] project, which performs a large-scale crowdsourcing of ethical opinions for
a few simple cases of the trolley problem. While this project has yielded many interest-
ing results [3], it can be argued that the low ﬁdelity of the experiments, as well as the
inconsideration of temporal and cultural externalities, diminish the feasibility of infer-
ring practical ethical policies that can be implemented in real-world driverless vehicles.
Furthermore, the Moral Machine experiment fails to account for the effect of environ-
mental nudges [15] in the simulated scenarios. Also, while the datasets and analytics
of this project were recently made available, the code for the simulation software it-
self is not accompanied, and hence does not accommodate the adoption, extension, and
customization of this platform for further research.
While at a smaller scale, the Ethical Autonomous Vehicles1 project also provides the
means for data collection and experimentation on ethical decision making. Albeit, this
project seems to be outdated due to lack of maintenance. Also, the limited scenarios and
ﬂexibility of this project, as well as the lack of documentation, may render the usability
of this project for extended research infeasible.
In [6], authors present an alternative data collection approach using a kinetic high-
ﬁdelity driving simulator equipped with a fully automated autonomous driver. Unfortu-
nately, the authors do not provide more information on the setup and replication proce-
dures for their experiments.
While these prior projects succeeded in providing very valuable insights into the
problem of ethical decision-making, there remains a need for an open-source, well-
documented, high-ﬁdelity, and highly-ﬂexible simulation platform to further facilitate
experimentation and research on crowdsourced ethical models for autonomous vehicles.
3
TrolleyMod v1.0
The goal of TrolleyMod is to provide an easy-to-use and ﬂexible platform for setting up
the conditions pertaining to ethical dilemmas. While the current version is mainly fo-
cused on the variations of trolley problem, this platform supports seamless customiza-
tion and adjustment of the experiment to broader classes of ethical decision-making,
such as abiding by the trafﬁc laws. TrolleyMod is designed to facilitate experiments
that require high-ﬁdelity simulations of ethical dilemmas that occur in driving tasks to
observe and record human decisions. The results of such experiments can be used for
sociological analyses, as well as the training and tuning of value-aligned AI agents for
autonomous driving based on social values that are inferred from observations.
In TrolleyMod, the trolley problems are set up such that there are one or more vic-
tims on each side of a road belonging to a simulation environment. The environment
(i.e., map) may be designed to represent realistic conditions in urban, suburban, high-
way, or custom settings. In each episode of the experiment, the subject is put in the
driver’s seat of a vehicle that accelerates automatically. The only control actions avail-
able to the subject are swerving left or right. Furthermore, the conditions of dilemma
can be reinforced via invisible barriers to ensure that the only available options to the
1 http://mchrbn.net/ethical-autonomous-vehicles/

--- Page 4 ---

4
V. Behzadan et al.
Fig. 1. Startup menu of a TrolleyMod simulation
driver are to collide with at least one group of victims or other objects. Upon collision,
the subject’s actions are written into a text ﬁle or a network socket for processing. In
TrolleyMod, each individual Trolley problem is called a scenario. A sequence of sce-
narios is what constitutes a TrolleyMod simulation. The components and procedures of
a simulation are detailed as follows:
3.1
CARLA
As the name suggests, TrolleyMod is a modiﬁcation of the CARLA (Car Learning to
Act) simulator [4]. CARLA is an open-source simulator for urban driving, designed to
support training, prototyping, and validation of autonomous driving models. This plat-
form allows for the ﬂexible conﬁguration of sensor suites and provides various signals
useful to the training of driving tasks, such as GPS coordinates, speed, acceleration,
and detailed data on collisions. CARLA is implemented over Unreal Engine 4 [7] to
provide ﬂexibility and realism in the physics and high-ﬁdelity visualization of driving
environments. CARLA follows a client-server architecture to provide an interface be-
tween the world and various types of agents. In this architecture, the server runs the
simulation and renders the scene, while the client uses a Python API to interact with the
simulation.
The environments of CARLA are composed of 3D models of static objects, such as
trafﬁc signs, buildings, infrastructure, vegetation, as well as dynamic objects, such as
vehicles and pedestrians. The default sensors in CARLA are comprised of RGB (Red,
Green, and Blue) camera and pseudo-sensors which provide semantic segmentations
in terms of road, trafﬁc sign, sidewalk, pedestrian, etc. Furthermore, CARLA provides
various measurements associated with the state of the agent as well as compliance with
trafﬁc rules. Such measurements include orientation and location, acceleration vector,

--- Page 5 ---

TrolleyMod v1.0
5
Fig. 2. Blueprint functions for execution and control of the simulation
speed, and the cumulative impact of collisions. Signals corresponding to trafﬁc rules
include the state of trafﬁc lights and speed limits.
3.2
Components of TrolleyMod
There are three types of objects that can be spawned automatically with TrolleyMod:
pedestrians, vehicles, and prop objects. These correspond to the Walker, the CarlaWheeled-
Vehicle, and StaticActor classes respectively. The ﬁrst two classes are native to CARLA,
while StaticActor is a product of TrolleyMod. Our extension adjusts these classes to en-
able their instance to store new information pertaining to trolley scenarios. All three
classes share two variables:
1. TestNum: an integer that tracks what scenario is being run.
2. GroupMemberNames: a delineated string that lumps together the names and prop-
erties of all victims in the scenario to which the class instance belongs.
Walker actors also retain the following additional information for the pedestrian
character: age, gender, ID number of the pedestrian’s group in the scenario, size of the
pedestrian’s group, and special traits (e.g., pregnant, disabled, etc.)
3.3
Conﬁguration
TrolleyMod spawns object models into a “level” (i.e., episode of simulation) in the
Unreal Engine 4. It takes an input text ﬁle, which contains a list of tuples specifying
an object (e.g., pedestrian, car, cones, etc.) that can be collided with by the subject
and provides any other ancillary data that describes the object. This text is parsed to
provide a reference to Unreal Engine’s Actor class in memory. TrolleyMod implements

--- Page 6 ---

6
V. Behzadan et al.
a custom format for the speciﬁcation of objects in a scenario, as detailed in the online
documentation2.
Fig. 3. Manual conﬁguration of Actor objects
To generate a scenario in TrolleyMod, the experiment designer runs a generation
Blutility ((Editor Utility Blueprint)) named ScenarioGen. A blutility is an Unreal En-
gine object that enables execution of functions outside of the runtime. In TrolleyMod,
blutilities are essential for providing a means to quickly modify the CARLA-provided
maps to facilitate the generation of various scenarios in a relatively short period of time.
After the ScenarioGen blutility is run, the experiment designer may add other sce-
narios in unused locations in the map by manually placing Actor objects into the level,
as illustrated in Fig. 3. Also, for the data recording script to recognize a new scenario,
a Target object must be placed into the map ﬁrst.
TrolleyMod provides the necessary functions and assets to set up scenarios, but it
is up to the user on how to arrange and utilize them in customized environments and
settings. Since each user will want to deﬁne a simulation differently, TrolleyMod only
provides a functional framework. Further details on this procedure is available in the
online documentation.
3.4
Execution of Simulation
TrolleyMod utilizes a modular structure based on Blueprint Function Library, which
is an Unreal Engine feature that allows for the functions in the library to be reused
over multiple projects. In TrolleyMod, blueprints provide a prepackaged set of func-
tions to be used in the level blueprint of maps derived from CARLA’s native environ-
ments. Currently, TrolleyMod contains only one blueprint, named “FunctionLibrary”.
2 https://github.com/zminton/TrolleyMod/wiki

--- Page 7 ---

TrolleyMod v1.0
7
This blueprint contains all of the functions required to run TrolleyMod simulations.
When the subject’s agent collides with a victim, that result is recorded and the next
scenario is spawned. Once all scenarios are complete, the simulation terminates and the
results are written to a text ﬁle or network socket.
Each TrolleyMod simulation includes an Event Tick node, which is called at every
frame during the simulation. The purpose of this node is to make the car controlled
by the subject to automatically accelerate, thus forcing the subject to decide quickly on
what victim to collide with. As depicted in Fig. 2, the initial event object of this blueprint
(i.e., BeginPlay) ﬁrst calls the InitValues function in order to initialize the environment
and object attributes. Then, it binds the subject’s agent to a hit event –that is, whenever
the agent collides with any object in the map, it will generate an event that calls the
OnActorHit Event 0 node. Next, assuming the agent hits one of the intended victims,
the blueprint generates a text message describing what the player collided with using
the SetDisplay function. If the player does not hit an intended target, the simulation
refers to the PlayerRotation variable to reset where the car is facing and rebinds hit
events to it.
Otherwise, the CollisionHandler function analyzes the Actor hit by the player, ex-
tracts its data to the Output variable, and then prepares the simulation to move on to the
next scenario. This continues until all the scenarios in the Locations array have been
visited, after which the simulation writes the data to a text ﬁle. It is also possible for the
player to specify only one scenario to complete using the start menu, and consequently
the simulation will terminate after the speciﬁed scenario is run.
4
Future Work
TrolleyMod is a recently conceived and an ongoing project, hence there are many in-
teresting directions for pursuit of its extension. First and foremost in our roadmap is to
demonstrate the integration of TrolleyMod with inference techniques such as IRL. Fur-
thermore, our plan for the near-future includes the gradual extension of functionalities to
support seamless conﬁguration for more well-known moral dilemmas, and enhance the
front and backend to provide better support for handling larger numbers of experiments
and volumes of results in a distributed architecture. A similar priority is the develop-
ment of web and smartphone interfaces to enhance the reach and accessibility of this
platform for large scale research. As noted, TrolleyMod is an open-source project with
the aim of facilitating research on ethical autonomous vehicles, and is looking forward
to contributions and comments from the community.
References
1. Abel, D., MacGlashan, J., Littman, M.L.: Reinforcement learning as a framework for ethical
decision making. In: AAAI Workshop: AI, Ethics, and Society. vol. 92 (2016)
2. Arnold, T., Kasenberg, D., Scheutz, M.: Value alignment or misalignment–what will keep
systems accountable. In: 3rd International Workshop on AI, Ethics, and Society (2017)
3. Awad, E., Dsouza, S., Kim, R., Schulz, J., Henrich, J., Shariff, A., Bonnefon, J.F., Rahwan,
I.: The moral machine experiment. Nature p. 1 (2018)

--- Page 8 ---

8
V. Behzadan et al.
4. Dosovitskiy, A., Ros, G., Codevilla, F., Lopez, A., Koltun, V.: Carla: An open urban driving
simulator. arXiv preprint arXiv:1711.03938 (2017)
5. Dwork, C., Hardt, M., Pitassi, T., Reingold, O., Zemel, R.: Fairness through awareness. In:
Proceedings of the 3rd innovations in theoretical computer science conference. pp. 214–226.
ACM (2012)
6. Frison, A.K., Wintersberger, P., Riener, A.: First person trolley problem: Evaluation of
drivers’ ethical decisions in a driving simulator. In: Adjunct proceedings of the 8th inter-
national conference on automotive user interfaces and interactive vehicular applications. pp.
117–122. ACM (2016)
7. Games, E.: Unreal engine. Online: https://www. unrealengine. com (2007)
8. GENANDER, J., NYLANDER, A.: Control of self-driving vehicles using deep learning
9. Goodall, N.J.: Machine ethics and automated vehicles. In: Road vehicle automation, pp. 93–
102. Springer (2014)
10. Greene, J., Rossi, F., Tasioulas, J., Venable, K.B., Williams, B.C.: Embedding ethical princi-
ples in collective decision support systems. In: AAAI. vol. 16, pp. 4147–4151 (2016)
11. Jarvis Thomson, J.: The trolley problem. Yale Law Journal 94(6), 5 (1985)
12. Kasenberg, D., Arnold, T., Scheutz, M.: Norms, rewards, and the intentional stance: Compar-
ing machine learning approaches to ethical training. In: Proceedings of the First AAAI/ACM
Conference on Artiﬁcial Intelligence, Ethics, and Society (2018)
13. Kim, R., Kleiman-Weiner, M., Abeliuk, A., Awad, E., Dsouza, S., Tenenbaum, J., Rahwan,
I.: A computational model of commonsense moral decision making (2017)
14. Kim, R., Kleiman-Weiner, M., Abeliuk, A., Awad, E., Dsouza, S., Tenenbaum, J., Rah-
wan, I.: A computational model of commonsense moral decision making. arXiv preprint
arXiv:1801.04346 (2018)
15. Leonard, T.C.: Richard h. thaler, cass r. sunstein, nudge: Improving decisions about health,
wealth, and happiness (2008)
16. Liang, X., Wang, T., Yang, L., Xing, E.: Cirl: Controllable imitative reinforcement learning
for vision-based self-driving. arXiv preprint arXiv:1807.03776 1 (2018)
17. Noothigattu, R., Gaikwad, S., Awad, E., Dsouza, S., Rahwan, I., Ravikumar, P., Procaccia,
A.D.: A voting-based system for ethical decision making. arXiv preprint arXiv:1709.06692
(2017)
18. Taylor, J., Yudkowsky, E., LaVictoire, P., Critch, A.: Alignment for advanced machine learn-
ing systems. Machine Intelligence Research Institute (2016)
19. Wallach, W., Allen, C.: Moral machines: Teaching robots right from wrong. Oxford Univer-
sity Press (2008)
20. Wang, Y., Wan, Y., Wang, Z.: Using experimental game theory to transit human values to
ethical ai. arXiv preprint arXiv:1711.05905 (2017)

```
