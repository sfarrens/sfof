/*Cat Merge Code*/

#include "cat_merge.hpp"

void Cat_Merge::read_options (int argc, char *argv[]) {
  // Function to read code options.
  double version_number = 1.0;
  opt.read_merge_opts(argc, argv, version_number);
}

void Cat_Merge::read_files () {
  // Function to read cluster member files.
  merge_fileio.read_file_list(opt.input_file, clusters, galaxies, opt.input_mode);
  std::cout<<"Total Clusters Read: "<<clusters.size()<<std::endl;
}

void Cat_Merge::merge_clusters () {
  // Function to merge clusters.
  Merge::join_uf(clusters);
  Merge::rearrange_clusters(galaxies, clusters);
  std::cout<<"Total Merged Clusters: "<<clusters.size()<<std::endl;
}

void Cat_Merge::assign_cluster_props () {
  // Funciton that assigns cluster properties.
  std::vector<double> z_vals, count_vals;
  if (!opt.bg_data.empty()) {
    merge_fileio.read_bg_data(opt.bg_data, z_vals, count_vals);
    spline.set_points(z_vals, count_vals);
  }
  for(int i = 0; i < clusters.size(); i++) {
    /* Remove duplicate members */
    clusters[i].unique();
    /* Assing properties */
    clusters[i].assign_props();
    if (!opt.bg_data.empty()) 
      clusters[i].assign_sn(spline(clusters[i].z));
  }
  /* Sort clusters by number of members */
  std::sort(clusters.begin(), clusters.end());
  std::reverse(clusters.begin(), clusters.end());
  /* Rename clusters */
  for(int i = 0; i < clusters.size(); i++) 
    clusters[i].rename(i + 1);
}

void Cat_Merge::write_files () { 
  // Function to write cluster properties to output files.
  std::string cluster_file_name, member_file_name;
  merge_fileio.output_file_names(opt.output_file, opt.output_mode, 
				 cluster_file_name, member_file_name);
  if(opt.output_mode == "ascii")
    fileio.write_ascii(clusters, cluster_file_name, member_file_name);
  else
    fileio.write_fits(clusters, cluster_file_name, member_file_name);
}

int main (int argc, char *argv[]) {
  Cat_Merge run_code;
  run_code.comp.start_time();
  run_code.read_options(argc, argv);
  run_code.read_files();
  run_code.merge_clusters();
  run_code.assign_cluster_props();
  run_code.write_files();
  run_code.comp.end_time();
  run_code.comp.print_time();
}
