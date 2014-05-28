######################
# OPTPARSE FUNCTIONS #
######################

import optparse

def single_input(parser):
    """
    Function that defines options and help for a single input file.
    """
    parser.add_option("-i", "--input", dest = "input_file", help = "Input file name.")
    parser.add_option("--input_type", dest = "input_type", default = "ascii", help = "Data type [default: %default].")


def multiple_input(parser):
    """
    Function that defines options and help for multiple input files.
    """
    parser.add_option("-f", "--file", action = "append", dest = "input_files", help = "Append input file name.")
    parser.add_option("-l", "--list", dest = "input_file_list", help = "List of input file names.")
    parser.add_option("--input_type", dest = "input_type", default = "ascii", help = "Data type [default: %default].")

def single_output(parser):
    """
    Function that defines options and help for a single output file.
    """
    parser.add_option("-o", "--output", dest = "output_file", help = "Output file name.")
    parser.add_option("--output_type", dest = "output_type", default = "ascii", help = "Data type [default: %default].")

def cosmo(parser):
    """
    Function that defines options and help for cosmological parameters.
    """
    parser.add_option("--omega_m", dest = "Omega_M", type = "float", default = 0.3, help = "Matter density. [Default: %default]")
    parser.add_option("--omega_l", dest = "Omega_L", type = "float", default = 0.7, help = "Dark energy Density. [Default: %default]")
    parser.add_option("--H0", dest = "H0", type = "float", default = 100, help = "Hubble constant. [Default: %default]")
    parser.add_option("--c", dest = "c", type = "float", default = 2.997e5, help = "Speed of light. [Default: %default]")
    
def fof(parser):
    """
    Function that defines options and help specific to pyfof.py.
    """
    parser.add_option("-r", "--link_r", dest = "link_r", type = "float", help = "Transverse linking length.")
    parser.add_option("-z", "--link_z", dest = "link_z", type = "float", help = "Line-of-sight linking length.")
    parser.add_option("--mode", dest = "mode", default = "spec", help = "FoF Mode. [Default: %default]")
    parser.add_option("--data_type", dest = "data_type", default = "ascii", help = "Input data type. [Default: %default]")
    parser.add_option("--min_mem", dest = "min_mem", type = "int", default = 3,
                    help = "Minimum number of cluster members required. [Default: %default]")
    parser.add_option("--z_min", dest = "z_min", type = "float", help = "Minimum redshift. [Default: %default]")
    parser.add_option("--z_max", dest = "z_max", type = "float", help = "Maximum redshift. [Default: %default]")
    parser.add_option("--z_bin_size", dest = "z_bin_size", type = "float", default = 0.01, help = "Redshift bin size. [Default: %default]")
    parser.add_option("--z_ref", dest = "z_ref", type = "float", default = 0.5, help = "Reference redshift bin. [Default: %default]")
    parser.add_option("--tree_dist", dest = "tree_dist", type = "float", default = 0.5,
                      help = "Maximum kd-tree distance in RA/DEC. [Default: %default]")
    parser.add_option("--id_col", dest = "id_col", type = "int", default = 1, help = "ID column number. [Default: %default]")
    parser.add_option("--ra_col", dest = "ra_col", type = "int", default = 2, help = "RA column number. [Default: %default]")
    parser.add_option("--dec_col", dest = "dec_col", type = "int", default = 3, help = "Dec column number. [Default: %default]")
    parser.add_option("--z_col", dest = "z_col", type = "int", default = 4, help = "Z column number. [Default: %default]")
    parser.add_option("--dz_col", dest = "dz_col", type = "int", default = 5, help = "dZ column number. [Default: %default]")

def merge(parser):
    """
    Function that defines options and help specific to pyfof.py and pymerge.py.
    """
    parser.add_option("-b", "--bg_expect", dest = "bg_expect", type = "float",
                    help = "Expected number of background galaxies per arcminute.")
    parser.add_option("-p", "--progress", action = "store_true", dest = "progress",
                    help = "Display progress bar in terminal.")

def catcut(parser):
    """
    Function that defines options and help secific to pycatcut.py.
    """
    parser.add_option("--mode", dest = "mode", default = "spec", help = "FoF Mode. [Default: %default]")
    parser.add_option("--id_col", dest = "id_col", type = "int", default = 1, help = "ID column number. [Default: %default]")
    parser.add_option("--ra_col", dest = "ra_col", type = "int", default = 2, help = "RA column number. [Default: %default]")
    parser.add_option("--dec_col", dest = "dec_col", type = "int", default = 3, help = "Dec column number. [Default: %default]")
    parser.add_option("--z_col", dest = "z_col", type = "int", default = 4, help = "Z column number. [Default: %default]")
    parser.add_option("--dz_col", dest = "dz_col", type = "int", default = 5, help = "dZ column number. [Default: %default]")
    parser.add_option("--ra_lower", dest = "ra_lower", type = "float", help = "Lower limit on RA.")
    parser.add_option("--ra_upper", dest = "ra_upper", type = "float", help = "Upper limit on RA.")
    parser.add_option("--dec_lower", dest = "dec_lower", type = "float", help = "Lower limit on Dec.")
    parser.add_option("--dec_upper", dest = "dec_upper", type = "float", help = "Upper limit on Dec.")
    parser.add_option("-r", "--ra_bin", dest = "ra_bin", type = "int", help = "Number of RA bins.")
    parser.add_option("-d", "--dec_bin", dest = "dec_bin", type = "int", help = "Number of Dec bins.")
    parser.add_option("--ra_overlap", dest = "ra_overlap", type = "float", default = 1.0,
                    help = "Overlap between RA bins. [default: %default]")
    parser.add_option("--dec_overlap", dest = "dec_overlap", type = "float", default = 1.0,
                  help = "Overlap between Dec bins. [default: %default]")
