---
title: "2016-Purzycki-Religious Belief and the Moral Circle - PDF Extract"
source_pdf: "2016-Purzycki-Religious Belief and the Moral Circle.pdf"
pages: 7
extracted_at: "2026-01-29T13:51:03.816187"
---

# PDF Extract: 2016-Purzycki-Religious Belief and the Moral Circle

**Source PDF:** 2016-Purzycki-Religious Belief and the Moral Circle.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Data Descriptor: Single-shot
diffraction data from the
Mimivirus particle using
an X-ray free-electron laser
Tomas Ekeberg et al.#
Free-electron lasers (FEL) hold the potential to revolutionize structural biology by producing X-ray pules
short enough to outrun radiation damage, thus allowing imaging of biological samples without the
limitation from radiation damage. Thus, a major part of the scientiﬁc case for the ﬁrst FELs was
three-dimensional (3D) reconstruction of non-crystalline biological objects. In a recent publication we
demonstrated the ﬁrst 3D reconstruction of a biological object from an X-ray FEL using this technique.
The sample was the giant Mimivirus, which is one of the largest known viruses with a diameter of 450 nm.
Here we present the dataset used for this successful reconstruction. Data-analysis methods for
single-particle imaging at FELs are undergoing heavy development but data collection relies on very limited
time available through a highly competitive proposal process. This dataset provides experimental data to
the entire community and could boost algorithm development and provide a benchmark dataset for new
algorithms.
Design Type(s)
macromolecular structure generation objective
Measurement Type(s)
X-ray diffraction data
Technology Type(s)
X-ray free electron laser
Factor Type(s)
Sample Characteristic(s)
Acanthamoeba polyphaga mimivirus
Correspondence and requests for materials should be addressed to T.E. (email: ekeberg@xray.bmc.uu.se).
#A full list of authors and their afﬁliations appears at the end of the paper.
OPEN
SUBJECT CATEGORIES
» Biological physics
» Virus structures
» X-rays
Received: 04 February 2016
Accepted: 22 June 2016
Published: 1 August 2016
www.nature.com/scientificdata
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
1

--- Page 2 ---

Background & Summary
Free-electron lasers (FEL) provide ultra short and extremely bright pulses of coherent X-rays1. It has been
predicted that such pulses could enable structure determination without crystallization by outrunning
radiation damage and thus capturing diffraction data before the particle has time to respond and
eventually be destroyed by the deposited energy2. Experimental veriﬁcation of this ‘diffraction-before-
destruction’ principle has been demonstrated several times for resolution down to 10 nm (refs 3,4).
Using many such diffraction patterns from multiple copies of a reproducible sample, the patterns
could be assembled into a 3D diffraction space from which the 3D structure could be derived5,6. This
promise was a main part of the scientiﬁc case for building free-electron lasers7. Several examples of 2D
reconstructions from biological samples at X-ray FEL have been demonstrated4,8,9 but 3D reconstructions
have remained elusive.
A single diffraction pattern represents a curved slice through the Fourier transform of the electron
density of the object. For successful 3D reconstruction many diffraction patterns from identical particles
need to be assembled into the complete 3D Fourier transform of the particle. This is difﬁcult since the
orientation of the injected particles is unknown and has to be recovered from the diffraction data alone.
A recent paper10 demonstrates this, using a modiﬁed version of the expand, maximize and compress
algorithm5 (EMC) on the Mimivirus particle. Here we describe the data collection, data preprocessing
and the dataset that was used for this reconstruction.
Today, beam time at free-electron lasers is scarce as there are few facilities and they serve a multitude
of scientiﬁc disciplines. Furthermore, applications such as 3D imaging require a large amount of effort in
algorithm development and testing. Several groups around the world are active in this development but
the majority of them don’t have regular beam time access. This dataset can thus serve as a benchmark for
algorithm testing and give many more groups access to experimental data.
For any new method, validation tools are of crucial importance. Therefore, together with the 3D
reconstruction of the Mimivirus we also presented two new validation methods10. Further development
of these methods, and the development of new ones will therefore beneﬁt from being applied to this
dataset in particular.
The sample in this dataset is the Mimivirus (Acanthamoeba polyphaga mimivirus)11,12. Mimivirus is
part of a recently discovered class of giant DNA viruses. Viral capsid is pseudo-icosahedral with a
corner-to-corner diameter of 500 nm and a face-to-face diameter of 400 nm (ref. 13). The virus is covered
by ﬁbres with a length of 125 nm giving it a total diameter of 750 nm (ref. 14).
Methods
These methods were described in ref. 10. The description here is more detailed with regards to data
collection and on-line data analysis.
Sample injection
Puriﬁed Mimivirus particles15 were transferred into a volatile buffer (250 mM ammonium acetate, pH
7.5) and the suspension was aerosolized with helium in a gas dynamic nebulizer16. The aerosol of
hydrated and adiabatically cooled particles entered a differentially pumped aerodynamic lens17.
Data collection
Experiments were performed at the Atomic Molecular Optics (AMO) beam line18 of the Linac Coherent
Light Source (LCLS) hard X-ray laser1, using the CAMP19 instrument20,21. The experiment was part of an
experiment running from June 17 to June 21 of 2010 with proposal number L150. Diffraction data were
recorded on a pair of pnCCD detectors19 at a repetition rate of 60 Hz matching the repetition rate of
LCLS. The two detectors were placed at a distance of 740 mm from the interaction region with a gap
between them of 2.1 mm to let the direct beam through. The pixel size is 75 μm and each detector in the
pair has 512 × 1,024 pixels giving the full setup a pixel count of 1,024 × 1,024 pixels.
The photon energy was 1.2 keV corresponding to a wavelength of 1.03 nm. At this wavelength the
full-period resolution at the edge of the detector is 19.9 nm. The electron bunch used to create the X-ray
pulse was 70 fs long (full duration at half maximum) and the X-ray pulse is believed to be shorter than
this22. The focus was ~10 μm (full width at half maximum) at the interaction point, giving a power
density of ~3.4 1015 W cm −2 or 1012 photons per pulse.
The experiment was performed at a pressure of 10 −6 mbar to reduce background scattering. Some of
the most important experiment parameters are summarized in Table 1.
On-line data analysis
On-line hit-identiﬁcation provided real-time statistics that guided injector alignment and tuning. Hits
with a high scattering strength were identiﬁed by counting the number of pixels that measured a value
above a threshold. Diffraction patterns with more than 500 pixels with a value above 170 ADU were
deﬁned as a hit. See ref. 21 for a detailed description.
Data Records
Two datasets are provided: the full record of all collected data and a smaller preprocessed dataset. Both
data sets are available in the same CXIDB entry (Data Citation 1).
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
2

