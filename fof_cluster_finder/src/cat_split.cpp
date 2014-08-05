#include "cat_split.hpp"
#include "exceptions.hpp"

void Cat_Split::read_options (int argc, char *argv[]) {
  // Function to read code options.
  double version_number = 1.0;
  opt.read_split_opts(argc, argv, version_number);
}

void Cat_Split::set_up () {
  if (opt.ra_upper <= 0 || opt.ra_upper > 360)
    throw RuntimeException("Cat_Split::set_up", "opt.ra_upper", "in the range 0.0 < opt.ra_upper <= 360.0");
  if (opt.ra_lower < 0 || opt.ra_lower >= 360)
    throw RuntimeException("Cat_Split::set_up", "opt.ra_lower", "in the range 0.0 <= opt.ra_lower < 360.0");
  if (opt.ra_lower > opt.ra_upper)
    throw RuntimeException("Cat_Split::set_up", "opt.ra_lower", "< opt.ra_upper");
  if (opt.dec_upper <= -90 || opt.dec_upper > 90)
    throw RuntimeException("Cat_Split::set_up", "opt.dec_upper", "in the range -90.0 < opt.ra_upper <= 90.0");
  if (opt.dec_lower < -90 || opt.dec_lower >= 90)
    throw RuntimeException("Cat_Split::set_up", "opt.dec_lower", "in the range -90.0 <= opt.ra_lower < 90.0");
  if (opt.dec_lower > opt.dec_upper)
    throw RuntimeException("Cat_Split::set_up", "opt.dec_lower", "< opt.dec_upper");
  if (opt.ra_overlap <= 0.0)
    throw RuntimeException("Cat_Split::set_up", "opt.ra_overlap", "> 0.0");
  if (opt.dec_overlap <= 0.0)
    throw RuntimeException("Cat_Split::set_up", "opt.dec_overlap", "> 0.0");
  if (opt.n_procs == 0) {
    if (opt.n_ra_bins <= 0)
      throw RuntimeException("Cat_Split::set_up", "opt.n_ra_bins", "> 0");
    if (opt.n_dec_bins <= 0)
      throw RuntimeException("Cat_Split::set_up", "opt.n_dec_bins", "> 0");
    number_of_files = opt.n_ra_bins * opt.n_dec_bins;
    ra_bin_size = ((opt.ra_upper - opt.ra_lower) / opt.n_ra_bins);
    dec_bin_size = ((opt.dec_upper - opt.dec_lower) / opt.n_dec_bins);
  }
  else {
    if (opt.n_procs < 1)
      throw RuntimeException("Cat_Split::set_up", "opt.n_procs", "> 1");
    number_of_files = opt.n_procs;
    ra_bin_size = pow(((opt.ra_upper - opt.ra_lower) * (opt.dec_upper - opt.dec_lower)) / double(number_of_files), 0.5);
    opt.n_ra_bins = int(ceil((opt.ra_upper - opt.ra_lower) / ra_bin_size));
    ra_bin_size = ((opt.ra_upper - opt.ra_lower) / opt.n_ra_bins);
    opt.n_dec_bins = int(double(number_of_files) / double(opt.n_ra_bins));
    dec_bin_size = ((opt.dec_upper - opt.dec_lower) / opt.n_dec_bins);
  }
  std::cout<<"Number of bins in RA: "<<opt.n_ra_bins<<std::endl;
  std::cout<<"Number of bins in Dec: "<<opt.n_dec_bins<<std::endl;
  std::cout<<"Bin size in RA: "<<ra_bin_size<<std::endl;
  std::cout<<"Bin size in Dec: "<<dec_bin_size<<std::endl;
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
  double ra, dec;
  std::string line;
  std::vector<int> bins; std::vector<std::string> cols; 
  std::ifstream read_file(opt.input_file.c_str()); /* open file */
  if(read_file.good()) 
    while(std::getline(read_file, line)) { /* read each line */
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
  else
    throw RuntimeException("Cat_Split::set_up", "opt.input_file", "be valid");
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
