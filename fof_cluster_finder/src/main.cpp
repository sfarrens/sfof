/*Main Code*/

#include "main.hpp"

void Main::read_options (int argc, char *argv[]) {
  //! Function to read code options.
  double version_number = 3.0;
  param_file = "param_file.ini";
  opt.read_param_file(param_file);
  opt.read_opts(argc, argv, version_number);
}

void Main::read_data () {
  //! Function to read input file.
  if (opt.fof_mode == "spec")
    fileio.set_up(1, 2, 3, 4);
  else
    fileio.set_up(1, 2, 3, 4, 5);
  if(opt.input_mode == "fits") 
    fileio.read_fits(opt.input_file, opt.fof_mode, opt.z_min, 
		     opt.z_max, opt.dz_max, galaxies);
  else if(opt.input_mode == "ascii")
    fileio.read_ascii(opt.input_file, opt.fof_mode, opt.z_min, 
		      opt.z_max, opt.dz_max, galaxies);  
}

void Main::set_up_zbins () {
  //! Function to set up the redshift bins.
  num_bins = astro.num_bins(opt.z_min, opt.z_max, opt.z_bin_size);
  for(int i = 0; i < num_bins; i++){
    Zbin zbin(i, opt.z_min + i * opt.z_bin_size, opt.z_bin_size);
    zbin.assign_dist(opt.c, opt.H0, opt.omega_m, opt.omega_l);
    zbins.push_back(zbin);
  }
  for(int i = 0; i < galaxies.size(); i++) {
    galaxies[i].assign_bin(opt.z_min, opt.z_bin_size);
    if(opt.fof_mode == "spec") {
      galaxies[i].set_cluster_status(1);
      galaxies[i].assign_dist(opt.c, opt.H0, opt.omega_m, opt.omega_l);
    }
    else
      galaxies[i].set_cluster_status(zbins.size());
    zbins[galaxies[i].bin].count++;
  }
}

void Main::assign_linking_param () {
  //! Function to assign linking parameter values to redshift bins.
  //! A reference value is defined in order to ensure uniformity.
  int z_ref_index = astro.find_bin(opt.z_ref, opt.z_min, opt.z_bin_size);
  double r_ref = pow(double(zbins[z_ref_index].count) 
		     / (opt.z_bin_size * zbins[z_ref_index].dvdz), 0.5) * opt.link_r;
  for(int i = 0; i < num_bins; i++)
    zbins[i].assign_rfriend(r_ref); 
}

void Main::make_kdtree () {
  //! Function to split data into kd-tree.
  std::cout<<"Building kd-tree to depth of "<<opt.kdtree_depth<<std::endl;
  tree.set_kdtree(galaxies, opt.kdtree_depth);
}

void Main::find_friends () {
  //! Function that implements the friends-of-friends.
  std::cout<<"Performing FoF in "<<opt.fof_mode<<" mode."<<std::endl;
  int nbins = num_bins, cluster_count = 0;
  if(opt.fof_mode == "spec") nbins = 1;
  std::vector<FoF> fof_list;
  for (int i = 0; i < nbins; i++) {
    FoF fof_bin;
    fof_list.push_back(fof_bin);
  }
  //Start OMP//
#pragma omp parallel 
  {
    int nts=omp_get_num_threads();
    int tid=omp_get_thread_num();
#pragma omp master
    std::cout<<" OMP: Using "<<nts<<" threads."<<std::endl;
#pragma omp for
    for (int i = 0; i < nbins; i++) {
      std::cout<<"ID: "<<tid<<" finding clusters at z = "<<zbins[i].z<<std::endl;
      fof_list[i].setup(opt.link_r, opt.link_z, opt.fof_mode);
      fof_list[i].friends_of_friends(i, zbins, galaxies, tree);
      fof_list[i].remove(opt.min_ngal);
    }
  }
  //End OMP//
  for (int i = 0; i < nbins; i++) 
    for (int j = 0; j < fof_list[i].list_of_clusters.size(); j++) {
      fof_list[i].list_of_clusters[j].rename(cluster_count);
      clusters.push_back(fof_list[i].list_of_clusters[j]);
      cluster_count++;
    }
}

void Main::merge_clusters () {
  //! Function that merges clusters with members in common.
  std::cout<<"Merging clusters."<<std::endl;
  Merge merge_clusters(clusters);
}

void Main::assign_cluster_props () {
  //! Funciton that assigns cluster properties.
  for(int i = 0; i < clusters.size(); i++) {
    /**< Remove duplicate members */
    clusters[i].unique();
    /**< Assing properties */
    clusters[i].assign_props();
  }
  /**< Sort clusters by number of members */
  std::sort(clusters.begin(), clusters.end());
  std::reverse(clusters.begin(), clusters.end());
  //**< Rename clusters */
  for(int i = 0; i < clusters.size(); i++) 
    clusters[i].rename(i + 1);
}

void Main::output_results () {
  //! Function that outputs detected clusters.
  std::string cluster_file_name, member_file_name;
  fileio.output_file_names(opt.input_file, opt.fof_mode, 
			   opt.output_mode, opt.link_r, opt.link_z, 
			   cluster_file_name, member_file_name);
  if(opt.output_mode == "fits") 
    fileio.write_fits(clusters, cluster_file_name, member_file_name);
  else if(opt.output_mode == "ascii") 
    fileio.write_ascii(clusters, cluster_file_name, member_file_name);  
}

int main (int argc, char *argv[]) {
  Main run_code;
  run_code.comp.start_time();
  run_code.read_options(argc, argv);
  run_code.read_data();
  run_code.set_up_zbins();
  run_code.assign_linking_param();
  run_code.make_kdtree();
  run_code.find_friends();
  run_code.merge_clusters();
  run_code.assign_cluster_props();
  run_code.output_results();
  run_code.comp.end_time();
  run_code.comp.print_time();
}
