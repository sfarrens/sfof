#include "find_rich.hpp"

void Find_Rich::set_const (double radius, double frac) {
  Omega_M = 0.3;
  Omega_L = 0.7;
  c = 2.997e5; //km/s
  H0 = 100; //km/s/Mpc
  radial_threshold = radius; //Mpc
  lum_frac = log10(frac) / 0.4;
}

void Find_Rich::read_mstar_vals (const std::string &input_file) {
  std::string line;
  std::vector<std::string> cols; 
  std::ifstream read_file(input_file.c_str()); /* open file */
  while(!read_file.eof()) { /* while not the end of the file */
    std::getline(read_file, line); /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      ms_z.push_back(atof(cols[0].c_str()));
      ms_mag.push_back(atof(cols[1].c_str()));
      cols.clear();
    }
  }
}

void Find_Rich::read_clusters (const std::string &input_file) {
  std::string line;
  std::vector<std::string> cols; 
  std::ifstream read_file(input_file.c_str()); /* open file */
  while(!read_file.eof()) { /* while not the end of the file */
    std::getline(read_file, line); /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      Cluster clt_here(atoi(cols[0].c_str()));
      clt_here.ra = atof(cols[1].c_str());
      clt_here.dec = atof(cols[2].c_str());
      clt_here.z = atof(cols[3].c_str());
      clt_here.assign_dist(c, H0, Omega_M, Omega_L);
      clusters.push_back(clt_here);
      cols.clear();
    }
  }
}

double Find_Rich::abs_mag (double mag, double z) {
  return mag - 5 * log10((lumdis(z, Omega_M, Omega_L) * 
			  (c / H0) * 1e6) / 10);
}

double Find_Rich::get_mstar (double z) {  
  tk::spline s;
  s.set_points(ms_z, ms_mag);
  std::cout<<s(z)<<" "<<abs_mag(s(z), z)<<" "<<abs_mag(s(z), z)-lum_frac<<std::endl;
  return abs_mag(s(z), z);
}

bool Find_Rich::check_mag (double mag, double z) {
  double M = abs_mag(mag, z);
  return (M <= get_mstar(z) - lum_frac);
}

void Find_Rich::check_radius (const Galaxy &gal) {
  double dist;
  for (int i = 0; i < clusters.size(); i++) {
    dist = (astro.angsep(clusters[i].ra, clusters[i].dec, 
			 gal.ra, gal.dec)) * clusters[i].da;
    if (dist <= radial_threshold)
      //if (dist <= radial_threshold && fabs(gal.z - clusters[i].z) <= 4 * 0.05) 
      clusters[i].add_gal(gal);
      //else
      //std::cout<<gal.ra<<" "<<gal.dec<<" "<<gal.z<<std::endl;
  }
}

void Find_Rich::read_ascii (const std::string &input_file) { 
  //! Function to read in an ASCII file and store the contents in a vector of Galaxy instances.
  int count = 0;
  double ra, dec, z, dz, m;
  unsigned long id;
  std::string line;
  std::vector<std::string> cols; 
  std::ifstream read_file(input_file.c_str()); /* open file */
  while(!read_file.eof()) { /* while not the end of the file */
    std::getline(read_file, line); /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      id = strtoul(cols[0].c_str(), NULL, 0);
      ra = atof(cols[1].c_str());
      dec = atof(cols[2].c_str());
      z = atof(cols[3].c_str());
      dz = atof(cols[4].c_str());
      if (z == 0) z += 0.001;
      m = atof(cols[5].c_str());
      if (check_mag(m, z)) {
	Galaxy gal_here(count, id, ra, dec, z, dz);
	check_radius(gal_here);
	count++;
      }
      cols.clear();
    }
  }
  std::cout<<"Count: "<<count<<std::endl;
}

void Find_Rich::assign_cluster_props () {
  //! Funciton that assigns cluster properties.
  for(int i = 0; i < clusters.size(); i++) {
    /**< Remove duplicate members */
    clusters[i].unique();
    /**< Assing properties */
    clusters[i].assign_props();
    clusters[i].assign_sn(30);
  }
}

void Find_Rich::write_files () { 
  //! Function to write cluster properties to output files.
  std::string cluster_file_name, member_file_name;
  cluster_file_name = "rich_cat_clusters.dat";
  member_file_name = "rich_cat_members.dat";
  fileio.write_ascii(clusters, cluster_file_name, member_file_name);
}

int main (int argc, char *argv[]) {
  Find_Rich run_code;
  run_code.comp.start_time();
  run_code.set_const(atof(argv[4]), atof(argv[5]));
  run_code.read_mstar_vals(argv[3]);
  run_code.read_clusters(argv[2]);
  run_code.read_ascii(argv[1]);
  run_code.assign_cluster_props();
  run_code.write_files();
  run_code.comp.end_time();
  run_code.comp.print_time();
}
