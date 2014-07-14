/*Class header for Main*/

#ifndef CAT_MERGE_CLASS_H
#define CAT_MERGE_CLASS_H

#include <iostream>
#include <omp.h>
#include <vector>

#include "comp.hpp"
#include "cluster_class.hpp"
#include "cat_merge_fileio.hpp"
#include "fileio_class.hpp"
#include "merge_class.hpp"
#include "option_class.hpp"

class Cat_Merge { //! Class structure for Cat_Merge.
private:
  Fileio fileio;
  Option opt;
  Merge_Fileio merge_fileio;
  std::vector<Cluster> clusters;
public:
  Comp comp;
  void read_options (int, char *[]);
  void read_files ();
  void merge_clusters ();
  void assign_cluster_props ();
  void write_files ();
};

#endif /* CAT_MERGE_CLASS_H */
