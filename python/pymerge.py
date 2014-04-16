#######################
#    PYMERGE V.1.1    #
#######################
# Samuel Farrens 2014 #
#######################

"""@file pycatcut.v.1.1
@brief Code that merges cluster catalogues into a single catalogue.
@author Samuel Farrens
"""

import math, optparse, numpy as np
import errors
from classes.cluster import Cluster
from functions import merge, options
        
# Functions:

def read_file(file):
    """
    Function that reads a "galaxies" file and extracts the relevant fields. 
    """
    if opts.input_type == 'fits':
        data = fileio.read_fits(file)
    else:
        data = fileio.read_ascii(file)
    c_id = data[0,:]
    g_num = np.array(range(len(c_id)), dtype = 'int')
    g_id = data[3,:]
    g_ra = np.array(data[4,:], dtype = 'float')
    g_dec = np.array(data[5,:], dtype = 'float')
    g_z = np.array(data[6,:], dtype = 'float')
    return c_id, g_num, g_id, g_ra, g_dec, g_z

def gal_count(clusters):
    """
    Function that computes the total number of galaxies in clusters.
    """
    sum = 0
    for x in clusters:
        sum += x.ngal
    return sum

# Read Arguments:

parser = optparse.OptionParser()
options.multiple_input(parser)
options.single_output(parser)
options.merge(parser)
(opts, args) = parser.parse_args()
 
if not opts.input_files and not opts.input_file_list:
    parser.error('Input filename(s) not provided.')
if not opts.output_file:
    parser.error('Output filename not provided.')
if not opts.bg_expect:
    parser.error('Expected background density not provided.')

# Read List of Files:

if opts.input_file_list:
    errors.file_name_error(opts.input_file_list)             
    file_list = np.genfromtxt(opts.input_file_list, dtype="S", unpack = True)
elif opts.input_files:
    file_list = opts.input_files
    
# Read Files and Store Elements in Clusters:

clusters = []
cluster_count = 0

for file in file_list:
    errors.file_name_error(file)
    print 'Reading: ', file             
    c_id, g_num, g_id, g_ra, g_dec, g_z = read_file(file)
    cluster_list = np.unique(c_id)
    for clt in cluster_list:
        index = (c_id == clt)
        clusters.append(Cluster(cluster_count))
        clusters[cluster_count].extend(g_num[index], g_id[index], g_ra[index], g_dec[index], g_z[index])
        clusters[cluster_count].props(opts.bg_expect)
        cluster_count += 1

# Find matches and merge clusters:

print 'Original number of clusters:', len(clusters)
print 'Original number of cluster members:', gal_count(clusters)
print 'Finding cluster matches and merging:'
        
merge.merge_clusters(clusters, opts.progress, opts.bg_expect, 0.5, 0.2)
        
print 'Final number of merged clusters:', len(clusters)
print 'Final number of merged cluster members:', gal_count(clusters)

# Output merged clusters:

ngals = []
for i in range(len(clusters)):
    ngals.append(clusters[i].ngal)
ngals = np.array(ngals)
index = ngals.argsort()[::-1]

if opts.output_type == 'ascii':
    clt_file = opts.output_file + '_clusters.dat'
    gal_file = opts.output_file + '_galaxies.dat'
    clt_out = open(clt_file,'w')
    gal_out = open(gal_file,'w')
    print>> clt_out, '#C_ID        C_RA    C_DEC   C_Z   C_NGAL C_SN   C_AREA C_SIZE'
    print>> gal_out, '#C_ID        C_NGAL G_ID         G_RA    G_DEC  G_Z'
    for i in index:
        print>> clt_out, '%012d' % clusters[i].id,'%07.3f' % clusters[i].ra,
        print>> clt_out, '%+07.3f' % clusters[i].dec, '%05.3f' % clusters[i].z,
        print>> clt_out, '%06d' % clusters[i].ngal, '%06.3f' % clusters[i].sn,
        print>> clt_out, '%06.3f' % clusters[i].area, '%06.3f' % clusters[i].size
        for j in range(clusters[i].ngal):
            print>> gal_out, '%012d' % clusters[i].id,'%06d' % clusters[i].ngal,
            print>> gal_out, '%12s' % clusters[i].g_id[j],'%07.3f' % clusters[i].g_ra[j],
            print>> gal_out, '%+07.3f' % clusters[i].g_dec[j], '%05.3f' % clusters[i].g_z[j]
