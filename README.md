# Friends-of-Friends Galaxy Cluster Detection Algorithm

> Author: **Samuel Farrens**

> Year: **2016**

> Version: **3.2**

> Email: **[samuel.farrens@gmail.com](mailto:samuel.farrens@gmail.com)**

## Contents

1. [Introduction](#intro_anchor)
1. [Notice](#note_anchor)
1. [Contributors](#contribute_anchor)
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

<img src="docs/images/fof_1.png" width="400" align="right">

### Angular Percolation

Unlike a standard FoF this algorithm percolates in angular space. The distance between two galaxies is calculated as follows:

> D = arcos(sin(Dec1)sin(Dec2) + cos(Dec1)cos(Dec2)cos(RA1-RA2))

For two galaxies in a given redshift bin to be considered friends (*i.e.* linked) they must satisfy the following condition:

> D <= D_friend(z)

where *D_friend(z)* is the transverse linking length for a given redshift bin.

### Redshift Binning

The first task the code performs is to bin all of the input galaxies by redshift. This is used to calculate *dn/dz* where *dn* is the number of galaxies in a given bin and *dz* is the bin width. Each galaxy is only counted once for this calculation, thus for photometric data the peak photometric redshift value of the galaxy is used.

`NOTE: If a predefined N(z) is provided, then these values are used for the dn/dz calculation.`

The differential comoving volume as a function of redshift, *dV/dz*, and the agular diameter distance, *da*, are then calculated for each bin using the values of *H0*, *Omega_M* and *Omega_L* provided.

Finally the angular linking length, *D_friend*, for each bin is defined as:

> D_friend = ((dn/dz x dz/dV) ^ -0.5 x C_friend) / da

where *C_friend* is the value of *D_friend* at the reference redshift, *z_ref*. In other words, the value of *D_friend* at *z_ref* will be the input value of *link_r*.

## Something...

<img src="docs/images/fof_2.png" width="400" align="middle">

<img src="docs/images/fof_3.png" width="300" align="middle">

### Singal-to-Noise

The singal-to-noise ratio is calculated as follows:

S/N = (N<sub>gal</sub> - A * Bg) / (A * Bg)<sup>0.5</sup>

where A is the cluster area and Bg is the background level at the
cluster redshift. Unless an N(z) is provided the code simply takes the
number of objects at the cluster redshift divided by the catalogue
area as Bg.
