/*Class header for Galaxy*/

#ifndef MERGE_CLASS_H
#define MERGE_CLASS_H

#include <algorithm> 
#include <vector>
#include "cluster_class.hpp"

class Merge { //! Class for merge functions
private:
  bool gal_in_clt (const Galaxy &, const Cluster &);
  bool check_mem (const Cluster &, const Cluster &);
  void assimilate (Cluster &, Cluster &);
  void seek (std::vector<Cluster> &);
  void destroy (std::vector<Cluster> &);
public:
  Merge (std::vector<Cluster> &clusters) {
    /**< Initialise Merge instance. */
    seek(clusters);
    destroy(clusters);
  };
};

#endif /* MERGE_CLASS_H */
