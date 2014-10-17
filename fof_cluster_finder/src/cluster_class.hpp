/**
 * @file cluster_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef CLUSTER_CLASS_H
#define CLUSTER_CLASS_H

/**
 * @class Cluster
 *
 * @brief Class for storing galaxy cluster properties and members.
 *
 * This class stores Galaxy instances as galaxy cluster members and 
 * calculates the corresponding Cluster properties from the member
 * properties.
 */

#include <math.h>
#include "astro.hpp"
#include "cosmo.hpp"
#include "galaxy_class.hpp"
#include "point_class.hpp"

class Cluster { // Class structure for cluster properties.

public:
  
  /// Number asscosiated to Cluster instance.
  int num;
  
  /// Number of members in Cluster instance.
  int ngal;

  /// Right ascension of Cluster instance.
  double ra;

  /// Right ascension error of Cluster instance.
  double ra_err;

  /// Declination of Cluster instance.
  double dec;

  /// Declination error of Cluster instance.
  double dec_err;

  /// Redshift of Cluster instance.
  double z;

  /// Redshift error of Cluster instance.
  double z_err;

  /// Size of Cluster instance in arcminutes.
  double size;

  /// Area of Cluster instance in arcminutes squared.
  double area;

  /// Signal-to-noise of Cluster instance.
  double sn;

  /// Angular diameter distance of Cluster instance.
  double da;

  /// Vector of Cluster member Galaxy instances.
  std::vector<Galaxy*> mem;

  /** 
   * Initialise Cluster instance. 
   * @param[in] num_val Integer value.
   */
  Cluster (int num_val) { 
    num = num_val;
    ngal = 0;
    ra = 0;
    ra_err = 0;
    dec = 0;
    dec_err = 0;
    z = 0;
    z_err = 0;
    size = 0;
    area = 0;
    da = 0;  
  };
  
  /**
   * This method adds a Galaxy instance to a Cluster instance.
   * @param gal Galaxy instance.
   */
  void add_gal (Galaxy*);

  /**
   * This method calculates the angular diameter distance of a
   * Cluster instance for a given cosmology.
   * @param[in] c Speed of light [km/s].
   * @param[in] H0 Hubble parameter [km/s/Mpc].
   * @param[in] Omega_M Matter density.
   * @param[in] Omega_L Dark energy density.
   */
  void assign_dist (double, double, double, double);

  /**
   * This method assigns properties based on those of the 
   * members to the Cluster instance.
   */
  void assign_props ();

  /**
   * This method assigns a signal-to-noise value to a Cluster
   * instance given a value of the expected background number density.
   * @param bg_expect background number density [n_gal / arcmin^2]
   */
  void assign_sn (double);

  /**
   * This method clears all members from a Cluster instance.
   */
  void clear ();

  /**
   * This method resets the number associated to a Cluster instance.
   * @param[in] num_val Integer value.
   */
  void rename (int);

  /**
   * This method removes all duplicate members from a Cluster instance.
   */
  void unique ();

  friend bool operator< (const Cluster& clt1, const Cluster& clt2);

private:

  /// Include Astro class.
  Astro astro;

  /// Include Cosmo class.
  Cosmo cosmo;

}; 

/**
 * Bool < operator for Cluster class. Compares the number of members
 * between two Cluster instances.
 */
inline bool operator< (const Cluster& clt1, const Cluster& clt2) {
  return clt1.ngal < clt2.ngal;
}

#endif // CLUSTER_CLASS_H
