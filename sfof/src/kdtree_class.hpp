/**
 * @file kdtree_class.hpp
 *
 * @author Luca Toranatore, Samuel Farrens
 */

#ifndef KDTREE_CLASS_H
#define KDTREE_CLASS_H

/**
 * @class Kdtree
 *
 * @brief Class for constructing a kd-tree.
 *
 * This class constructs a kd-tree.
 *
 */

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include "astro.hpp"
#include "galaxy_class.hpp"
#include "point_class.hpp"

#define FLTC (1.0 + 1e-5)
enum node_to_galaxy {External, Intersects, Internal};

class Kdtree{ //! Class structure for kd-tree properties

public:

  class Kdtree_node{ //! Nested class structure for kd-tree node properties

  private:
    Astro astro;

  public:
    Galaxy *Gal;
    Kdtree_node *left, *right;

    class Point bottom_left, top_right;
    class Point center;
    double radius;
    int axis;
    unsigned int Ngalaxies;

    void print_node_info(class Kdtree_node *, const std::vector<Galaxy> &);

    node_to_galaxy check_node(class Point &, double, int);

  }; /*End of Kdtree_node nested class*/

private:
  Astro astro;

public:

  class Kdtree_node *Nodes, *root;
  std::vector<Galaxy> AllG;
  std::vector<Galaxy*> GalPtrs;

  Point MIN, MAX;
  int NNodes, NMaxNodes, NLeaves;
  double max_axis_inequality;

  double sample_area;

  class Kdtree_node* build_kdtree (std::vector<Galaxy*>::iterator begin,
                                   std::vector<Galaxy*>::iterator end,
                                   class Point [2],
                                   int);

  void set_Kdtree(std::vector<Galaxy> &, double);

  void write_Kdtree(const std::string &);

  void WalkTree(class Kdtree_node *, int);

  void WalkTree(class Kdtree_node *, std::ofstream &);

  int range_search(Point &, int, double, std::deque<Galaxy*> &) const;

  int range_search(Galaxy &, double, std::deque<Galaxy*> &) const;

  int range_search_loop(Kdtree_node *, class Point &, int, double, node_to_galaxy, std::deque<Galaxy*> &) const;

};

#endif /* KDTREE_CLASS_H */
