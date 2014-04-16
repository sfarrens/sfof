###################
# CLUSTER CLASSES #
###################

import math, functions.astro, numpy as np

class Cluster:
    """
    Class for storing cluster members and deriving properties from those members.
    """
    def __init__(self, c_id):
        """
        Function that initialises a Cluster instance.
        """
        self.id = c_id
        self.g_num = []
        self.g_id = []
        self.g_ra = []
        self.g_dec = []
        self.g_z = []
        self.g_x = []
        self.g_y = []
        self.match_flags = []
        self.match_flag = False
        self.match_list = []
    def clean(self, c_id):
        """
        Function that resets the cluster ID and empties the match flags.
        """
        self.id = c_id
        self.match_flags = []
        self.match_flag = False
        self.match_list = []
    def extend(self, g_num, g_id, g_ra, g_dec, g_z, g_x, g_y):
        """
        Function that adds galaxy properties to Cluster.
        """
        self.g_num.extend(g_num)
        self.g_id.extend(g_id)
        self.g_ra.extend(g_ra)
        self.g_dec.extend(g_dec)
        self.g_z.extend(g_z)
        self.g_x.extend(g_x)
        self.g_y.extend(g_y)
    def flag(self, c_id):
        """
        Function that adds Cluster ID to list of match flags.
        """
        self.match_flags.extend(c_id)
    def props(self, bg_expect):
        """
        Function that sets Cluster properties.
        """                
        self.ra = np.median(self.g_ra)
        self.dec = np.median(self.g_dec)
        self.z = np.median(self.g_z)
        self.x = np.median(self.g_x)
        self.y = np.median(self.g_y)
        self.ngal = len(self.g_id)
        distances = []        
        for i in range(self.ngal):
            distances.extend([functions.astro.projected_distance(self.g_ra[i], self.ra,
                                                                 self.g_dec[i], self.dec)])
        self.size = np.mean(distances)
        self.area = self.size ** 2 * math.pi
        if bg_expect != None:
            self.sn = (self.ngal) / ((self.area * bg_expect) ** 0.5)
        else:
            self.sn = None
    def unique(self):
        """
        Function that removes duplicate galaxies from Cluster.
        """
        unique_ids, index = np.unique(self.g_id, return_index = True)
        self.g_id = list(unique_ids)
        self.g_num = list(np.array(self.g_num)[index])
        self.g_ra = list(np.array(self.g_ra)[index])
        self.g_dec = list(np.array(self.g_dec)[index])
        self.g_z = list(np.array(self.g_z)[index])
