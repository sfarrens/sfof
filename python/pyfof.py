#######################
#     PYFOF V.1.0     #
#######################
# Samuel Farrens 2014 #
#######################

import math, optparse
from functions import astro, comp, cosmo, errors, fileio, kdtree, merge, options
import numpy as np, scipy
from scipy import spatial
from classes.cluster import Cluster

# Classes:

class Galaxy:
    """
    Class for storing galaxy properties.
    """
    def __init__(self, data, number):
        """
        Function that initialises a Galaxy instance.
        """
        self.num = number
        self.id = data[opts.id_col - 1]
        self.ra = float(data[opts.ra_col - 1])
        self.dec = float(data[opts.dec_col - 1])
        self.z = float(data[opts.z_col - 1])
        self.dz = float(data[opts.dz_col - 1])
        self.v = self.z / (1 + self.z)
        self.da = ((opts.c / opts.H0) * cosmo.angdidis(self.z, opts.Omega_M, opts.Omega_L))
        self.x, self.y = astro.radec2xy(self.ra, self.dec, self.da)
    def assign_bin(self, bins):
        """
        Function that assigns a Galaxy instance to the
        corresponding Z_bin instances.
        """
        self.bin = comp.find_bin(self.z, opts.z_min, opts.z_bin_size)        
        bins[self.bin].count += 1
    def assign_clt(self, nbins):
        self.clt = [None] * nbins        

class Z_bin:
    """
    Class for...
    """
    def __init__(self, id, z):
        """
        Function that initialises a Z_bin instance.
        """
        self.id = id
        self.z = z
        self.count = 0
        self.r_ref = 0
        self.dcmv = cosmo.dcomvoldz(z, opts.Omega_M, opts.Omega_L)
        self.link_z = opts.link_z / (1 + self.z)
        self.da = ((opts.c / opts.H0) * cosmo.angdidis(self.z, opts.Omega_M, opts.Omega_L))
    def linking_param(self, r_ref):
        """
        Function that calculates the linking length for each
        redshift bin.
        """
        self.dndz = self.count / opts.z_bin_size
        self.dndv = self.dndz / self.dcmv
        if self.dndv > 0:     
            self.link_r = self.dndv ** -0.5 * r_ref
        else:
            self.link_r = 0
        self.rfriend = self.link_r / self.da
            
# Functions:

def set_up_z_bins(z_min, z_max, z_bin_size):
    """
    Function that sets up the redshift bins.
    """
    n_z_bins = int(((z_max - z_min) / z_bin_size) + 1)
    z_bins = []
    for i in range(n_z_bins):
        z_bins.append(Z_bin(i, z_min + i * z_bin_size))    
    return np.array(z_bins)

def assign_linking_parameters(z_bins):
    """
    Function that finds which redshift bin each galaxy
    corresponds to.
    """
    z_ref_index = np.floor(((opts.z_ref - opts.z_min) / opts.z_bin_size) + 0.5).astype('int')
    r_ref = (z_bins[z_ref_index].count / (opts.z_bin_size * z_bins[z_ref_index].dcmv)) ** 0.5 * opts.link_r
    for i in range(z_bins.size):
        z_bins[i].linking_param(r_ref)

def friendship(zbin, gal1, gal2, mode):
    """
    Function that checks if two galaxies are friends in
    a given redshift bin.
    """
    if mode == 'spec':
        rfriend = zbin.link_r / gal1.da
    else:
        rfriend = zbin.rfriend
    dist =  astro.deg2rad(astro.projected_distance(gal1.ra, gal2.ra, gal1.dec, gal2.dec) / 60.0)
    check1 = (dist < rfriend)    
    if mode == 'spec':
        check2 = (math.fabs(gal1.v - gal2.v) <= zbin.link_z)
        check = (check1 & check2)
    else:
        check = check1
    return check

def bin_check(mode, gal, zbin):
    """
    Function that checks if a bla ....
    """
    if mode == 'spec':
        check = True
    else:
        check = (np.abs(gal.z - zbin.z) <= opts.link_z * gal.dz)
    return check

