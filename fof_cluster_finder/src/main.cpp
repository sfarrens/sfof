/*Main Code*/

#include "main.hpp"

void Main::read_options (int argc, char *argv[]) {
  //! Function to read code options.
  param_file = "param_file.ini";
  opt.read_param_file(param_file);
  opt.read_opts(argc, argv);
}

void Main::read_data () {
  //! Function to read input file.
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
  std::cout<<"Building kd-tree to depth of "<<max_depth_val<<std::endl;
  tree.set_kdtree(galaxies, opt.kdtree_depth);
}

void Main::find_friends () {
  //! Function that implements the friends-of-friends.
  std::cout<<"Performing FoF in "<<opt.fof_mode<<" mode."<<std::endl;
  int nbins = num_bins, cluster_count = 0;
  std::vector<FoF> fof_list;
  if(opt.fof_mode == "spec") nbins = 1;
  for (int i = 0; i < nbins; i++) {
    FoF fof_bin(opt.link_r, opt.link_z, opt.fof_mode, tree, zbins, galaxies);
    fof_bin.friends_of_friends(i);
    fof_bin.remove(opt.min_ngal);
    fof_list.push_back(fof_bin);
  }
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
  fileio.output_file_names(opt.input_file, opt.fof_mode, 
			   opt.output_mode, opt.link_r, opt.link_z);
  if(opt.output_mode == "fits") 
    fileio.write_fits(clusters);
  else if(opt.output_mode == "ascii") 
    fileio.write_ascii(clusters);  
}

int main (int argc, char *argv[]) {
  Main run_code;
  run_code.read_options(argc, argv);
  run_code.read_data();
  run_code.set_up_zbins();
  run_code.assign_linking_param();
  run_code.make_kdtree();
  run_code.find_friends();
  run_code.merge_clusters();
  run_code.assign_cluster_props();
  run_code.output_results();
}
