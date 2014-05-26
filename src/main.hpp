/*Class header for Main*/

#ifndef MAIN_CLASS_H
#define MAIN_CLASS_H

#include <iostream>
#include <vector>

#include "../include/dh.c"

#include "astro.cpp"
#include "cluster_class.cpp"
#include "fileio_class.cpp"
#include "fof_class.cpp"
#include "galaxy_class.cpp"
#include "kdtree_class.cpp"
#include "merge_class.cpp"
#include "option_class.cpp"
#include "zbin_class.cpp"

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