--- Page 3 ---

Full data record
We provide all data collected from the Mimivirus at this beamtime before any preprocessing or sorting.
This dataset is in the extended tagged container (XTC) ﬁle format. This can be converted to HDF5 format
using programs such as CASS23 or Cheetah24. This conversion normally also involves preprocessing and
the data is therefore provided in the untouched XTC format.
The record contains 19 LCLS runs. 14 of these had the sample injector and X-ray laser turned on while
the remaining 5 runs only collected detector background noise. These so called ‘dark runs’ can be used for
to better subtract the background from the actual data. Table 2 shows a list of all 19 runs.
Initial hit ﬁnding showed that 0.3% of the frames contained diffraction that was stronger than the
background. The rest were misses, i.e., frames that were read out when the pulse did not hit any particle.
In addition to hits from single Mimivirus particles the hits also include droplets of buffer, clusters of
viruses and a few particles that were injected earlier and had stayed in the injection system.
Preprocessed and ﬁltered data
This dataset contains the 198 preprocessed (see ref. 19) diffraction patterns that were used in ref. 10 to
recover the 3D structure of the Mimivirus particle. This data is in the CXIDB format described in ref. 25.
The pixel values in the data are in arbitrary detector units (ADU). The conversion factor from ADU to
number of photons is 7 ADU per photon. Some areas of the detector were unreadable and some
scattering angles were not covered by the detector, such as the gap between the two detector halves that
lets the direct beam through. These areas are identiﬁed by a mask entry in the CXIDB ﬁle format.
The data was ﬁltered in three steps. (1) Hits were distinguished from blanks using methods described
in refs 21 and 24. This yielded 1,600 hits. (2) 307 Diffraction patterns that correspond to a Mimivirus
Parameter
Value
Photon energy
1,200 keV
Detector distance
0.74 m
Pixel size
75 μm
Number of pixels
1,024 × 1,024
Focal size
10 μm2
Table 1. Summary of experimental parameters.
Run number
Sample
Number of frames
Number of frames selected for analysis in ref. 10
73
Dark
651
N/A
80
Mimivirus
14,273
0
81
Mimivirus
14,450
0
82
Mimivirus
11,371
0
83
Dark
15,636
N/A
84
Mimivirus
65,594
0
87
Mimivirus
93,840
0
89
Dark
3,821
N/A
90
Mimivirus
77,644
30
91
Mimivirus
4,943
6
92
Mimivirus
33,721
39
93
Mimivirus
43,679
24
94
Mimivirus
58,931
40
95
Mimivirus
42,083
10
97
Mimivirus
36,899
33
98
Dark
7,794
N/A
152
Dark
2,498
N/A
156
Mimivirus
64,977
3
157
Mimivirus
90,403
13
Table 2. List of experimental runs. Runs labeled as dark had the X-ray beam turned off and are included to
allow for detector calibration. The lack of good hits before run 90 was possibly ﬁxed by a changed injection
nozzle at this point.
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
3

