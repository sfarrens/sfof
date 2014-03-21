#################
# PYMERGE V.1.1 #
#################

"""@file pycatcut.v.1.1
@brief Code that merges cluster catalogues into a single catalogue.
@author Samuel Farrens
"""

import math, optparse, numpy as np
import astro, errors, interface

# Classes:

class Cluster:
    """
    Class for storing cluster members and deriving properties from those members.
    """
    def __init__(self, c_id):
        self.c_id = c_id
        self.g_id = []
        self.g_ra = []
        self.g_dec = []
        self.g_z = []
        self.match_flags = []
    def clean(self, c_id):
        self.c_id = c_id
        self.match_flags = []
    def extend(self, g_id, g_ra, g_dec, g_z):
        self.g_id.extend(g_id)
        self.g_ra.extend(g_ra)
        self.g_dec.extend(g_dec)
        self.g_z.extend(g_z)
    def flag(self, c_id):
        self.match_flags.extend(c_id)
    def props(self, bg_expect):
        self.c_ra = np.median(self.g_ra)
        self.c_dec = np.median(self.g_dec)
        self.c_z = np.median(self.g_z)
        self.ngal = len(self.g_id)
        distances = []        
        for i in range(self.ngal):
            distances.extend([astro.projected_distance(self.g_ra[i], self.c_ra,
                                                       self.g_dec[i], self.c_dec)])
        self.size = np.mean(distances)
        self.area = self.size ** 2 * math.pi
        self.sn = (self.ngal) / ((self.area * bg_expect) ** 0.5)
    def unique(self):
        unique_ids, index = np.unique(self.g_id, return_index = True)
        self.g_id = list(unique_ids)
        self.g_ra = list(np.array(self.g_ra)[index])
        self.g_dec = list(np.array(self.g_dec)[index])
        self.g_z = list(np.array(self.g_z)[index])
        
# Functions:

def read_file(file):
    """
    Function that reads a "galaxies" file and extracts the relevant fields. 
    """
    data = np.genfromtxt(file, dtype="S", unpack = True)
    c_id = data[0,:]
    g_id = data[3,:]
    g_ra = np.array(data[4,:], dtype = 'f')
    g_dec = np.array(data[5,:], dtype = 'f')
    g_z = np.array(data[6,:], dtype = 'f')
    return c_id, g_id, g_ra, g_dec, g_z

def gal_count(clusters):
    """
    Function that computes the total number of galaxies in clusters.
    """
    sum = 0
    for x in clusters:
        sum += x.ngal
    return sum

def find_matches(clusters):
    """
    Function that finds clusters with galaxies in common.
    """
    ra_dec_lim = 0.5
    z_lim = 0.2
    matches = []
    ras = []
    decs = []
    zs = []
    for i in range(len(clusters)):
        ras.append(clusters[i].c_ra)
        decs.append(clusters[i].c_dec)
        zs.append(clusters[i].c_z)
    for i in range(len(clusters)):
        interface.progress_bar(i, len(clusters))
        index = np.where((np.fabs(clusters[i].c_ra - ras) <= ra_dec_lim) & (np.fabs(clusters[i].c_dec - decs) <= ra_dec_lim) &
                        (np.fabs(clusters[i].c_z - zs) <= z_lim))[0]
        for j in index:
            if((j not in clusters[i].match_flags) & (np.any(np.in1d(clusters[i].g_id, clusters[j].g_id))) & (i != j)):
                matches.append([i, j])
                clusters[j].flag([clusters[i].c_id])
    matches = np.array(matches)
    print ""
    return matches

def merge(cluster1, cluster2):
    """
    Fuction that merges two clusters.
    """
    cluster1.extend(cluster2.g_id, cluster2.g_ra, cluster2.g_dec, cluster2.g_z)

def merge_and_clean(clusters, matches):
    """
    Function that merges all matched clusters and deletes the redundant structures.
    """
    if len(matches > 0):
        x = matches[:, 0]
        y = matches[:, 1]
        z = np.unique(y)
        for i in range(len(matches)):
            merge(clusters[x[i]], clusters[y[i]])
        for i in range(len(z) - 1, -1, -1):
            del clusters[z[i]]
    for i in range(len(clusters)):
        clusters[i].unique()
        clusters[i].props(opts.bg_expect)
        clusters[i].clean(i)
    
# Read Arguments:

parser = optparse.OptionParser()
parser.add_option("-l", "--list", dest = "file_list", help = "List of file names.")
parser.add_option("-o", "--output", dest = "out_file_name", help = "Name for output files.")
parser.add_option("-b", "--bg_expect", dest = "bg_expect", type = "float",
                   help = "Expected number of background galaxies per arcminute.")
(opts, args) = parser.parse_args()

if not opts.file_list:
    parser.error('Input filename not provided.')
if not opts.out_file_name:
    parser.error('Output filename not provided.')
if not opts.bg_expect:
    parser.error('Expected background density not provided.')

errors.file_name_error(opts.file_list)             

# Read List of Files:
 
file_list = np.genfromtxt(opts.file_list, dtype="S", unpack = True)

# Read Files and Store Elements in Clusters:

clusters = []
cluster_count = 0

for file in file_list:
    errors.file_name_error(file)
    print 'Reading: ', file             
    c_id, g_id, g_ra, g_dec, g_z = read_file(file)
    cluster_list = np.unique(c_id)
    for clt in cluster_list:
        index = (c_id == clt)
        clusters.append(Cluster(cluster_count))
        clusters[cluster_count].extend(g_id[index], g_ra[index], g_dec[index], g_z[index])
        clusters[cluster_count].props(opts.bg_expect)
        cluster_count += 1

# Find matches and merge clusters:

print 'Original number of clusters:', len(clusters)
print 'Original number of cluster members:', gal_count(clusters)
print 'Finding cluster matches and merging:'
    
matches = [None]
sweep = 1
    
while len(matches) > 0:
    print ' >> Sweep:', sweep
    matches = find_matches(clusters)
    merge_and_clean(clusters, matches)
    sweep += 1

print 'Final number of merged clusters:', len(clusters)
print 'Final number of merged cluster members:', gal_count(clusters)

# Output merged clusters:

ngals = []
for i in range(len(clusters)):
    ngals.append(clusters[i].ngal)
ngals = np.array(ngals)
index = ngals.argsort()[::-1]
    
clt_file = opts.out_file_name + '_clusters.dat'
gal_file = opts.out_file_name + '_galaxies.dat'

clt_out = open(clt_file,'w')
gal_out = open(gal_file,'w')

print>> clt_out, '#C_ID        C_RA    C_DEC   C_Z   C_NGAL C_SN   C_AREA C_SIZE'
print>> gal_out, '#C_ID        C_NGAL G_ID         G_RA    G_DEC  G_Z'

for i in index:
    print>> clt_out, '%012d' % clusters[i].c_id,'%07.3f' % clusters[i].c_ra,
    print>> clt_out, '%+07.3f' % clusters[i].c_dec, '%05.3f' % clusters[i].c_z,
    print>> clt_out, '%06d' % clusters[i].ngal, '%06.3f' % clusters[i].sn,
    print>> clt_out, '%06.3f' % clusters[i].area, '%06.3f' % clusters[i].size
    for j in range(clusters[i].ngal):
        print>> gal_out, '%012d' % clusters[i].c_id,'%06d' % clusters[i].ngal,
        print>> gal_out, '%12s' % clusters[i].g_id[j],'%07.3f' % clusters[i].g_ra[j],
        print>> gal_out, '%+07.3f' % clusters[i].g_dec[j], '%05.3f' % clusters[i].g_z[j]
