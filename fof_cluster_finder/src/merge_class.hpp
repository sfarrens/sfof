/**
 * @file merge_class.hpp
 *
 * @author Samuel Farrens
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
#include "cluster_class.hpp"
#include "exceptions.hpp"

class Merge { // Class for merge functions

public:

  /** 
   * Initialise Merge instance.
   * @param[in] clusters Vector of Cluster instances.
   */
  Merge (std::vector<Cluster> &clusters) {
    if (clusters.empty())
      throw BadArgumentException("Merge", "clusters", "a valid vector");
    seek(clusters);
    destroy(clusters);
  };

private:

  /**
   * This method checks if a given Galaxy instance is a member
   * of a given Cluster instance.
   * @param[in] gal Galaxy instance.
   * @param[in] clt Cluster instance.
   */
  bool gal_in_clt (Galaxy *, const Cluster &);

  /**
   * This method checks if two given Cluster instances have any
   * common member Galaxy instances.
   * @param[in] clt1 Cluster instance 1.
   * @param[in] clt2 Cluster instance 2.
   */
  bool check_mem (const Cluster &, const Cluster &);

  /**
   * This method merges the member Galaxy instances from  
   * Cluster instance 2 into Cluster instance 1 and removes
   * duplicates.
   * @param[in] clt1 Cluster instance 1.
   * @param[in] clt2 Cluster instance 2.
   */
  void assimilate (Cluster &, Cluster &);

  /**
   * This method searches for Cluster instances with common
   * members.
   * @param[in] clusters Vector of Cluster instances.
   */
  void seek (std::vector<Cluster> &);

  /**
   * This method removes empty Cluster instances from the
   the list.
   * @param[in] clusters Vector of Cluster instances.
   */
  void destroy (std::vector<Cluster> &);

};

#endif // MERGE_CLASS_H
