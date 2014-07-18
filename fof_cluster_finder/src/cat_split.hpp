/**
 * @file cat_split.hpp
 *
 * @author Samuel Farrens
 */

#ifndef CAT_SPLIT_H
#define CAT_SPLIT_H

/**
 * @class Cat_Split
 *
 * @brief Class for splitting galaxy catalogues.
 *
 * This class splits a catalogue of galaxies into overlapping 
 * pieces.
 */

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

class Cat_Split { // Class for Cat_Split functions

public:

  /// Include Comp class.
  Comp comp;

  /**
   * This method calls Option to read the code options from the 
   * provided arguments.
   * @param[in] argc Argument count.
   * @param[in] argv Argument vector.
   */
  void read_options (int, char *[]);

  /**
   * This method sets up the of split files.
   */
  void set_up ();

  /**
   * This method opens all of the split files.
   */
  void open_files ();

  /**
   * This method closes all of the split files.
   */
  void close_files ();
  
  /**
   * This method determines to which split file a given galaxy
   * should be written.
   * @param[in] ra Right ascension of galaxy.
   * @param[in] dec Declination of galaxy.
   * @param[in] bins Vector of split file numbers.
   */
  void find_bin (double, double, std::vector<int> &);

  /**
   * This method reads the galaxies from the input catalogues and
   * writes them to the corresponding split files.
   */
  void read_ascii ();

private:

  /// Include Fileio class.
  Fileio fileio;

  /// Include Option class.
  Option opt;

  /// Number of files to which split data will be written.
  int number_of_files;

  /// Range in right ascension covered by each split file.
  double ra_bin_size;
  
  /// Range in declination covered by each split file.
  double dec_bin_size;

  /// Vector of output file pointers.
  std::vector<std::ofstream*> file_list;

};

#endif // CAT_SPLIT_H
