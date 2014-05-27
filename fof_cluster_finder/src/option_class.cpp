/*Class for code options*/

#include "option_class.hpp"

void Option::help() {
  //! Function that prints help information.
  std::cout<<"Help!\n"<<std::flush;
  exit(0);
}

void Option::version() {
  //! Function that prints current code version.
  std::cout<<"Version: 3.0\n"<<std::flush;
}

void Option::read_opts(int argc, char *argv[]) {
  //! Function that reads code arguments.
  int index, iarg = 0;
  const char *option_tags;
  option_tags = "hv:f:t:i:o:r:z:k:n:a:b:s:d:c:e:m:l:";
  const struct option longopts[] = {
      {"help", no_argument, 0, 'h'},
      {"version", no_argument, 0, 'v'},
      {"input_file", required_argument, 0, 'f'},
      {"fof_mode", required_argument, 0, 't'},
      {"input_mode", required_argument, 0, 'i'},
      {"output_mode", required_argument, 0, 'o'},
      {"link_r", required_argument, 0, 'r'},
      {"link_z", required_argument, 0, 'z'},
      {"kdtree_depth", required_argument, 0, 'k'},
      {"min_ngal", required_argument, 0, 'n'},
      {"z_min", required_argument, 0, 'a'},
      {"z_max", required_argument, 0, 'b'},
      {"z_bin_size", required_argument, 0, 's'},
      {"z_ref", required_argument, 0, 'd'},
      {"c", required_argument, 0, 'c'},
      {"H0", required_argument, 0, 'e'},
      {"omega_m", required_argument, 0, 'm'},
      {"omega_l", required_argument, 0, 'l'},
      {0, 0, 0, 0},
    };  
  while(iarg != -1) {
    iarg = getopt_long(argc, argv, option_tags, longopts, &index);
    switch (iarg) {
    case 'h':
      help();
    case 'v':
      version();
    case 'f':
      input_file = optarg;
    case 't':
      fof_mode = optarg;
    case 'i':
      input_mode = optarg;
    case 'o':
      output_mode = optarg;
    case 'r':
      link_r = atof(optarg);
    case 'z':
      link_z = atof(optarg);
    case 'k':
      kdtree_depth = atoi(optarg);
    case 'n':
      min_ngal = atoi(optarg);
    case 'a':
      z_min = atof(optarg);
    case 'b':
      z_max = atof(optarg);
    case 's':
      z_bin_size = atof(optarg);
    case 'd':
      z_ref = atof(optarg);
    case 'c':
      c = atof(optarg);
    case 'e':
      H0 = atof(optarg);
    case 'm':
      omega_m = atof(optarg);
    case 'l':
      omega_l = atof(optarg);
    }
  }
}

void Option::read_param_file(const std::string &file_name) {
  //! Function to read parameter file values.
  std::string line; /* line string */
  std::vector<std::string> values; /* values vector */
  std::ifstream read_file(file_name.c_str()); /* open file */
  if(read_file.good()){ /* make sure file exits */
    std::cout<<"Reading Parameter Values from: "<<file_name<<"\n"<<std::flush;
    while(!read_file.eof()) { /* while not the end of the file */
      std::getline(read_file, line);
      if(line.length() >= 1 && 
	 line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
	values.clear();
	fileio.split(line, values, " "); /* split line into values */
	if(values[0] == "input_file") input_file = values[1];
	if(values[0] == "fof_mode") fof_mode = values[1];
	if(values[0] == "input_mode") input_mode = values[1];
	if(values[0] == "output_mode") output_mode = values[1];
	if(values[0] == "link_r") link_r = atof(values[1].c_str());
	if(values[0] == "link_z") link_z = atof(values[1].c_str());
	if(values[0] == "kdtree_depth") kdtree_depth = atoi(values[1].c_str());
	if(values[0] == "min_ngal") min_ngal = atoi(values[1].c_str());
	if(values[0] == "z_min") z_min = atof(values[1].c_str());
	if(values[0] == "z_max") z_max = atof(values[1].c_str());
	if(values[0] == "z_bin_size") z_bin_size = atof(values[1].c_str());
	if(values[0] == "z_ref") z_ref = atof(values[1].c_str());
	if(values[0] == "c") c = atof(values[1].c_str());
	if(values[0] == "H0") H0 = atof(values[1].c_str());
	if(values[0] == "omega_m") omega_m = atof(values[1].c_str());
	if(values[0] == "omega_l") omega_l = atof(values[1].c_str());
      }
    }
  }
}
