/**
 * @file fileio_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef FILEIO_CLASS_H
#define FILEIO_CLASS_H

/**
 * @class Fileio
 *
 * @brief Class for file input and output.
 *
 * This class contains functions for reading and writing ASCII and
 * FITS files.
 */

#include <fitsio.h> //*Include FITSIO packages*//

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include "astro.hpp"
#include "cluster_class.hpp"
#include "galaxy_class.hpp"
#include "zbin_class.hpp"

class Fileio { // Class structure for file input and output

public:
 
  /**
   * This method sets the column numbers where galaxy properties are
   * stored in the input file. [Spectroscopic mode]
   * @param[in] id_col_val Column number for galaxy ID.
   * @param[in] ra_col_val Column number for galaxy right ascension.
   * @param[in] dec_col_val Column number for galaxy declination.
   * @param[in] z_col_val Column number for galaxy spectroscopic redshift.
   */
  void set_up (int, int, int, int);

  /**
   * This method sets the column numbers where galaxy properties are
   * stored in the input file. [Photometric mode]
   * @param[in] id_col_val Column number for galaxy ID.
   * @param[in] ra_col_val Column number for galaxy right ascension.
   * @param[in] dec_col_val Column number for galaxy declination.
   * @param[in] z_col_val Column number for galaxy photometric redshift.
   * @param[in] dz_col_val Column number for galaxy photometric redshift error.
   */
  void set_up (int, int, int, int, int);

  /**
   * This method splits a string into columns.
   * @param[in] str String.
   * @param[out] tokens Vector of column data.
   * @param[in] delimiter Column delimiter.
   */
  void split (const std::string &, std::vector<std::string> &, 
	      const std::string &);

  /**
   * This method reads in an ASCII file and store the contents in a vector 
   * of Galaxy instances.
   * @param[in] fname Input file name.
   * @param[in] mode FoF mode ["spec"/"phot"].
   * @param[in] z_min Minimum redshift allowed.
   * @param[in] z_max Maximum redshift allowed.
   * @param[in] dz_max Maximum photometric redshift error allowed.
   * @param[out] gals Vector of Galaxy instances.
   */
  void read_ascii (const std::string &, const std::string &, double, 
		   double, double, std::vector<Galaxy> &);

  /**
   * This method reads in a FITS file and store the contents in a vector of
   * Galaxy instances.
   * @param[in] fname Input file name.
   * @param[in] mode FoF mode ["spec"/"phot"].
   * @param[in] z_min Minimum redshift allowed.
   * @param[in] z_max Maximum redshift allowed.
   * @param[in] dz_max Maximum photometric redshift error allowed.
   * @param[out] gals Vector of Galaxy instances.
   */
  void read_fits (const std::string &, const std::string &, double, 
		  double, double, std::vector<Galaxy> &);

  /**
   * This method sets the cluster output file name.
   * @param[in] fname Input file name.
   * @param[in] mode FoF mode ["spec"/"phot"].
   * @param[in] output Ouput mode ["ascii"/"fits"].
   * @param[in] link_r Transverse linking parameter value.
   * @param[in] link_z Line-of-sight linking parameter value.
   * @param[out] cluster_file_name Output Cluster list file name.
   */
  void output_cluster_name (const std::string &, const std::string &,
			    const std::string &, double, double, 
			    std::string &);

  /**
   * This method sets the member output file name.
   * @param[in] fname Input file name.
   * @param[in] mode FoF mode ["spec"/"phot"].
   * @param[in] output Ouput mode ["ascii"/"fits"].
   * @param[in] link_r Transverse linking parameter value.
   * @param[in] link_z Line-of-sight linking parameter value.
   * @param[out] member_file_name Output member Galaxy list file name.
   */
  void output_member_name (const std::string &, const std::string &,
			   const std::string &, double, double, 
			   std::string &);

  /**
   * This method writes a list of the specified Cluster instances and a list 
   * of the corresponding member Galaxy instances to two ASCII files.
   * @param[in] cluster_list Vector of Cluster instances.
   * @param[in] cluster_file_name Output Cluster list file name.
   * @param[in] member_file_name Output member Galaxy list file name.
   */
  void write_ascii (const std::vector<Cluster> &, const std::string &, 
		    const std::string &);

  /**
   * This method writes a list of the specified Cluster instances and a list 
   * of the corresponding member Galaxy instances to two FITS files.
   * @param[in] cluster_list Vector of Cluster instances.
   * @param[in] cluster_file_name Output Cluster list file name.
   * @param[in] member_file_name Output member Galaxy list file name.
   */
  void write_fits (const std::vector<Cluster> &, const std::string &, 
		   const std::string &);

private:

  /// Column number for galaxy ID.
  int id_col;

  /// Column number for galaxy right ascension.
  int ra_col;
  
  /// Column number for galaxy declination.
  int dec_col;
  
  ///Column number for galaxy redshift.
  int z_col;

  /// Column number for galaxy photometric redshift error.
  int dz_col;

};

#endif // FILEIO_CLASS_H
