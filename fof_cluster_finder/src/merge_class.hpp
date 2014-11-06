/**
 * @file merge_class.hpp
 *
 * @author Stefano Sartor, Samuel Farrens
 */

#ifndef MERGE_CLASS_H
#define MERGE_CLASS_H

/**
 * @class Merge
 *
 * @brief Class for merging Cluster instances. 
 *
 * This class merges Cluster instances that have common Galaxy 
 * instances.
 */

#include <algorithm> 
#include <vector>
#include <map>
#include "cluster_class.hpp"
#include "exceptions.hpp"

class Merge { // Class for merge functions
public:
  /**
    * This method uses the union-find algorithm to create union-find groups in agreement with the
    * Cluster members.
    */
  static void join_uf(std::vector<Cluster> &);

  /**
    * This method creates the Clusters following the UnionFind data in each Galaxy.
    * @param[in] vector of Galaxy where iterate.
    * @param[out] vector of Cluster to be used to store new clusters. previously content is cleared.
    */
  static void rearrange_clusters(std::vector<Galaxy>&, std::vector<Cluster>&);

  /**
    * This method creates the Clusters following the UnionFind data in each Galaxy.
    * @param[in] map of Galaxy where iterate.
    * @param[out] vector of Cluster to be used to store new clusters. previously content is cleared.
    */
  static void rearrange_clusters(std::map<unsigned long, Galaxy>&, std::vector<Cluster>&);

};

#endif // MERGE_CLASS_H
