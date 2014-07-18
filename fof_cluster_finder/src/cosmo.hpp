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
 * @brief Class containing basic functions required for astronomy.
 *
 * This class encompasses a selection of functions that perform some
 * basic calculations that often required for astronomy or cosmology.
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

class Cosmo { // Class structure for cosmology functions

public:

  double angdidis(double, double, double);

  double angdidis2(double, double, double, double);
 
  double comdis(double, double, double);

  double comvol(double, double, double);

  double dcomdisdz(double, double, double);

  double dcomvoldz(double, double, double);

  double dlookbackdz(double, double, double);

  double doptdepthdz(double, double, double);

  double dpropmotdisdz(double, double, double);

  double intcomvol(double, double, double);

  double lookback(double, double, double);

  double lumdis(double, double, double);

  double optdepth(double, double, double);

  double propmotdis(double, double, double);

};

#endif // COSMO_H
