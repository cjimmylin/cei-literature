---
title: "Towards Understanding Sycophancy in LMs 2310.13548v2"
source_pdf: "AI Labs/Anthropic/Papers/Towards_Understanding_Sycophancy_in_LMs_2310.13548v2.pdf"
company: "Anthropic"
pages: 15
extracted_at: "2026-01-31T17:32:32.984492"
type: "ai_lab_paper"
---

# Towards Understanding Sycophancy in LMs 2310.13548v2

**Company/Lab:** Anthropic
**Source PDF:** AI Labs/Anthropic/Papers/Towards_Understanding_Sycophancy_in_LMs_2310.13548v2.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Floquet Non-Abelian Topological Insulator and Multifold Bulk-Edge Correspondence
Tianyu Li1 and Haiping Hu1, 2∗
1Beijing National Laboratory for Condensed Matter Physics,
Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China and
2School of Physical Sciences, University of Chinese Academy of Sciences, Beijing 100049, China
Topological phases characterized by non-Abelian charges are beyond the scope of the paradigmatic
tenfold way and have gained increasing attention recently. Here we investigate topological insula-
tors with multiple tangled gaps in Floquet settings and identify uncharted Floquet non-Abelian
topological insulators without any static or Abelian analog. We demonstrate that the bulk-edge
correspondence is multifold and follows the multiplication rule of the quaternion group Q8. The
same quaternion charge corresponds to several distinct edge-state configurations that are fully de-
termined by phase-band singularities of the time evolution. In the anomalous non-Abelian phase,
edge states appear in all bandgaps despite trivial quaternion charge. Furthermore, we uncover an
exotic swap effect—the emergence of interface modes with swapped driving, which is a signature
of the non-Abelian dynamics and absent in Floquet Abelian systems. Our work, for the first time,
presents Floquet topological insulators characterized by non-Abelian charges and opens up exciting
possibilities for exploring the rich and uncharted territory of non-equilibrium topological phases.
The past few decades have witnessed a remarkable
surge of research in topological phases of matter [1, 2],
culminating in the renowned Altland-Zirnbauer tenfold
way [3–7]. Based on the underlying symmetries and spa-
tial dimensions, gapped bulk Hamiltonians are character-
ized by Abelian-type topological invariants (Z or Z2) with
their own manifestation of protected boundary states.
Very recently, the notion of band topology has been ex-
tended to tangled multi-gap scenarios [8–15].
For in-
stance, in the presence of space-time inversion (PT) sym-
metry, one-dimensional (1D) insulators involving multi-
ple bandgaps may carry non-Abelian quaternion charges
[8] and host richer topological phases as experimentally
observed in transmission line networks [16, 17]. Yet in
its infancy, the tangled multi-gap topology plays a vi-
tal role in describing, e.g., the disclination defects of ne-
matic liquids [18–22], the admissible nodal lines [23–27]
and the reciprocal braiding of Dirac/Weyl/exceptional
points [11, 28–31].
Floquet engineering provides a powerful knob in ma-
nipulating band structures [32–41], offering unprece-
dented control over the topological properties of mate-
rials and the exploration of non-equilibrium phenomena.
With a time-periodic Hamiltonian H(t) = H(t + T) (T
is the driving period), the stroboscopic dynamics is dic-
tated by an effective Floquet Hamiltonian. Notably, Flo-
quet systems exhibit intriguing topological features with
no static analog arising from the replicas of quasienergy
bands, such as the emergence of anomalous chiral edge
modes [42–45] despite the triviality of all bulk bands. In-
corporating the multi-gap scenario, this paper aims to
address three fundamental questions regarding Floquet
multi-gap topology. (i) Does a Floquet topological insu-
lating phase characterized by non-Abelian charge exist,
and if so, how can it be implemented through periodic
∗hhu@iphy.ac.cn
driving? (ii) What novel bulk-edge correspondence does
such a non-Abelian phase possess, and how can it be
described? (iii) Are there any unique topological or dy-
namical phenomena associated with this phase?
Here we answer these questions affirmatively. Firstly,
we propose the realization of the simplest Floquet non-
Abelian topological insulator (FNATI) in a 1D three-
band system with PT symmetry. Secondly, the FNATI is
characterized by a quaternion charge, which, on its own,
cannot predict the existence or the number of edge states.
Moreover, each quaternion charge corresponds to multi-
ple edge-state configurations, demonstrating a multifold
bulk-edge correspondence that obeys the multiplication
rule of the quaternion group. The full topology or edge-
state configuration is completely captured by the phase-
band singularities of the time-evolution operator over one
driving period. Intriguingly, we identify an anomalous
FNATI hosting edge modes inside all bandgaps with a
trivial bulk quaternion charge.
Thirdly, we reveal the
emergence of interface modes with swapped driving se-
quences as a genuine non-Abelian effect. It indicates the
non-commutative nature of the FNATI. This is in sharp
contrast to Floquet Abelian topological insulators, where
such interface modes are absent due to the same spectral
structures regardless of the choice of time frame.
We
emphasize that the intriguing properties of FNATI stem
from the presence of multiple tangled bandgaps.
Our
findings expand the scope of Floquet topological insula-
tors into the non-Abelian regime and open up new av-
enues for investigating the vast and unexplored territory
of non-equilibrium topological phases.
Results
Multi-gap topology and driving protocol. Let us
recap the static three-band topological insulator charac-
terized by the quaternion charge Q8 [8]. In the presence
of PT symmetry, the Hamiltonian becomes real-valued
in momentum space H(k) = H∗(k) when expressed on
a suitable basis. Consequently, the eigenstates represent
three real vectors that are orthonormal to each other and
arXiv:2310.08819v1  [cond-mat.mes-hall]  13 Oct 2023

--- Page 2 ---

2
A
B
C
A
B
C
-1
0
1
2-nd gap
3-rd gap
1-st gap
X
Y
Z
c
d
e
a
b
0
0.4
0.2
1
25
50
1
25
50
0
FIG. 1.
Multi-gap topology in Floquet systems.
a Sketch
of the frame rotation of eigenstates for topological insulator
characterized by quaternion charge.
The loci of eigenstate
on the unit sphere with varying momentum k from −π to π
are marked in red/green/blue for the first/second/third band,
respectively. b Building blocks for our Floquet driving. H1
(H2) contains only intracell (intercell) coupling terms. c La-
beling of the quasienergy bandgaps. The third gap straddles
the FBZ edge at ± π
T . d,e Quasienergy spectra and spatial
distributions (represented by color shades) of their eigenstates
for quaternion charge q = j with open boundaries. In d, the
edge states emerge at both the first and second gaps. In e
the edge states emerge at the third gap. The lattice length is
L = 50. The parameters are listed in Methods.
span a coordinate frame, as sketched in Fig. 1a. When
simultaneously considering both bandgaps, the configu-
ration space of the Hamiltonian is M3 =
O(3)
O(1)3 , where
O(N) denotes the orthogonal group of N dimension. The
O(1) = Z2 factor comes from the gauge freedom (±1)
for each real eigenstate. With the variation of momen-
tum k from −π to π, the eigenstate frame rotates on
the unit sphere.
The mapping from the 1D Brillouin
zone k ∈[−π, π] = S1 to M3 is governed by the funda-
mental group of M3, which describes the frame rotation.
This fundamental group is given by the quaternion group
π1(M3) = Q8 [8]. As a non-Abelian group, Q8 has eight
elements and five conjugacy classes {1, ±i, ±j, ±k, −1}
with multiplication rule i2 = j2 = k2 = ijk = −1, ij =
−ji, ik = −ki, jk = −kj. The quaternion charge cap-
tures the multi-gap band topology and governs the num-
ber of edge states in both bandgaps [16].
The trivial
phase with charge q = 1 has no edge states under open
boundaries.
We consider a 1D lattice with three sites, denoted as
A, B, C per unit cell. Our Floquet driving is based on
two ingredients, namely H1 and H2 as depicted in Fig.
1b. H1 (H2) contains only intracell (intercell) couplings
and respects PT symmetry,













