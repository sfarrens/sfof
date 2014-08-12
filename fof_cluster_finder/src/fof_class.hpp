/**
 * @file fof_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef FOF_CLASS_H
#define FOF_CLASS_H

/**
 * @class FoF
 *
 * @brief Class for perfoming friends-of-friends cluster detection.
 *
 * This class produces a vector of Cluster instances by performing a 
 * friends-of-friends search in a given Zbin instance.
 */

#include <string>
#include <vector>
#include "astro.hpp"
#include "cluster_class.hpp"
#include "galaxy_class.hpp"
#include "kdtree_class.hpp"
#include "zbin_class.hpp"

class FoF { // Class for friends-of-friends functions

public:

  /// Vector of Cluster instances.
  std::vector<Cluster> list_of_clusters;

  /** 
   * Initialise FoF instance.
   */
  FoF() { 
    cluster_count = -1;
    link_r = 0;
    link_z = 0;
  };

  /**
   * This method sets-up a FoF instance.
   * @param[in] link_r_val Transverse linking parameter value.
   * @param[in] link_z_val Line-of-sight linking parameter value.
   * @param[in] mode_val FoF mode ["spec"/"phot"].
   */
  void setup (double, double, const std::string &);

  /**
   * This method removes Cluster instances that have too few member Galaxy instances.
   * @param[in] min_ngal Minimum number of member Galaxy instances required.
   */
  void remove (int);

  /**
   * This method performs a friends-of-friends search for Cluster instances in a given 
   * Zbin instance.
   * @param[in] bin_num Zbin number.
   * @param[in] zbin_list Vector of Zbin instances.
   * @param[in] gal_list Vector of Galaxy instances.
   * @param[in] tree Vector of Kdtree node instances.
   */
  void friends_of_friends (int, const std::vector<Zbin> &, std::vector<Galaxy> &,
			   const Kdtree &);

private:

  /// Include Astro class.
  Astro astro;

  /// Count of current number of Cluster instances.
  int cluster_count;

  /// Transverse linking parameter.
  double link_r;
  
  /// Line-of-sight linking parameter.
  double link_z;

  /// FoF mode ["spec"/"phot"].
  std::string mode;

  /**
   * This method checks if a Galaxy instance is compatible with a given 
   * Zbin instance.
   * @param[in] zbin Zbin instance.
   * @param[in] gal Galaxy instance.
   */
  bool bin_check (const Zbin &, const Galaxy &);

  /**
   * This method checks if a Galaxy instance is compatibile with a given Kdtree 
   * node instance.
   * @param[in] gal Galaxy instance.
   * @param[in] node Kdtree node instance.
   * @param[in] rfriend R_friend value.
   */
  bool node_check (const Galaxy &, const Kdtree::Kdtree_node &, double);

  /**
   * This method checks if two Galaxy instances satisfy the linking conditions in a 
   * given Zbin instance.
   * @param[in] zbin Zbin instance.
   * @param[in] gal1 Galaxy instance 1.
   * @param[in] gal2 Galaxy instance 2.
   * @param[in] rfriend R_friend value.
   */
  bool friendship (const Zbin &, const Galaxy &, const Galaxy &, double);

  /**
   * This method creates a new Cluster instance.
   * @param[in] zbin Zbin instance.
   * @param[in] gal1 Galaxy instance 1.
   * @param[in] gal2 Galaxy instance 2.
   */
  void new_cluster (const Zbin &, Galaxy &, Galaxy &);

  /**
   * This method adds a new member Galaxy instance to an existing Cluster instance.
   * @param[in] zbin Zbin instance.
   * @param[in] gal Galaxy instance.
   * @param[in] cluster Cluster instance.
   */
  void add_member (const Zbin &, Galaxy &, Cluster &);
  
  /**
   * This method finds Galaxy instances linked to a given Galaxy instance in a given
   * Zbin instance.
   * @param[in] zbin Zbin instance.
   * @param[in] gal Galaxy instance.
   * @param[in] rfriend R_friend value.
   * @param[in] gal_list Vector of Galaxy instances.
   * @param[in] tree Vector of Kdtree node instances.
   */
  void find_friends (const Zbin &, Galaxy &, double, std::vector<Galaxy> &, const Kdtree &);

  /**
   * This method finds Galaxy instances linked to the members of a given Cluster 
   * instance in a given Zbin instance.
   * @param[in] zbin Zbin instance.
   * @param[in] cluster Cluster instance.
   * @param[in] rfriend R_friend value.
   * @param[in] gal_list Vector of Galaxy instances.
   * @param[in] tree Vector of Kdtree node instances.
   */
  void find_friends_of_friends (const Zbin &, Cluster &, double,
				std::vector<Galaxy> &, const Kdtree &);

};

#endif // FOF_CLASS_H
