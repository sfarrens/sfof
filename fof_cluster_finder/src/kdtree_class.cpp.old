/*Class for storing kdtree properties*/

#include "kdtree_class.hpp"

void Kdtree::set_kdtree (const std::vector<Galaxy> &gals, int max_depth_val) {
  //! Set up a Kdtree instance.
  max_depth = max_depth_val;
  build_kdtree(gals, 0);
};

void Kdtree::build_kdtree (const std::vector<Galaxy> &gals, int depth) {
  //! Build kd-tree.
  int axis = depth % 2;
  if (depth <= max_depth) {
    if (depth == max_depth) {
      Kdtree_node node(gals);
      node_list.push_back(node);
    }
    std::vector<Galaxy> gals_left, gals_right;
    std::vector<double> ra_list, dec_list;
    for (int i = 0; i < gals.size(); i++) {
      ra_list.push_back(gals[i].ra);
      dec_list.push_back(gals[i].dec);
    }
    double median_val;
    for (int i = 0; i < gals.size(); i++) {
      if (axis == 1){
	median_val = astro.median(ra_list);
	if (ra_list[i] <= median_val)
	  gals_left.push_back(gals[i]);
	else
	  gals_right.push_back(gals[i]);
      }
      else {
	median_val = astro.median(dec_list);
	if (dec_list[i] <= median_val)
	  gals_left.push_back(gals[i]);
	else
	  gals_right.push_back(gals[i]);   
      }
    }
    build_kdtree(gals_left, depth + 1);
    build_kdtree(gals_right, depth + 1);
  }
}

