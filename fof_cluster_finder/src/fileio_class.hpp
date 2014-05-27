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
  std::string cluster_file_name, member_file_name;
public:
  void split (const std::string &, std::vector<std::string> &, 
	      const std::string &);
  void read_ascii (const std::string &, const std::string &, 
		   std::vector<Galaxy> &);
  void read_fits (const std::string &, const std::string &, 
		  std::vector<Galaxy> &);
  void output_file_names (const std::string &, const std::string &,
			  const std::string &, double, double);
  void write_ascii (const std::vector<Cluster> &);
  void write_fits (const std::vector<Cluster> &);
};

#endif /* FILEIO_CLASS_H */