--- Page 4 ---

particle were selected by hand. An icosahedral or pseudo-icosahedral particle will in most orientations
yield a distinctive type of pattern showing six outwards-going streaks. This feature and particle size,
determined from the fringe spacing, was used for this selection. (3) When the detector is exposed to high
intensities, the intensity can spill over from a pixel to neighboring pixels. We start seeing these effects at
intensities above 750 photons per pixel. In the ﬁnal dataset, diffraction patterns suffering from this effect
were ﬁltered out, resulting in 198 unsaturated diffraction patterns. A subset of this dataset is shown in Fig. 1.
Technical Validation
3D reconstruction
The 198 diffraction patterns were successfully assembled in a 3D Fourier volume and subsequent
phase retrieval provided the full 3D electron density of the virus with a full-period resolution of 125 nm10.
This indicates that the Mimivirus is reproducible to at least this resolution.
Validation of the 3D reconstruction
In cryo-electron microscopy (cryo-EM), data is routinely split prior to analysis and the analysis is
performed in parallel on the two sets26. Our ﬁrst method for validating the 3D reconstruction is an
adaptation of this technique. The diffraction patterns are randomly split in two sets of equal size. The
recovery of the 3D alignment is performed independently on the two sets using the same parameters but
independent random starting points. Phase retrieval is also performed independently using the same
parameters. The standard practice in the ﬁeld is to repeat the reconstruction at least 100 times and the
results are then averaged to average out effects of the random starting point4,27.
The EMC algorithm recovers the relative orientation of the particles from the diffracted data alone but
the arbitrary rotation of the entire system can be different comparing the two resulting 3D electron
density maps. In order to compare the two recovered electron densities we therefore have to rotate one of
the two data sets to best match the other. This is done using brute force by interpolating one of the maps
at a regular array corresponding to the tested rotation. To compare the two maps, the Pearson correlation
coefﬁcient is calculated. The rotation with the highest Pearson correlation is assumed to correspond to
the proper relative orientation.
The two aligned electron density maps are then compared using the Fourier shell correlation (FSC)26,
which provides a measure of the similarity as a function of resolution. The threshold for what is regarded
as an acceptable ﬁt ranges between 0.14 and 0.5 in cryo-EM literature28,29.
820
1
Figure 1. The ﬁrst 24 of the 198 diffraction patterns in this dataset. The color scale is logarithmic and ranges
from 1 to 820 photons per pixel. This is a modiﬁcation of a ﬁgure previously presented in ref. 10.
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
4

--- Page 5 ---

