###########################
# CLUSTER MERGE FUNCTIONS #
###########################

import numpy as np, scipy
from scipy import spatial
from classes.cluster import Cluster
from functions import interface, kdtree

def find_matches(clusters, progress, tree_dist):
    """
    Function that returns the indicies of matching Cluster instances.
    """
    matches = []
    tree = kdtree.make_kdtree(clusters)
    for i in range(len(clusters)):
        if progress: interface.progress_bar(i, len(clusters))
        if not clusters[i].match_flag:
            list = tree.query_ball_point([clusters[i].x, clusters[i].y], tree_dist)
            for j in list:
                if not clusters[j].match_flag:
                    if ((j > i) & (np.any(np.in1d(clusters[i].g_id, clusters[j].g_id)))):
                        matches.append([i, j])
                        clusters[i].match_flag = True
                        clusters[j].match_flag = True
    matches = np.array(matches)
    if progress: print ""
    return matches

def merge(cluster1, cluster2):
    """
    Fuction that merges two Cluster instances.
    """
    cluster1.extend(cluster2.g_num, cluster2.g_id, cluster2.g_ra, cluster2.g_dec, cluster2.g_z, cluster2.g_x, cluster2.g_y)

def merge_and_clean(clusters, matches, bg_expect):
    """
    Function that merges all matched Cluster instances and deletes the redundant structures.
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
        clusters[i].props(bg_expect)
        clusters[i].clean(i)

def merge_clusters(list_of_clusters, progress, bg_expect, tree_dist):
    """
    Function that finds matching Cluster instances and merges them.
    """
    matches = [None]
    sweep = 1
    while len(matches) > 0:
        if progress: print ' >> Sweep:', sweep
        matches = find_matches(list_of_clusters, progress, tree_dist)
        merge_and_clean(list_of_clusters, matches, bg_expect)
        sweep += 1
