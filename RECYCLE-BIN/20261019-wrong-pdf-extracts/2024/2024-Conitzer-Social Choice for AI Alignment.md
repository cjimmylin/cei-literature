---
title: "Social Choice for AI Alignment - PDF Extract"
source_pdf: "2024-Conitzer-Social Choice for AI Alignment.pdf"
pages: 27
extracted_at: "2026-01-24T17:05:28.390050"
---

# PDF Extract: Social Choice for AI Alignment

**Source PDF:** 2024-Conitzer-Social Choice for AI Alignment.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

Calculation of DC Stark Resonances for the Ammonia Molecule
Patrik Pirkola∗and Marko Horbatsch†
Department of Physics and Astronomy,
York University, Toronto, Ontario M3J 1P3, Canada
(Dated: April 17, 2024)
Abstract
A model potential previously developed for the ammonia molecule is treated in a single-center
partial-wave approximation in analogy with a self-consistent field method developed by Moccia.
The latter was used in a number of collision studies. The model potential is used to calculate dc
Stark resonance parameters, i.e., resonance positions and shifts within a single-center partial wave
expansion, using the exterior complex scaling method for the radial coordinate. Three molecular
valence orbitals are investigated for fields along the three Cartesian coordinates, i.e., along the
molecular axis and in two perpendicular directions. The work extends previous work on the planar-
geometry water molecule for which non-monotonic shifts were observed. We find such non-monotonic
shifts for fields along the molecular axis. For perpendicular fields we report the splitting of the 1e
orbitals into a fast- and a slow-ionizing orbital.
∗patpirko@my.yorku.ca
† marko@yorku.ca
1
arXiv:2404.10000v1  [physics.chem-ph]  28 Mar 2024

--- Page 2 ---

I.
INTRODUCTION
Research into ionization of ammonia molecules (NH3) has been an ongoing topic of interest
with recently proposed new ideas about multiple ionization (or rather the lack thereof) in the
context of experimental fragmentation studies in proton-ammonia collisions at intermediate
and high energies [1]. The fragmentation study puts (perhaps) in doubt the validity of
an independent electron model approach which was used in various forms to explain total
(net) ionization cross sections, as well as doubly differential cross sections which represent
the emission properties of ionized electrons, i.e., their distribution over polar angle and
energy. Such studies of net ionization differential cross sections were reported in the Born
approximation [2], and a continuum distorted wave method [3], which described the earlier
measurements [4] quite well. The fact that these experimental data were consistent with
net ionization was demonstrated in yet another study by showing the contributions from
particular molecular orbitals (MOs) [5]. Most of these studies employed the single-centre
Slater-type orbital based Hartree-Fock calculations of Moccia [6].
From a theoretical perspective the role of multiple ionization in proton collisions with
the ‘isoelectronic’ molecules water (H2O) [7–9], methane (CH4) [10], and ammonia [1] was
analyzed in the framework of the independent-atom model [11]. An accurate representation
of proton-water molecule differential cross sections at an intermediate energy (250 keV) was
obtained with a classical trajectory Monte-Carlo method [12] which was based on a three-
center model potential. Collision calculations using this model potential have been carried
out recently for the ammonia molecule [13]. These works, and the problem with interpreting
fragmentation cross sections [1] serve as a motivation to extend our previous studies of Stark
resonance parameters for the water molecule within a model potential approach to the case
of the ammonia molecule. The main idea of the model potential approach is to avoid the
technical difficulties of a self-consistent effective potential.
We are studying the molecule for fixed orientation, i.e., the rotational (and vibrational)
degrees of freedom are ignored. In collision problems at intermediate and high energies this
approach is justified by the time scale of the collision process, and orientation averaging is
applied when computing probabilities or cross sections, such as, e.g., in Refs. [11, 12]. For
the dc Stark problem the fixed orientation with respect to the external field does represent
a more serious issue, since over longer time scales the field would act to orient a molecule
2

--- Page 3 ---

with permanent dipole moment [14, 15]. An exception would be if the molecule was found
in a matrix isolation environment, e.g., by trapping in a cold rare gas matrix. This subject
has received recently renewed attention in the context of proposals to measure the electron
electric dipole moment using diatomic molecules [16, 17]. Given that strong electric fields
are potentially going to be applied (cf. Ref. [18]) the problem of Stark ionization should be
researched in this context, as well.
The Stark resonance problem is addressed in this paper by following the exterior complex
scaling (ECS) method which implements a derivative discontinuity at the radial distance
where complex scaling sets in [19]. The ECS methodology was developed over the years and
has been compared to the complex absorbing potential (CAP) method [20, 21]. Following
Moiseyev [22, 23] one can argue that the smooth ECS and CAP methods are equivalent.
They share the features that starting at some critical radial distance rs either a gradual
continuation of the real r-axis into the complex plane is carried out, or a complex absorber
is implemented for r > rs. Both methods show some dependence on either the scaling angle
θs which extends the path into the complex plane, or on the strength parameter of the CAP.
Perturbative corrections can be employed in the case of the CAP.
The hard ECS method was developed further by Scrinzi [24] as an effective absorber for
time-dependent problems. A derivative discontinuity in the wave function at the scaling
radius rs needs to be implemented, and it allows for the choice of scaling angles close to the
critical value of θs = π/2. This, in turn, allows to use a reduced region rs < r < rmax to
compute the tails of the resonance states. At the outer boundary rmax the Dirichlet condition
of vanishing wave function is applied. We used his methodology previously for the planar
water molecule [25]. The extension from a planar geometry does not pose additional problems
for the present case of the ammonia molecule: a partial wave expansion of the orbitals is
implemented, and as before, the radial functions are solved using a finite element method.
The choices for scaling radius rs = 16.2 a.u., and rmax = 24.3 a.u. were made in this work
combined with a scaling angle θs = 0.9 π/2. Atomic units (ℏ= me = e = 4πϵ0 = 1) are used
throughout this work.
The geometry of the NH3 molecule is shown in Fig. 1 together with the three directions
along which electric fields are applied. The arrows indicate the force directions that are
applied individually, i.e., one Cartesian direction at a time. The force directions Fi are
opposite to the electric field directions Ei due to the negative charge of the electron.
3

