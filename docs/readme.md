fof_cluster_finder
==================

@authors Samuel Farrens, Stefano Sartor, Luca Tornatore

Introduction
------------
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

Dependencies
------------

The codes (main.cpp, cat\_split.cpp, cat\_merge.cpp) require the
following packages:

* <a href="http://www.cmake.org/" target="_blank">CMake</a> 

* <a href="http://www.boost.org/" target="_blank">Boost</a> *(Note:
   Must be built with a  C++11 compatible compiler e.g. gcc)*

* <a href="http://heasarc.gsfc.nasa.gov/fitsio/" target="_blank">CFITSIO</a> 

* <a href="http://openmp.org/wp/" target="_blank">OMP</a>

* <a href="https://gcc.gnu.org/projects/cxx0x.html" target="_blank">C++0x/C++11</a>

Compilation
------------

To compile the codes simply run:

> cmake CMakeLists.txt

On some systems it may be neccesary to specify the paths to
packages. This can be done with the following options:

* To specify the CFITSIO directory use the following option after the
cmake command:
> -DCFITSIO_ROOT_DIR

`e.g cmake CMakeLists.txt -DCFITSIO_ROOT_DIR=/usr/cfitsio/`

* To specify the Boost directory use the following option after the
cmake comamnd:
> -DBOOST_ROOT

`e.g cmake CMakeLists.txt -DCFITSIO_ROOT_DIR=/usr/boost/`

* The C and C++ compilers can also be specified using the following
  options before the cmake command:
> CC & CXX
`e.g CC=gcc-4.9.0 CXX=g++-4.9.0 cmake CMakeLists.txt`

Upon successful compilation of the code three executables will be
generated in the fof\_cluster\_finder subdirectory: main, cat\_split
and cat\_merge.

Execution
------------

#Main Code

The friends-of-friends (FoF) algorithm can be run in two different
modes (spectroscopic or photometric) depending on the type of input
data.

**Input Format**

The expected input file formats (ASCII or FITS) for the
corresponding modes are as follows:

* `Spectroscopic Mode`:
  1. Galaxy ID
  2. Galaxy Right Ascension
  3. Galaxy Declination
  4. Galaxy Redshift

* `Photometric Mode`:
  1. Galaxy ID
  2. Galaxy Right Ascension
  3. Galaxy Declination
  4. Galaxy Photometric Redshift
  5. Galaxy Photometric Redshift Error

**Run**

The code options can be provided either in a parameter file (Note: the
defult parameter file name is param_file.ini) or directly as
arguments.

If a parameter file is available the code can be run simply as
follows:

> main

All parameter file options can be overridden by providing a command
line argument. For example to ignore a file name specified in the
parameter file the following option can be used:

> main --input_file FILE_NAME

All of the code options are listed below, but can be viewed by
running:

> main --help

The majority of the code options have defualt values that will be
applicable to most data sets. The only options that need to be
specified for every run are the input file name and the linking
parameter values. For example to run the code in photometric mode on a
data set that is well sampled around z=0.5 and does not extend beyond
z=3.0 the following command would be sufficient to run the code:

> main -i FILE_NAME --link_r 0.06 --link_z 1.1

See [examples](../examples/readme.md) for example data sets and
parameter files to test the code.

**Code Options**

* ` -h [ --help ]`: This option produces the help message with all the
  code options and exits.

* ` -v [ --version ]`: This option prints the current version of the
  code and exits.

* ` -p [ --parameters ]`: This option prints the values assigned to each
  of the code parameters.

* ` -c [ --config ]`: This option specifies the configuration file
  name. The default file name is param_file.ini.
 
* ` -i [ --input_file ]`: This option specifies the input file name.

* ` --output_clusters`: This option specifies the output file name of
  the cluster properties.

* `--output_members`: This option specifies the ouput file name of the
  cluster member properties

* `--link_r`: This option specifies the value of the transverse
  linking parameter.

* `--link_z`: This option specifies the value of the Line-of-sight
  linking parameter.

* `--input_mode`: This option specifies the input file format. The
options permitted are ascii or fits. The default value is ascii.

* `--output_mode`: This option specifies the output file format. The
options permitted are ascii or fits. The default value is ascii.

* `--fof_mode`: This option specifies the FoF redshift mode. The options
  permitted are spec or phot. The default value is phot.
  
*  `--link_mode`: This option specifies the FoF linking mode. The
   options permitted are fixed or dynamic. The default value is dynamic.
   
*  `--min_ngal`:  This option specifies the minimum number of galaxies
   members required to form a cluster. The default value is 10.
   
*  `--z_min`: This option specifies the low redshift limit of the
   sample. The default value is 0.0.

*  `--z_max`: This option specifies the high redshift limit of  the
   sample. The default value is 3.0.

*  `--z_bin_size`: This option specifies the size of redshift bins. The
   default value is 0.01.

*  `--z_ref`: This option specifies the reference redshift for
   calculations. The default value is 0.5.

*  `--dz_max`: This option specifies the maximum photometric redshift
   error allowed. The default value is 0.05.

*  `--nz_data`: This option specifies the file name for a predefined
   N(z) distribution. 

*  `--c`: This option specifies the speed of light in km/s. The default
   value is 2.997e5.

*  `--H0`: This option specifies the value of the Hubble parameter in
   km/s/Mpc. The default value is 100.0.

*  `--omega_m`: This option specifies the value of the matter density of
   the Universe. The default value is 0.3.

*  `--omega_l`: This option specifies the value of the dark energy
   density of the Universe. The default value is 0.7.

*  `--print_bin_data`: This option specifies that the redshift bin data
   should be printed to a file.

*  `--print_kdtree_data`:  This option specifies that the kd-tree data
   should be printed to a file.

*  `--print_bg_data`:  This option specifies that the background field
   data should be printed to a file.