H1 =
L
X
n=1
X
X,Y
sXY c†
X,ncY,n + h.c.,
H2 =
L−1
X
n=1
X
X,Y
vXY c†
X,ncY,n+1 + h.c..
(1)
Here c†
X,n and cX,n represent the creation and annihila-
tion operators at site X (X = A, B, C) of the n-th unit
cell, respectively. The lattice length is L. The coupling
parameters sXY and vXY used in this paper are listed
in the Methods. Without loss of generality, the driving
period is set as T = 1. We adopt a symmetric driving
protocol: H(t) = H1 for t ∈mT + [0, T/4] ∪[3T/4, T]
and H(t) = H2 for t ∈mT + [T/4, 3T/4] (m ∈Z). The
dynamics of the system is governed by the time evolution
operator U(t) = T e−i
R t
0 H(τ)dτ, where T means time or-
dering. The stroboscopic evolution of the system is de-
scribed by the Floquet operator,
U(T) = e−iH1T/4e−iH2T/2e−iH1T/4.
(2)
The effective Floquet Hamiltonian HF is defined through
U(T) = e−iHF T . Due to the symmetric driving, the Flo-
quet Hamiltonian respects PT symmetry, i.e., HF (k) =
H∗
F (k). After the diagonalization: HF |un⟩= ϵn|un⟩(n is
the band index), we obtain the quasienergy ϵn and eigen-
states |un⟩. The quasienergies are well-defined modulo
2π/T, and form the quasienergy bands. In the follow-
ing, we set ϵn to be in the first Brillouin zone (FBZ) of
quasienergy ϵn ∈(−π/T, π/T].
Unlike the static three-band model with two bandgaps,
the Floquet system exhibits an additional bandgap that
spans across the FBZ boundary at ±π/T [See Fig. 1c],
which arises from the replica of Floquet spectra. As a
consequence, the multi-gap topology is greatly enriched
in Floquet settings. The closing and reopening of this
bandgap lead to the emergence of extra edge modes un-
der open boundary conditions. For ease of reference, we
denote the band from bottom to top as the first, second,
and third bands, respectively, while bearing in mind their
replicated nature. The gap between them is then labeled
as the first, second, and third bandgap. In Figs. 1d, e, we
present the quasienergy spectra and their spatial profiles
(of their associated eigenstates) with open boundaries.
In both cases, the bulk Floquet Hamiltonian carries a
quaternion charge of q = j. In Fig. 1d, we observe one
edge mode (for each end of the lattice) at the first and sec-
ond bandgaps, respectively, which is similar to the static
case [16]. While in Fig. 1e, there is only a single edge
mode within the third bandgap. Similar scenarios apply
to other cases as well. For instance, for charge i, edge
states can exist in both the first and third bandgaps or
solely in the second gap. Likewise, for charge k, the edge
state may exist in both the second and third bandgaps
or only in the first gap.

--- Page 3 ---

3
-1
0
1
0.4
0.7
1
-1
0
1
-1
1
1
0.25
b
1
25
50
0
0
0.4
0.2
a
FIG. 2. FNATI with anomalous edge states. a Quasienergy
spectra and the spatial distributions of their eigenstates with
open boundaries. The bulk quaternion charge is q = 1. The
lattice length is L = 50.
b Phase bands of ˜U(k, t) in the
2D momentum-time space. The Dirac-point singularities are
marked with red dots. The inset: locations of the Dirac points
with quaternion charges ˜j, −˜i, and ˜k in the (k, t)-space. P is
the base point for the encircling paths. The quaternion charge
of the bulk Floquet Hamiltonian and Dirac points are related
via 1 = ˜k · (−˜i) · ˜j. The parameters are listed in Methods.
Anomalous
FNATI. Owning to the additional
bandgap at the FBZ edge, the periodically driven sys-
tem can exhibit an intriguing phase with protected edge
modes even when the bulk quaternion invariant is triv-
ial. This is in stark contrast with the static systems [16],
wherein the charge q = 1 system does not possess any
nontrivial edge states. Note that a similar anomaly also
happens on 2D driven lattice with protected chiral edge
states despite the triviality of bulk Chern bands [42]. We
thus dub this phase anomalous FNATI. In Fig. 2a, we
plot the quasienergies and the spatial profiles of their as-
sociated eigenstates for this anomalous phase. We can
clearly observe the existence of edge states (one for each
end of the lattice) in all three bandgaps.
In the anomalous phase, the bulk invariant of the Flo-
quet Hamiltonian, regardless of whether it is the quater-
nion charge or Berry phase of Abelian type introduced for
static systems [16], is unable to view the edge-state land-
scape. In fact, the emergence of edge state has dynami-
cal origin and the complete information of the dynamical
topology is encoded in the full-time evolution operator.
A unified analysis of the bulk-edge correspondence can
be achieved through the introduction of phase band and
its associated momentum-time singularities [41, 46–48].
It should be noted that the time-evolution operator U(t)
is not always PT symmetric. To this end, we adopt a PT
symmetric operator ˜U(k, t) via a smooth deformation of
U(t) [49]. ˜U(k, t) preserves the phase-band structure (in-
cluding its singularities) and satisfies ˜U(k, t) = U(k, t) at
t = 0, T. Formally, the operator ˜U(k, t) can be expressed
in terms of the spectral decomposition,
˜U(k, t) =
3
X
n=1
e−iϕn(k,t)|ψn(k, t)⟩⟨ψn(k, t)|,
(3)
where e−iϕn(k,t) denotes the eigenvalues of ˜U(k, t) and
ϕn(k, t) ∈(−π/T, π/T] forms the phase bands in the 2D
momentum-time space.
The phase band may touch and reopen with the vari-
ation of time, leaving degenerate Dirac points in the
bandgaps in the 2D momentum-time space. At t = T, the
phase bands become the quasienergy bands. As shown
in Fig. 2b, the phase bands touch once in each gap for
the anomalous phase. The presence of Dirac singularities
in the phase band leads to the emergence of edge states
in the corresponding gap. As the three gaps are tangled,
each Dirac point can be assigned a quaternion charge
through the Wilson loop along an enclosing path nearby
[49]. The quaternion charge q of the Floquet Hamiltonian
HF is related to the quaternion charge of the phase-band
singularities via
q =
Y
m
˜qm.
(4)
Here m labels the Dirac point, and the multiplication
is ordered such that the concatenation of the small en-
closing paths coincide with the orientation of momentum
integral −π →π.
As a distinction, the charge of the
Dirac singularity is marked with a tilde. In the anoma-
lous FNATI depicted in Fig.
2b, the three singulari-
ties from right to left possess quaternion charge ˜q1 = ˜k,
˜q2 = −˜i, and ˜q3 = ˜j, respectively [See the inset]. It is
evident that the relation 1 = ˜k · (−˜i) · ˜j holds.
Multifold bulk-edge correspondence. The phase-
band singularities and their non-Abelian nature offer
a straightforward interpretation of the bulk-edge corre-
spondence in FNATI. As indicated by Eq. (4), various
patterns of edge states may corresponds to the same
quaternion charge of the Floquet Hamiltonian.
Such
multifold bulk-edge correspondence follows the multipli-
cation rule of the quaternion group Q8.
For example,
in Figs.
1d,e, the two phases with the same quater-
nion charge q = j have distinct edge-state patterns. In
their phase bands, there are two Dirac singularities with
charge ˜k and ˜i for the former, while there is a single
singularity with charge ˜j for the latter.
They satisfy
the multiplication rule ˜k · ˜i = ˜j.
Similar discussions
can be applied to other cases. The multifold bulk-edge
correspondence can be deduced from two key observa-
tions. Firstly, the edge state within each bandgap is de-
termined by the phase-band closings that occur within
that bandgap during time evolution. Each gap closing
results in a change of the mass term and the emergence of
an in-gap mode by Jackiw-Rebbi’s argument [50]. With
multiple bandgaps present, the edge-state patterns are
determined by considering the phase-band singularities
within each bandgap. Secondly, the phase-band singu-
larities relate to the bulk quaternion charge via Eq. (4).
It then becomes evident that the edge-state pattern is
linked to the quaternion charge, and the bulk-edge cor-
respondence showcases a multifold nature that adheres
to the multiplication rule.
In Fig. 3, we present a comprehensive list of bandgap