--- Page 4 ---

FIG. 1.
The geometry for the NH3 molecule as implemented in this work showing the nitrogen
atom (in green) and the three hydrogen atoms (in blue) schematically. Electric fields are applied
pushing electrons out along the x-direction (black arrow), the y-direction (brown arrow), and the
z-direction (red arrow), and will be denoted by positive values of Fx, Fy, Fz respectively. Negative
values of Fx, Fy, Fz correspond to fields pushing in the opposite directions. The coordinates are
given in atomic units.
II.
MODEL
The model potential for the ammonia molecule is a straightforward extension of previous
modelling of the water molecule (Refs. [26–30]). The model combines three spherically
symmetric potentials for the atomic constituents. Each part contains a screening contribution,
and the parameters are adjusted such that the overall potential falls of as −1/r at large
distances, as is required to avoid contributions from electronic self-interaction. We keep the
model parameters for the hydrogen atoms, and model the central nitrogen atom in analogy
to the oxygen atom in H2O.
Thus, the potential is defined as follows:
Veff = VN(r) + VH(r1) + VH(r2) + VH(r3) ,
(1)
4

--- Page 5 ---

VN(r) = −7 −NN
r
−NN
r (1 + αNr) exp(−2αNr) ,
VH(rj) = −1 −NH
rj
−NH
rj
(1 + αHrj) exp(−2αHrj) .
(2)
The scalar variables rj (with j = 1, 2, 3) represent the electron distances from the protons.
The hydrogenic parameters αH = 0.6170 and NH = 0.9075 are taken from previous works
for the water molecule. The latter choice then fixes the potential parameter NN = 6.2775
to yield the appropriate asymptotic effective potential at large r, as 3 (1 −NH) = 0.2775
is the long-range effective charge contribution to the potential from the hydrogen atoms.
The nitrogen atom screening parameter was chosen as αN = 1.525 in order for the model to
yield orbital energies that follow closely values obtained in the Hartree-Fock approximation.
The geometry of NH3 is adopted from the work of Moccia [6], with a N-H bond length of
1.928 a.u., polar angle θp = 108.9 degrees, and azimuthal angles ϕj for the three hydrogenic
protons spaced apart by 120 degrees. In particular, the azimuthal angles of the hydrogen
atoms are chosen to be 90, 210, 330 degrees, which singles out the y −z plane as containing
one of the protons.
The Schrödinger equation for the MOs and an electric field in the ˆz direction can be
written as

−1
2∇2 −
3
X
i=0
Zi(|⃗ri|)
|⃗ri|
−Fzr cos(θ)

ψν = ϵν ψν,
(3)
with r0 ≡r, while the Zi(ri) are screening functions for the constituent atomic centers, i.e.,
Z0(r) = rVN(r) for the nitrogen atom, and Zi(r) = rVH(r) with i = 1, 2, 3 for the hydrogens,
as defined in eq. (2). Note that the electric field component is Ez = −Fz, i.e., our notation
Fz refers to the force experienced by a free electron.
The MO wavefunctions ψ ≡ψν are expanded in complex-valued spherical harmonics,
ψ(r, θ, ϕ) =
ℓmax
X
ℓ=0
ℓ
X
m=−ℓ
I,N
X
i,n
cinℓm
fin(r)
r
Y m
ℓ(θ, ϕ) ,
(4)
and the radial functions are expanded using a finite-element method (FEM). The functions
fin are local basis functions on interval i of the radial interval 0 < r < rmax. The index n
labels the polynomial basis functions [19]. The Schrödinger equation is solved as outlined
in Ref. [25, 31] and leads to a matrix eigenvalue problem with the cinℓm being elements of
the eigenvectors. With this discretization technique we are solving the three-dimensional
problem, which is defined in eq. (3) for a field along the ˆz direction. The force direction
5

--- Page 6 ---

