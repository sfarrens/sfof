/*Class header for Kdtree*/

#ifndef KDTREE_CLASS_H
#define KDTREE_CLASS_H

#include <algorithm>
#include <string>
#include <vector>
#include "astro.hpp"
#include "galaxy_class.hpp"

class Kdtree { //! Class structure for kd-tree properties
private:
  Astro astro;
public:
  class Kdtree_node{ //! Nested class structure for kd-tree node properties
  private:
    Astro astro;
  public:
    std::vector<Galaxy> members;
    double ra, dec, size, radius;
    Kdtree_node (std::vector<Galaxy*>::iterator begin,  std::vector<Galaxy*>::iterator end){
      /**< Initialise kdtree_node instance. */
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

  }; /*End of Kdtree_node nested class*/
  int max_depth;
  std::vector<Kdtree_node> node_list; 
  std::vector<Galaxy*> gaps_ptrs;
  void set_kdtree (std::vector<Galaxy>&, int);
  void build_kdtree (
          std::vector<Galaxy*>::iterator begin,
          std::vector<Galaxy*>::iterator end,
          int depth);
};

#endif /* KDTREE_CLASS_H */
