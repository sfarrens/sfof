/*Class header for Option*/

#ifndef OPTION_CLASS_H
#define OPTION_CLASS_H

#include <iostream> 
#include <getopt.h>
#include "fileio_class.hpp"

class Option { //! Class for code options
private:
  Fileio fileio;
  void help();
  void version(double);
public:
  int kdtree_depth, min_ngal, n_ra_bins, n_dec_bins;
  double link_r, link_z, z_bin_size, z_min, z_max;
  double z_ref, dz_max, c, H0, omega_m, omega_l;
  double ra_lower, ra_upper, dec_lower, dec_upper;
  double ra_overlap, dec_overlap;
  std::string input_file, output_file, fof_mode;
  std::string input_mode, output_mode;
  void read_opts (int, char *[], double);
  void read_merge_opts (int, char *[], double);
  void read_split_opts (int, char *[], double);
  void read_param_file (const std::string &);
};

#endif /* OPTION_CLASS_H */
