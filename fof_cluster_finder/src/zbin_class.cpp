/*Class for storing redshift bin properties*/

#include <math.h>
#include "zbin_class.hpp"
#include "dh.h"

void Zbin::assign_dist (double c, double H0, double Omega_M, double Omega_L) {
  //! Calculate the angular diameter distance and the differential comoving 
  //! volume element for a Zbin instance.
  dvdz = dcomvoldz(z, Omega_M, Omega_L);
  da = ((c / H0) * angdidis(z, Omega_M, Omega_L));
}

void Zbin::assign_rfriend (double r_ref) {
  //! Assign redshift bin to Galaxy instance.
  dndz = double(count) / dz;
  dndv = dndz / dvdz;
  if(dndv > 0)
    link_r = pow(dndv, -0.5) * r_ref;
  else
    link_r = 0.0;
  rfriend = link_r / da;
}
