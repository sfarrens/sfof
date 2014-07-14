/*Class header for Abs_Mag*/

#ifndef FIND_RICH_H
#define FIND_RICH_H

#include <math.h>

#include "dh.h"
#include "astro.hpp"
#include "cluster_class.hpp"
#include "comp.hpp"
#include "fileio_class.hpp"
#include "galaxy_class.hpp"
#include "option_class.hpp"
#include "spline.h"

class Find_Rich { //! Class for Find_Rich functions
private:
  Astro astro;
  Fileio fileio;
  Option opt;
  double c, H0, Omega_M, Omega_L, M_star, radial_threshold, lum_frac;
  std::vector<double> ms_z, ms_mag;
  std::vector<Cluster> clusters;
public:
  Comp comp;
  void set_const (double, double);
  void read_mstar_vals (const std::string &);
  void read_clusters (const std::string &);
  double abs_mag (double, double);
  double get_mstar (double);
  bool check_mag (double, double);
  void check_radius (const Galaxy &);
  void read_ascii (const std::string &);
  void assign_cluster_props();
  void write_files();
};

#endif /* FIND_RICH_H */
