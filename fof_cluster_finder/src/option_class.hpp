/**
 * @file option_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef OPTION_CLASS_H
#define OPTION_CLASS_H

/**
 * @class Option
 *
 * @brief Class for reading code options.
 *
 * This class reads the code options as arguments or from a
 * parameter file.
 */

#include <iostream> 
#include <getopt.h>
#include "fileio_class.hpp"

class Option { // Class for code options

public:

  /// Maximum depth to which the Kdtree instance should be built.
  int kdtree_depth;

  /// Minimum number of member Galaxy instances required to form a 
  /// Cluster instance.
  int min_ngal;

  /// Number of bins in right ascension.
  int n_ra_bins;

  /// Number of bins in declination.
  int n_dec_bins;

  /// Transverse linking parameter.
  double link_r;

  /// Line-of-sight linking parameter.
  double link_z;

  /// Redshift bin size.
  double z_bin_size;

  /// Minimum redshift allowed.
  double z_min; 

  /// Maximum redshift allowed.
  double z_max;

  /// Expected background number density [n_gal / arcmin^2].
  double bg_expect;

  /// Reference redshift for calculations.
  double z_ref;

  /// Maxmimum photometric redshift error allowed.
  double dz_max;

  /// Speed of light [km/s].
  double c;

  /// Hubble parameter [km/s/Mpc].
  double H0;

  /// Matter density.
  double omega_m;

  /// Dark energy density.
  double omega_l;

  /// Minimum right ascension of range.
  double ra_lower;

  /// Maximum right ascension of range.
  double ra_upper;

  /// Minimum declination of range.
  double dec_lower;

  /// Maximum declination of range.
  double dec_upper;

  /// Overlap in right ascension.
  double ra_overlap;

  /// Overlap in declination.
  double dec_overlap;

  /// Input file name.
  std::string input_file;
  
  /// Output file name.
  std::string output_file;

  /// Option to print Zbin data ["yes"/"no"].
  std::string print_bin_data;

  /// Input mode ["ascii"/"fits"].
  std::string input_mode;

  /// Output mode ["ascii"/"fits"].
  std::string output_mode;

  /// FoF mode ["spec"/"phot"].
  std::string fof_mode;

  /// FoF linking mode ["dynamic"/"fixed"].
  std::string link_mode;

  /**
   * This method reads options provided as arguments for Main.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   * @param[in] version_number Code version number.
   */
  void read_opts (int, char *[], double);

  /**
   * This method reads options provided as arguments for Cat_Merge.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   * @param[in] version_number Code version number.
   */
  void read_merge_opts (int, char *[], double);

  /**
   * This method reads options provided as arguments for Cat_Split.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   * @param[in] version_number Code version number.
   */
  void read_split_opts (int, char *[], double);

  /**
   * This method reads options provided in a parameter file for Main.
   * @param[in] file_name Parameter file name.
   */
  void read_param_file (const std::string &);

private:

  /// Include Fileio class.
  Fileio fileio;

  /**
   * This method prints help information for Main.
   */
  void help();

  /**
   * This method prints help information for Cat_Merge.
   */
  void merge_help();

  /**
   * This method prints help information for Cat_Split.
   */
  void split_help();

  /**
   * This method prints the code version number.
   */
  void version(double);

};

#endif /* OPTION_CLASS_H */