--- Page 4 ---

4
Quaternion 
charge
Phase-band crossings
Edge states
1
{±�}
{±�}
{±�}
-1
       
FIG. 3. Multifold bulk-edge correspondence for FNATI. The
first column lists the quaternion charge for the Floquet Hamil-
tonian, and the five conjugacy classes of Q8 correspond to dif-
ferent rows. The second and third columns sketch the phase
band structure with singularities depicted by red dots. The
cases with band crossing at the FBZ edge are listed in the
third column.
The fourth/fifth columns sketches the edge-
state patterns corresponding to the phase bands in the sec-
ond/third column.
The black dots represent edge states.
Empty circles mark the fickle edge states. The configurations
unique to Floquet systems are listed in fifth column. The list
applies equally to the domain-wall problem.
closings and their corresponding edge-state patterns
(per edge) for all quaternion charges.
Notably, we
observe similar bandgap closings and edge-state con-
figurations for quaternion charges that belong to the
same conjugacy class, such as ±i.
This is due to the
anti-commutating relations of quaternion charge.
For
example, the existence of a type ˜j and type ˜k singularity
in the phase band (regardless of their ordering) results in
two edge states (located at the first and third bandgap).
Switching them yields conjugate quaternion charges:
˜j · ˜k = −˜k · ˜j. In addition to the patterns that appeared
in the static case (the fourth column) [16], Floquet
systems can exhibit unique edge-state patterns (the
fifth column) because of the additional phase-band
touchings at the FBZ edge. It should be noted that for
a particular gap, multiple touchings can exist [49], such
as i = ˜k · ( ˜
−k) ·˜i, which has two Dirac points in the first
bandgap.
However, such cases can be reduced to the
simpler cases listed in Fig. 3 by eliminating two Dirac
points of the same gap pairwise, resulting in a factor
±1.
Furthermore, in the case of charge q = −1, two
fickle edge states [16] (with an unspecified bandgap) may
appear according to −1 = ˜i2 = ˜j2 = ˜k2, or three separate
edge states may appear according to −1 = ˜i · ˜j · ˜k. We
note that the multifold bulk-edge correspondence can be
25
1
51
0
0.4
0.2
0
a
b
x
y
z
c
FIG. 4. Interface modes with swapped driving as a manifesta-
tion of the non-Abelian topology. a The Floquet setting: two
subsystems connected by an interface have swapped driving
sequences. b Quasienergy spectra and spatial profiles of their
eigenstates with open boundaries at the two ends. A pair of
domain-wall states emerge at the third bandgap. The lattice
length is L = 51, and the interface is located at n = 26.
Other parameters are the same as Fig. 2. c Trajectory of
the transformation O (blue curve) in the parameter space of
SO(3) (represented by a solid ball). As k varies from −π to
π, O follows a closed nontrivial loop that connects a pair of
antipodal points in SO(3). For comparison, the black curve
represents a trivial loop in SO(3).
extended directly to the domain-wall problem. For two
Floquet systems with charge qL and qR, the patterns
of topological domain-wall states between them are
dictated by the quotient qL/qR. Different from the static
case, the bandgap closings across the domain wall are
fully captured by the phase-band singularities, yielding
a multifold bulk-domain-wall correspondence [49]. Last,
our numerical analysis indicates that the edge/domain-
wall states are robust against small disorders.
In the
presence of domain-wall decorations, it is possible for
additional trivial bound states to emerge. However, the
non-trivial domain states, governed by the non-Abelian
topology, remain unaffected [49].
Interface
modes
induced
by
swapped
driv-
ing. Besides the multifold bulk-edge correspondence,
here we uncover a counter-intuitive phenomenon of
FNATI as a manifestation of the Floquet non-Abelian
topology. As illustrated in Fig. 4a, we consider a system
with two sides featuring swapped (mismatched) driving
sequences. Within one full period, the Hamiltonians on

--- Page 5 ---

5
the left and right sides are given by H1 →H2 →H1
and H2 →H1 →H2, respectively.
The bulk Floquet
operators for these two sides, denoted as UL and UR, are
related via a similarity transformation UL = V −1URV
where V = e−iH2T/4e−iH1T/4 accounts for the time shift.
This shift does not alter the quasienergy spectra irre-
spective of the boundary conditions. In Floquet Abelian
topological phases [39, 40], the bulk topological invariant
is defined for each individual quasienergy bandgap (or
branch-cut). The two subsystems should have the same
topological invariant for each bandgap to match with the
edge states, and no stable interface modes are expected
to exist [49]. However, in our non-Abelian system with
multiple intertwined gaps, this is not always true.
In
Fig.
4b, we plot the quasienergy spectra in the pres-
ence of an interface of swapped driving using the same
parameters as Fig. 2. We can clearly observe a pair of
domain-wall states (located near ± π
T ) in the third gap.
The emergence of the interface modes signifies the non-
commutativity of the two driving sequences and it is a
genuine non-Abelian effect of the Floquet dynamics. We
have also verified the appearance of domain-wall states
for other cases with different quaternion charges.
To understand this fascinating effect, we define the
bulk eigenstates of UL and UR on two sides as SL =
(|u1L⟩, |u2L⟩, |u3L⟩) and SR = (|u1R⟩, |u2R⟩, |u3R⟩). With
PT symmetry, they are related by an SO(3) transforma-
tion SL = OSR, with O = SLST
R (T denotes transpo-
sition).
It is important to note that O may alter the
quaternion charge.
In particular, when O corresponds
to the non-identity element in the fundamental group
π1(SO(3)) = Z2, the bulk quaternion charge for the two
sides satisfy qL = −qR. In fact, according to the exact
sequence of homotopy groups [51]:
· · · →π1(SO(3))
j1
−→π1(SO(3)
D2
)
∂1
−→π0(D2)
i0
−→0, (5)
the kernel of ∂1-mapping is {1, −1} in π1( SO(3)
D2 ) = Q8.
Thus j1 maps the non-identity element of Z2 to −1 in
Q8. For our case, O traces a nontrivial path in SO(3)
as the momentum k varies from −π to π [See Fig. 4c].
UL has a quaternion charge of qL = 1, while UR has
qR = −1, indicating the emergence of domain-wall states.
Alternatively, one can scrutinize this effect through the
phase-band singularities [49]. With time variation, the
phase band undergoes crossings with charge ˜k, −˜i, ˜j and
−˜k,˜i, −˜j for UL and UR, respectively. They satisfy Eq.
(4), qL = 1 = ˜k · (−˜i) · ˜j and qR = −1 = (−˜k) ·˜i · (−˜j).
Discussion. In summary, our exploration of the
FNATI represents a significant advancement in the
field of out-of-equilibrium topological phases. We have
demonstrated the implementation of FNATI through
step-like driving and fully characterized its topological
properties via phase-band singularities. Our analysis re-
vealed a multifold bulk-edge correspondence, governed by
the multiplication rule of the quaternion group Q8. We
have identified an anomalous phase that possesses edge
modes within all bandgaps despite a trivial bulk, which
lacks a static analog. Furthermore, we have uncovered a
novel interface effect resulting from swapped driving that
serves as a key signature of the non-Abelian topology.
Our findings offer novel insights into Floquet topo-
logical phases with multiple intertwined bandgaps. Our
results can be extended to higher-band cases, such as
a four-band topological insulator characterized by the
non-Abelian group Q16 [17]. In higher dimensions, the
phase-band singularities may extend to nodal lines, and
it would be intriguing to explore their interwinding in
momentum-time space and the associated non-Abelian
effects. From a wider perspective, the multi-gap topology
belongs to the fragile topology and relies on the partition
of energy bands [10]. A different partition (2 + 1) yields
a different flag manifold RP2 and is relevant for the
Floquet Euler phase [14]. Other tantalizing extensions
include the 3D nodal-line metals [8] characterized by
non-Abelian frame charges and non-Hermitian phases
with non-Abelian band braidings [52–54] by relaxing the
PT symmetry to allow for a complex flag manifold. A
natural issue is how these non-Abelian features interplay
with Floquet driving. Besides the step-like driving uti-
lized for illustration purposes, smooth Floquet driving
should also be suitable for implementing FNATI. With
the high feasibility of Floquet engineering [32–41] and
the ability to manipulate tight-binding models in various
platforms, such as ultracold atoms [45, 55–58], photonic
or acoustic materials [43, 44, 59, 60], we anticipate that
the uncharted FNATI and non-Abelian effect will be
observed in near-future experiments.
Methods
Calculation of quaternion charge. The quaternion
charge q ∈Q8 characterizes the rotations of the eigen-
state frame as the momentum k varies from −π to π. In
the case of the Dirac singularity in the phase band, the
quaternion charge describes the frame rotation along the
enclosing path. According to Ref. [8], the generalized
Wilson operator can be used to obtain the quaternion
charge. Formally, the Wilson loop along a closed path Γ
is defined as follows:
WΓ = Pe
H
Γ Aall(k)·dk.
(6)
Here, [Aall(k)]mn
= ⟨um(k)|∂k|un(k)⟩represents the
Berry-Wilczek-Zee connection. The band indices m and
n take values from 1 to 3, and |un(k)⟩is the eigenstate of
the Floquet Hamiltonian HF . For the Dirac-point case,
we use the phase band instead. Aall(k) is anti-symmetric
and can be decomposed into the so(3) Lie-algebra basis:
Aall(k) =
X
i=1,2,3
βiLi,
(7)
where (Li)jk = −ϵijk and ϵijk is the anti-symmetric ten-
sor. We then lift Aall to the spin(3)-valued 1-form [8] by
replacing Li with ti, where ti = −i
2σi and σi represents

