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
  int cluster_count;
  double link_r, link_z;
  std::string mode;
public:
  std::vector<Cluster> list_of_clusters;
  void setup (double, double, const std::string &);
  bool bin_check (const Zbin &, const Galaxy &);
  bool node_check (const Galaxy &, const Kdtree::Kdtree_node &, double);
  bool friendship (const Zbin &, const Galaxy &, const Galaxy &, double);
  void remove (int);
  void new_cluster (const Zbin &, Galaxy &, Galaxy &);
  void add_member (const Zbin &, Galaxy &, Cluster &);
  void find_friends (const Zbin &, Galaxy &, double, std::vector<Galaxy> &, const Kdtree &);
  void find_friends_of_friends (const Zbin &, Cluster &, double,
				std::vector<Galaxy> &, const Kdtree &);
  void friends_of_friends (int, const std::vector<Zbin> &, std::vector<Galaxy> &,
			   const Kdtree &);
};

#endif /* FOF_CLASS_H */
