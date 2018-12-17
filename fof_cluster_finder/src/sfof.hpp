/**
 * @file main.hpp
 *
 * @author Samuel Farrens
 */

#ifndef MAIN_CLASS_H
#define MAIN_CLASS_H

/**
 * @class Main
 *
 * @brief Class for running the FoF algorithm.
 *
 * This class runs the friends-of-friends cluster detection
 * algorithm.
 */

#include <iostream>
#include <omp.h>
#include <string>
#include <vector>
#include "astro.hpp"
#include "comp.hpp"
#include "cluster_class.hpp"
#include "fileio_class.hpp"
#include "fof_class.hpp"
#include "galaxy_class.hpp"
#include "kdtree_class.hpp"
#include "merge_class.hpp"
#include "option_class.hpp"
#include "zbin_class.hpp"
#include "spline.hpp"

class Main { // Class structure for Main.

public:

  /// Include Comp class.
  Comp comp;

  /**
   * This method calls Option to read the code options from the
   * provided arguments and/or the parameter file.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   */
  void read_options (int, char *[]);

  /**
   * This method calls Fileio to read the input file and stores the
   * data in Galaxy instances.
   */
  void read_data ();

  /**
   * This method sets up redshift bins in Zbin instances.
   */
  void set_up_zbins ();

  /**
   * This method assigns linking parameter values to Zbin instances.
   * A reference value is defined in order to ensure uniformity.
   */
  void assign_linking_param ();

  /**
   * This method checks how many cluster candidates have been
   * detected.
   */
  void check_results();

  /**
   * This method initialises a Kdtree instance.
   */
  void make_kdtree ();

  /**
   * This method counts the number of background galaxies at each
   * redshift.
   */
  void background_counts ();

  /**
   * This method initialises a series of FoF instances for the
   * corresponding Zbin instances.
   */
  void find_friends ();

  /**
   * This method initialises a Merge instance.
   */
  void merge_clusters ();

  /**
   * This method assigns properties to the Cluster instances.
   */
  void assign_cluster_props ();

  /**
   * This method calls Fileio to write the Cluster instances and
   * corresponding member Galaxy instances to files.
   */
  void output_results ();

private:

  /// Include Astro class.
  Astro astro;

  /// Include Fileio class.
  Fileio fileio;

  /// Include Kdtree class.
  Kdtree tree;

  /// Include Option class.
  Option opt;

  /// Include Spline.
  Spline spline_nz, spline_bg;

  /// Number of redshift bins.
  int num_bins;

  /// Option parameter file name.
  std::string param_file;

  /// Vector of Zbin instances.
  std::vector<Zbin> zbins;

  /// Vector of Galaxy instances.
  std::vector<Galaxy> galaxies;

  /// Vector of Cluster instances.
  std::vector<Cluster> clusters;

};

#endif // MAIN_CLASS_H