--- Page 6 ---

6
the Pauli matrix. This gives us:
Aall(k) =
X
i=1,2,3
βiti.
(8)
Finally, the non-Abelian charge is defined by:
q = Pe
H
Γ Aall(k)·dk.
(9)
The elements of the quaternion group are represented by
1 →σ0, i →−iσx, j →−iσy, and k →−iσz.
Smooth deformation of time evolution. To de-
fine the quaternion charge of the Dirac singularity, real
wave functions of the phase bands are required. To this
end, we smoothly deform U(k, t) into ˜U(k, t) such that
˜U ∗(k, t) ˜U(k, t) = 1 for all t ∈[0, 1] (we set T = 1 for con-
venience). The time evolution operator for our driving
protocol is
U =





e−iH1t,
t ∈[0, 1/4],
e−iH2(t−1/4)e−iH1/4,
t ∈[1/4, 3/4],
e−iH1(t−3/4)e−iH2/2e−iH1/4,
t ∈[3/4, 1].
(10)
We can define the PT symmetric operator ˜U(k, t) as
˜U =







e−iH1t,
t ∈[0, 1/4],
e−iH1/8e−iH2(t−1/4)e−iH1/8, t ∈[1/4, 3/4],
e−i
2 (t−1
2 )H1e−iH2/2e−i
2 (t−1
2 )H1, t ∈[3/4, 1].
(11)
To visualize the smoothness of the deformation, let us
consider the continuous interpolation between them:
U(s, k, t) =
(12)





e−iH1t,
t ∈[0, 1/4],
e−iH1 s
8 e−iH2(t−1/4)e−iH1(1−s
2 ) 1
4 , t ∈[1/4, 3/4],
e−i[(1−s
2 )t+ 2s−3
4
]H1e−iH2/2e−i( s
2 t+ 1−2s
4
)H1, t ∈[3/4, 1],
such that U(s = 0, k, t) = U(k, t) and U(s = 1, k, t) =
˜U(k, t). During the deformation from s = 0 to s = 1, the
phase bands and the Dirac singularities are unchanged.
Coefficients of the tight binding model. The co-
efficients used in the paper are listed in Table I. In all
the cases, we take sAA = sBB = sCC = 0, sAB = sBA =
r, sBC = sCB = s, sCA = sAC = t and vAB = vBA =
iu, vBC = vCB = iv, vCA = vAC = iw, where r, s, t, u, v
and w are all real numbers.
Data availability
All data is available upon reasonable request.
Code availability
The code that support the findings of this study are avail-
able at https://doi.org/10.5281/zenodo.8294074.
References
[1] X. -L. Qi and S. -C. Zhang, Topological insulators and
superconductors. Rev. Mod. Phys. 83, 1057–1110 (2011).
doi: 10.1103/RevModPhys.83.1057
[2] M. Z. Hasan and C. L. Kane, Colloquium: topological
insulators. Rev. Mod. Phys. 82, 3045–3067 (2010). doi:
10.1103/RevModPhys.82.3045
[3] A. Altland and M. R. Zirnbauer, Nonstandard symme-
try classes in mesoscopic normal-superconducting hy-
brid structures. Phys. Rev. B 55,
1142(1997). doi:
10.1103/PhysRevB.55.1142
[4] S. Ryu, A. P. Schnyder, A. Furusaki and A. W. W. Lud-
wig, Topological insulators and superconductors:
ten-
fold way and dimensional hierarchy. New J. Phys. 12,
065010(2010). doi: 10.1088/1367-2630/12/6/065010
[5] A. P. Schnyder, S. Ryu, A. Furusaki and A. W. W. Lud-
wig, Classification of topological insulators and super-
conductors in three spatial dimensions, Phys. Rev. B 78,
195125(2008). doi: 10.1103/PhysRevB.78.195125
[6] A. Kitaev, Periodic table for topological insulators and
superconductors, AIP Conference Proceedings 1134, 22
(2009). doi: 10.1063/1.3149495
[7] C. -K. Chiu, J. C. Y. Teo, A. P. Schnyder and S.
Ryu, Classification of topological quantum matter with
symmetries. Rev. Mod. Phys. 88, 035005(2016). doi:
10.1103/RevModPhys.88.035005
[8] Q. Wu, A. A. Soluyanov and T. Bzdusek, Non-Abelian
band topology in noninteracting metals. Science 365,
1273–1277 (2019). doi: 10.1126/science.aau8740
[9] J. Ahn, S. Park and B.-J. Yang, Failure of Nielsen-
Ninomiya
Theorem
and
Fragile
Topology
in
Two-
Dimensional Systems with Space-Time Inversion Symme-
try: Application to Twisted Bilayer Graphene at Magic
Angle. Phys. Rev. X 9, 021013(2019).doi: 10.1103/Phys-
RevX.9.021013
[10] A. Bouhon, T. Bzdusek and R.-J. Slager, Geometric ap-
proach to fragile topology beyond symmetry indicators.
Phys. Rev. B 102, 115135 (2020).doi:
10.1103/Phys-
RevB.102.115135
[11] C.-X. Guo, S. Chen, K. Ding and H. Hu, Exceptional
Non-Abelian Topology in Multiband Non-Hermitian
Systems. Phys. Rev. Lett. 130,
157201 (2023).doi:
10.1103/PhysRevLett.130.157201
[12] B. Jiang, A. Bouhon, Z.-K. Lin, X. Zhou, B. Hou, F. Li,
R.-J. Slager and J.-H. Jiang, Experimental observation
of non-Abelian topological acoustic semimetals and their
phase transitions. Nat. Phys. 17, 1239–1246 (2021).doi:
10.1038/s41567-021-01340-x
[13] B. Jiang, A. Bouhon, S.-Q. Wu, Z.-L. Kong, Z.-K.
Lin, R.-J. Slager and J.-H. Jiang, Experimental obser-
vation of meronic topological acoustic Euler insulators.
arXiv:2205.03429 (2022).doi: 10.48550/arXiv.2205.03429
[14] R. -J. Slager,
A. Bouhon and F. N.Unal,
Floquet

