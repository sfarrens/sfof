#######################
#   PYCATCUT V.2.0    #
#######################
# Samuel Farrens 2014 #
#######################

"""@file pycatcut.v.2.0
@brief Code that divides a galaxy catalogue into overlapping pieces.
@author Samuel Farrens
"""

import math, optparse, numpy as np
from functions import astro, errors, fileio, interface, options

# Read Arguments and Set Defaults:

parser = optparse.OptionParser()
options.single_input(parser)
options.single_output(parser)
options.catcut(parser)
(opts, args) = parser.parse_args()

if not opts.input_file:
    parser.error('Input filename not provided.')
if (not opts.ra_bin) or (not opts.dec_bin):
    parser.error('Number of RA or Dec bins not provided.')
if (opts.ra_bin == 1) and (opts.dec_bin == 1):
    parser.error('Number of RA or Dec bins must be greater than one.')
    
#Check for errors

errors.file_name_error(opts.input_file)                                                       
            
#Read catalogue
    
print 'Reading data from ' + opts.input_file
if opts.input_type == 'fits':
    catalogue = fileio.read_fits(opts.input_file)
else:
    catalogue = fileio.read_ascii(opts.input_file)

id = np.array(catalogue[opts.id_col - 1, :])
ra = np.array(catalogue[opts.ra_col - 1, :], dtype="float")
dec = np.array(catalogue[opts.dec_col - 1, :], dtype="float")
z = np.array(catalogue[opts.z_col - 1, :], dtype="float")
if opts.mode == 'phot':
    dz = np.array(catalogue[opts.dz_col - 1, :], dtype="float")

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
        if opts.output_file == None:
            opts.output_file = opts.input_file
        if opts.output_type == 'ascii':
            out_file_name = opts.output_file + '_piece_' + ('%02d' % piece_num) + '.dat'
            out_file = open(out_file_name, 'w')
        else:
            out_file_name = opts.output_file + '_piece_' + ('%02d' % piece_num) + '.fits'
        print 'Printing data to ' + out_file_name + ' (' + str(np.sum(index)) + ')'
        if opts.output_type == 'ascii':
            for k in np.transpose(catalogue[:, index]):
                print>> out_file, ' '.join(k)
        else:
            from astropy.io import fits
            tbhdu = fits.new_table(fits.ColDefs([fits.Column(name='id', format='8A', array = id[index]),
                                                 fits.Column(name='ra', format='D', array = ra[index]),
                                                 fits.Column(name='dec', format='D', array = dec[index]),
                                                 fits.Column(name='z', format='D', array = z[index]),
                                                 fits.Column(name='dz', format='D', array = dz[index])]))
            n = np.arange(100.0)
            hdu = fits.PrimaryHDU(n)
            thdulist = fits.HDUList([hdu, tbhdu])
            thdulist.writeto(out_file_name)
        piece_num += 1
