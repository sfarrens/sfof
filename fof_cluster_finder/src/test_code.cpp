#include "fileio_class.hpp"
#include "option_class.hpp"

#include <iostream>
#include <sstream>

int main (int argc, char *argv[]) {
  
  Option opt;
  std::string param_file_name = "param_file.ini";
  opt.read_param_file(param_file_name);
  opt.read_opts(argc, argv);
  std::cout<<opt.omega_l<<"\n"<<std::flush;

}
