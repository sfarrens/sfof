/*Class header for FoF*/

#ifndef FOF_CLASS_H
#define FOF_CLASS_H

#include <string>
#include <vector>
#include "astro.hpp"
#include "cluster_class.hpp"
#include "galaxy_class.hpp"
#include "kdtree_class.hpp"
#include "zbin_class.hpp"

class FoF { //! Class for friends-of-friends functions
private:
  Astro astro;
public:
  double link_r, link_z;
  std::string mode;
  std::vector<Cluster> list_of_clusters;
  FoF (double link_r_val, double link_z_val, std::string mode_val) { 
    /**< Initialise FoF instance. */
    link_r = link_r_val;
    link_z = link_z_val;
    mode = mode_val;
  };
  bool bin_check (const Zbin&, const Galaxy&);
  bool node_check (const Galaxy&, const Kdtree::Kdtree_node&, double);
  bool friendship (const Zbin&, const Galaxy&, const Galaxy&, double);
  void remove (int);
  void friends_of_friends (const Kdtree&, const Zbin&, std::vector<Galaxy>&);
};

#endif /* FOF_CLASS_H */
