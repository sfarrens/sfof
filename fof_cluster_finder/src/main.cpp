/*Main Code*/

#include "main.hpp"

void Main::read_options (int argc, char *argv[]) {
  // Function to read code options.

  double version_number = 3.1;

  param_file = "param_file.ini";
  opt.read_opts(argc, argv, version_number);

}

void Main::read_data () {
  // Function to read input file.

  if (opt.fof_mode == "spec")
    fileio.set_up(1, 2, 3, 4);
  else
    fileio.set_up(1, 2, 3, 4, 5);

  /* Read in FITS file. */
  if(opt.input_mode == "fits") 
    fileio.read_fits(opt.input_file, opt.fof_mode, opt.z_min, 
		     opt.z_max, opt.dz_max, galaxies);
  /* Read in ASCII file. */
  else if(opt.input_mode == "ascii")
    fileio.read_ascii(opt.input_file, opt.fof_mode, opt.z_min, 
		      opt.z_max, opt.dz_max, galaxies);  

}

void Main::set_up_zbins () {
  // Function to set up the redshift bins.

  /* Read N(z) from file. */
  if (!opt.nz_data.empty()) {
    std::vector<double> z_vals, count_vals;
    fileio.read_nz_data(opt.nz_data, z_vals, count_vals);
    spline_nz.set_points(z_vals, count_vals);
  }

  /* Set number of z-bins. */
  num_bins = astro.num_bins(opt.z_min, opt.z_max, opt.z_bin_size);

  /* Creat vector of Zbin instances. */
  for (int i = 0; i < num_bins; i++) {
    Zbin zbin(i, opt.z_min + (i + 0.5) * opt.z_bin_size, opt.z_bin_size);
    zbin.assign_dist(opt.c, opt.H0, opt.omega_m, opt.omega_l);
    zbins.push_back(zbin);
    if (!opt.nz_data.empty()) 
      zbins[i].count = spline_nz(zbins[i].z);
  }
  
  /* Assign Zbin instances to Galaxy instances. */
  for (int i = 0; i < galaxies.size(); i++) {
    galaxies[i].assign_bin(opt.z_min, opt.z_bin_size);
    galaxies[i].assign_bins(opt.z_min, opt.z_bin_size, opt.link_z);
    if(opt.fof_mode == "spec") {
      galaxies[i].set_cluster_status(1);
      galaxies[i].assign_dist(opt.c, opt.H0, opt.omega_m, opt.omega_l);
    }
    else
      galaxies[i].set_cluster_status(zbins.size());
    if (opt.nz_data.empty())
      for (int j = 0; j < galaxies[i].bins.size(); j++)
	zbins[galaxies[i].bins[j]].count++;
  }

}

void Main::assign_linking_param () {
  // Function to assign linking parameter values to redshift bins.
  // A reference value is defined in order to ensure uniformity.

  /* Set reference linking value from reference z */
  if(opt.link_mode == "fixed")
    for(int i = 0; i < num_bins; i++)
      zbins[i].assign_fixed_rfriend(opt.link_r); 
  else {
    int z_ref_index = astro.find_bin(opt.z_ref, opt.z_min, opt.z_bin_size);
    double r_ref = pow(double(zbins[z_ref_index].count) 
    		       / (opt.z_bin_size * zbins[z_ref_index].dvdz), 0.5) * opt.link_r;
    for(int i = 0; i < num_bins; i++)
      zbins[i].assign_rfriend(r_ref); 
  }

  /* Print redshift bin data to file */
  if(opt.print_bin_data) {
    std::string z_bin_data = opt.input_file + ".z_bin_data.dat";
    //const char* z_bin_data = opt.input_file.c_str() + ".z_bin_data.dat";
    std::cout<<"Printing redshift bin data to "<<z_bin_data<<"."<<std::endl;
    std::ofstream zbin_out(z_bin_data);
    zbin_out<<"#Num[1] Z[2] Link_R[3] R_Friend[4] Count[5]"<<std::endl;
    for(int i = 0; i < num_bins; i++) 
      zbin_out<<zbins[i].num<<" "<<zbins[i].z<<" "<<zbins[i].link_r<<" "
	       <<zbins[i].rfriend<<" "<<zbins[i].count<<std::endl;
    zbin_out.close();
  }

}

void Main::make_kdtree () {
  // Function to split data into kd-tree.

  std::cout<<"Building kd-tree."<<std::endl;

  /* Set-up kd-tree */
  tree.set_Kdtree(galaxies, 0.3);

  /* Print kd-tree data to file */
  std::string kdtree_data = opt.input_file + ".kdtree_data.dat";
  if(opt.print_kdtree_data) 
    tree.write_Kdtree(kdtree_data);

}

void Main::background_counts () {
  // Function to count number of background objects
  // at a given redshift.

  std::vector<double> z_vals, count_vals;

  /* Find background density as a function of z. */
  for (int i = 0; i < zbins.size(); i++) {
    z_vals.push_back(zbins[i].z);
    count_vals.push_back(double(zbins[i].count) / (tree.sample_area * 3600.0));
  }  

  /* Fit spline to background density. */
  spline_bg.set_points(z_vals, count_vals);

  /* Print background data to file. */
  if(opt.print_bg_data) {
    std::string bg_data = opt.input_file + ".bg_data.dat";
    std::cout<<"Printing background data to "<<bg_data<<"."<<std::endl;
    std::ofstream bg_out(bg_data);
    bg_out<<"#Z[1] BG_Density[2]"<<std::endl;
    for(int i = 0; i < z_vals.size(); i++) 
      bg_out<<z_vals[i]<<" "<<count_vals[i]<<std::endl;
    bg_out.close();
  }

}

