/*Class header for Fileio*/

#ifndef MERGE_FILEIO_CLASS_H
#define MERGE_FILEIO_CLASS_H

#include <fitsio.h> //*Include FITSIO packages*//

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "cluster_class.hpp"
#include "fileio_class.hpp"

class Merge_Fileio { //! Class structure for file input and output
private:
  Fileio fileio;
  int gal_count, clt_count;
  std::vector<std::string> file_list;
public:
  void split (const std::string &, std::vector<std::string> &, 
	      const std::string &);
  bool existing_clt (int, const std::vector<int> &);
  void read_file_list (const std::string &, std::vector<Cluster> &, 
		       const std::string &);
  void read_ascii (const std::string &, std::vector<Cluster> &);
  void read_fits (const std::string &, std::vector<Cluster> &);
  void output_file_names (const std::string &, const std::string &, 
			  std::string &, std::string &);
};

#endif /* MERGE_FILEIO_CLASS_H */