--- Page 7 ---

7
multi-gap topology: Non-Abelian braiding and anoma-
lous Dirac string phase. arXiv:2208.12824 (2022). doi:
10.48550/arXiv.2208.12824
[15] F. N. Unal, A. Bouhon and R. -J. Slager, Topological
Euler Class as a Dynamical Observable in Optical Lat-
tices. Phys. Rev. Lett. 125, 053601 (2020). doi: Phys-
RevLett.125.053601
[16] Q. Guo, T. Jiang, R.-Y. Zhang, L. Zhang, Z.-Q. Zhang,
B. Yang, S. Zhang and C. T. Chan, Experimental ob-
servation of non-Abelian topological charges and edge
states. Nature 594, 7862 (2021). doi: 10.1038/s41586-
021-03521-3
[17] T. Jiang, Q. Guo, R.-Y. Zhang, Z.-Q. Zhang, B. Yang and
C. T. Chan, Four-band non-Abelian topological insulator
and its experimental realization. Nat. Commun. 12, 6471
(2021). doi: 10.1038/s41467-021-26763-1
[18] G. P. Alexander, B. G. Chen, E. A. Matsumoto and R.
D. Kamien, Disclination loops, point defects, and all that
in nematic liquid crystals. Rev. Mod. Phys. 84, 497514
(2012). doi: 10.1103/RevModPhys.84.497
[19] G. E. Volovik and V. P. Mineev, Investigation of singular-
ities in superfluid He3 in liquid crystals by the homotopic
topology methods. Zh. Eksp. Teor. Fiz. 72, 2256–2274
(1977). doi: 10.1051/jphys:01977003808088700
[20] V. Poenaru and G. Toulouse,
The crossing of de-
fects
in
ordered
media
and
the
topology
of
3-
manifolds. J. Phys. Lett. 38,
887–895 (1977). doi:
10.1051/jphys:01977003808088700
[21] L. A. Madsen, T. J. Dingemans, M. Nakata and E. T.
Samulski, Thermotropic biaxial nematic liquid crystals.
Phys. Rev. Lett. 92, 145505 (2004). doi: 10.1103/Phys-
RevLett.92.145505
[22] K. Liu, J. Nissinen, R.-J. Slager, K. Wu and J. Zaanen,
Generalized liquid crystals: giant fluctuations and the
vestigial chiral order of I, O and T matter. Phys. Rev. X
6, 041025 (2016). doi: 10.1103/PhysRevX.6.041025
[23] A. Tiwari and T. Bzdusek, Non-Abelian topology of
nodal-line rings in PT-symmetric systems. Phys. Rev. B
101, 195130 (2020). doi: 10.1103/PhysRevB.101.195130
[24] E. Yang, B. Yang, O. You, H.-C. Chan, P. Mao, Q.
Guo, S. Ma, L. Xia, D. Fan, Y. Xiang and S. Zhang,
Observation of Non-Abelian Nodal Links in Photonics.
Phys. Rev. Lett. 125, 033901 (2020). doi: 10.1103/Phys-
RevLett.125.033901
[25] D. Wang, B. Yang, Q. Guo, R.-Y. Zhang, L. Xia, X. Su,
W.-J. Chen, J. Han, S. Zhang and C. T. Chan, Intrinsic
in-plane nodal chain and generalized quaternion charge
protected nodal link in photonics. Light.: Sci. Appl. 10,
83 (2021). doi: 10.1038/s41377-021-00523-8
[26] H. Park, S. Wong, X. Zhang and S. S. Oh, Non-
Abelian Charged Nodal Links In Dielectric Photonic
Crystal. ACS Photonics 2021, 8, 9, 2746–2754(2021). doi:
10.1021/acsphotonics.1c00876
[27] M. Wang, S. Liu, Q. Ma, R.-Y. Zhang, D. Wang, Q.
Guo, B. Yang, M. Ke, Z. Liu and C. T. Chan, Experi-
mental observation of non-Abelian earring nodal links in
phononic crystals. Phys. Rev. Lett. 128, 246601 (2022).
doi: 10.1103/PhysRevLett.128.246601
[28] A. Bouhon, Q. S. Wu, R. -J. Slager, H. Weng, O. V.
Yazyev and T. Bzdusek, Non-Abelian reciprocal braiding
of Weyl points and its manifestation in ZrTe. Nat. Phys.
16, 1137-1143(2020). doi: 10.1038/s41567-020-0967-9
[29] B. Peng, A. Bouhon, R.-J. Slager and B. Monserrat,
Multi-gap topology and non-Abelian braiding of phonons
from first principles. Phys. Rev. B 105, 085115 (2022).
doi: 10.1103/PhysRevB.105.085115
[30] B. Peng, A. Bouhon, B. Monserrat and R.-. Slager,
Phonons as a platform for non-Abelian braiding and its
manifestation in layered silicates. Nat. Commun. 13, 423
(2022). doi: 10.1038/s41467-022-28046-9
[31] H. Qiu, Q. Zhang, T. Liu, X. Fan, F. Zhang and C. Qiu,
Minimal non-abelian nodal braiding in ideal metamateri-
als. Nat. Commun. 14, 1261 (2023). doi: 10.1038s41467-
023-36952-9
[32] T. Kitagawa, E. Berg, M. Rudner and E. Demler,
Topological characterization of periodically driven quan-
tum systems. Phys. Rev. B 82,
235114(2010). doi:
10.1103/PhysRevB.82.235114
[33] L. Jiang, T. Kitagawa, J. Alicea, A. R. Akhmerov,
D. Pekker, G. Refael, J. I. Cirac, E. Demler, M. D.
Lukin, and P. Zoller, Majorana Fermions in Equilib-
rium and in Driven Cold-Atom Quantum Wires. Phys.
Rev. Lett. 106, 220402 (2011). doi:
10.1103/Phys-
RevLett.106.220402
[34] A. Eckardt, Colloquium: Atomic quantum gases in pe-
riodically driven optical lattices. Rev. Mod. Phys. 2,
305(1930). doi: 10.1103/RevModPhys.89.011004
[35] J. Cayssol, B. Dra, F. Simon and R. Moessner, Floquet
topological insulators. Phys. Status Solidi RRL 7, 101
(2013). doi: 10.1002/pssr.201206451
[36] M. S. Rudner and N. H. Lindner, Band structure engi-
neering and non-equilibrium dynamics in Floquet topo-
logical insulators. Nature Reviews Physics 2, 229 (2020).
doi: 10.1038/s42254-020-0170-z
[37] N. H. Lindner, G. Refael and V. Galitski, Floquet topo-
logical insulator in semiconductor quantum wells, Nat.
Phys. 7, 490 (2011). doi: 10.1038/nphys1926
[38] M.
Lababidi,
I.
I.
Satija
and
E.
Zhao,
Counter-
propagating edge modes and topological phases of a
kicked quantum Hall system. Phys. Rev. Lett. 112,
026805 (2014). doi: 10.1103/PhysRevLett.112.026805
[39] R. Roy and F. Harper, Periodic table for Floquet topo-
logical insulators. Phys. Rev. B 96, 155118 (2017). doi:
10.1103/PhysRevB.96.155118
[40] S. Yao, Z. Yan and Z. Wang, Topological invariants of
Floquet systems: General formulation, special proper-
ties, and Floquet topological defects. Phys. Rev. B 96,
195303 (2017). doi: 10.1103/PhysRevB.96.195303
[41] F. N. Unal, B. Seradjeh and A. Eckardt, How to Di-
rectly Measure Floquet Topological Invariants in Opti-
cal Lattices. Phys. Rev. Lett. 122, 253601 (2019). doi:
10.1103/PhysRevLett.122.253601
[42] M. S. Rudner, N. H. Lindner, E. Berg and M. Levin,
Anomalous Edge States and the Bulk-Edge Correspon-
dence for Periodically Driven Two-Dimensional Systems.
Phy. Rev. X 3, 031005 (2013). doi:
10.1103/Phys-
RevX.3.031005
[43] L. J. Maczewsky, J. M. Zeuner, S. Nolte and A. Sza-
meit, Observation of photonic anomalous Floquet topo-
logical insulators. Nat. Commun. 8, 13756 (2017). doi:
10.1038/ncomms13756
[44] S. Mukherjee, A. Spracklen, M. Valiente, E. Andersson,
P. Ohberg, N. Goldman and R. R. Thomson, Experimen-
tal observation of anomalous topological edge modes in
a slowly driven photonic lattice. Nat. Commun. 8, 13918
(2017). doi: 10.1038/ncomms13918
[45] K. Wintersperger, C. Braun, F. N. Unal, A. Eckardt, M.
D. Liberto, N. Goldman, I. Bloch and M. Aidelsburger,