due to the external dc field as experienced by the electron is controlled by the sign of Fz as
explained in Fig. 1.
The FEM approach from Ref. [25, 31], and outlined in Ref. [19, 32] was used with the
partial wave expansion of ψ truncated at ℓmax = 3 to test how the MO eigenvalues respond
to changes in the one free screening parameter contained in the model potential. The partial
wave expansion allowed the spherical components of the matrix elements to be calculated
using a Wigner 3j coefficient package [33] (which can be found on the author(s) homepage1)
as before in our work with water [25, 31, 32]. The hydrogenic potentials are expanded in
spherical harmonics which allows for the use of Wigner 3j coefficients rather than evaluating
three-dimensional integrals numerically.
Comparison with the SCF eigenvalues of Moccia shows that the three outermost MOs
can be reproduced well with the simple model potential. The 2a1 MO is too weakly bound
at the level of 10%, which is deemed acceptable, since it is expected to contribute less to the
overall molecular ionization rate. The comparison of eigenvalues obtained for ℓmax = 3 and
ℓmax = 5 is provided, since the resonance parameter calculations are performed with ℓmax = 3
only. The table also contains results from a localized Hartree-Fock method as implemented
in Turbomole [34–37].
E1a1
E2a1
E1e
E3a1
Ref. [6]
-15.5222
-1.1224
-0.5956
-0.4146
FEM(ℓmax = 3)
-15.930
-0.976
-0.594
-0.410
FEM(ℓmax = 5)
-15.930
-0.982
-0.609
-0.413
LHF
-14.087
-0.986
-0.619
-0.424
OEP-EXX
-14.154
-0.986
-0.611
-0.430
TABLE I. MO eigenvalues for the model potential as compared to the SCF eigenvalues of Moccia
(Ref. [6]). The E1e energy appears twice, i.e. for the MOs 1e1 and 1e2. The fourth row shows the
localized HF method [34, 35] eigenvalues based on the optimized geometry in HF approximations
as calculated in Turbomole [37] using the def2-QZVPPD basis set, while the fifth row gives the
eigenvalues from the optimized effective potential method [36] using the d-aug-cc-pVTZ-oep basis.
1 https://www-stone.ch.cam.ac.uk/wigner.shtml
6

--- Page 7 ---

III.
RESULTS
A.
Resonance parameters for fields along the vertical ±ˆz-direction
We begin the discussion of resonance parameters with fields along ±ˆz for which the two
degenerate MOs 1e1 and 1e2 should yield identical results. The dominant contribution to
dc field ionization is expected from the weakest bound orbital (3a1). For this orbital the
combined molecular and external electric field leads to over-the-barrier ionization at the
strongest fields calculated (|Fz| of order 0.1 a.u.).
In Fig. 2 the top row shows the resonance position (left column) and resonance half-width
(right column) for this orbital as a function of field strength Fz. Positive values Fz > 0
correspond to the field direction pushing electrons out in the direction from the hydrogen
atom plane past the nitrogen atom, while negative values Fz < 0 are for electrons ejected
from the hydrogen plane (at negative z) away from the nitrogen atom which is located at
z = 0.
The change of the resonance position with field strength can be described as monotonically
stronger binding for Fz > 0, since electron density is transferred from the hydrogen atoms
in the direction of the central nitrogen atom. For the opposite field direction (Fz < 0)
we observe non-monotonic behavior. First one expects marginally weaker binding when
transferring electron density from a nitrogen to a hydrogen atom.
In the molecule the shift in electron density will be towards regions around the partially
shielded protons where the electron binding is weaker. This feature becomes apparent at
strong fields (over-the-barrier regime), but there is an intermediate range of field strengths
(−0.08 < Fz < −0.04 a.u.) where there is a non-monotonic variation of the resonance position
with field strength.
The resonance widths are obviously small in the tunneling regime. They change by orders
of magnitude as the field is increased, and the ionization rate for emission from the hydrogen
plane (Fz < 0) is stronger than in the opposite direction, by more than a factor of two.
For field strengths of the order of 0.1 a.u. saturation in the ionization rate sets in, which
is associated with the over-the-barrier regime. At these field strengths one may reach the
limitations of the exponential decay model, and, thus, results for stronger fields are not
reported.
7

--- Page 8 ---

