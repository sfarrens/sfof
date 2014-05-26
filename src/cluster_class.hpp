/*Class header for Cluster*/

#ifndef CLUSTER_CLASS_H
#define CLUSTER_CLASS_H

#include <vector>
#include "astro.hpp"
#include "galaxy_class.hpp"

class Cluster { //! Class structure for cluster properties.
private:
  Astro astro;
public:
  int num, ngal;
  double ra, dec, z, size, area, sn;
  std::vector<Galaxy> mem;
  Cluster (int num_val) { 
    /**< Initialise Cluster instance. */
    num = num_val;
  };
  void add_gal (const Galaxy &);
  void assign_props ();
  void assign_sn (double);
  void clear ();
  void rename (int);
  void unique ();
  friend bool operator< (const Cluster& clt1, const Cluster& clt2);
}; 

bool operator< (const Cluster& clt1, const Cluster& clt2) {
  //! Bool < operator for Cluster class.
  return clt1.ngal < clt2.ngal;
}

#endif /* CLUSTER_CLASS_H */