else:
    clt_file = opts.output_file + '_clusters.fits'
    gal_file = opts.output_file + '_galaxies.fits'
    c_id = []
    c_ra = []
    c_dec = []
    c_z = []
    c_ngal = []
    c_sn = []
    c_area = []
    c_size = []
    c_id2 = []
    c_ngal2 = []
    g_id = []
    g_ra = []
    g_dec = []
    g_z = []
    for i in index:
        c_id.append(clusters[i].id)
        c_ra.append(clusters[i].ra)
        c_dec.append(clusters[i].dec)
        c_z.append(clusters[i].z)
        c_ngal.append(clusters[i].ngal)
        c_sn.append(clusters[i].sn)
        c_area.append(clusters[i].area)
        c_size.append(clusters[i].size)
        for j in range(clusters[i].ngal):
            c_id2.append(clusters[i].id)
            c_ngal2.append(clusters[i].ngal)
            g_id.append(clusters[i].g_id[j])
            g_ra.append(clusters[i].g_ra[j])
            g_dec.append(clusters[i].g_dec[j])
            g_z.append(clusters[i].g_z[j])
    c_id = np.array(c_id)
    c_ra = np.array(c_ra, dtype = 'float')
    c_dec = np.array(c_dec, dtype = 'float')
    c_z = np.array(c_z, dtype = 'float')
    c_ngal = np.array(c_ngal, dtype = 'float')
    c_sn = np.array(c_sn, dtype = 'float')
    c_area = np.array(c_area, dtype = 'float')
    c_size =np.array(c_size, dtype = 'float')
    c_id2 = np.array(c_id2)
    c_ngal2 = np.array(c_ngal2, dtype = 'float')
    g_id = np.array(g_id)
    g_ra = np.array(g_ra, dtype = 'float')
    g_dec = np.array(g_dec, dtype = 'float')
    g_z = np.array(g_z, dtype = 'float')
    from astropy.io import fits
    tbhdu1 = fits.new_table(fits.ColDefs([fits.Column(name='c_id', format='8A', array = c_id),
                                          fits.Column(name='c_ra', format='D', array = c_ra),
                                          fits.Column(name='c_dec', format='D', array = c_dec),
                                          fits.Column(name='c_z', format='D', array = c_z),
                                          fits.Column(name='c_ngal', format='D', array = c_ngal),
                                          fits.Column(name='c_sn', format='D', array = c_sn),
                                          fits.Column(name='c_area', format='D', array = c_area),
                                          fits.Column(name='c_size', format='D', array = c_size)]))
    tbhdu2 = fits.new_table(fits.ColDefs([fits.Column(name='c_id', format='8A', array = c_id2),
                                          fits.Column(name='c_ngal', format='D', array = c_ngal2),
                                          fits.Column(name='g_id', format='8A', array = g_id),
                                          fits.Column(name='g_ra', format='D', array = g_ra),
                                          fits.Column(name='g_dec', format='D', array = g_dec),
                                          fits.Column(name='g_z', format='D', array = g_z)]))
    n = np.arange(100.0)
    hdu = fits.PrimaryHDU(n)
    thdulist1 = fits.HDUList([hdu, tbhdu1])
    thdulist2 = fits.HDUList([hdu, tbhdu2])
    thdulist1.writeto(clt_file)
    thdulist2.writeto(gal_file)
