/*Class for storing redshift bin properties*/

#include <cmath>
#include "zbin_class.hpp"

void Zbin::assign_dist (double c, double H0, double Omega_M, double Omega_L) {
  // Calculate the angular diameter distance and the differential comoving 
  // volume element for a Zbin instance.
  if (c <= 0)
    throw BadArgumentException("Zbin::assign_dist", "c", "> 0.0");
  if (H0 <= 0)
    throw BadArgumentException("Zbin::assign_dist", "H0", "> 0.0");
  cosmo.set_up(Omega_M, Omega_L);
  dvdz = cosmo.dcomvoldz(z);
  da = ((c / H0) * cosmo.angdidis(z));
}

void Zbin::assign_rfriend (double r_ref) {
  // Scale linking length to redshift bin.
  if (r_ref <= 0)
    throw BadArgumentException("Zbin::assign_rfriend", "r_ref", "> 0.0");
  if (count < 0)
    throw RuntimeException("Zbin::assign_rfriend", "count", ">= 0.0");
  if (dvdz <= 0)
    throw RuntimeException("Zbin::assign_rfriend", "dvdz", "> 0.0");
  if (da <= 0)
    throw RuntimeException("Zbin::assign_rfriend", "da", "> 0.0");
  dndz = double(count) / dz;
  dndv = dndz / dvdz;
  if(dndv > 0) 
    link_r = pow(dndv, -0.5) * r_ref;
  else
    link_r = 0.0;
  rfriend = link_r / da;
}

void Zbin::assign_fixed_rfriend (double link_r_val) {
  // Assign fixed linking length value.
  if (link_r_val <= 0)
    throw BadArgumentException("Zbin::assign_fixed_rfriend", "link_r_val", "> 0.0");
  if (count < 0)
    throw RuntimeException("Zbin::assign_rfriend", "count", ">= 0.0");
  if (dvdz <= 0)
    throw RuntimeException("Zbin::assign_rfriend", "dvdz", "> 0.0");
  if (da <= 0)
    throw RuntimeException("Zbin::assign_rfriend", "da", "> 0.0");
  dndz = double(count) / dz;
  dndv = dndz / dvdz;
  if(dndv > 0)
    link_r = link_r_val;
  else
    link_r = 0.0;
  rfriend = link_r / da;
}
