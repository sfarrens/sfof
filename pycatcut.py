#######################
#   PYCATCUT V.2.0    #
#######################
# Samuel Farrens 2014 #
#######################

import math, optparse, numpy as np, pycatcut_help as pch
import astro, errors, interface

# Read Arguments and Set Defaults:

parser = optparse.OptionParser()
parser.add_option("-f", "--list", dest = "file_name", help = "Name of input file.")
parser.add_option("-o", "--output", dest = "output", help = "Name for output files.")
parser.add_option("--ra_col", dest = "ra_col", type = "int", default = 2, help = "RA column number. [default: %default]")
parser.add_option("--dec_col", dest = "dec_col", type = "int", default = 3, help = "Dec column number. [default: %default]")
parser.add_option("--ra_lower", dest = "ra_lower", type = "float", help = "Lower limit on RA.")
parser.add_option("--ra_upper", dest = "ra_upper", type = "float", help = "Upper limit on RA.")
parser.add_option("--dec_lower", dest = "dec_lower", type = "float", help = "Lower limit on Dec.")
parser.add_option("--dec_upper", dest = "dec_upper", type = "float", help = "Upper limit on Dec.")
parser.add_option("-r", "--ra_bin", dest = "ra_bin", type = "int", help = "Number of RA bins.")
parser.add_option("-d", "--dec_bin", dest = "dec_bin", type = "int", help = "Number of Dec bins.")
parser.add_option("--ra_overlap", dest = "ra_overlap", type = "float", default = 1.0, help = "Overlap between RA bins. [default: %default]")
parser.add_option("--dec_overlap", dest = "dec_overlap", type = "float", default = 1.0, help = "Overlap between Dec bins. [default: %default]")

(opts, args) = parser.parse_args()

if not opts.file_name:
    parser.error('Input filename not provided.')
if (not opts.ra_bin) or (not opts.dec_bin):
    parser.error('Number of RA or Dec bins not provided.')
if (opts.ra_bin == 1) and (opts.dec_bin == 1):
    parser.error('Number of RA or Dec bins must be greater than one.')
    
#Check for errors

errors.file_name_error(opts.file_name)                                                       
            
#Read catalogue
    
print 'Reading data from ' + opts.file_name
catalogue = np.genfromtxt(opts.file_name, dtype="S", unpack = True)

ra = np.array(catalogue[opts.ra_col - 1, :], dtype="float")
dec = np.array(catalogue[opts.dec_col - 1, :], dtype="float")

#Set bin sizes

if opts.ra_lower == None: opts.ra_lower = min(ra)
if opts.ra_upper == None: opts.ra_upper = max(ra)
if opts.dec_lower == None: opts.dec_lower = min(dec)
if opts.dec_upper == None: opts.dec_upper = max(dec)
        
ra_bin_size = ((opts.ra_upper - opts.ra_lower) / opts.ra_bin)
dec_bin_size = ((opts.dec_upper - opts.dec_lower) / opts.dec_bin)
    
#Cut-up catalogue and print pieces
    
piece_num = 0

for i in range(opts.ra_bin):
    ra_bin_limit_lower = (ra_bin_size * i) + opts.ra_lower - opts.ra_overlap
    ra_bin_limit_upper = (ra_bin_size * (i + 1)) + opts.ra_lower + opts.ra_overlap
    ra_index_1 = ((ra >= ra_bin_limit_lower) | ((ra + 360) < ra_bin_limit_upper))
    ra_index_2 = ((ra < ra_bin_limit_upper) | ((ra - 360) >= ra_bin_limit_lower))
    for j in range(opts.dec_bin):
        dec_bin_limit_lower = (dec_bin_size * j) + opts.dec_lower - opts.dec_overlap
        dec_bin_limit_upper = (dec_bin_size * (j + 1)) + opts.dec_lower + opts.dec_overlap
        dec_index_1 = (dec >= dec_bin_limit_lower)
        dec_index_2 = (dec < dec_bin_limit_upper)
        index = (ra_index_1 & ra_index_2 & dec_index_1 & dec_index_2)
        if opts.output == None:
            out_file_name = opts.file_name + '_piece_' + ('%02d' % piece_num) + '.dat'
            out_file = open(out_file_name, 'w')
        else:
            out_file_name = opts.output + '_piece_' + ('%02d' % piece_num) + '.dat'
            out_file = open(out_file_name, 'a')
        print 'Printing data to ' + out_file_name + ' (' + str(np.sum(index)) + ')'
        for k in np.transpose(catalogue[:, index]):
            print>> out_file, ' '.join(k)
        piece_num += 1
