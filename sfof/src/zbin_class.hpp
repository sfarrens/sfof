/**
 * @file zbin_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef ZBIN_CLASS_H
#define ZBIN_CLASS_H

/**
 * @class Zbin
 *
 * @brief Class for storing redshift bin properties.
 *
 * This class calculates and stores Zbin properties.
 */

#include "cosmo.hpp"
#include "exceptions.hpp"

class Zbin { // Class structure for redshift bin properties.

public:

  /// Number associated to Zbin instance.
  int num;

  /// Number of Galaxy instances corresponding to Zbin instance.
  int count;

  /// Redshift of Zbin instance.
  double z;

  /// Redshift bin size of Zbin instance.
  double dz;

  /// Angular diameter distance of Zbin instance.
  double da;

  /// Differential comoving volume of Zbin instance.
  double dvdz;

  /// Surface number density of Zbin instance.
  double dndz;

  /// Volume number density of Zbin instance.
  double dndv;

  /// Corrected transverse linking parameter value of Zbin instance.
  double link_r;
  
  /// Transverse linking radius of Zbin instance.
  double rfriend;

  /** 
   * Initialise Zbin instance.
   * @param[in] num_val Integer value.
   * @param[in] z_val Redshift.
   * @param[in] z_bin_size Redshift bin size.
   */
  Zbin(int num_val, double z_val, double z_bin_size) { 
    /**< Initialise Zbin instance. */
    if (z_val <= 0)
      throw BadArgumentException("Zbin", "z_val", "> 0.0");
    if (z_bin_size <= 0)
      throw BadArgumentException("Zbin", "z_bin_size", "> 0.0");
    num = num_val;
    z = z_val;
    dz = z_bin_size;
    count = 0;
    da = 0;
    dvdz = 0;
    dndz = 0;
    dndv = 0;
    link_r = 0;
    rfriend = 0;
  };

  /**
   * This method calculates the angular diameter distance of a
   * Zbin instance for a given cosmology.
   * @param[in] c Speed of light [km/s].
   * @param[in] H0 Hubble parameter [km/s/Mpc].
   * @param[in] Omega_M Matter density.
   * @param[in] Omega_L Dark energy density.
   */
  void assign_dist (double, double, double, double);

  /**
   * This method scales transverse lining parameter value to the
   * redshift of the Zbin instance.
   * @param[in] r_ref Reference transverse linking parameter value.
   */
  void assign_rfriend (double);

  /**
   * This method sets a fixed transverse lining parameter value for
   * the Zbin instance.
   * @param[in] link_r_val Transverse linking parameter value.
   */
  void assign_fixed_rfriend (double);

private:
  
  /// Include Cosmo class.
  Cosmo cosmo;

};

#endif // ZBIN_CLASS_H
