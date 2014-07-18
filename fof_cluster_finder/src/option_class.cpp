/*Class for code options*/

#include "option_class.hpp"

void Option::help() {
  // Function that prints help information.
  std::cout<<"Help!"<<std::endl;
  exit(0);
}

void Option::merge_help() {
  // Function that prints help information.
  std::cout<<"Merge Help!"<<std::endl;
  exit(0);
}

void Option::split_help() {
  // Function that prints help information.
  std::cout<<"Split Help!"<<std::endl;
  exit(0);
}

void Option::version(double version_number) {
  // Function that prints current code version.
  std::cout<<"Version: "<<std::fixed<<std::setprecision(1)
	   <<version_number<<std::endl;
  exit(0);
}

void Option::read_opts(int argc, char *argv[], double version_number) {
  // Function that reads code arguments.
  int index = 0, opt = 0;
  const char *option_tags;
  option_tags = "hvf:t:i:o:l:p:r:z:k:n:a:b:s:d:g:c:e:m:q:j:";
  const struct option longopts[] = {
      {"help", no_argument, 0, 'h'},
      {"version", no_argument, 0, 'v'},
      {"input_file", required_argument, 0, 'f'},
      {"fof_mode", required_argument, 0, 't'},
      {"input_mode", required_argument, 0, 'i'},
      {"output_mode", required_argument, 0, 'o'},
      {"link_mode", required_argument, 0, 'l'},
      {"print_bin_data", required_argument, 0, 'p'},
      {"link_r", required_argument, 0, 'r'},
      {"link_z", required_argument, 0, 'z'},
      {"kdtree_depth", required_argument, 0, 'k'},
      {"min_ngal", required_argument, 0, 'n'},
      {"z_min", required_argument, 0, 'a'},
      {"z_max", required_argument, 0, 'b'},
      {"z_bin_size", required_argument, 0, 's'},
      {"z_ref", required_argument, 0, 'd'},
      {"dz_max", required_argument, 0, 'g'},
      {"c", required_argument, 0, 'c'},
      {"H0", required_argument, 0, 'e'},
      {"omega_m", required_argument, 0, 'm'},
      {"omega_l", required_argument, 0, 'q'},
      {"bg_expect", required_argument, 0, 'p'},
      {0, 0, 0, 0}
    };  
  while(opt != -1) {
    opt = getopt_long(argc, argv, option_tags, longopts, &index);
    switch (opt) {
    case 'h': help();
      break;
    case 'v': version(version_number);
      break;
    case 'f': input_file = optarg;
      break;
    case 't': fof_mode = optarg;
      break;
    case 'i': input_mode = optarg;
      break;
    case 'o': output_mode = optarg;
      break;
    case 'r': link_r = atof(optarg);
      break;
    case 'z': link_z = atof(optarg);
      break;
    case 'k': kdtree_depth = atoi(optarg);
      break;
    case 'n': min_ngal = atoi(optarg);
      break;
    case 'a': z_min = atof(optarg);
      break;
    case 'b': z_max = atof(optarg);
      break;
    case 's': z_bin_size = atof(optarg);
      break;
    case 'd': z_ref = atof(optarg);
      break;
    case 'g': dz_max = atof(optarg);
      break;
    case 'c': c = atof(optarg);
      break;
    case 'e': H0 = atof(optarg);
      break;
    case 'm': omega_m = atof(optarg);
      break;
    case 'l': omega_l = atof(optarg);
      break;
    case 'p': bg_expect = atof(optarg);
      break;
    }
  }
}

void Option::read_merge_opts(int argc, char *argv[], double version_number) {
  // Function that reads code arguments.
  //**SET DEFUALTS **//
  input_mode = "fits";
  output_mode = "fits";
  output_file = "cat_merge_output";
  bg_expect = 0;
  //*****************//
  int index = 0, opt = 0;
  const char *option_tags;
  option_tags = "hvf:d:i:o:b:";
  const struct option longopts[] = {
      {"help", no_argument, 0, 'h'},
      {"version", no_argument, 0, 'v'},
      {"input_file", required_argument, 0, 'f'},
      {"output_file", required_argument, 0, 'd'},
      {"input_mode", required_argument, 0, 'i'},
      {"output_mode", required_argument, 0, 'o'},
      {"bg_expect", required_argument, 0, 'b'},
      {0, 0, 0, 0}
    };  
  while(opt != -1) {
    opt = getopt_long(argc, argv, option_tags, longopts, &index);
    switch (opt) {
    case 'h': merge_help();
      break;
    case 'v': version(version_number);
      break;
    case 'f': input_file = optarg;
      break;
    case 'd': output_file = optarg;
      break;
    case 'i': input_mode = optarg;
      break;
    case 'o': output_mode = optarg;
      break;
    case 'b': bg_expect = atof(optarg);
      break;
    }
  }
}

void Option::read_split_opts(int argc, char *argv[], double version_number) {
  // Function that reads code arguments.
  //**SET DEFUALTS **//
  ra_overlap = 0.5;
  dec_overlap = 0.5;
  //*****************//
  int index = 0, opt = 0;
  const char *option_tags;
  option_tags = "hvf:a:b:c:e:g:i:r:d:";
  const struct option longopts[] = {
      {"help", no_argument, 0, 'h'},
      {"version", no_argument, 0, 'v'},
      {"input_file", required_argument, 0, 'f'},
      {"ra_lower", required_argument, 0, 'a'},
      {"ra_upper", required_argument, 0, 'b'},
      {"dec_lower", required_argument, 0, 'c'},
      {"dec_upper", required_argument, 0, 'e'},
      {"ra_overlap", required_argument, 0, 'g'},
      {"dec_overlap", required_argument, 0, 'i'},
      {"n_ra_bins", required_argument, 0, 'r'},
      {"n_dec_bins", required_argument, 0, 'd'},
      {0, 0, 0, 0}
    };  
  while(opt != -1) {
    opt = getopt_long(argc, argv, option_tags, longopts, &index);
    switch (opt) {
    case 'h': split_help();
      break;
    case 'v': version(version_number);
      break;
    case 'f': input_file = optarg;
      break;
    case 'a': ra_lower = atof(optarg);
      break;
    case 'b': ra_upper = atof(optarg);
      break;
    case 'c': dec_lower = atof(optarg);
      break;
    case 'e': dec_upper = atof(optarg);
      break;
    case 'g': ra_overlap = atof(optarg);
      break;
    case 'i': dec_overlap = atof(optarg);
      break;
    case 'r': n_ra_bins = atoi(optarg);
      break;
    case 'd': n_dec_bins = atoi(optarg);
      break;
    }
  }
}

void Option::read_param_file(const std::string &file_name) {
  // Function to read parameter file values.
  //**SET DEFUALTS **//
  fof_mode = "phot";
  input_mode = "fits";
  output_mode = "fits";
  link_mode = "dynamic";
  print_bin_data = "no";
  z_min = 0.0;
  z_max = 3.0;
  dz_max = 0.06;
  z_bin_size = 0.01;
  z_ref = 0.5;
  c = 2.997e5;
  H0 = 100;
  omega_m = 0.3;
  omega_l = 0.7;
  bg_expect = 0;
  //*****************//
  std::string line; /* line string */
  std::vector<std::string> values; /* values vector */
  std::ifstream read_file(file_name.c_str()); /* open file */
  if(read_file.good()){ /* make sure file exits */
    std::cout<<"Reading Parameter Values from: "<<file_name<<std::endl;
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
	if(values[0] == "link_mode") link_mode = values[1];
	if(values[0] == "print_bin_data") print_bin_data = values[1];
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
