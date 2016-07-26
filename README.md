# Friends-of-Friends Galaxy Cluster Detection Algorithm

> Author: **Samuel Farrens**

> Year: **2016**

> Version: **3.2**

> Email: **[samuel.farrens@gmail.com](mailto:samuel.farrens@gmail.com)**

## Contents

1. [Introduction](#intro_anchor)
1. [Notice](#note_anchor)
1. [Contributors](#contributors_anchor)
1. [Scientific Background and Method](#method_anchor)
1. [Installation and Execution](./docs/readme.md)
1. [Examples](./examples/readme.md)

<a name="intro_anchor"></a>
## Introduction
FOF_OMP is a friends-of-friends galaxy cluster detection algorithm that operates in
either spectroscopic or photometric redshift space. The linking parameters,
both transverse and along the line-of-sight, change as a function of
redshift to account for selection effects.

The code is written in C++ and implements OMP to loop through the
photometric redshift bins.

Larger catalogues can be split into overlapping pieces using the
cat\_split.cpp code. These pieces can than be run through the FoF
independently and the subsequent results merged using the cat\_merge.cpp
code.

<a name="note_anchor"></a>
## Notice

This software is fully open source and all are welcome to use or modify it for
any purpose.

I would kindly request that any scientific publications making use of this software cite <a href="http://adsabs.harvard.edu/abs/2011MNRAS.417.1402F" target="_blank">Farrens et. al (2011)</a>.

<a name="contributors_anchor"></a>
## Contributors

The vast majority of this code has been written from scratch by Samuel Farrens. Additional contributions have been made by:

* Filipe Abdalla - (debugging, concepts and ideas)
* Eduardo Cypriano - (proto-code, concepts and ideas )
* Stefano Sartor - (optimisation)
* Luca Tornatore - (optimisation)

<a name="method_anchor"></a>
## Scientific Background and Method

### Angular Percolation

<img src="docs/images/fof_1.png" width="400" align="right">

Unlike a standard FoF this algorithm percolates in angular space. The angular distance in radians between two galaxies is calculated as follows:

> D = arcos(sin(Dec<sub>1</sub>)sin(Dec<sub>2</sub>) + cos(Dec<sub>1</sub>)cos(Dec<sub>2</sub>)cos(RA<sub>1</sub>-RA<sub>2</sub>))

For two galaxies in a given redshift bin to be considered friends (*i.e.* linked) they must satisfy the following condition:

> D <= D<sub>friend</sub>(z)

where *D<sub>friend</sub>(z)* is the transverse linking length in radians for a given redshift bin.

### Redshift Binning

This section is only relevant for *fof_mode = dynamic*.

The first task the code performs is to bin all of the input galaxies by redshift. This is used to calculate *dn/dz* where *dn* is the number of galaxies in a given bin and *dz* is the bin width. Each galaxy is only counted once for this calculation, thus for photometric data the peak photometric redshift value of the galaxy is used.

`NOTE: If a predefined N(z) is provided, then these values are used for the dn/dz calculation.`

The differential comoving volume as a function of redshift, *dV/dz*, and the agular diameter distance, *da*, are then calculated for each bin using the values of *H0*, *Omega<sub>M</sub>* and *Omega<sub>L</sub>* provided.

Finally the angular linking length, *D<sub>friend</sub>(z)*, for each bin is defined as:

> D<sub>friend</sub>(z) = ((dn(z)/dz x dz/dV(z)) ^ -0.5 x r<sub>ref</sub>) / da(z)

where *r<sub>ref</sub>* is:

> r<sub>ref</sub> = (dn(z<sub>ref</sub>)/dz x dz/dV(z<sub>ref</sub>)) ^ 0.5 x link<sub>r</sub>

*z<sub>ref</sub>* is the specified reference redshift and *link<sub>r</sub>* is the input transverse linking parameter. This calculation ensures that:

> D<sub>friend</sub>(z<sub>ref</sub>) = link<sub>r</sub> / da(z<sub>ref</sub>)

and that for bins with less galaxies (*e.g.* at higher redshifts when selection effects have a stronger impact) the value of *D<sub>friend</sub>(z)* will increase, while for bins with more galaxies the value of *D<sub>friend</sub>(z)* will decrease. This produces *N<sub>gal</sub>* values that are more redshift independent.

### Spectroscopic Line-of-Sight Linking

<img src="docs/images/fof_2.png" width="300" align="right">

In spectroscopic mode the line-of-sight linking length is calculated as follows:

> z<sub>friend</sub> = link<sub>z</sub> / (1 + z)

For two galaxies to be friends they must satisfy:

> |z<sub>1</sub> - z<sub>2</sub>| <= z<sub>friend</sub>

In this sense the percolation is peformed in 3 dimensions.

### Photometric Line-of-Sight Linking

<img src="docs/images/fof_3.png" width="200" align="left">

In photometric mode a galaxy is allocated to a redshift bin if it satisfies the following:

> |z<sub>gal</sub> - z<sub>bin</sub>| <= z<sub>gal_err</sub> x link<sub>z</sub>

In this case *link<sub>z</sub>* is a factor that determines how much the galaxies smear along the line-of-sight.

In this mode percolation is performed in 2 dimensions for each redshift bin independently. As galaxies can exist in multiple bins it is possible to form "proto-clusters" in different bins with similar members.

When the percolation has finished for all of the bins proto-clusters with common members are merged to form the final detections.

### Cluster properties

**Centre**

The cluster centre (RA, Dec, z) is calculated as the median of the galaxy members. The errors all calculated as the standard error on the median (*i.e.* sigma/n^0.5).

**Richness**

The cluster richness is calculated a the number of member galaxies.

**Singal-to-Noise**

The cluster singal-to-noise ratio is calculated as follows:

> S/N = (N<sub>gal</sub> - A * Bg) / (A * Bg)<sup>0.5</sup>

where *A* is the cluster area and *Bg* is the background level at the cluster redshift. Unless an *N(z)* is provided the code simply takes the number of objects at the cluster redshift divided by the catalogue area as *Bg*.

**Radius**

The cluster radius is calculated as the distance from the cluster center to the position of the farthest member in the units specified.

**Area**

The cluster area is calculated as:

> pi x radius ^ 2

in the units specified.
