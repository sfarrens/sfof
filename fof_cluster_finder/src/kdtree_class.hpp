/**
 * @file kdtree_class.hpp
 *
 * @author Samuel Farrens + Stefano Sartor
 */

#ifndef KDTREE_CLASS_H
#define KDTREE_CLASS_H

/**
 * @class Kdtree
 *
 * @brief Class for building a kd-tree in RA-DEC space.
 *
 * This class builds a two-dimentional kd-tree in RA-DEC space to a specified
 * depth.
 */

#include <algorithm>
#include <string>
#include <vector>
#include "astro.hpp"
#include "galaxy_class.hpp"

class Kdtree { // Class structure for kd-tree properties
  
public:

  /**
   * @class Kdtree_node
   *
   * @brief Class for storing Kdtree_node properties. 
   *
   * This class assigns Galaxy instances to a node at a specified depth.
   */
  class Kdtree_node{ // Nested class structure for kd-tree node properties
  
  public:

    /// Vector of node member Galaxy instances.
    std::vector<Galaxy> members;

    /// Right ascension of node instance.
    double ra;

    /// Declination of node instance.
    double dec;

    /// Size of node instance.
    double size;

    /// Radius of node instance.
    double radius;

    /** 
     * Initialise Kdtree_node instance.
     * @param[in] begin Begining itterator of Galaxy vector.
     * @param[in] end Ending itterator of Galaxy vector.
     */
    Kdtree_node (std::vector<Galaxy*>::iterator begin,  
		 std::vector<Galaxy*>::iterator end){
      size = end-begin;
      members.reserve(size);
      while(begin != end){
          members.push_back(*(*begin));
          ++begin;
      }
      std::vector<double> ra_list, dec_list;
      for (int i = 0; i < size; i++) {
    ra_list.push_back(members[i].ra);
    dec_list.push_back(members[i].dec);
      }
      ra = astro.mean(ra_list);
      dec = astro.mean(dec_list);
      radius = std::max(astro.angsep(ra, dec, astro.min(ra_list), astro.min(dec_list)),
            astro.angsep(ra, dec, astro.max(ra_list), astro.max(dec_list)));
    }
    
  private:

    /// Include Astro class.
    Astro astro;

  }; /*End of Kdtree_node nested class*/

  /// Maximum depth to which the Kdtree instance should be built.
  int max_depth;

  /// Vector of Kdtree_node instances.
  std::vector<Kdtree_node> node_list; 

  /// Pointers to vector of Galaxy instances.
  std::vector<Galaxy*> gaps_ptrs;

  /**
   * This method sets-up a Kdtree instance.
   * @param[in] gals Vector of Galaxy instances.
   * @param[in] max_depth_val Maximum depth of Kdtree.
   */
  void set_kdtree (std::vector<Galaxy>&, int);

  /**
   * This method splits the data at a given depth and itterates until the maximum
   * depth is reached.
   * @param[in] begin Begining itterator of Galaxy vector.
   * @param[in] end Ending itterator of Galaxy vector..
   * @param[in] depth Current depth of Kdtree.
   */
  void build_kdtree (
          std::vector<Galaxy*>::iterator begin,
          std::vector<Galaxy*>::iterator end,
          int depth);

private:
  
  /// Include Astro class.
  Astro astro;
  
};

#endif // KDTREE_CLASS_H