In X-ray crystallography some Bragg spots are usually excluded from the analysis and instead that
information is used to verify the recovered expected strength of the respective Bragg spot30. Using the
same idea, 10% of the diffraction patterns were selected to be used for validation only. In the EMC
scheme these patterns are excluded from the analysis but are still compared to the recovered Fourier
transform of the particle. The measure for determining whether the recovered model agrees with the
excluded diffraction patterns is the likelihood function used internally in EMC.
The analogy with the Rfree value in crystallography should not be over emphasized. Bragg peaks are
linearly independent parameters and ther is no suitable analogy in the continuous diffraction case.
Furthermore, in the case described here, the process that is validated is that of pattern alignment and not
phase retrieval. It is therefore natural to choose individual diffraction patterns as the information unit to
exclude rather than i.e., individual pixels or regions of pixels.
These validation methods were previously described in ref. 10.
Usage Notes
Data was stored in the CXIDB25 data format which uses the HDF5 format. HDF5 ﬁles are readable in
many computing environments including python using the h5py module and MATLAB using e.g., the
h5read function. Convenient functions for accessing the CXIDB data ﬁle exist in the libspimage package
for C and python31. For visualizing data the CXIDB ﬁle browser Owl (https://github.com/FilipeMaia/owl)
is recommended.
References
1. Emma, P. et al. First lasing and operation of an ångström-wavelength free-electron laser. Nat. Photonics 4, 641–647 (2010).
2. Neutze, R., Wouts, R., van der Spoel, D., Weckert, E. & Hajdu, J. Potential for biomolecular imaging with femtosecond X-ray
pulses. Nature 406, 752–757 (2000).
3. Chapman, H. N. et al. Femtosecond diffractive imaging with a soft-X-ray free-electron laser. Nat. Phys 2, 839–843 (2006).
4. Seibert, M. M. et al. Single mimivirus particles intercepted and imaged with an X-ray laser. Nature 470, 78–81 (2011).
5. Loh, N.-T. D. & Elser, V. Reconstruction algorithm for single-particle diffraction imaging experiments. Phys. Rev. E. Stat. Nonlin.
Soft Matter Phys 80, 026705 (2009).
6. Fung, R., Shneerson, V., Saldin, D. K. & Ourmazd, A. Structure from ﬂeeting illumination of faint spinning objects in ﬂight. Nat.
Phys 5, 64–67 (2008).
7. Galayda, J. LCLS The First Experiments. Available at http://www.slac.stanford.edu/pubs/slacreports/reports03/slac-r-611.pdf
(2003).
8. Hantke, M. F. et al. High-throughput imaging of heterogeneous cell organelles with an X-ray laser. Nat. Photonics 8,
943–949 (2014).
9. van der Schot, G. et al. Imaging single cells in a beam of live cyanobacteria with an X-ray laser. Nat. Commun 6, 5704 (2015).
10. Ekeberg, T. et al. Three-Dimensional Reconstruction of the Giant Mimivirus Particle with an X-Ray Free-Electron Laser. Phys.
Rev. Lett. 114, 098102 (2015).
11. Raoult, D. et al. The 1.2-megabase genome sequence of Mimivirus. Science 306, 1344–1350 (2004).
12. Claverie, J.-M. & Abergel, C. Mimivirus and its virophage. Annu. Rev. Genet. 43, 49–66 (2009).
13. Xiao, C. et al. Structural studies of the giant mimivirus. PLoS Biol. 7, e92 (2009).
14. Xiao, C. et al. Cryo-electron microscopy of the giant Mimivirus. J. Mol. Biol. 353, 493–496 (2005).
15. Byrne, D. et al. The polyadenylation site of Mimivirus transcripts obeys a stringent ‘hairpin rule’. Genome Res. 19,
1233–1242 (2009).
16. DePonte, D. P. et al. Gas dynamic virtual nozzle for generation of microscopic droplet streams. J. Phys. D. Appl. Phys 41,
195505 (2008).
17. Bogan, M., Benner, W. & Boutet, S. Single particle X-ray diffractive imaging. Nano Lett. 8, 310–316 (2008).
18. Bostedt, C. et al. Ultra-fast and ultra-intense X-ray sciences: ﬁrst results from the Linac Coherent Light Source free-electron laser.
J. Phys. B At. Mol. Opt. Phys 46, 164003 (2013).
19. Strüder, L. et al. Large-format, high-speed, X-ray pnCCDs combined with electron and ion imaging spectrometers in a
multipurpose chamber for experiments at 4th generation light sources. Nucl. Instruments Methods Phys. Res. Sect. A Accel.
Spectrometers, Detect. Assoc. Equip 614, 483–496 (2010).
20. Yoon, C. H. et al. Unsupervised classiﬁcation of single-particle X-ray diffraction snapshots by spectral clustering. Opt. Express 19,
16542 (2011).
21. Kassemeyer, S. et al. Femtosecond free-electron laser X-ray diffraction data sets for algorithm development. Opt. Express 20,
4149 (2012).
22. Young, L. et al. Femtosecond electronic response of atoms to ultra-intense X-rays. Nature 466, 56–61 (2010).
23. Foucar, L. et al. CASS—CFEL-ASG software suite. Comput. Phys. Commun. 183, 2207–2213 (2012).
24. Barty, A. et al. Cheetah: software for high-throughput reduction and analysis of serial femtosecond X-ray diffraction data. J. Appl.
Crystallogr 47, 1118–1131 (2014).
25. Maia, F. R. N. C. The Coherent X-ray Imaging Data Bank. Nat. Methods 9, 854–855 (2012).
26. Harauz, G. & van Heel, M. Exact ﬁlters for general geometry three dimensional reconstruction. Optik (Stuttg) 78, 146–156 (1986).
27. Chapman, H. N. et al. High-resolution ab initio three-dimensional X-ray diffraction microscopy. J Opt Soc Am A Opt Image Sci
Vis. 23, 1179–1200 (2006).
28. Rosenthal, P. B. & Henderson, R. Optimal Determination of Particle Orientation, Absolute Hand, and Contrast Loss in
Single-particle Electron Cryomicroscopy. J. Mol. Biol. 333, 721–745 (2003).
29. Böttcher, B., Wynne, S. & Crowther, R. Determination of the fold of the core protein of hepatitis B virus by electron
cryomicroscopy. Nature 386, 88–91 (1997).
30. Brünger, A. Free R value: a novel statistical quantity for assessing the accuracy of crystal structures. Nature 355, 472 (1992).
31. Maia, F. R. N. C., Ekeberg, T., van der Spoel, D. & Hajdu, J. Hawk: the image reconstruction package for coherent X-ray diffractive
imaging. J. Appl. Crystallogr 43, 1535–1539 (2010).
Data Citation
1. Ekeberg, T. et al. Coherent X-ray Imaging Data Bank http://dx.doi.org/10.11577/1236752 (2015).
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
5

--- Page 6 ---

Acknowledgements
This work was supported by the Swedish Research Council, the Knut and Alice Wallenberg Foundation,
the Max Planck Society, the European Research Council, the Röntgen-Ångström Cluster, and Stiftelsen
Olle Engkvist Byggmästare. Portions of this research were carried out at the Linac Coherent Light Source,
a national user facility operated by Stanford University on behalf of the US Department of Energy, Ofﬁce
of Basic Energy Sciences. We are grateful to the scientiﬁc and technical staff of the LCLS for support.
Author Contributions
T.E. wrote the manuscript with contributions from all authors. C.A., J.-M.C., V.S. contributed the
Mimivirus particles. D.D.P., R.L.S., L.L., M.J.B. developed and ran the sample delivery system. O.J.,
D.W., B.I., C.Y.H., R.S., M.S., D.O. prepared the samples and performed ofﬂine injection analysis. L.F.,
S.K. performed the online data analysis. MM.L., N.-T.D.L., F.R.N.C.M., M.F.H., T.E., A.M., A.B.
performed ofﬂine data analysis. L.F., S.W.E., D.R., A.R., B.R., B.E., J.U., C.S., F.K., I.S. designed,
constructed, and operated the CAMP instrument. R.H., A.H., N.K., P.H., L.S., G.W., G.H., C.R., and H.S.
designed, constructed, and operated the pnCCD detectors. C.W., H.H., and H.G. contributed to the
detector and its implementation. S.B., M.B., H.F., and L.G. contributed instrumentation. J.K.
characterized the FEL focus. A.A., J.A., B.I., M.M., S.S., N.C., C.B., J.D.B., M.F., M.S., and J.A. were
involved in collecting the data. C.B. and J.D.B. were in charge of the AMO endstation. I.S., M.B., H.C.,
and J.H. designed the experiment. I.A. and J.H. conceived the experiment.
Additional Information
Competing ﬁnancial interests: The authors declare no competing ﬁnancial interest.
How to cite this article: Ekeberg, T et al. Single-shot diffraction data from the Mimivirus particle using
an X-ray free-electron laser. Sci. Data 3:160060 doi: 10.1038/sdata.2016.60 (2016).
This work is licensed under a Creative Commons Attribution 4.0 International License. The
images or other third party material in this article are included in the article’s Creative
Commons license, unless indicated otherwise in the credit line; if the material is not included under the
Creative Commons license, users will need to obtain permission from the license holder to reproduce the
material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0
Metadata associated with this Data Descriptor is available at http://www.nature.com/sdata/ and is released
under the CC0 waiver to maximize reuse.
© The Author(s) 2016
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
6

--- Page 7 ---

Tomas Ekeberg1,2, Martin Svenda1, M. Marvin Seibert1, Chantal Abergel3,
Filipe R.N.C. Maia1, Virginie Seltzer3, Daniel P. DePonte2,4, Andrew Aquila4,5,
Jakob Andreasson1, Bianca Iwan1,6, Olof Jönsson1,7, Daniel Westphal1, Duško Odic´1,
Inger Andersson1, Anton Barty2, Meng Liang2,4, Andrew V. Martin2,8, Lars Gumprecht2,
Holger Fleckenstein2, Saša Bajt9, Miriam Barthelmess9, Nicola Coppola2,
Jean-Michel Claverie3, N. Duane Loh10,11, Christoph Bostedt4, John D. Bozek12,
Jacek Krzywinski4, Marc Messerschmidt4, Michael J. Bogan10, Christina Y. Hampton10,
Raymond G. Sierra10, Matthias Frank13, Robert L. Shoeman14, Lukas Lomb14,
Lutz Foucar14,15, Sascha W. Epp15,16, Daniel Rolles14,15,17, Artem Rudenko15,16,17,
Robert Hartmann18, Andreas Hartmann18, Nils Kimmel19,20, Peter Holl18,
Georg Weidenspointner19,20, Benedikt Rudek15,16, Benjamin Erk15,16,
Stephan Kassemeyer14, Ilme Schlichting14,15, Lothar Strüder18,21, Joachim Ullrich15,16,22,
Carlo Schmidt15,16, Faton Krasniqi14,15, Günter Hauser19,20, Christian Reich18,
Heike Soltau18, Sebastian Schorb23, Helmut Hirsemann9, Cornelia Wunderer9,
Heinz Graafsma9, Henry Chapman2,24 & Janos Hajdu1,5
1Department of Cell and Molecular Biology, Laboratory of Molecular Biophysics, Uppsala University, Husargatan 3
(Box 596), SE-751 24 Uppsala, Sweden. 2Center for Free-Electron Laser Science, DESY, Notkestrasse 85, 22607
Hamburg, Germany. 3Information Génomique et Structurale (UMR7256) CNRS & Aix-Marseille Université, Institut
de Microbiologie de la Méditerranée (FR3479), Parc Scientiﬁque de Luminy, Case 934, 13288 Marseille Cedex 9,
France. 4LCLS, SLAC National Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, California 94025, USA.
5European XFEL, Albert-Einstein-Ring 19, 22761 Hamburg, Germany. 6Commissariat à l’énergie atomique et aux
énergies alternatives, Centre d’études de Saclay, 91191 Gif sur Yvette cedex, France. 7Molekyl- och kondenserade
materiens fysik, Institutionen för Fysik och Astronomi, Uppsala University, Lägerhyddsvägen 1 (Box 524), SE-751
20 Uppsala, Sweden. 8The University of Melbourne, 161 Barry Street, Parkville, 3010 Victoria, Australia. 9Photon
Science, DESY, Notkestrasse 85, 22607 Hamburg, Germany. 10Stanford PULSE Institute, SLAC National
Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, California 94025, USA. 11Centre for BioImaging
Sciences, National University of Singapore, 14 Science Drive 4 Blk S1 A, Singapore 117546, Singapore.
12Synchrotron SOLEIL, L’orme des Merisiers roundabout of St Aubin, 91190 Saint Aubin, France. 13Lawrence
Livermore National Laboratory, 7000 East Avenue, Mail Stop L-211, Livermore, California 94551, USA. 14Max-
Planck-Institut für medizinische Forschung, Jahnstr. 29, 69120 Heidelberg, Germany. 15Max Planck Advanced Study
Group, Center for Free Electron Laser Science, Notkestrasse 85, 22607 Hamburg, Germany. 16Max-Planck-Institut für
Kernphysik, Saupfercheckweg 1, 69117 Heidelberg, Germany. 17Department of Physics, J.R. Macdonald Laboratory,
Kansas State University, 116 Cardwell Hall, Manhattan, Kansas 66506, USA. 18PNSensor GmbH, Otto-Hahn-Ring 6,
81739 Munich, Germany. 19Max-Planck-Institut Halbleiterlabor, Otto-Hahn-Ring 6, 81739 Munich, Germany.
20Max-Planck-Institut für extraterrestrische Physik, Giessenbachstrasse, 85741 Garching, Germany. 21Universität
Siegen, Emmy-Noether Campus, Walter Flex Str. 3, 57068 Siegen, Germany. 22Physikalisch-Technische
Bundesanstalt, Bundesallee 100, 38116 Braunschweig, Germany. 23Institut für Optik und Atomare Physik,
Technische Universität Berlin, Hardenbergstrasse 36, 10623 Berlin, Germany. 24University of Hamburg,
Notkestrasse 85, 22607 Hamburg, Germany.
www.nature.com/sdata/
SCIENTIFIC DATA | 3:160060 | DOI: 10.1038/sdata.2016.60
7

```
