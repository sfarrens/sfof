/*Class header for Cluster*/

#ifndef CLUSTER_CLASS_H
#define CLUSTER_CLASS_H

#include <math.h>
#include <vector>

#include "astro.hpp"
#include "galaxy_class.hpp"

class Cluster { //! Class structure for cluster properties.
private:
  Astro astro;
public:
  int num, ngal;
  double ra, ra_err, dec, dec_err, z, z_err, size, area, sn, da;
  std::vector<Galaxy> mem;
  Cluster (int num_val) { 
    /**< Initialise Cluster instance. */
    num = num_val;
  };
  void add_gal (const Galaxy &);
  void assign_dist (double, double, double, double);
  void assign_props ();
  void assign_sn (double);
  void clear ();
  void rename (int);
  void unique ();
  friend bool operator< (const Cluster& clt1, const Cluster& clt2);
}; 

inline bool operator< (const Cluster& clt1, const Cluster& clt2) {
  //! Bool < operator for Cluster class.
  return clt1.ngal < clt2.ngal;
}

#endif /* CLUSTER_CLASS_H */
