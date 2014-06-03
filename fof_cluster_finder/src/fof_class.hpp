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
  Kdtree tree;
  std::vector<Zbin> zbin_list;
  std::vector<Galaxy> gal_list;
  int cluster_count;
  double link_r, link_z;
  std::string mode;
public:
  std::vector<Cluster> list_of_clusters;
  FoF (double link_r_val, double link_z_val, std::string mode_val, 
       const Kdtree &tree_val, const std::vector<Zbin> &zbin_val, std::vector<Galaxy> &gal_val) { 
    /**< Initialise FoF instance. */
    link_r = link_r_val;
    link_z = link_z_val;
    mode = mode_val;
    tree = tree_val;
    zbin_list = zbin_val;
    gal_list = gal_val;
  };
  bool bin_check (const Zbin &, const Galaxy &);
  bool node_check (const Galaxy &, const Kdtree::Kdtree_node &, double);
  bool friendship (const Zbin &, const Galaxy &, const Galaxy &, double);
  void remove (int);
  void new_cluster (const Zbin &, Galaxy &, Galaxy &);
  void add_member (const Zbin &, Galaxy &, Cluster &);
  void find_friends (const Zbin &, Galaxy &, double);
  void find_friends_of_friends (const Zbin &, Cluster &, double);
  void friends_of_friends (int);
};

#endif /* FOF_CLASS_H */
