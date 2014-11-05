/**
 * @file cat_merge_fileio.hpp
 *
 * @author Samuel Farrens
 */

#ifndef MERGE_FILEIO_CLASS_H
#define MERGE_FILEIO_CLASS_H

/**
 * @class Merge_Fileio
 *
 * @brief Class for reading files for Cat_Merge.
 *
 * This class handles the file input for Cat_Merge.
 */

#include <fitsio.h> //*Include FITSIO packages*//

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "galaxy_class.hpp"
#include "cluster_class.hpp"
#include "fileio_class.hpp"

class Merge_Fileio { // Class structure for file input and output

public:

  /// Map of Galaxy instances.
  typedef std::map<unsigned long, Galaxy> gal_container;

  /**
   * This method checks to see if a Cluster instance ID already exists.
   * @param[in] id ID of Cluster instance.
   * @param[in] list Vector of Cluster instance IDs.
   */
  bool existing_clt (int, const std::vector<int> &);

  /**
   * This method reads in the list containing the input file names.
   * @param[in] list File name containing the list of input file names.
   * @param[out] cluster_list Vector of Cluster instances.
   * @param[in] input_mode Input mode ["ascii"/"fits"].
   */
  void read_file_list (const std::string &, std::vector<Cluster> &, gal_container&,
		       const std::string &);

  /**
   * This method reads in an ASCII file and store the contents in a vector 
   * of Cluster instances.
   * @param[in] fname Input file name.
   * @param[out] cluster_list Vector of Cluster instances.
   */
  void read_ascii (const std::string &, std::vector<Cluster> &, gal_container&);

  /**
   * This method reads in an FITS file and store the contents in a vector 
   * of Cluster instances.
   * @param[in] fname Input file name.
   * @param[out] cluster_list Vector of Cluster instances.
   */
  void read_fits (const std::string &, std::vector<Cluster> &, gal_container&);

  /**
   * This method sets the output file names.
   * @param[in] output Output file name.
   * @param[in] output_mode Ouput mode ["ascii"/"fits"].
   * @param[out] cluster_file_name Output Cluster list file name.
   * @param[out] member_file_name Output member Galaxy list file name.
   */
  void output_file_names (const std::string &, const std::string &, 
			  std::string &, std::string &);

  /**
   * This reads backround data.
   * @param[in] background data file name.
   * @param[out] Spline instance.
   */
  void read_bg_data (const std::string &, std::vector<double> &, std::vector<double> &);

private:
  
  /// Include Fileio class.
  Fileio fileio;

  /// Current number of Galaxy instances.
  int gal_count;

  /// Current number of Cluster instances.
  int clt_count;

  /// Vector of file names.
  std::vector<std::string> file_list;
  
};

#endif // MERGE_FILEIO_CLASS_H
