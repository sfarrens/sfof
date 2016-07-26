# Examples

> Author: **Samuel Farrens**

> Year: **2016**

## Set Up

In order to run the following examples the codes need to be compiled
following the instructions provided in [docs](../docs/readme.md).

## Spec Test

The directory *spec\_test* provides a simple example of how to run the
code in spectroscopic mode. The file *test\_spec.dat* shows the expected
input for spectroscopic data, which has the following format:

`Galaxy_ID Galaxy_RA Galaxy_Dec Galaxy_z`

A configuraiton file (*param_file.ini*) is already provided. Simply run the following:

> \>> main

The resulting output files can then be compared with the expected
outputs provided in *expected_output*.

## Phot Test

The directory *phot\_test* provides a simple example of how to run the
code in photometric mode. The file *test\_phot.dat* shows the expected
input for photometric data, which has the following format:

`Galaxy_ID Galaxy_RA Galaxy_Dec Galaxy_zphot Galaxy_zphot_err`

A configuraiton file (*param_file.ini*) is already provided. Simply run the following:

> \>> main

The resulting output files can then be compared with the expected
outputs provided in *expected_output*.
