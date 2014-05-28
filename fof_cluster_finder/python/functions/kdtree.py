############################
# CLUSTER KDTREE FUNCTIONS #
############################

import numpy as np, scipy
from scipy import spatial

def make_kdtree(object_list):
    """
    Function that returns a kd-tree of the
    provided object list.
    """
    pos = []
    for i in object_list:
        pos.append([i.x, i.y])
    kdtree = scipy.spatial.cKDTree(pos)
    return kdtree