def friends_of_friends(zbin, gals, tree_dist, mode, cluster_count):
    """
    Function that looks for galaxy friends in a given
    redshift bin and returns a list of the resulting
    Cluster instances.
    """
    #make kd-tree
    tree = kdtree.make_kdtree(gals)
    #loop over galaxies
    cluster_list = []
    for i in range(len(gals)):
        if  mode == 'spec':
            link_zbin = z_bins[gals[i].bin]
        else:
            link_zbin = z_bins[zbin]
        if bin_check(mode, gal[i], link_zbin):
            #friends loop
            if gals[i].clt[zbin] == None:
                list = tree.query_ball_point([gals[i].x, gals[i].y], tree_dist)            
                for j in list:
                    if ((bin_check(mode, gal[j], link_zbin)) & (gals[i].id != gals[j].id) & (gals[j].clt[zbin] == None)):
                        if friendship(link_zbin, gals[i], gals[j], opts.mode):                              
                            if gals[i].clt[zbin] == None:
                                gals[i].clt[zbin] = len(cluster_list)
                                gals[j].clt[zbin] = gals[i].clt[zbin]
                                cluster_list.append(Cluster(cluster_count))
                                cluster_count += len(cluster_list)
                                cluster_list[gals[i].clt[zbin]].extend([gals[i].num], [gals[i].id], [gals[i].ra],
                                                                        [gals[i].dec], [gals[i].z], [gals[i].x], [gals[i].y])
                                cluster_list[gals[i].clt[zbin]].extend([gals[j].num], [gals[j].id], [gals[j].ra],
                                                                        [gals[j].dec], [gals[j].z], [gals[j].x], [gals[j].y])
                            else:
                                gals[j].clt[zbin] = gals[i].clt[zbin]
                                cluster_list[gals[i].clt[zbin]].extend([gals[j].num], [gals[j].id], [gals[j].ra],
                                                                        [gals[j].dec], [gals[j].z], [gals[j].x], [gals[j].y])
            #friends-of-friends loop
            if gals[i].clt[zbin] != None:
                clt_now = cluster_list[gals[i].clt[zbin]]
                for k in range(len(clt_now.g_id)):
                    if(gals[i].id != clt_now.g_id[k]):
                        list = tree.query_ball_point([clt_now.g_x[k], clt_now.g_y[k]], tree_dist)
                        for l in list:
                            if ((bin_check(mode, gal[l], link_zbin)) & (clt_now.g_id[k] != gals[l].id)
                                & (gals[l].clt[zbin] == None)):
                                if friendship(link_zbin, gals[clt_now.g_num[k]], gals[l], opts.mode):
                                    gals[l].clt[zbin] = gals[i].clt[zbin]
                                    cluster_list[gals[i].clt[zbin]].extend([gals[l].num], [gals[l].id], [gals[l].ra],
                                                                        [gals[l].dec], [gals[l].z], [gals[l].x], [gals[l].y])
    return cluster_list

def assign_cluster_props(cluster_list):
    """
    Funcion that assigns Cluster properties and
    deletes those with less than the minimum number
    of members.
    """
    for i in range(len(cluster_list) - 1, -1, -1):
        cluster_list[i].unique()
        cluster_list[i].props(None)
        if cluster_list[i].ngal < opts.min_mem:
            del cluster_list[i]
    return cluster_list

##################
# READ ARGUMENTS #
##################

parser = optparse.OptionParser()
options.single_input(parser)
options.single_output(parser)
options.cosmo(parser)
options.fof(parser)
options.merge(parser)
(opts, args) = parser.parse_args()
  
if not opts.input_file:
    parser.error('Input file name not provided.')
if not opts.output_file:
    opts.output_file = opts.input_file
if not opts.link_r:
    parser.error('Transverse linking length not provided.')
if not opts.link_z:
    parser.error('Line-of-sight linking length not provided.')
    
#############
# READ DATA #
#############

#make sure files exit
errors.file_name_error(opts.input_file)

#read input file
print 'Reading file:', opts.input_file
if opts.input_type == 'fits':
    data = fileio.read_fits(opts.input_file)
else:
    data = fileio.read_ascii(opts.input_file)
    
################
# SET DEFAULTS #
################

all_gal_z = np.array(data[opts.z_col - 1]).astype('float')

#set redshift limits
if not opts.z_min or not opts.z_max:
    if not opts.z_min: opts.z_min = np.min(all_gal_z)
    if not opts.z_max: opts.z_max = np.max(all_gal_z)

#restrict data to redshift limits
data = data[:, ((all_gal_z >= opts.z_min) & (all_gal_z < opts.z_max))]

del all_gal_z

#set up redshift bins
z_bins = set_up_z_bins(opts.z_min, opts.z_max, opts.z_bin_size)

############################
# DEFINE GALAXY PROPERTIES #
############################

#assign input data to Galaxy class
print 'Assign galaxy properties...'
gal = []
for i in range(len(data[0])):
    gal.append(Galaxy(data[:,i], i))
    gal[i].assign_bin(z_bins)
    if opts.mode == 'phot':
        gal[i].assign_clt(z_bins.size)
    else:
        gal[i].assign_clt(1)

############################
# SET LININKING PARAMETERS #
############################

#set up bin properties and assign galaxies to bins
print 'Assign linking parameters...'
assign_linking_parameters(z_bins)

######################
# SEARCH FOR FRIENDS #
######################

if opts.mode == 'phot':
    loop_over_zbins = len(z_bins)
else:
    loop_over_zbins = 1

#loop through redshift bins and perform friends-of-friends
print 'Find clusters...'
clusters = []
for i in range(loop_over_zbins):
    clusters.extend(friends_of_friends(i, gal, opts.tree_dist, opts.mode, len(clusters)))
    print '>>', z_bins[i].z, len(clusters)
    
#assign properties to detected clusters
assign_cluster_props(clusters)

print 'Found', len(clusters), 'clusters.'

##################
# MERGE CLUSTERS #
##################

#merge clusters with galaxies in common
print 'Merge clusters...'
merge.merge_clusters(clusters, opts.progress, opts.bg_expect, opts.tree_dist)

print 'Merged into', len(clusters), 'clusters.'

###################
# OUTPUT CLUSTERS #
###################

ngal_list = []
for x in clusters:
    ngal_list.append(x.ngal)
index = np.array(ngal_list).argsort()[::-1]

clusters = np.array(clusters)[index]

#output = open(opts.output_file, 'w')

#for x in clusters:
#    for y in range(x.ngal):
#        print>> output, x.id, x.ngal, x.g_id[y], x.g_ra[y], x.g_dec[y], x.g_z[y]

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
