/*Class header for Cat_Split*/

#ifndef CAT_SPLIT_H
#define CAT_SPLIT_H

#include <fstream>
#include <iomanip>
#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
#include <vector>

#include "comp.hpp"
#include "fileio_class.hpp"
#include "option_class.hpp"

class Cat_Split { //! Class for Cat_Split functions
private:
  Fileio fileio;
  Option opt;
  int number_of_files;
  double ra_bin_size, dec_bin_size;
  std::vector<std::ofstream*> file_list;
public:
  Comp comp;
  void read_options (int, char *[]);
  void set_up ();
  void open_files ();
  void close_files ();
  void find_bin (double, double, std::vector<int> &);
  void read_ascii ();
};

#endif /* CAT_SPLIT_H */