-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
-0.5
-0.45
-0.4
-0.35
E3a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
-0.64
-0.62
-0.6
-0.58
-0.56
E1e (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
-1.04
-1.02
-1
-0.98
-0.96
-0.94
E2a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fz (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
FIG. 2.
Resonance positions (left panels) and half-widths (right panels) in atomic units for the
outer MOs for electric fields along the axis connecting the nitrogen atom with the atomic hydrogen
plane. Fz > 0 values correspond to fields pushing electrons out on the nitrogen side, while Fz < 0
corresponds to emission from the side of the hydrogen atom plane. Top row: 3a1, middle row: the
doubly degenerate 1e MO (identical results for 1e1 and 1e2), bottom row for 2a1.
We note that the behavior of the resonance position is consistent with the change in
ionization rate (or resonance width) as a function of field direction. In the strong field regime
(at about 0.1 a.u. and beyond) the binding energies are quite different and the ionization
8

--- Page 9 ---

rates change by a factor of two when the field is reversed. An interesting observation for
Fz > 0 is the rise in the ionization rate even though the resonance position indicates stronger
binding. This phenomenon is associated with density being driven by the field towards the
barrier region.
In the middle panel the results are shown for the two degenerate 1e MOs. The dependence
of the resonance position on field strength Fz is monotonic in this case, and varies only at
the 5% level in the given field strength range. The corresponding decay rates are weaker by
orders of magnitude as compared to the 3a1 MO, and remain in the tunneling regime. This
conclusion will be supported further below by probability density plots for |Fz| = 0.1 a.u..
The bottom panel shows results for the more deeply bound 2a1 MO. Here the variation in
the resonance position is only at the level of 3%, and the ionization rate is suppressed by
two to three additional orders of magnitude. The shape of the dc Stark shift (left panel) as a
function of field strength and orientation is similar to what is observed for the 1e pair of
MOs. A small asymmetry can be observed in the decay rates, with a small enhancement for
Fz > 0 vs Fz < 0.
In Fig. 3 we illustrate the situation with probability density contour plots of the MOs. The
field-free case is shown in the middle row. The outermost MO (3a1) shown on the left has an
asymmetric probability density with respect to z = 0 with higher probability values on the
nitrogen side. When the dc field is pushing electrons out on this side the nitrogen potential
provides attraction, and causes some concentration of probability in this distribution, as
shown in the top left panel (strong red drop-like shape at z > 0, and also at z < 0). The
interpretation of the density plots is that they describe steady-state decay.
The bottom left panel shows the case of a strong field pushing in the direction past the
hydrogen atoms. The probability distribution is more diffuse, showing that the outflow on the
side of the hydrogen plane is hindered less. This observation is consistent with the decay rate
results shown in the top right panel of Fig. 2. The outflow of probability density is consistent
with above-the-barrier ionization for both the top and bottom rows, i.e., |Fz| = 0.1 a.u..
The other two MOs show much less outflow at comparable fields, and are clearly in the
tunneling regime. For the 1e1 MO (middle column) with field turned on in either direction
there is a limited amount of density change compared to the 3a1 MO. For the 2a1 MO (right
column) we observe symmetry in the field-free case, and shifting of probability density in
the direction of the applied force, but in the tunneling regime not much probability density
9

--- Page 10 ---

appears far away from the molecule.
10

--- Page 11 ---

FIG. 3.
Probability density contour plots for the MOs 3a1, 1e1, 2a1 (left to right) in the y = 0
plane, i.e., as a function of x and z. Middle row: field-free case; top row: Fz = 0.1 a.u.; bottom row:
Fz = −0.1 a.u.. The contours are at values: [0.00, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14].
The positions of the atomic nuclei are indicated by white dots with the N atom at z = 0 and the
three proton locations projected onto the x −z plane. The central dot corresponds to the proton
residing below the positive y-axis.
11

--- Page 12 ---

B.
Resonance parameters for fields along the ±ˆx-direction
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
-0.46
-0.44
-0.42
-0.4
E3a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
-0.64
-0.62
-0.6
-0.58
-0.56
E1e (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
-1.01
-1
-0.99
-0.98
-0.97
E2a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fx (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
FIG. 4.
Same as in Fig. 2 but for electric dc fields along the x−axis. In the middle panel results
are shown for the MOs 1e1 (orange dots) and 1e2 (blue dots). The 1e1 MO has the larger ionization
rate for this field orientation.
In Fig. 4 results are presented for fields in a perpendicular direction relative to the axis
connecting the N atom with the hydrogen atom plane. The arrangement of the three hydrogen
atoms is such that one resides on the y-axis, i.e., field emission occurs along the direction
12

--- Page 13 ---

of the H-H bond perpendicular to this axis. The degeneracy between the 1e1 and 1e2 MO
energies is expected to be broken when a dc field is applied in this ˆx (or the perpendicular ˆy)
direction.
The top row for the outermost MO 3a1 shows a symmetric behaviour in the dc Stark
shift (left panel) and likewise a symmetric ionization rate with respect to reversal of the
field direction. The change in the rise of the ionization rate at strong fields indicates that
one is only approaching the over-the-barrier regime, i.e., saturation has not set in yet at
|Fx| = 0.1 a.u.. The increase in binding is at the 10% level for the strongest fields. The
ionization rates for these fields are smaller than for ionization along the ˆz axis by a substantial
factor (about three or six, depending on the field direction ±ˆz)
The middle row shows the different behaviors for the 1e1 and 1e2 MOs. We classify the
two orbitals as fast- vs slow-ionizing under ˆx oriented fields (orange vs blue markers). The
behavior is symmetric with respect to field orientation. The 1e1 MO (orange dots) shifts
towards less binding for both field orientations, and the 1e2 (blue dots) is bound more deeply
as the field is increased in either direction.
The ionization rates (right panel) are also symmetrical with respect to field reversal. The
1e1 ionizes more readily by almost a factor of two for this field orientation. It is remarkable
that these MOs ionize easily at strong fields with the 1e1 MO displaying a rate which is
moving towards that of the more weakly bound 3a1 MO. Comparing the ionization rates for
the 1e1 and 1e2 orbitals for fields along ˆx versus ˆz we notice an order-of-magnitude increase.
The reverse trend is true for the 3a1 MO.
The bottom row shows that the results for the 2a1 MO are symmetric with respect to field
orientation (as for 3a1). The decay rates are somewhat larger than in the case of z-oriented
fields, even though the MO is bound more deeply with increasing field strength.
We support our resonance parameter values again with selective plots of probability
densities from the ECS approach in Fig. 5. The middle row is identical with that in Fig. 5,
but is included for direct comparison of the cases with electric field. It is immediately
apparent that three MOs (3a1, 1e1, and also 1e2 which is not shown), contribute strongly to
ionization of the molecule for this field orientation.
For the 3a1 MO we observe outflow in the form of two jets directed above and below the
hydrogen atom plane. For the 1e1 MO we find that the apparent asymmetry in the x −z
plane for the field-free case has no repercussions for the outflow in the case with fields of
13

--- Page 14 ---

FIG. 5.
Same as in Fig. 3, but for dc electric fields along the ˆx axis. Left to right: MOs 3a1, 1e1,
2a1; middle panel: field-free, top panel Fx = +0.1 a.u., bottom panel Fx = −0.1 a.u..
either direction: both cases show very symmetric probabilities under these conditions which
is consistent with the findings for the resonance parameters.
For the 2a1 MO shown in the right column symmetry with respect to field orientation is
expected. This is evident from the density plots by comparing the top and bottom panels.
We note the relatively strong effect the field has on this relatively deeply bound orbital.
14

--- Page 15 ---

C.
Resonance parameters for fields along the ±ˆy-direction
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
-0.46
-0.44
-0.42
-0.4
E3a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
-0.66
-0.64
-0.62
-0.6
-0.58
-0.56
E1e (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
-1.01
-1
-0.99
-0.98
-0.97
E2a1 (a.u.)
Resonance Position
-0.12
-0.08
-0.04
0
0.04
0.08
0.12
Fy (a.u.)
10-9
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
Γ/2 (a.u.)
Resonance Half-width
FIG. 6.
Same as in Fig. 4 but for electric dc fields along the y−axis. In the middle panel results
are shown for the MOs 1e1 (blue dots) and 1e2 (orange dots) which are clasified as the slow- vs
fast-ionizing 1e orbital respectively. Note that the y −z plane contains a hydrogen atom at y > 0
and this causes an asymmetry in the resonance parameters with respect to the sign of Fy.
In Fig. 6 results are given for field orientation along ˆy. Given the triangular nature of
the hydrogen atom plane these results differ strongly from those in the previous section. By
15

--- Page 16 ---

choice of azimuthal angles ϕi = 90, 210, 330 degrees, a proton is located on the positive y
axis, and asymmetry is expected when reversing the field direction.
The top row shows that this asymmetry plays a very small role for the outermost MO 3a1
at weak fields, and is barely noticeable. The tabulated data (cf. Appendix C) show that the
shifts differ by less than a percent.
The 1e1 and 1e2 MOs (blue and orange dots, middle row) show markedly different behavior
when compared to ±ˆx oriented fields. The shifts follow monotonic curves, as there is no
longer symmetry under field orientation reversal. The 1e2 MOs is ionizing more rapidly as
compared to 1e1 by about two orders of magnitude. The variation in resonance position is
clearly at odds with this result, i.e., it apparently does not play a role here. As discussed
before, the actual value of the MO binding energy is not the deciding factor, but rather how
the electron density is driven towards the potential barrier by the external field.
The 1e1 MO ionizes very weakly, and its rate is comparable to those obtained for ±ˆz
oriented fields. Thus, one may conclude that the 1e2 MO is affected by this field orientation
dramatically.
In the third row we give results for the deeply bound 2a1 MO which remains deeply in
the tunneling regime for the given field strengths. It shows a small amount of asymmetry in
the dc Stark shifts and in the decay rates.
The probability density plots shown in Fig. 7 again help to understand the finding for
the parameter values. The results for MO 3a1 are very close to the corresponding plots in
Fig. 5 and are not shown. Instead we show over the x −y plane probability densities for
the strongly ionizing 1e2 MO (left column), the much more weakly ionizing 1e1 MO (middle
column) and 2a1 in the right column.
For the field-free case the density plots show that the MOs 1e2 and 1e1 are actually not
perfectly aligned with our x- and y-axes. This is related to the fact that they share the
same probability density shapes, except that they are rotated by 90 degrees, and this is
incompatible with the three-fold symmetry. Once the strong field is turned on along either
the x- or the y-axis, however, the densities respect the symmetry of the external field, and
one can identify 1e1 = 1ex and 1e2 = 1ey.
The results for the 1e2 MO (left column) show an asymmetry in the outflow for the case
Fy > 0 vs Fy < 0. It is interesting to observe that while the shape of the outflow is very
different for both cases, the ionization rates are actually differ only at the level of up to 50 %
16

--- Page 17 ---

(cf. Appendix C).
FIG. 7.
Probability densities in the z = 0 plane for dc fields along the ˆy direction. Left column:
MO 1e2, middle column: 1e1, right column: 2a1 are shown over the x −y plane. Middle row shows
the field-free case, top row: Fy = 0.1 a.u., bottom row: Fy = −0.1 a.u..
17

--- Page 18 ---

In the middle column for MO 1e1 we observe a symmetry in the outflows despite the fact
that the arrangement of hydrogen atoms is asymmetric. For the case of MO 2a1 we find that
the central parts of the density are very different for the two field directions, but the parts
showing the outflow are again very similar, and this is similar to what one observes for MO
1e1.
IV.
CONCLUSIONS
We have extended our previous model calculation for H2O to the case of NH3. A simple
model potential was applied to approximate what an SCF model (e.g., local density functional
theory) might obtain for dc field ionization. In fact, the MO eigenvalues were shown to be
comparable to the LHF results, as shown in Table I.
The results demonstrate that depending on the orientation of the electric field the three
outer MOs of ammonia, i.e., 3a1, 1e1, and 1e2 can have appreciable ionization rates. This
supports the case for multiple ionization being important whether in ion-molecule collisions
or in strong-field laser-molecule interactions.
Interesting details emerge from our model calculations: (i) non-monotonic dc shifts for
the 3a1 MO for fields along ˆz; (ii) for perpendicular fields to the molecular axis we observe
that the 1e orbitals separate into fast- and slow-ionizing ones; the (iii) fast-ionizing 1e orbital
can acquire a comparable ionization rate ti the outermost 3a1 orbital.
It would be of interest to test these prediction with more sophisticated models, such as
Hartree-Fock theory for MO ionization rates, density functional theory (DFT) with electron
correlation, or even coupled-cluster theory of net ionization which is possible within a recently
developed quantum chemistry code [38–40]. Work is in progress to replace the model potential
by exchange-correlation potentials obtained from DFT.
18

--- Page 19 ---

V.
APPENDIX: TABLES OF RESONANCE PARAMETER VALUES
A.
Fields along ±ˆz
MO: 3a1
Fz
Re
Im
-0.12
−0.3780
−5.893 × 10−2
-0.10
−0.4034
−4.630 × 10−2
-0.08
−0.4139
−2.349 × 10−2
-0.06
−0.4117
−6.434 × 10−3
-0.04
−0.4065
−2.686 × 10−4
-0.02
−0.4066
−1.556 × 10−9
0.00
−0.4103
NA
0.02
−0.4161
NA
0.04
−0.4242
−9.049 × 10−5
0.06
−0.4356
−2.484 × 10−3
0.08
−0.4472
−9.694 × 10−3
0.10
−0.4561
−2.027 × 10−2
0.12
−0.4615
−3.230 × 10−2
MO: 1e
Fz
Re
Im
-0.12
−0.6362
−5.524 × 10−4
-0.10
−0.6267
−1.032 × 10−4
-0.08
−0.6183
−7.178 × 10−6
-0.06
−0.611
−6.516 × 10−8
-0.04
−0.6045
NA
-0.02
−0.5987
NA
0.00
−0.5936
NA
0.02
−0.5891
NA
0.04
−0.5853
NA
0.06
−0.5820
−7.860 × 10−8
0.08
−0.5795
−7.737 × 10−6
0.10
−0.5778
−1.003 × 10−4
0.12
−0.5769
−4.911 × 10−4
19

--- Page 20 ---

MO: 2a1
Fz
Re
Im
-0.12
−1.030
−3.287 × 10−6
-0.10
−1.020
−1.437 × 10−7
-0.08
−1.009
−1.161 × 10−9
-0.06
−1.000
NA
-0.04
−0.9914
NA
-0.02
−0.9835
NA
0.00
−0.9763
NA
0.02
−0.9698
NA
0.04
−0.9642
NA
0.06
−0.9594
NA
0.08
−0.9554
−1.834 × 10−9
0.10
−0.9523
−2.197 × 10−7
0.12
−0.9503
−4.861 × 10−6
20

--- Page 21 ---

B.
Fields along ±ˆx
MO: 3a1
Fx
Re
Im
-0.12
−0.4358
−9.906 × 10−3
-0.10
−0.4288
−4.740 × 10−3
-0.08
−0.4221
−1.488 × 10−3
-0.06
−0.4165
−1.803 × 10−4
-0.04
−0.4129
−1.736 × 10−6
-0.02
−0.4109
NA
0
−0.4103
NA
0.02
−0.4109
NA
0.04
−0.4129
−1.736 × 10−6
0.06
−0.4165
−1.803 × 10−4
0.08
−0.4221
−1.488 × 10−3
0.10
−0.4288
−4.740 × 10−3
0.12
−0.4358
−9.906 × 10−3
MO: 1e1(fast)
Fx
Re
Im
-0.12
−0.5741
−6.925 × 10−3
-0.10
−0.5754
−2.515 × 10−3
-0.08
−0.5770
−4.623 × 10−4
-0.06
−0.5797
−1.799 × 10−5
-0.04
−0.5837
−1.296 × 10−8
-0.02
−0.5884
NA
0
−0.5936
NA
0.02
−0.5884
NA
0.04
−0.5837
−1.296 × 10−8
0.06
−0.5797
−1.799 × 10−5
0.08
−0.5770
−4.623 × 10−4
0.10
−0.5754
−2.515 × 10−3
0.12
−0.5741
−6.925 × 10−3
21

--- Page 22 ---

MO: 1e2(slow)
Fx
Re
Im
-0.12
−0.6388
−4.592 × 10−3
-0.10
−0.6292
−1.551 × 10−3
-0.08
−0.6201
−2.475 × 10−4
-0.06
−0.6122
−8.496 × 10−6
-0.04
−0.6054
−5.725 × 10−9
-0.02
−0.5992
NA
0
−0.5936
NA
0.02
−0.5992
NA
0.04
−0.6054
−5.730 × 10−9
0.06
−0.6122
−8.496 × 10−6
0.08
−0.6201
−2.475 × 10−4
0.10
−0.6292
−1.551 × 10−3
0.12
−0.6388
−4.592 × 10−3
MO: 2a1
Fx
Re
Im
-0.12
−1.006
−6.357 × 10−6
-0.10
−0.9972
−2.855 × 10−7
-0.08
−0.9897
−2.367 × 10−9
-0.06
−0.9838
NA
-0.04
−0.9796
NA
-0.02
−0.9771
NA
0
−0.9763
NA
0.02
−0.9771
NA
0.04
−0.9796
NA
0.06
−0.9838
NA
0.08
−0.9897
−2.366 × 10−9
0.10
−0.9972
−2.855 × 10−7
0.12
−1.006
−6.357 × 10−6
22

--- Page 23 ---

C.
Fields along ±ˆy
MO: 3a1
Fy
Re
Im
-0.12
−0.4349
−9.669 × 10−3
-0.10
−0.4283
−4.644 × 10−3
-0.08
−0.4218
−1.471 × 10−3
-0.06
−0.4164
−1.833 × 10−4
-0.04
−0.4128
−1.962 × 10−6
-0.02
−0.4109
NA
0
−0.4103
NA
0.02
0.411
NA
0.04
−0.4129
−1.559 × 10−6
0.06
−0.4166
−1.788 × 10−4
0.08
−0.4223
−1.506 × 10−3
0.10
−0.4293
−4.825 × 10−3
0.12
−0.4366
−1.011 × 10−2
MO: 1e2(fast)
Fy
Re
Im
-0.12
−0.571
−1.201 × 10−2
-0.10
−0.5739
−4.555 × 10−3
-0.08
−0.5756
−8.496 × 10−4
-0.06
−0.5786
−3.357 × 10−5
-0.04
−0.5831
−2.476 × 10−8
-0.02
−0.5882
NA
0
−0.5936
NA
0.02
−0.5991
NA
0.04
−0.6047
−1.254 × 10−8
0.06
−0.6107
−1.906 × 10−5
0.08
−0.6180
−5.480 × 10−4
0.10
−0.6267
−3.325 × 10−3
0.12
−0.6353
−9.772 × 10−3
23

--- Page 24 ---

MO: 1e1(slow)
Fy
Re
Im
-0.12
−0.6429
−5.352 × 10−4
-0.10
−0.6318
−9.919 × 10−5
-0.08
−0.6221
−6.839 × 10−6
-0.06
−0.6136
−6.150 × 10−8
-0.04
−0.6061
NA
-0.02
−0.5994
NA
0
−0.5936
NA
0.02
−0.5886
NA
0.04
−0.5843
NA
0.06
−0.5809
−1.040 × 10−7
0.08
−0.5784
−1.043 × 10−5
0.10
−0.5770
−1.380 × 10−4
0.12
−0.5767
−6.887 × 10−4
MO: 2a1
Fy
Re
Im
-0.12
−1.004
−5.367 × 10−6
-0.10
−0.9959
−2.436 × 10−7
-0.08
−0.9890
−2.045 × 10−9
-0.06
−0.9835
NA
-0.04
−0.9795
NA
-0.02
−0.9771
NA
0
−0.9763
NA
0.02
−0.9771
NA
0.04
−0.9797
NA
0.06
−0.9841
NA
0.08
−0.9903
−2.701 × 10−9
0.10
−0.9984
−3.287 × 10−7
0.12
−1.008
−7.362 × 10−6
24

--- Page 25 ---

ACKNOWLEDGMENTS
Discussions with Tom Kirchner and Michael Haslam are gratefully acknowledged. We
would also like to thank Steven Chen for support with the high performance computing
server used for our calculations. Financial support from the Natural Sciences and Engineering
Research Council of Canada is gratefully acknowledged.
[1] W. Wolff, H. Luna, E. C. Montenegro, and L. C. Rodrigues Junior, Phys. Rev. A 102, 052821
(2020).
[2] B. Senger, Zeitschrift für Physik D Atoms, Molecules and Clusters 9, 79 (1988).
[3] C. A. Tachino, J. M. Monti, O. A. Fojón, C. Champion, and R. D. Rivarola, Journal of Physics:
Conference Series 583, 012020 (2015).
[4] D. Lynch, L. Toburen, and W. Wilson, The Journal of Chemical Physics 64, 2616 (1976).
[5] A. Mondal, S. Halder, S. Mukherjee, C. R. Mandal, and M. Purkait, Phys. Rev. A 96, 032710
(2017).
[6] R.
Moccia,
The
Journal
of
Chemical
Physics
40,
2176
(2004),
https://pubs.aip.org/aip/jcp/article-pdf/40/8/2176/10949818/2176_1_online.pdf.
[7] U. Werner, K. Beckord, J. Becker, and H. O. Lutz, Phys. Rev. Lett. 74, 1962 (1995).
[8] F. Gobet, S. Eden, B. Coupier, J. Tabet, B. Farizon, M. Farizon, M. J. Gaillard, M. Carré,
S. Ouaskit, T. D. Märk, and P. Scheier, Phys. Rev. A 70, 062716 (2004).
[9] A. C. Tavares, H. Luna, W. Wolff, and E. C. Montenegro, Phys. Rev. A 92, 032714 (2015).
[10] H. Luna, W. Wolff, E. C. Montenegro, and L. Sigaud, Phys. Rev. A 99, 012709 (2019).
[11] H. J. Lüdde, M. Horbatsch, and T. Kirchner, Phys. Rev. A 106, 022813 (2022).
[12] A. Bhogale, S. Bhattacharjee, M. R. Chowdhury, C. Bagdia, M. F. Rojas, J. M. Monti, A. Jorge,
M. Horbatsch, T. Kirchner, R. D. Rivarola, and L. C. Tribedi, Phys. Rev. A 105, 062822
(2022).
[13] A. Jorge, M. Horbatsch, and T. Kirchner, Journal of Physics B: Atomic, Molecular and Optical
Physics 57, 045201 (2024).
[14] G. Quéméner and P. S. Julienne, Chemical Reviews 112, 4949 (2012), pMID: 22921011,
https://doi.org/10.1021/cr300092g.
25

--- Page 26 ---

[15] J. M. Rost, J. C. Griffin, B. Friedrich, and D. R. Herschbach, Phys. Rev. Lett. 68, 1299 (1992).
[16] S. J. Li, H. D. Ramachandran, R. Anderson, and A. C. Vutha, New Journal of Physics 25,
082001 (2023).
[17] G. Koyanagi, R. Lambo, A. Ragyanszki, R. Fournier, M. Horbatsch, and E. Hessels, Journal
of Molecular Spectroscopy 391, 111736 (2023).
[18] A. C. Vutha, M. Horbatsch, and E. A. Hessels, Phys. Rev. A 98, 032513 (2018).
[19] A. Scrinzi and N. Elander, The Journal of Chemical Physics 98, 3866 (1993).
[20] U. V. Riss and H. D. Meyer, Journal of Physics B: Atomic, Molecular and Optical Physics 26,
4503 (1993).
[21] R. Santra, Phys. Rev. A 74, 034701 (2006).
[22] N. Moiseyev, Journal of Physics B: Atomic, Molecular and Optical Physics 31, 1431 (1998).
[23] N. Moiseyev, Non-Hermitian Quantum Mechanics (Cambridge University Press, 2011).
[24] A. Scrinzi, Phys. Rev. A 81, 053845 (2010).
[25] P. Pirkola and M. Horbatsch, Phys. Rev. A 105, 032814 (2022).
[26] H. J. Lüdde, A. Jorge, M. Horbatsch, and T. Kirchner, Atoms 8 (2020), 10.3390/atoms8030059.
[27] L. Errea, C. Illescas, L. Méndez, I. Rabadán, and J. Suárez, Chemical Physics 462, 17 (2015).
[28] C. Illescas, L. F. Errea, L. Méndez, B. Pons, I. Rabadán, and A. Riera, Phys. Rev. A 83,
052704 (2011).
[29] A. Jorge, M. Horbatsch, C. Illescas, and T. Kirchner, Phys. Rev. A 99, 062701 (2019).
[30] A. Jorge, M. Horbatsch, and T. Kirchner, Phys. Rev. A 102, 012808 (2020).
[31] P. Pirkola and M. Horbatsch, Atoms 10 (2022), 10.3390/atoms10030084.
[32] P. Pirkola, “Exterior complex scaling approach for atoms and molecules in strong dc fields,”
(2021), arXiv:2103.05058 [quant-ph].
[33] A. J. Stone and C. P. Wood, Computer Physics Communications 21, 195 (1980).
[34] F. Della Sala and A. Görling, The Journal of Chemical Physics 115, 5718 (2001),
https://pubs.aip.org/aip/jcp/article-pdf/115/13/5718/19256057/5718_1_online.pdf.
[35] F. Della Sala and A. Görling, The Journal of Chemical Physics 116, 5374 (2002),
https://pubs.aip.org/aip/jcp/article-pdf/116/13/5374/19308073/5374_1_online.pdf.
[36] A.
Heßelmann,
A.
W.
Götz,
F.
Della
Sala,
and
A.
Görling,
The
Jour-
nal
of
Chemical
Physics
127,
054102
(2007),
https://pubs.aip.org/aip/jcp/article-
pdf/doi/10.1063/1.2751159/13589492/054102_1_online.pdf.
26

--- Page 27 ---

[37] “TURBOMOLE V7.8 2024, a development of University of Karlsruhe and Forschungszentrum
Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, since 2007; available from
http://www.turbomole.com.”.
[38] T.-C. Jagau, D. Zuev, K. B. Bravaya, E. Epifanovsky, and A. I. Krylov, The Journal of Physical
Chemistry Letters 5, 310 (2014).
[39] T.-C.
Jagau,
The
Journal
of
Chemical
Physics
148,
204102
(2018),
https://doi.org/10.1063/1.5028179.
[40] T.-C. Jagau, Chem. Commun. 58, 5205 (2022).
27

```
