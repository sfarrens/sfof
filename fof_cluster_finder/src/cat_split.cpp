#include "cat_split.hpp"

void Cat_Split::read_options (int argc, char *argv[]) {
  //! Function to read code options.
  double version_number = 1.0;
  opt.read_split_opts(argc, argv, version_number);
}

void Cat_Split::set_up () {
  number_of_files = opt.n_ra_bins * opt.n_dec_bins;
  ra_bin_size = ((opt.ra_upper - opt.ra_lower) / opt.n_ra_bins);
  dec_bin_size = ((opt.dec_upper - opt.dec_lower) / opt.n_dec_bins);
}

void Cat_Split::open_files () {
  std::stringstream file_name;
  for(int i = 0; i < number_of_files; i++) {
    file_name<<"piece_"<<std::setw(2)<<std::setfill('0')<<i;
    file_list.push_back(new std::ofstream (file_name.str().c_str()));
    file_name.str("");
  }
}

void Cat_Split::close_files () {
  for(int i = 0; i < number_of_files; i++)
    file_list[i] -> close();
}

void Cat_Split::find_bin (double ra, double dec, std::vector<int> &bins) {
  double ra_bin_low = (fabs(ra - opt.ra_lower) / ra_bin_size) - opt.ra_overlap / ra_bin_size;
  double ra_bin_up = (fabs(ra - opt.ra_lower) / ra_bin_size);
  double dec_bin_low = (fabs(dec - opt.dec_lower) / dec_bin_size) - opt.dec_overlap / dec_bin_size;
  double dec_bin_up = (fabs(dec - opt.dec_lower) / dec_bin_size);
  bins.push_back(int(ra_bin_low) + int(dec_bin_low) * opt.n_ra_bins);
  bins.push_back(int(ra_bin_up) + int(dec_bin_low) * opt.n_ra_bins);
  bins.push_back(int(ra_bin_low) + int(dec_bin_up) * opt.n_ra_bins);
  bins.push_back(int(ra_bin_up) + int(dec_bin_up) * opt.n_ra_bins);
  std::sort(bins.begin(), bins.end());
  bins.erase(std::unique(bins.begin(), bins.end()), bins.end()); 
}

void Cat_Split::read_ascii () { 
  //! Function to read in an ASCII file and store the contents in a vector of Galaxy instances.
  double ra, dec;
  std::string line;
  std::vector<int> bins;
  std::vector<std::string> cols; 
  std::ifstream read_file(opt.input_file.c_str()); /* open file */
  while(!read_file.eof()) { /* while not the end of the file */
    std::getline(read_file, line); /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      ra = atof(cols[1].c_str());
      dec = atof(cols[2].c_str());
      find_bin(ra, dec, bins);
      for(int i = 0; i < bins.size(); i++) {
	*file_list[bins[i]]<<line<<std::endl;
      }
      cols.clear();
      bins.clear();
    }
  }
}

int main (int argc, char *argv[]) {
  Cat_Split run_code;
  run_code.comp.start_time();
  run_code.read_options(argc, argv);
  run_code.set_up();
  run_code.open_files();
  run_code.read_ascii();
  run_code.close_files();
  run_code.comp.end_time();
  run_code.comp.print_time();
}