--- Page 8 ---

8
Realization of an anomalous Floquet topological system
with ultracold atoms. Nat. Phys. 16, 1058 (2020). doi:
10.1038/s41567-020-0949-y
[46] F. Nathan and M. S. Rudner, Topological singularities
and the general classification of Floquet Bloch systems.
New J. Phys. 17, 125014 (2015). doi:
10.1088/1367-
2630/17/12/125014
[47] H. Hu, B. Huang, E. Zhao and W. V. Liu, Dynam-
ical Singularities of Floquet Higher-Order Topological
Insulators. Phys. Rev. Lett. 124, 057001 (2020). doi:
10.1103/PhysRevLett.124.057001
[48] H. Hu and E. Zhao, Topological invariants for quan-
tum quench dynamics from unitary evolution. Phys.
Rev. Lett. 124, 160402 (2020). doi:
10.1103/Phys-
RevLett.124.160402
[49] See Supplementary Material for additional details on the
multiplication rule in Eq. (4), examples with multiple
Dirac singularities in the same gap, the phase-band ex-
planation of the interface effect, the quotient relation
in domain-wall problem, the Zak phase of quasienergy
bands, and the stability of edge/domain-wall states.
[50] S. -Q. Shen, Topological insulators , pages 19-22 (Berlin:
Springer, 2012).
[51] A. Hatcher, Algebraic Topology (Cambridge University
Press, Cambridge, UK, 2002).
[52] C. C. Wojcik, X. -Q. Sun, T. Bzduˇsek and S. Fan, Ho-
motopy characterization of non-Hermitian Hamiltonians.
Phys. Rev. B. 101, 205417 (2020). doi: 10.1103/Phys-
RevB.101.205417
[53] Z. Li and R. S. K. Mong, Homotopical characterization
of non-Hermitian band structures. Phys. Rev. B 103,
155129 (2021). doi: 10.1103/PhysRevB.103.155129
[54] H. Hu and E. Zhao, Knots and Non-Hermitian Bloch
Bands. Phys. Rev. Lett. 126,
010401 (2021). doi:
10.1103/PhysRevLett.126.010401
[55] N. R. Cooper, J. Dalibard and I. B. Spielman, Topo-
logical bands for ultracold atoms. Rev. Mod. Phys. 91,
015005 (2019). doi: 10.1103/RevModPhys.91.015005
[56] G. Jotzu, M. Messer, R. Desbuquois, M. Lebrat, T.
Uehlinger, D. Greif and T. Esslinger, Experimental real-
ization of the topological Haldane model with ultracold
fermions. Nature 515, 237–240 (2014). doi: 10.1038/na-
ture13915
[57] C. D. Brown, S.-W. Chang, M. N. Schwarz, T. -H.
Leung, V. Kozii, A. Avdoshkin, J. E. Moore and D.
Stamper-Kurn, Direct geometric probe of singularities
in band structure. Science 377, 1319-1322 (2022). doi:
10.1126/science.abm6442
[58] T. -H. Leung, M. N. Schwarz, S.-W. Chang, C. D. Brown,
G. Unnikrishnan and D. Stamper-Kurn, Interaction-
enhanced group velocity of bosons in the flat band of
an optical kagome lattice. Phys. Rev. Lett. 125, 133001
(2020). doi: 10.1103/PhysRevLett.125.133001
[59] Y. -K. Sun, X. -L. Zhang, F. Yu, Z.-N. Tian, Q. -D.
Chen and H.-B. Sun, Non-Abelian Thouless pumping in
photonic waveguides. Nat. Phys. 18, 1080–1085 (2022).
doi: 10.1038/s41567-022-01669-x
[60] O. You, S. Liang, B. Xie, W. Gao, W. Ye, J. Zhu and
S. Zhang, Observation of Non-Abelian Thouless Pump.
Phys. Rev. Lett. 128, 244302 (2022). doi: 10.1103/Phys-
RevLett.128.244302
Acknowledgments
This work is supported by the National Key Re-
search and Development Program of China (Grant
No. 2022YFA1405800) and the start-up grant of IOP-
CAS. T. L. also acknowledges the support from the
Project Funded by China Postdoctoral Science Founda-
tion (Grant No. 2023M733719).
Author contributions
H.H. conceived the main idea, and performed the theo-
retical analysis with T. L. T. L. did the numerical cal-
culations. Both authors contribute to the writing of the
paper.
Competing interests
The authors declare no competing interests.
Tables
TABLE I. Coefficients used in the paper.
q
r s t
u
v
w
vAA vBB vCC
j [Fig. 1d]
1 1 2
2
0
0
0
-2
2
j [Fig. 1e]
1 0 4
3
0
0
-1
0
1
1 [Fig. 2a]
1 0 3
0
0
-3
-2
0
2
i [Fig. S2a]
1 0 1
0
1
1
-1
0
1
−1 [Fig. S2b]
1 0 1
-1
0
1
0
-2
2
j [Fig. S4ab(left)] 1 0 4
3
0
0
-1
0
1
j [Fig. S4a(right)] 1 1 2
2
0
0
0
-2
2
j [Fig. S4b(right)] 1 0 4 1.4 0 1.4
-2
0
2
i [Fig. S5-S7]
1 0 2
0
1
1
-2
0
2
k [Fig. S5-S7]
1 1 1
-1
1
0
0
-1
1

--- Page 9 ---

9
Supplemental Material for “Floquet Non-Abelian Topological Insulator and Multifold
Bulk-Edge Correspondence”
This supplemental material provides additional details on the multiplication rule of Dirac sin-
gularities in the phase band, examples with multiple Dirac touchings in the same gap, the phase-
band picture of the interface effect, the quotient relation in domain-wall problem, the Zak phase of
quasienergy bands, and the stability of edge/domain-wall states.
Appendix A: Multiplication rule of Dirac singularities
In the main text, we have established a relationship between the quaternion charge q of the Floquet
Hamiltonian and the charges of the Dirac singularities. This is expressed through the equation:
q =
Y
m
˜qm,
(A1)
In the equation, we stipulate that the multiplication is from left to right. Since the quaternion group
Q8 is non-Abelian, the ordering in the product is important. We use Fig. S1 to illustrate our choice
of ordering in the 2D momentum-time space. Firstly, all the enclosing paths of the Dirac points
share the same starting point P. Secondly, the composition of these paths, i.e., the concatenation
of paths in the fundamental group, should be smoothly deformed to the boundaries of the 2D (k, t)
space clockwise. For example, in Fig. S1, the path concatenation associated with the multiplication
˜q1 · ˜q2 · ... · ˜qn is equivalent to circling around the boundaries of the 2D (k, t) space clockwise. On
the other hand, the path concatenation associated with the multiplication ˜qn · ˜qn−1 · ... · ˜q2 · ˜q1 is
equivalent to circling around the boundaries counterclockwise. Notably, the former coincides with
the integral taken from −π to π in calculating the quaternion charge of the Floquet Hamiltonian.
-1
0
1
0
0.5
1
FIG. S1. Path concatenation and ordering of Dirac singularities. The quarternion charge q of the Floquet Hamiltonian is
related to the charges of the singularities through q = ˜q1 · ˜q2 · ... · ˜qn.
Appendix B: Examples with multiple phase-band touchings in the same gap
In the main text, we have listed all the phase-band patterns with at most one touching in each gap
in Fig. 3. In principle, multiple touchings within the same gap are possible, as demonstrated by two
such cases in Fig. S2a and b. Specifically, in Fig. S2a, the quaternion charge of the bulk Floquet
Hamiltonian and the Dirac points are related through i = −˜k · ˜k · ˜i, while in Fig. S2b, they are

