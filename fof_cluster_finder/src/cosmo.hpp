/**
 * @file cosmo.hpp
 *
 * @author Samuel Farrens, David Hogg & Eduardo Cypriano
 */

#ifndef COSMO_H
#define COSMO_H

/**
 * @class Cosmo
 *
 * @brief Class containing basic functions required for Cosmology.
 *
 * This class encompasses a selection of functions that perform some
 * basic calculations required for cosmology.
 */

class Cosmo { // Class structure for cosmology functions

public:

  /// Matter density parameter value.
  double OmegaM;
  
  /// Dark energy density parameter value.
  double OmegaL;

  /**
   * This function sets the cosmological parameter values for the Cosmo
   * functions.
   */
  void set_up(double, double);

  /**
   * This function calculates the angular diameter distance d_A as a
   * function of z, Omega_M and Omega_L in a matter-dominated universe,
   * using the function propmotdis().  H0=c=1.
   */
  double angdidis(double);

  /**
   * This function calculates the angular diameter distance d_A from z1
   * to z2 as a function of Omega_M and Omega_L in a matter-dominated
   * universe, using the function propmotdis().  H0=c=1.
   */
  double angdidis2(double, double);
 
  /**
   * This function calculates the line-of-sight comoving distance d_C as
   * a function of z, Omega_M and Omega_L in a matter-dominated
   * universe, using dcomdisdz().  H0=c=1.
   */
  double comdis(double);

  /**
   * This function calculates the all-sky comoving volume V as a
   * function of z, Omega_M and Omega_L in a matter-dominated universe.
   * Formulae from Carrol, Press & Turner, 1992, and my own calculation.
   */
  double comvol(double);

  /**
   * This function calculates the differential line-of-sight comoving
   * distance dD_c/dz as a function of z, Omega_M and Omega_L in a
   * matter-dominated universe.  H0=c=1.
   */
  double dcomdisdz(double);

  /**
   * This function calculates the one-steradian differential comoving
   * volume dV/dz as a function of z, Omega_M and Omega_L in a
   * matter-dominated universe.  Formulae from Carrol, Press & Turner,
   * 1992, Kolb & Turner, 1990, and my own calculation.  H0=c=1.
   */
  double dcomvoldz(double);

  /**
   *  This function calculates the change in lookback time dt/dz with
   * redshift z as a function of z, Omega_M and Omega_L in a
   * matter-dominated universe.  Formula from Carrol, Press & Turner,
   * 1992.  H0=c=1.
   */
  double dlookbackdz(double);

  /**
   * This function calculates the change in optical depth dtau/dz with
   * redshift z as a function of z, Omega_M and Omega_L in a
   * matter-dominated universe.  Formula from Peebles, 1993.
   * H0=c=sigma=n=1.
   */
  double doptdepthdz(double);

  /**
   * This function calculates the derivative of the proper motion
   * distance d_M with respect to redshift z as a function of z, Omega_M
   * and Omega_L in a matter-dominated universe.  Formula from Carrol,
   * Press & Turner, 1992.  This function also requires the function
   * propmotdis(). H0=c=1.
   */
  double dpropmotdisdz(double);

  /**
   * This function calculates the all-sky comoving volume V as a
   * function of z, Omega_M and Omega_L in a matter-dominated universe
   * by integrating dcomvoldz().  It was written to test comvol().
   */
  double intcomvol(double);

  /**
   * This function calculates the lookback time t(0)-t(z) as a function
   * of z, OmegaM and OmegaL by integrating the output of dlookbackdz.
   */
  double lookback(double);

  /**
   *  This function calculates the luminosity distance d_L as a function
   * of z, Omega_M and Omega_L in a matter-dominated universe, using the
   * function propmotdis().  H0=c=1.
   */
  double lumdis(double);

  /**
   * This function calculates the optical depth tau as a function
   * of z, OmegaM and OmegaL by integrating the output of doptdepthdz.
   * Again, H0=c=sigma=n=1.
   */
  double optdepth(double);

  /**
   * This function calculates the proper motion distance d_M as a
   * function of z, Omega_M and Omega_L in a matter-dominated universe.
   * Formulae from Carrol, Press & Turner, 1992, Kolb \& Turner, 1990,
   * and my own derivation.  Makes use of comdis().  H0=c=1.
   */
  double propmotdis(double);

};

#endif // COSMO_H
