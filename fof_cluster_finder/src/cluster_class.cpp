/*Class for storing cluster properties*/

#include "dh.h"
#include "cluster_class.hpp"

void Cluster::add_gal (const Galaxy &gal) {
  // Add galaxy properties to Cluster instance.
  mem.push_back(gal);
}

void Cluster::assign_dist (double c, double H0, double Omega_M, double Omega_L) {
  // Calculate angular diameter distance for Cluster instance;
  da = ((c / H0) * angdidis(z, Omega_M, Omega_L));
}

void Cluster::assign_props () {
  // Assign properties to Cluster instance.
  double sum = 0.0;
  std::vector<double> g_ra, g_dec, g_z;
  ngal = mem.size();
  if(ngal > 0) {
    for(int i = 0; i < ngal; i++) {
      g_ra.push_back(mem[i].ra);
      g_dec.push_back(mem[i].dec);
      g_z.push_back(mem[i].z);
    }
    ra = astro.median(g_ra);
    dec = astro.median(g_dec);
    z = astro.median(g_z);
    ra_err = astro.stderr_median(g_ra);
    dec_err = astro.stderr_median(g_dec);
    z_err = astro.stderr_median(g_z);
    for(int i = 0; i < ngal; i++)
      sum += astro.rad2deg(astro.angsep(ra, dec, g_ra[i], g_dec[i]));
    size = (sum * 60) / double(ngal);
    area = M_PI * pow(size, 2);
  }
}

void Cluster::assign_sn (double bg_expect) {
  // Assign singal-to-noise to Cluster instance
  // given the expected background counts.
  if(bg_expect == 0) 
    sn = -1.0;
  else
    sn = double(ngal) / pow((area * bg_expect), 0.5);
}

void Cluster::clear () {
  // Clear all members from Cluster instance.
  mem.clear();
}

void Cluster::rename (int num_val) {
  // Reset Cluster instance number.
  num = num_val;
}

void Cluster::unique () {
  // Remove duplicate elements from a cluster instance.
  std::sort(mem.begin(), mem.end());
  mem.erase(std::unique(mem.begin(), mem.end()), mem.end()); 
}

