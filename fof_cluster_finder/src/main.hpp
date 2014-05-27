/*Class header for Main*/

#ifndef MAIN_CLASS_H
#define MAIN_CLASS_H

#include <iostream>
#include <vector>

//#include "../include/dh.c"

#include "astro.hpp"
#include "cluster_class.hpp"
#include "fileio_class.hpp"
#include "fof_class.hpp"
#include "galaxy_class.hpp"
#include "kdtree_class.hpp"
#include "merge_class.hpp"
#include "option_class.hpp"
#include "zbin_class.hpp"

class Main { //! Class structure for Main.
private:
  Astro astro;
  Fileio fileio;
  Kdtree tree;
  Option opt;
  int num_bins;
  std::string param_file;
  std::vector<Zbin> zbins;
  std::vector<Galaxy> galaxies;
  std::vector<Cluster> clusters;
public:
  void read_options (int, char *[]);
  void read_data ();
  void set_up_zbins ();
  void assign_linking_param ();
  void make_kdtree ();
  void find_friends ();
  void merge_clusters ();
  void assign_cluster_props ();
  void output_results ();
};

#endif /* MAIN_CLASS_H */
