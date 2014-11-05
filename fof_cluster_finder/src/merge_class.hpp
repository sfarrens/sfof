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
   * Initialise Merge instance.
   * @param[in] clusters Vector of Cluster instances.
   */

  Merge(){
  }

private:

public:

  /**
    * This method ...
    */
  void join_uf(std::vector<Cluster> &);

  /**
    * This method ...
    */
  void rearrange_clusters(std::vector<Galaxy>&, std::vector<Cluster>&);

  /**
   * This method ...
   */
  void rearrange_clusters(std::map<unsigned long, Galaxy>&, std::vector<Cluster>&);

};

#endif // MERGE_CLASS_H
