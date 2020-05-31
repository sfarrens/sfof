# SFoF Installation and Execution

> Author: **Samuel Farrens**  
> Email: **[samuel.farrens@cea.fr](mailto:samuel.farrens@cea.fr)**  
> Version: **4.0**  
## Contents

1. [Introduction](#Introduction)
1. [Dependencies](#Dependencies)
1. [Installation](#Installation)
   1. [Docker Image](#Docker-Image)
   1. [From Source](#From-Source)
   1. [CMake Options](#CMake-Options)
   1. [macOS Issues](#macOS-Issues)
1. [Execution](#Execution)
   1. [SFoF Code](#SFoF-Code)
   1. [Cat_Split Code](#Cat_Split-Code)
   1. [Cat_Merge Code](#Cat_Merge-Code)

## Introduction

This section provides details for installing and running the SFoF algorithm.

Detailed information about class methods and functions can be found [here](http://sfarrens.github.io/sfof/).

## Dependencies

The codes (`main.cpp`, `cat_split.cpp`, `cat_merge.cp`) require the
following packages:

* [CMake](http://www.cmake.org/)
* [Boost](http://www.boost.org/)
* [CFITSIO](http://heasarc.gsfc.nasa.gov/fitsio/)
* [OMP](http://openmp.org/wp/)
* [C++0x/C++11](https://gcc.gnu.org/projects/cxx0x.html)

## Installation

### Docker Image

If you have [Docker](https://www.docker.com/) installed, you can pull the latest build of the SFoF image from [Docker Hub](https://hub.docker.com/r/sfarrens/sfof).

```bash
$ docker pull sfarrens/sfof
```

To run this image on data in the current directory, simply run:

```bash
$ docker run -v ${PWD}:/workdir -it sfarrens/sfof /bin/bash -c "cd workdir && sfof"
```

The reference to `${PWD}` can be replaced by the path to any directory on your system and options can be passed to `sfof` inside the double quotes.

### From Source

To compile the codes from source, first clone the repository.

```bash
$ git clone https://github.com/sfarrens/sfof.git
$ cd sfof
```

Then create a build directory.

```bash
$ mkdir build
$ cd build
```

Then run CMake to generate a makefile.

```bash
$ cmake ..
```

Finally, run make to compile.

```bash
$ make
```

Upon successful compilation of the code three executables will be
generated in the `sfof` subdirectory: `sfof`, `cat_split`
and `cat_merge`.

You can install these to your `bin` directory by running:

```bash
$ mask install
```

> Note: On some systems it may be necessary to run `sudo make install`.

### CMake Options

On some systems it may be neccessary to specify the paths to
packages. This can be done with the following options:

* To specify the CFITSIO directory use the following option after the
cmake command: `-DCFITSIO_ROOT_DIR` *e.g*

  ```bash
  cmake .. -DCFITSIO_ROOT_DIR=/usr/cfitsio/
  ```

* To specify the Boost directory use the following option after the
cmake comamnd: `-DBOOST_ROOT` *e.g*
  ```bash
  cmake .. -DCFITSIO_ROOT_DIR=/usr/boost/
  ```

* The C and C++ compilers can also be specified using the following
  options before the cmake command: `CC & CXX` *e.g.*
  ```bash
  CC=gcc-9 CXX=g++-9 cmake ..
  ```

### macOS Issues

For help with comilation on macOS see [here](./mac_osx_install.md).

## Execution

### SFoF Code

The Super Friends-of-Friends (SFoF) algorithm can be run in two different modes (spectroscopic or photometric) depending on the type of input data.

**Input Format**

The expected input file formats \(ASCII or FITS\) for the
corresponding modes are as follows:

* **Spectroscopic Mode**:
  1. Galaxy ID
  2. Galaxy Right Ascension
  3. Galaxy Declination
  4. Galaxy Redshift

* **Photometric Mode**:
  1. Galaxy ID
  2. Galaxy Right Ascension
  3. Galaxy Declination
  4. Galaxy Photometric Redshift
  5. Galaxy Photometric Redshift Error

**Output Format**

The code produces two output files. The first contains the properties
of the detected cluster candidates and the second contains the
properties of the member galaxies that belong to each of these
candidates according to the FoF. The formats for the output files are
as follows:

* **Cluster Prorperties**:
  1. Cluster ID
  2. Cluster Right Ascension \[degrees\] (median of members)
  3. Cluster Right Ascension Error \[degrees\] (error on median)
  4. Cluster Declination \[degrees\] (median of members)
  5. Cluster Declination Error \[degrees\] (error on median)
  6. Cluster Redshift (median of members)
  7. Cluster Redshift Error (error on median)
  8. Cluster N<sub>gal</sub> (i.e. number of members)
  9. Cluster Signal-to-noise ratio (see below for calculation)
  10. Cluster radius \[arcmin\] (average distance of members from centre)
  11. Cluster area \[arcmin<sup>2</sup>\]

* **Member Prorperties**:
  1. Cluster ID
  2. Cluster N<sub>gal</sub>
  3. Cluster Redshift
  4. Galaxy ID
  5. Galaxy Right Ascension \[degrees\]
  6. Galaxy Declination \[degrees\]
  7. Galaxy Redshift

**Run**

The code options can be provided either in a configuration file (Note: the default configuration file name is `param_file.ini`) or directly as
arguments.

If a configuration file is available in the same directory the code can be run simply as follows:

```bash
$ sfof
```

All configuration file options can be overridden by providing a command
line argument. For example, to override a file name specified in the
configuration file the following option can be used:

```bash
$ sfof --input_file FILE_NAME
```

All of the code options are listed below, but can be viewed by
running:

```bash
$ sfof --help
```

The majority of the code options have default values that will be
applicable to most data sets. The only options that need to be
specified for every run are the input file name and the linking
parameter values. For example to run the code in photometric mode on a
data set that is well sampled around `z=0.5` and does not extend beyond
`z=3.0` the following command would be sufficient to run the code:

```bash
$ sfof -i FILE_NAME --link_r 0.06 --link_z 1.1
```

See [examples](../examples/) for example data sets and
configuration files to test the code.

**Code Options**

* ` -h [ --help ]`: This option produces the help message with all the code options and exits.

* ` -v [ --version ]`: This option prints the current version of the code and exits.

* ` -p [ --parameters ]`: This option prints the values assigned to each of the code parameters.

* ` -c [ --config ]`: This option specifies the configuration file name. The default file name is *param_file.ini*.

* ` -i [ --input_file ]`: This option specifies the input file name.

* ` --output_clusters`: This option specifies the output file name of the cluster properties.

* ` --output_members`: This option specifies the ouput file name of the cluster member properties.

* ` --link_r`: This option specifies the value of the transverse linking parameter.

* ` --link_z`: This option specifies the value of the line-of-sight linking parameter.

* ` --input_mode`: This option specifies the input file format. The
options permitted are *ascii* or *fits*. The default value is *ascii*.

* ` --output_mode`: This option specifies the output file format. The
options permitted are *ascii* or *fits*. The default value is *ascii*.

* ` --fof_mode`: This option specifies the FoF redshift mode. The options permitted are *spec* (for a spectroscopic data set) or *phot* (for a photometric data set). The default value is *phot*.

* ` --link_mode`: This option specifies the FoF linking mode. The options permitted are *fixed* (for a fixed linking parameter value) or *dynamic* (for a redshift dependent linking parameter value). The default value is *dynamic*.

* ` --size_units`: This option specifies the cluster size units in the output. The options permitted are *arcmin*, *deg* or *Mpc*. The default value is *arcmin*.

* ` --min_ngal`:  This option specifies the minimum number of galaxies members required to form a cluster in a given redshift bin. The default value is *10*.

* ` --max_ngal`:  This option specifies the maximum number of galaxies members allowed to form a cluster in a given redshift bin. The default value is *10000*.

* ` --z_min`: This option specifies the low redshift limit of the sample. The default value is *0.0*.

* ` --z_max`: This option specifies the high redshift limit of the sample. The default value is *3.0*.

* ` --z_bin_size`: This option specifies the size of redshift bins. The default value is *0.01*.

* ` --z_ref`: This option specifies the reference redshift for calculations. The default value is *0.5*.

* ` --z_err_max`: This option specifies the maximum photometric redshift error allowed for each galaxy. The default value is *0.05*.

* ` --nz_data`: This option specifies the file name for a predefined N(z) distribution. If unused the N(z) distribution is calculated from the input data.

* ` --c`: This option specifies the speed of light in km/s. The default value is *2.997e5*.

* ` --H0`: This option specifies the value of the Hubble parameter in km/s/Mpc. The default value is *100.0*.

* ` --omega_m`: This option specifies the value of the matter density of the Universe. The default value is *0.3*.

* ` --omega_l`: This option specifies the value of the dark energy density of the Universe. The default value is *0.7*.

* ` --print_bin_data`: This option specifies that the redshift bin data should be printed to a file.

* ` --print_kdtree_data`: This option specifies that the kd-tree data should be printed to a file.

* ` --print_bg_data`: This option specifies that the background field data should be printed to a file.

------------

### Cat_Split Code

This code divides galaxy catalogues into overlapping pieces to
facilitate the running of SFoF.

> At present the code can only read ASCII files.

**Input Format**

The input ASCII file can contain any number of columns, but the code  expects to find the right ascension and declination of the galaxies in columns 2 and 3 respectively. Additionally, if the resulting pieces are to be used as inputs for the SFoF code then the the input should
adhere to the same format (see [above](#SFoF-Code)).

**Ouput Format**

The code output will retain the exact same format as that of the input.

**Run**

To run the code the following properties need to be specified:

1. The input file name.
2. The limits (in RA and Dec) of the input catalogue.
3. The total number of pieces required.
4. The desired amount of overlap between pieces. (Default value is 0.5 degrees)

For example, the following command will split the input file (100
deg<sup>2</sup>) into 4 pieces with an overlap of 0.5 degrees between each piece:

```bash
$ cat_split --input_file FILE_NAME --ra_lower 30.0 --ra_upper 4.0 --dec_lower 10.0 --dec_upper 20.0 --ra_bins 2 --dec_bins 2
```

**Code Options**

* ` -h [ --help ]`: This option produces the help message with all the code options and exits.

* ` -v [ --version ]`: This option prints the current version of the code and exits.

* ` -i [ --input_file ]`: This option specifies the input file name.

* ` --ra_lower`: Lower limit in right ascension of the catalogue.

* ` --ra_upper`: Upper limit in right ascension of the catalogue.

* ` --dec_lower`: Lower limit in declination of the catalogue.

* ` --dec_upper`: Upper limit in declination of the catalogue.

* ` --ra_overlap`: Overlap in right ascension between pieces. The
default is 0.5 degrees.

* ` --dec_overlap`: Overlap in declination between bins. The
default is 0.5 degrees.

* ` --n_ra_bins`: Number of bins in right ascension.

* ` --n_dec_bins`: Number of bins in declination.

* ` --n_procs`: Number of processes. Use this option instead of `n_ra_bins` and `n_dec_bins` to define the total number of bins.

------------

### Cat_Merge Code

This code merges together the SFoF outputs from various pieces of a
larger catalogue.

**Input Format**

The input file is simply a list of the SFoF code members output files.

*e.g.*

`piece_00_members_0.046_0.9_phot.dat`  
`piece_01_members_0.046_0.9_phot.dat`  
`piece_02_members_0.046_0.9_phot.dat`  
`piece_03_members_0.046_0.9_phot.dat`

**Output Format**

The output format is exactly the same as that of the SFoF code (see [above](#SFoF-Code)). If, however, the background data is not provided the signal-to-noise ratio for each cluster candidate will be set to `0.0`.

**Run**

To run simply specify the input file name and the desired output file
name as follows:

```bash
$ cat_merge --input_file FILE_NAME --ouput_file MERGED_CLUSTERS
```

In order to provide signal-to-noise ratio values for each of the
clusters the `bg_data` option must also be used as follows:

```bash
$ cat_merge --input_file FILE_NAME --ouput_file MERGED_CLUSTERS --bg_data BG_DATA_FILE
```

**Code Options**

* ` -h [ --help ]`: This option produces the help message with all the code options and exits.

* ` -v [ --version ]`: This option prints the current version of the
code and exits.

* ` -i [ --input_file ]`: This option specifies the input file name.

* ` -o [ --output_file ]`: This option specifies the output file name.

* ` --input_mode`: This option specifies the input file format. The
options permitted are *ascii* or *fits*. The default value is *ascii*.

* ` --output_mode`: This option specifies the output file format. The options permitted are *ascii* or *fits*. The default value is *ascii*.

* ` --bg_data`:  This option specifies the file name containing the background field data. (*i.e.* the output from the Main code option *print\_bg\_data*)
