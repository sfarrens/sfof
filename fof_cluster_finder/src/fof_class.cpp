/*Class for performing friends-of-friends*/

// [Header files]
#include "fof_class.hpp"

void FoF::setup (double link_r_val, double link_z_val, const std::string &mode_val) { 
  // Function to set-up a FoF instance.
  if (link_r_val <= 0)
    throw BadArgumentException("FoF::setup", "link_r_val", "> 0.0");
  if (link_z_val <= 0)
    throw BadArgumentException("FoF::setup", "link_z_val", "> 0.0");
  if (mode_val != "spec" && mode_val != "phot")
    throw BadArgumentException("FoF::setup", "mode_val", "a valid option [spec/phot]");
  link_r = link_r_val;
  link_z = link_z_val;
  mode = mode_val;
}

bool FoF::bin_check (const Zbin &zbin, const Galaxy &gal) {
  // Function that checks if a galaxy is compatible with a given redshift bin.
  if (mode == "spec")
    return true;
  else {
    if (std::abs(gal.z - zbin.z) < link_z * gal.dz)
      return true;
    else if (std::abs(std::abs(gal.z - zbin.z) - (link_z * gal.dz)) 
	     < std::numeric_limits<double>::epsilon())
      return true;
    else
      return false;
  }
}

bool FoF::friendship (const Zbin &zbin, const Galaxy &gal1, const Galaxy &gal2, double rfriend) {
  // Function that checks if two galaxies are friends in a given redshift bin.
  if (rfriend < 0)
    throw BadArgumentException("FoF::node_check", "rfriend", ">= 0.0");
  bool final_check;
  bool check0 = gal1.num != gal2.num;
  bool check1 = bin_check(zbin, gal2);
  bool check2 = !gal2.in_cluster[zbin.num];
  double dist = astro.angsep(gal1.P, gal2.P);
  bool check3 = dist <= rfriend;    
  if (mode == "spec") {
    bool check4 = fabs(gal1.v - gal2.v) <= (link_z / (1 + gal1.z));
    final_check = check0 && check1 && check2 && check3 && check4;
  }
  else
    final_check = check0 && check1 && check2 && check3;
  return final_check;
}

void FoF::new_cluster (const Zbin &zbin, Galaxy* gal1, Galaxy *gal2) {
  // Function to create a new cluster.
  cluster_count++;
  Cluster cluster_here(cluster_count);
  gal1->in_cluster[zbin.num] = true;
  gal2->in_cluster[zbin.num] = true;
  cluster_here.add_gal(gal1);
  cluster_here.add_gal(gal2);
  list_of_clusters.push_back(std::move(cluster_here));
}

void FoF::add_member (const Zbin &zbin, Galaxy* gal, Cluster &cluster) {
  // Function to add a new member to an existing cluster.
  gal->in_cluster[zbin.num] = true;
  cluster.add_gal(gal);
}

int FoF::find_friends (const Zbin &zbin, Galaxy &gal, double rfriend, std::vector<Galaxy> &gal_list, const Kdtree &tree) {
  //! Function to find galaxies linked to the galaxy in question.
  /**< Loop through kd-tree nodes */

  std::deque<Galaxy*> myfriends;
  int unused_nodes;
  
  unused_nodes = tree.range_search(gal, rfriend, myfriends);
  
  std::deque<Galaxy*>::iterator itr;
  for(itr=myfriends.begin(); itr != myfriends.end(); itr++) {
    int gal_now = (*itr)->num;
    if(friendship(zbin, gal, gal_list[gal_now], rfriend)) {
      /**< Create new cluster */
      if(!gal.in_cluster[zbin.num]) { 
        new_cluster(zbin, &gal, &gal_list[gal_now]);
        //std::cout << "== nc zbin " << zbin.num << " gal " << gal_now << std::endl;
      }
      /**< Add new member to existing cluster */
      else {
        add_member(zbin, &gal_list[gal_now], list_of_clusters[cluster_count]);
        //std::cout << "== am zbin " << zbin.num << " gal " << gal_now << " cl " << cluster_count << std::endl;
      }
    }
  }
  
  myfriends.clear();
  return unused_nodes;
}

int FoF::find_friends_of_friends (const Zbin &zbin, Cluster &cluster, 
				   double rfriend, std::vector<Galaxy> &gal_list, 
				   const Kdtree &tree){
  // Function to find the galaxies linked to existing cluster members.
  /* Loop through cluster members */
  int unused_nodes = 0;
  for(int i = 0; i < cluster.mem.size(); i++) {
    unused_nodes += find_friends(zbin, gal_list[cluster.mem[i]->num], rfriend, gal_list, tree);
  } /* end of cluster member loop */
  return unused_nodes;
}

int FoF::friends_of_friends (int bin_num, const std::vector<Zbin> &zbin_list, 
			      std::vector<Galaxy> &gal_list, const Kdtree &tree) {
  // Funciton find friends-of-friends in a given redshift bin.
  if (bin_num < 0)
    throw BadArgumentException("FoF::friends_of_friends", "bin_num", ">= 0.0");
  if (link_r <= 0)
    throw RuntimeException("FoF::friends_of_friends", "link_r", "> 0.0");
  if (link_z <= 0)
    throw RuntimeException("FoF::friends_of_friends", "link_z", "> 0.0");
  cluster_count = -1;
  Zbin zbin = zbin_list[bin_num];
  double rfriend = zbin.rfriend;
  int unused_nodes = 0;
  /* Loop through galaxies */
  for(int i = 0; i < gal_list.size(); i++) {
    /* Modify rfriend for spectroscopic mode */
    if (mode == "spec") rfriend = zbin_list[gal_list[i].bin].link_r / gal_list[i].da;
    /* Check if galaxy is already in a cluster (f-loop) */
    if(!gal_list[i].in_cluster[zbin.num] && bin_check(zbin, gal_list[i])) { 
      unused_nodes += find_friends(zbin, gal_list[i], rfriend, gal_list, tree);
      /* Check if galaxy is now in a cluster (fof-loop) */
      if(gal_list[i].in_cluster[zbin.num])
	unused_nodes += find_friends_of_friends(zbin, list_of_clusters[cluster_count], rfriend, gal_list, tree);
    }
  } /* end of galaxy loop */
  return unused_nodes;
}

void FoF::remove (int min_ngal) {
  // Function that removes clusters that have too few members.
  if (min_ngal <= 0)
    throw BadArgumentException("FoF::remove", "min_ngal", "> 0.0");
  std::vector<int> remove_list;
  /* Loop through clusters */
  for(int i = 0; i < list_of_clusters.size(); i++) {
    list_of_clusters[i].unique();
    /* Check if cluster has less than the minimum number of members */
    if(list_of_clusters[i].mem.size() < min_ngal)
      remove_list.push_back(i);
  }
  /* Loop backwards through list of items to be removed */
  for(int i = remove_list.size(); i --> 0;)
    list_of_clusters.erase(list_of_clusters.begin() + remove_list[i]);
}