--- Page 10 ---

10
related through −1 = (−˜i)· ˜k ·(−˜i)· ˜k. Furthermore, we have plotted the corresponding quasienergy
spectra and spatial distributions of eigenstates under open boundary conditions in Figs. S2c and d.
For the former, we observe the existence of a single edge state in the second gap. For the latter, we
observe a pair of edge states for the first and second gap, respectively.
a
b
c
d
FIG. S2. Phase bands with multiple touchings in the same gap. a Phase bands with bulk quaternion charge q = i for the
Floquet Hamiltonian. It is related to the charges of the Dirac points through i = −˜k · ˜k ·˜i. b Phase bands with bulk quaternion
charge q = −1 for the Floquet Hamiltonian. It is related to the charges of the Dirac points through −1 = (−˜i) · ˜k · (−˜i) · ˜k. c,
d Quasienergy spectra and the spatial distributions of eigenstates with open boundaries corresponding to the phase bands in
a, b, respectively. The lattice length is L = 50. The parameters are listed in Methods.
Appendix C: Interface effect from the phase-band picture
An alternative explanation of the emergence of interface modes is from the phase-band picture.
The bulk Floquet operators on the left and right sides are UL = e−iH1T/4e−iH2T/2e−iH1T/4 and UR =
e−iH2T/4e−iH1T/2e−iH2T/4, respectively. We denote their bulk quaternion charges as qL and qR. Let
us formally consider the two PT symmetric operators as below:
˜U (1)(k, t) =
(
e−iH1t,
t ∈[0, 1/2],
e−iH1/4e−iH2(t−1/2)e−iH1/4, t ∈[1/2, 1],
(C1)
˜U (2)(k, t) =
(
e−iH1t,
t ∈[0, 1/2],
e−iH2(t−1/2)/2e−iH1/2e−iH2(t−1/2)/2,
t ∈[1/2, 1].
(C2)
˜U (1)(k, t) and ˜U (2)(k, t) are related by an SO(3) transform, and thus have the same phase bands. At
t = T, the phase bands of ˜U (1)(k, T) and ˜U (2)(k, T) coincide with the bulk quasienergy bands of UL
and UR, respectively:
˜U (1)(k, T) = UL,
˜U (2)(k, T) = UR.
(C3)

--- Page 11 ---

11
Our numerical analysis shows that there are three Dirac singularities with charges ˜k, −˜i, and ˜j
for ˜U (1)(k, t) and three Dirac singularities with charges −˜k, ˜i, and −˜j for ˜U (2)(k, t). According to
Eq. (A1), the quaternion charge of the bulk Floquet Hamiltonian is qL = ˜k · (−˜i) · ˜j = 1, and
qR = −˜k ·˜i · (−˜j) = −1. Therefore, domain-wall states are expected to emerge at the interface.
Appendix D: Quotient relation in the domain-wall problem
In this section, we address the domain-wall problem for Floquet non-Abelian topological insulators
(FNATIs). As depicted in Fig. S3a, let us denote qL and qR as the bulk quaternion charge of the
Floquet Hamiltonian on the left and right side, respectively. In the static case, the appearance of
domain-wall states between two topologically distinct phases is governed by the quotient relation
∆q = qL/qR. We demonstrate that in the Floquet setting, the quotient relation still holds. However,
due to the additional bandgap across the Floquet Brillouin zone edge, the quotient relation implies
a multifold bulk-domain-wall correspondence. For specific values of qL and qR, their quotient ∆q is
definite, but the domain-wall states may exhibit different configurations, as summarized in Fig. 3
of the main text. In fact, the edge-state patterns listed in Fig. 3 can be seen as a special case of
the domain-wall problem, where the system interfaces with the vacuum. Considering its multifold
nature, determining the domain-wall states requires additional information about the phase-band
singularities. These singularities are related to the bulk quaternion charge through qL = ˜qL1˜qL2...
and qR = ˜qR1˜qR2..., respectively. We proceed to demonstrate the quotient relation using three steps.
a
Domain-wall states 
Δ�= ��
−1��
Δ �= ��
−1��= (��1��2…)−1 (��1��2…)
��
�
�
�
�
�
�
��
��2
��1
��1
��2
��
��
v
v
v
v
Δ�
Edge state
Edge state
b
c
�3
FIG. S3. Quotient relation of Floquet non-Abelian topological insulators (FNATIs). a Sketch of the domain wall, where the
left and right sides correspond to bulk Hamiltonians with quaternion charges qL and qR, respectively. The domain wall is
described by the quotient relation ∆q = q−1
R qL. b Geometric visualization of the quaternion charge as a closed path (loop) in
the configuration space M3. The black dot is the base point. The change in quaternion charge from qR (blue) to qL (orange) is
given by ∆q (dotted black loop), and the concatenated path qR∆q is equivalent to qL. c Relationship between the quaternion
charge and the phase-band singularities.
Firstly, between two distinct topological phases, there are bandgap closings at the domain wall,
corresponding to the topological phase transition. This holds true for both static and Floquet cases.
Importantly, in Floquet systems, two systems being topologically distinct implies different phase-

--- Page 12 ---

12
band singularities or edge-state patterns. In Fig. 3 of the main text, for the same quaternion charge,
there may be multiple distinct phases due to their different phase-band singularities.
Secondly, the details of the bandgap closings, such as their position and times, are encoded in the
quotient relation ∆q = q−1
R qL. (Here qL/qR is treated as q−1
R qL; the other choice qLq−1
R is also fine as
they are conjugate). To visualize this, we remind that the quaternion charge is the first homotopy
invariant of the configuration space M3 =
O(3)
O(1)3 of PT-symmetric Hamiltonians. Geometrically, the
quaternion charge can be represented as a closed path in M3 space, as depicted in Fig. S3b. At the
domain wall, the quaternion charge undergoes a change from qR to qL through gap closings. This
change is described by an intermediate path (the dotted black loop) denoted as ∆q. In homotopy
language, concatenating the two paths qR∆q, first following qR and then ∆q, yields the path qL:
qL = qR∆q. Thus, we have ∆q = q−1
R qL. In Floquet systems, the quaternion charge on each side is
further related to the phase-band singularities through Eq. (4) in the main text, as sketched in Fig.
S3c. Consequently, we have ∆q = q−1
R qL = (˜qR1˜qR2...)−1(˜qL1˜qL2...).
Thirdly, the gap closings recorded in the ∆q above give rise to domain-wall states through the
Jackiw-Rebbi argument [50]: the number and locations of the gap closings determine the number
of edge states in that gap. In other words, whenever there is a gap closing, a domain-wall state
appears. By accounting for all gap closings inside ∆q represented by the phase-band singularities,
we can determine the patterns of domain-wall states.
a
b
FIG. S4. Quasienergy spectra and spatial distributions of the eigenstates in the presence of a domain wall. The bulk quaternion
charge for both sides is qL = qR = j. a A domain wall between qL = j (with singularity ˜j) and qR = j (with singularity ˜k˜i)
possesses three domain-wall states (one in each gap), as per ∆q = 1 = (˜i˜k)˜j. b A domain wall between qL = j (with singularity
˜j) and qR = j (with singularity ˜j) does not possess any domain-wall state.
To compare with the static case and demonstrate the multifold nature of Floquet systems, let us
consider a domain wall between two Floquet Hamiltonians of the same charge, qL = qR = j, as
shown in Fig. S4. The quotient is ∆q = 1. The domain wall between qL = j (with singularity ˜j) and
qR = j (with singularity ˜k˜i) possesses three domain-wall states as ∆q = (˜i˜k)˜j [See Fig. S4a]. On
the other hand, the domain wall between qL = j (with singularity ˜j) and qR = j (with singularity ˜j)
possesses no domain-wall state [See Fig. S4b]. The two different configurations are consistent with
the charge 1 class listed in Fig. 3 of the main text.
Appendix E: Zak phase of the quasienergy band
Besides the quaternion charge, the Zak phase is another topological invariant that is assigned to
each quasienergy band. The Zak phase can take two values, 0 or π. To calculate the Zak phase,
we diagonalize the Floquet Hamiltonian HF(k) = S(k)diag(ϵ1, ϵ2, ϵ3)ST(k). Here, the eigenvectors

--- Page 13 ---

13
are organized in the SO(3) transformation S(k) = (|u1⟩, |u2⟩, |u3⟩). The Zak phase can be extracted
from the evolution of these eigenvectors with respect to the lattice momentum k. As k ranges from
−π to π, the eigenvector |uj⟩(j = 1, 2, 3) may acquire an additional sign in a continuous manner,
|uj(k = π)⟩= −|uj(k = −π)⟩. This corresponds to the Zak phase taking π for the j-th band.
Otherwise, the Zak phase takes 0. Formally, one can consider the matrix S(π)TS(−π), which takes
the form of diag(λ1, λ2, λ3). λj (j = 1, 2, 3) = ±1. The Zak phase of the j-th band is 0 (π) if λj = 1
(λj = −1) [17]. It should be noted that in the static case [16], the Zak phase also takes other values,
such as −π and 2π. They are introduced solely to distinguish between two conjugate elements in
the same class. ±π are associated with different gauge choices of the eigenstates, and treated as the
same here. We list the obtained Zak phases for all quaternion charges below:
TABLE S1. Zak phase of the quasienergy band
q
1
{±i}
{±j}
{±k}
-1
Third band
0
π
π
0
0
Second band
0
π
0
π
0
First band
0
0
π
π
0
In the same conjugacy class (e.g., i and −i), the Zak phase pattern is the same. The constraint
that the summation of Zak phases for all three bands equals 0 (mod 2π) leads to four possible
Zak phase patterns. Since there are five conjugacy classes in the quaternion group Q, the class
−1 falls outside the scope of the Zak-phase description. Furthermore, the Zak phase is defined for
the Floquet Hamiltonian, while the topology of the system is fully encoded in the time-evolution
operator or phase-band singularities. As discussed in the main text, the bulk-edge (or domain-wall)
correspondence is multifold. Different patterns of edge states (domain-wall states) can have the
same quaternion charge and Zak phase configuration. Therefore, the quaternion charge or the Zak
phase is insufficient to predict the edge states, and descriptions based on phase-band singularities
are necessary.
Appendix F: Stability of edge/domain-wall states
In this section, we conduct numerical studies to test the stability of edge states and domain-wall
states. We start by varying the boundary conditions and showcase the emergence of edge states.
Starting from the periodic boundary condition, we gradually decrease the coupling strengths between
the first and the last (N-th) unit cell: vXY,N = (1−α)vXY . Here vXY represents the intercell coupling
in the bulk [See the model, Eq. (1) in the main text], and vXY,N denotes the intercell coupling between
the first and the last unit cell. In Fig. S5a, b, we plot the quasienergy bands for quaternion charges
i (with phase-band singularity ˜i) and k (with phase-band singularity ˜k), respectively. By varying α
continuously from 0 (periodic boundary condition) to 1 (open boundary condition), we observe the
appearance of edge states in the second gap for charge i and the first gap for charge k, detached
from neighboring bands.
We proceed to examine the robustness of the edge states by introducing onsite disorder: sXX,n =
sXX + δ (n = 1, 2, . . . N, X = A, B, C). Here, δ is taken from the uniform distribution of [−W, W],
with W representing the disorder strength. The numerical results are presented in Fig. S5c, d. It
is evident that the edge states persist as long as the bulk quasienergy gaps are not closed by the
disorder.
To test the stability of the domain-wall states, we consider four different types of domain walls,
as depicted in Fig. S6a-d. In Fig. S6a, b, the intracell couplings sXY of the interface unit cell are
set to be the same as those on the left and right sides, respectively. In Fig. S6c, d, the intracell

--- Page 14 ---

14
a
c
b
d
FIG. S5. Stability of edge states in the presence of disorder. a, b Quasienergy spectra for quaternion charges i and k as a
function of the boundary coupling strength α. The intercell coupling across the boundary is vXY,N = (1 −α)vXY , where α = 0
and α = 1 correspond to periodic and open boundary conditions, respectively. The in-gap edge modes (red lines) emerge from
the neighboring bulk bands. c, d Quasienergy spectra under open boundary condition as a function of the disorder strength
W. The edge states are encircled by red ellipses. The parameters used are listed in Table 1.
couplings are set to zero for the interface unit cell, except for the additional next-nearest-neighbor
couplings (with strength v = 0.5) in the latter case. We set the left/right side to possess quaternion
charges i (with phase-band singularity ˜i) and k (with phase-band singularity ˜k) as an example. For
all four types of domain wall, we observe the emergence of domain-wall states in the first and second
gaps, as shown in Fig. S6e-h. This is consistent with the quotient relation, ∆q = q−1
R qL = −˜k˜i.
Furthermore, we test the robustness of these domain-wall states against onsite disorder in Fig. S6i-l.
Similar to the edge states at the boundary, the domain-wall states survive weak disorder.
It is worth mentioning that the decorations of the domain wall may induce some additional bound
states, as illustrated in Fig. S7. We consider a tunable onsite potential with strength p at the
interface unit cell: sAA = sBB = sCC = p. In Fig. S7a to d, we take four values of p = 3, 9, 50, 1000
and plot the quasienergy spectra and spatial distributions of the eigenstates. The domain-wall states
located in the first and second gaps always exist. However, there also appear some trivial bound
states. These bound states have no topological origin. Their quasienergies depend on the added
potential and may merge into the bulk bands by adjusting the potential. In contrast, the domain-wall
states are robust. They originate from the non-Abelian topology and are described by the quotient
relation.

--- Page 15 ---

15
A
B
C
A
B
C
k
i
k
i
A
B
C
k
i
a
b
c
A
B
C
k
i
d
e
f
g
h
i
j
k
l
FIG. S6.
Stability of domain-wall states against different domain-wall settings and disorder. a-d Domain-wall configurations.
The left (right) side has bulk quaternion charge i (k). The black arrows in d indicate the next-nearest-neighbor couplings.
e-h Quasienergy spectra and spatial distributions of eigenstates for the four domain-wall settings. i-l Quasienergy spectra as
a function of the disorder strength W. The domain-wall states are encircled by red ellipses. The parameters used are listed in
Table 1.
a
b
c
d
FIG. S7. Quasienergy spectra and spatial distributions of eigenstates for different onsite potentials at the interface unit cell.
(a-d) The potential strengths are p = 3, 9, 50 and 1000, respectively. The domain-wall states in the first and second gaps always
exist (encircled by red ellipses). Trivial bound states may arise due to the local onsite potential. The parameters used are
listed in Table 1.

```
