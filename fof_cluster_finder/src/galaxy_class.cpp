/*Class for storing galaxy properties*/

#include "galaxy_class.hpp"

void Galaxy::assign_dist (double c, double H0, double Omega_M, double Omega_L) {
  // Calculate angular diameter distance for Galaxy instance;
  cosmo.set_up(Omega_M, Omega_L);
  da = ((c / H0) * cosmo.angdidis(z));
}

void Galaxy::assign_bin (double min_value, double bin_size) {
  // Assign redshift bin to Galaxy instance.
  bin = astro.find_bin(z, min_value, bin_size);
}

void Galaxy::set_cluster_status (int nbins) {
  // Set the initial cluster status for each redshift bin to false.
  for(int i = 0; i < nbins; i++)
    in_cluster.push_back(false);
}
