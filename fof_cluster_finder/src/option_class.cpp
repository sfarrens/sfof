/*Class for code options*/

#include "option_class.hpp"
#include <iostream> 
#include <boost/program_options.hpp>
namespace po = boost::program_options;

void Option::version(double version_number) {
  // Function that prints current code version.
  std::cout<<"Version: "<<std::fixed<<std::setprecision(1)
	   <<version_number<<std::endl;
  exit(0);
}

void Option::print_parameters() {
  // Function that prints current code parameter values.
  std::cout<<"Code Parameters:"<<std::endl;
  std::cout<<" - input_file = "<<input_file<<std::endl;
  std::cout<<" - output_clusters = "<<output_clusters<<std::endl;
  std::cout<<" - output_members = "<<output_members<<std::endl;
  std::cout<<" - input_mode = "<<input_mode<<std::endl;
  std::cout<<" - output_mode = "<<output_mode<<std::endl;
  std::cout<<" - fof_mode = "<<fof_mode<<std::endl;
  std::cout<<" - link_mode = "<<link_mode<<std::endl;
  std::cout<<" - print_bin_data = "<<print_bin_data<<std::endl;
  std::cout<<" - link_r = "<<link_r<<std::endl;
  std::cout<<" - link_z = "<<link_z<<std::endl;
  std::cout<<" - min_ngal = "<<min_ngal<<std::endl;
  std::cout<<" - z_min = "<<z_min<<std::endl;
  std::cout<<" - z_max = "<<z_max<<std::endl;
  std::cout<<" - z_bin_size = "<<z_bin_size<<std::endl;
  std::cout<<" - z_ref = "<<z_ref<<std::endl;
  std::cout<<" - dz_max = "<<dz_max<<std::endl;
  std::cout<<" - c = "<<c<<std::endl;
  std::cout<<" - H0 = "<<H0<<std::endl;
  std::cout<<" - omega_m = "<<omega_m<<std::endl;
  std::cout<<" - omega_l = "<<omega_l<<std::endl;
  exit(0);
}

void Option::read_opts(int argc, char *argv[], double version_number) {

  /* Define Generic Options */
  po::options_description generic("Generic options");
  generic.add_options()
    ("help,h", "Produce help message.")
    ("version,v", "Print code version.")
    ("parameters,p", "Print all parameter values.")
    ("config,c", po::value<std::string>(&config_file)->default_value("param_file.ini"),
     "Configuration file name.");
  
  /* Define Configuration Options */
  po::options_description config("Configuration");
  config.add_options()
    ("input_file,i", po::value<std::string>(&input_file),
     "Input file name.")
    ("output_clusters", po::value<std::string>(&output_clusters),
     "Output clusters file name.")
    ("output_members", po::value<std::string>(&output_members), 
     "Output members file name.")
    ("input_mode", po::value<std::string>(&input_mode)->default_value("fits"), 
     "File input mode [ascii/fits].")
    ("output_mode", po::value<std::string>(&output_mode)->default_value("fits"), 
     "File output mode [ascii/fits].")
    ("fof_mode", po::value<std::string>(&fof_mode)->default_value("phot"), 
     "Friends-of-friends redshift mode [spec/phot].")
    ("link_mode", po::value<std::string>(&link_mode)->default_value("dynamic"), 
     "Friends-of-friends linking mode [fixed/dynamic].")
    ("print_bin_data", po::value<std::string>(&print_bin_data)->default_value("no"), 
     "Print redshift bin data [yes/no].")
    ("print_bg_data", po::value<std::string>(&print_bg_data)->default_value("no"), 
     "Print background data [yes/no].")
    ("link_r", po::value<double>(&link_r), 
     "Transverse linking parameter value.")
    ("link_z", po::value<double>(&link_z), 
     "Line-of-sight linking parameter value.")
    ("min_ngal", po::value<int>(&min_ngal)->default_value(10, "10"), 
     "Minimum number of cluster galaxies members.")
    ("z_min", po::value<double>(&z_min)->default_value(0.0, "0.00"), 
     "Minimum redshift of sample.")
    ("z_max", po::value<double>(&z_max)->default_value(3.0, "3.00"), 
     "Maximum redshift of sample.")
    ("z_bin_size", po::value<double>(&z_bin_size)->default_value(0.01, "0.01"), 
     "Size of redshift bins.")
    ("z_ref", po::value<double>(&z_ref)->default_value(0.50, "0.50"), 
     "Reference redshift for calculations.")
    ("dz_max", po::value<double>(&dz_max)->default_value(0.06, "0.06"), 
     "Maxmimum photo-z error allowed.")
    ("c", po::value<double>(&c)->default_value(2.997e5, "2.997e5"), 
     "Speed of light in km/s.")
    ("H0", po::value<double>(&H0)->default_value(100, "100.00"), 
     "Hubble parameter in km/s/Mpc.")
    ("omega_m", po::value<double>(&omega_m)->default_value(0.30, "0.30"), 
     "Matter density.")
    ("omega_l", po::value<double>(&omega_l)->default_value(0.70, "0.70"), 
     "Dark energy density.");
 
  /* Command Line Options */
  po::options_description cmdline_options("\nFRIENDS-OF-FRIENDS CLUSTER DETECTION ALGORITHM\n\nCode Options");
  cmdline_options.add(generic).add(config);
  
  /* Configuration File Options */
  po::options_description config_file_options;
  config_file_options.add(config);
  
  /* Define Variables Map */
  po::variables_map v_map;
  store(po::command_line_parser(argc, argv).options(cmdline_options).run(), v_map);
  notify(v_map);

  /* Read Configuration File */
  std::ifstream read_config(config_file.c_str());
  if(read_config.good()) {
    store(parse_config_file(read_config, config_file_options), v_map);
    notify(v_map);
  }
  else 
    std::cout<<"Warning: configuration file ["<<config_file.c_str()<<"] not found."<<std::endl; 
  
  /* Print Help */
  if (v_map.count("help")) {
    std::cout << cmdline_options << "\n";
    exit(0);
  }
  
  /* Print Version */
  if (v_map.count("version"))
    version(version_number);    

  /* Print Parameters */
  if (v_map.count("parameters"))
    print_parameters();    
}