void Main::find_friends () {
  // Function that implements the friends-of-friends.

  std::cout<<"Performing FoF in "<<opt.fof_mode<<" mode."<<std::endl;

  int nbins = num_bins, cluster_count = 0;
  if(opt.fof_mode == "spec") nbins = 1;

  std::cout<<"   - using "<<num_bins<<" redshift bins."<<std::endl;

  /* Create vector of FoF instances. */
  std::vector<FoF> fof_list;
  for (int i = 0; i < nbins; i++) {
    FoF fof_bin;
    fof_list.push_back(fof_bin);
  }

  /* Start OMP */
  int unused_nodes = 0;
#pragma omp parallel
  {
    int nts=omp_get_num_threads();
    int tid=omp_get_thread_num();
#pragma omp master
    std::cout<<" OMP: Using "<<nts<<" threads."<<std::endl;
#pragma omp for reduction(+:unused_nodes)
    for (int i = 0; i < nbins; i++) {
      std::cout<<"ID: "<<tid<<" finding clusters at z = "<<zbins[i].z<<"; ";
      fof_list[i].setup(opt.link_r, opt.link_z, opt.fof_mode);
      unused_nodes += fof_list[i].friends_of_friends(i, zbins, galaxies, tree);
      fof_list[i].remove(opt.min_ngal);
      std::cout<<std::setw(4)<<fof_list[i].list_of_clusters.size()
	       <<" candidates detected."<<std::endl;
    }
  }
  /* End OMP */

  /* Create vector of cluster candidates. */
  for (int i = 0; i < nbins; i++) 
    for (int j = 0; j < fof_list[i].list_of_clusters.size(); j++) {
      fof_list[i].list_of_clusters[j].rename(cluster_count);
      clusters.push_back(fof_list[i].list_of_clusters[j]);
      cluster_count++;
    }

}

void Main::check_results() {
  // Function that checks how many cluster canidates 
  // have been detected.

  if (clusters.size() > 0)
    merge_clusters();
  else 
    std::cout<<"No clusters deteced in sample!"<<std::endl;

}

void Main::merge_clusters () {
  // Function that merges clusters with members in common.

  std::cout<<"Merging "<<clusters.size()<<" candidates."<<std::endl;
  
  /* Merge clusters */
  Merge::join_uf(clusters);
  Merge::rearrange_clusters(galaxies, clusters);

  std::cout<<"Total clusters detected with Ngal >= "<<opt.min_ngal
	   <<": "<<clusters.size()<<std::endl;

  /* Reasign cluster properties. */
  assign_cluster_props();

}

void Main::assign_cluster_props () {
  // Funciton that assigns cluster properties.

  for(int i = 0; i < clusters.size(); i++) {
    /* Remove duplicate members */
    clusters[i].unique();
    /* Assign properties */
    clusters[i].assign_props();
    /* Calculate distance to cluster */
    if (opt.size_units == "Mpc") 
      clusters[i].assign_dist(opt.c, opt.H0, opt.omega_m, opt.omega_l);
    /* Assign signal-to-noise using background density */
    clusters[i].assign_sn(fabs(spline_bg(clusters[i].z)));
    /* Update cluster size units */
    clusters[i].update_size(opt.size_units);
  }

  /* Sort clusters by number of members */
  std::sort(clusters.begin(), clusters.end());
  std::reverse(clusters.begin(), clusters.end());

  /* Rename clusters */
  for(int i = 0; i < clusters.size(); i++) 
    clusters[i].rename(i + 1);

  output_results();

}

void Main::output_results () {
  // Function that outputs detected clusters.

  /* Create clusters output file name. */
  if(opt.output_clusters.empty())
    fileio.output_cluster_name(opt.input_file, opt.fof_mode, 
			     opt.output_mode, opt.link_r, opt.link_z, 
			     opt.output_clusters);

  /* Create members output file name. */
  if(opt.output_members.empty())
    fileio.output_member_name(opt.input_file, opt.fof_mode, 
			     opt.output_mode, opt.link_r, opt.link_z, 
			     opt.output_members);

  std::cout<<"Cluster properties being written to: "<<opt.output_clusters<<std::endl;
  std::cout<<"Cluster member properties being written to: "<<opt.output_members<<std::endl;

  /* Write output to FITS file. */
  if(opt.output_mode == "fits") 
    fileio.write_fits(clusters, opt.output_clusters, opt.output_members);
  /* Write output to ASCII file. */
  else if(opt.output_mode == "ascii") 
    fileio.write_ascii(clusters, opt.output_clusters, opt.output_members);  

}

int main (int argc, char *argv[]) {

  try {
    Main run_code;
    run_code.comp.start_time();
    run_code.read_options(argc, argv);
    std::cout<<"=================================================="<<std::endl;
    std::cout<<"* FRIENDS-OF-FRIENDS CLUSTER DETECTION INITIATED *"<<std::endl;
    std::cout<<"=================================================="<<std::endl;
    run_code.read_data();
    run_code.set_up_zbins();
    run_code.assign_linking_param();
    run_code.make_kdtree();
    run_code.background_counts();
    run_code.find_friends();
    run_code.check_results();
    run_code.comp.end_time();
    run_code.comp.print_time();
    std::cout<<"=================================================="<<std::endl;
  }

  catch (const std::exception& e) {
    std::cerr << "ERROR!: " << e.what() << std::endl;
    return 1;
  }

}
