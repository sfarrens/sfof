fof_cluster_finder
==================

@author Samuel Farrens

Introduction
------------
FOF_OMP is a friends-of-friends galaxy cluster detection algorithm that operates in
either spectroscopic or photometric redshift space. The linking parameters,
both transverse and along the line-of-sight, change as a function of
redshift to account for selection effects.

The code is written in C++ and implements OMP to loop through the
photo-z bins.

Larger catalogues can be split into overlapping pieces using the
PYCATCUT python script. These pieces can than be run through the FoF
independently and the subsequent results merged using the PYMERGE
python script.

Configuration Parameters
------------------------

And here...

Class Overview
--------------

And here...
 
Dependencies
------------

FOF_OMP requires: CFITSIO and OMP

PYCATCUT requires: NUMPY

PYMERGE requires: NUMPY

@todo Make Euclid friendly.
