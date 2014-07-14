/*Class header for Fileio*/

#ifndef FILEIO_CLASS_H
#define FILEIO_CLASS_H

#include <fitsio.h> //*Include FITSIO packages*//

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "astro.hpp"
#include "cluster_class.hpp"
#include "galaxy_class.hpp"
#include "zbin_class.hpp"

class Fileio { //! Class structure for file input and output
private:
  int num_col, id_col, ra_col, dec_col, z_col, dz_col;
public:
  void set_up (int, int, int, int);
  void set_up (int, int, int, int, int);
  void split (const std::string &, std::vector<std::string> &, 
	      const std::string &);
  void read_ascii (const std::string &, const std::string &, double, 
		   double, double, std::vector<Galaxy> &);
  void read_fits (const std::string &, const std::string &, double, 
		  double, double, std::vector<Galaxy> &);
  void output_file_names (const std::string &, const std::string &,
			  const std::string &, double, double, 
			  std::string &, std::string &);
  void write_ascii (const std::vector<Cluster> &, const std::string &, 
		    const std::string &);
  void write_fits (const std::vector<Cluster> &, const std::string &, 
		   const std::string &);
};

#endif /* FILEIO_CLASS_H */