void Option::read_merge_opts(int argc, char *argv[], double version_number) {

  /* Define Options */
  po::options_description opts("Code options");
  opts.add_options()
    ("help,h", "Produce help message.")
    ("version,v", "Print code version.")
    ("input_file,i", po::value<std::string>(&input_file),
     "Input file name.")
    ("output_file,o", po::value<std::string>(&output_file),
     "Output file name.")
    ("input_mode", po::value<std::string>(&input_mode)->default_value("fits"), 
     "File input mode [ascii/fits].")
    ("output_mode", po::value<std::string>(&output_mode)->default_value("fits"), 
     "File output mode [ascii/fits].")
    ("bg_data", po::value<std::string>(&bg_data),
     "Input file name for background data.");
  
  /* Define Variables Map */
  po::variables_map v_map;
  store(po::command_line_parser(argc, argv).options(opts).run(), v_map);
  notify(v_map);

  /* Print Help */
  if (v_map.count("help")) {
    std::cout << opts << "\n";
    exit(0);
  }
  
  /* Print Version */
  if (v_map.count("version"))
    version(version_number);    
}

void Option::read_split_opts(int argc, char *argv[], double version_number) {

  /* Define Options */
  po::options_description opts("Code options");
  opts.add_options()
    ("help,h", "Produce help message.")
    ("version,v", "Print code version.")
    ("input_file,i", po::value<std::string>(&input_file),
     "Input file name.")
    ("ra_lower", po::value<double>(&ra_lower)->default_value(0),
     "Lower limit in right ascension.")
    ("ra_upper", po::value<double>(&ra_upper)->default_value(0),
     "Upper limit in right ascension.")
    ("dec_lower", po::value<double>(&dec_lower)->default_value(0),
     "Lower limit in declination.")
    ("dec_upper", po::value<double>(&dec_upper)->default_value(0),
     "Upper limit in declination.")
    ("ra_overlap", po::value<double>(&ra_overlap)->default_value(0.5),
     "Overlap in right ascension.")
    ("dec_overlap", po::value<double>(&dec_overlap)->default_value(0.5),
     "Overlap in declination.")
    ("n_ra_bins", po::value<int>(&n_ra_bins)->default_value(0),
     "Number of right ascension bins.")
    ("n_dec_bins", po::value<int>(&n_dec_bins)->default_value(0),
     "Number of declination bins.")
    ("n_procs", po::value<int>(&n_procs)->default_value(0),
     "Number of processes.");
  
  /* Define Variables Map */
  po::variables_map v_map;
  store(po::command_line_parser(argc, argv).options(opts).run(), v_map);
  notify(v_map);

  /* Print Help */
  if (v_map.count("help")) {
    std::cout << opts << "\n";
    exit(0);
  }
  
  /* Print Version */
  if (v_map.count("version"))
    version(version_number);    
}
