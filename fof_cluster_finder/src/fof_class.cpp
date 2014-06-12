/*Class for performing friends-of-friends*/

#include "fof_class.hpp"

bool FoF::bin_check (const Zbin &zbin, const Galaxy &gal) {
  //! Function that checks if a galaxy is compatible with a given redshift bin.
  if (mode == "spec")
    return true;
  else
    return fabs(gal.z - zbin.z) <= link_z * gal.dz;
}

bool FoF::node_check (const Galaxy &gal, const Kdtree::Kdtree_node &node, double rfriend) {
  //! Function that checks if a galaxy is compatibile with a given kd-tree node.
  double dist = astro.angsep(gal.ra, gal.dec, node.ra, node.dec) - node.radius;
  return dist <= rfriend;
}

bool FoF::friendship (const Zbin &zbin, const Galaxy &gal1, const Galaxy &gal2, double rfriend) {
  //! Function that checks if two galaxies are friends in a given redshift bin.
  bool final_check;
  bool check0 = gal1.num != gal2.num;
  bool check1 = bin_check(zbin, gal2);
  bool check2 = !gal2.in_cluster[zbin.num];
  double dist = astro.angsep(gal1.ra, gal1.dec, gal2.ra, gal2.dec);
  bool check3 = dist <= rfriend;    
  if (mode == "spec") {
    bool check4 = fabs(gal1.v - gal2.v) <= (link_z / (1 + gal1.z));
    final_check = check0 && check1 && check2 && check3 && check4;
  }
  else
    final_check = check0 && check1 && check2 && check3;
  return final_check;
}

void FoF::new_cluster (const Zbin &zbin, Galaxy &gal1, Galaxy &gal2) {
  //! Function to create a new cluster.
  cluster_count++;
  Cluster cluster_here(cluster_count);
  gal1.in_cluster[zbin.num] = true;
  gal2.in_cluster[zbin.num] = true;
  cluster_here.add_gal(gal1);
  cluster_here.add_gal(gal2);
  list_of_clusters.push_back(cluster_here);
}

void FoF::add_member (const Zbin &zbin, Galaxy &gal, Cluster &cluster) {
  //! Function to add a new member to an existing cluster.
  gal.in_cluster[zbin.num] = true;
  cluster.add_gal(gal);
}

void FoF::find_friends (const Zbin &zbin, Galaxy &gal, double rfriend) {
  //! Function to find galaxies linked to the galaxy in question.
  /**< Loop through kd-tree nodes */
  for(int j = 0; j < tree.node_list.size(); j++) {
    /**< Check if galaxy is compatible with kd-tree node */
    if(node_check(gal, tree.node_list[j], rfriend)) {
      /**< Loop through node members */
      for(int k = 0; k < tree.node_list[j].members.size(); k++) {
	/**< Check if galaxies are friends */
	int gal_now = tree.node_list[j].members[k].num;
	if(friendship(zbin, gal, gal_list[gal_now], rfriend)) {
	  /**< Create new cluster */
	  if(!gal.in_cluster[zbin.num]) 
	    new_cluster(zbin, gal, gal_list[gal_now]);
	  /**< Add new member to existing cluster */
	  else 
	    add_member(zbin, gal_list[gal_now], list_of_clusters[cluster_count]);
	}
      } // end of node member loop
    }
  } // end of node loop
}

void FoF::find_friends_of_friends (const Zbin &zbin, Cluster &cluster, double rfriend){
  //! Function to find the galaxies linked to existing cluster members.
  /**< Loop through cluster members */
  for(int i = 0; i < cluster.mem.size(); i++) {
    find_friends(zbin, gal_list[cluster.mem[i].num], rfriend);
  } // end of cluster member loop
}

void FoF::friends_of_friends (int bin_num) {
  //! Funciton that find friends-of-friends in a given redshift bin.
  cluster_count = -1;
  Zbin zbin = zbin_list[bin_num];
  double rfriend = zbin.rfriend;
  /**< Loop through galaxies */
  for(int i = 0; i < gal_list.size(); i++) {
    /**< Modify rfriend for spectroscopic mode*/
    if (mode == "spec") rfriend = zbin_list[gal_list[i].bin].link_r / gal_list[i].da;
    /**< Check if galaxy is already in a cluster (f-loop)*/
    if(!gal_list[i].in_cluster[zbin.num] && bin_check(zbin, gal_list[i])) { 
      find_friends(zbin, gal_list[i], rfriend);
      /**< Check if galaxy is now in a cluster (fof-loop)*/
      if(gal_list[i].in_cluster[zbin.num])
	find_friends_of_friends(zbin, list_of_clusters[cluster_count], rfriend);
    }
  } //end of galaxy loop
}

void FoF::remove (int min_ngal) {
  //! Function that removes clusters that have too few members.
  std::vector<int> remove_list;
  /**< Loop through clusters */
  for(int i = 0; i < list_of_clusters.size(); i++) {
    list_of_clusters[i].unique();
    /**< Check if cluster has less than the minimum number of members */
    if(list_of_clusters[i].mem.size() < min_ngal)
      remove_list.push_back(i);
  }
  /**< Loop backwards through list of items to be removed */
  for(int i = remove_list.size(); i --> 0;)
    list_of_clusters.erase(list_of_clusters.begin() + remove_list[i]);
}
