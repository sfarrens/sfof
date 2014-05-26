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
  void version();
public:
  int kdtree_depth, min_ngal;
  double link_r, link_z, z_bin_size, z_min, z_max;
  double z_ref, c, H0, omega_m, omega_l;
  std::string input_file, fof_mode;
  std::string input_mode, output_mode;
  void read_opts (int, char *[]);
  void read_param_file (const std::string &);
};

#endif /* OPTION_CLASS_H */
