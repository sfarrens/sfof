/**
 * @file cat_merge.hpp
 *
 * @author Samuel Farrens
 */

#ifndef CAT_MERGE_CLASS_H
#define CAT_MERGE_CLASS_H

/**
 * @class Cat_Merge
 *
 * @brief Class for merging cluster catalogues.
 *
 * This class merges Cluster instances that share commom
 * member Galaxy instances.
 */

#include <iostream>
#include <omp.h>
#include <vector>
#include "comp.hpp"
#include "cluster_class.hpp"
#include "galaxy_class.hpp"
#include "cat_merge_fileio.hpp"
#include "fileio_class.hpp"
#include "merge_class.hpp"
#include "option_class.hpp"

class Cat_Merge { // Class structure for Cat_Merge.

public:
  /// Include Comp class.
  Comp comp;

  /**
   * This method calls Option to read the code options from the 
   * provided arguments.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   */
  void read_options (int, char *[]);

  /**
   * This method calls Merge_Fileio to read the input file and stores the 
   * data in Galaxy instances.
   */
  void read_files ();

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
  void write_files ();
  
private:
  /// Include Fileio class.
  Fileio fileio;
  
  /// Include Option class.
  Option opt;
  
  /// Include Merge_Fileio class.
  Merge_Fileio merge_fileio;
 
  /// Vector of Cluster instances.
  std::vector<Cluster> clusters;

  /// Set of Galaxies.
  Merge_Fileio::gal_container galaxies;

};

#endif // CAT_MERGE_CLASS_H
