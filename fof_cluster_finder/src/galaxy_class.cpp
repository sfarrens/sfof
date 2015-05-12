/*Class for storing galaxy properties*/

#include "galaxy_class.hpp"

void Galaxy::assign_dist (double c, double H0, double Omega_M, double Omega_L) {
  // Calculate angular diameter distance for Galaxy instance;
  if (c <= 0)
    throw BadArgumentException("Galaxy::assign_dist", "c", "> 0.0");
  if (H0 <= 0)
    throw BadArgumentException("Galaxy::assign_dist", "H0", "> 0.0");
  cosmo.set_up(Omega_M, Omega_L);
  da = ((c / H0) * cosmo.angdidis(z));
}

void Galaxy::assign_bin (double min_value, double bin_size) {
  // Assign redshift bin to Galaxy instance.
  if (min_value < 0)
    throw BadArgumentException("Galaxy::assign_bin", "min_value", ">= 0.0");
  if (bin_size <= 0)
    throw BadArgumentException("Galaxy::assign_bin", "bin_size", "> 0.0");
  bin = astro.find_bin(z, min_value, bin_size);
}

void Galaxy::assign_bins (double min_value, double bin_size, double delta_z) {
  // Assign redshift bin to Galaxy instance.
  if (min_value < 0)
    throw BadArgumentException("Galaxy::assign_bin", "min_value", ">= 0.0");
  if (bin_size <= 0)
    throw BadArgumentException("Galaxy::assign_bin", "bin_size", "> 0.0");
  for(double x = z - delta_z * dz; x <= z + delta_z * dz; x += bin_size)
    if(x >= 0.0) bins.push_back(astro.find_bin(x, min_value, bin_size));
}

void Galaxy::set_cluster_status (int nbins) {
  // Set the initial cluster status for each redshift bin to false.
  if (nbins <= 0)
    throw BadArgumentException("Galaxy::set_cluster_status", "nbins", "> 0.0");
  for(int i = 0; i < nbins; i++)
    in_cluster.push_back(false);
}
