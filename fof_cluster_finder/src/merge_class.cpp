/*Class for merge clusters*/

#include "merge_class.hpp"

bool Merge::gal_in_clt (const Galaxy &gal, const Cluster &clt) {
  //! Function to check if a Galaxy instance is a member of a Cluster instance.
  return std::find(clt.mem.begin(), clt.mem.end(), gal) != clt.mem.end();
}

bool Merge::check_mem (const Cluster &clt1, const Cluster &clt2) {
  //! Funciton to check if two Cluster instances share any Galaxy instances.
  /**< Loop through cluster 1 members */
  for(int i = 0; i < clt1.mem.size(); i++) 
    /**< Check if member i is in cluster 2 */
    if(gal_in_clt(clt1.mem[i], clt2))
      return true;
  return false;
}

void Merge::assimilate (Cluster &clt1, Cluster &clt2) {
  //! Function to assimilate members from one Cluster instance into another.
  /**< Loop through cluster 2 members */
  for(int i = 0; i < clt2.mem.size(); i++) 
    /**< Add member i to cluster 1 */
    clt1.add_gal(clt2.mem[i]);
  /**< Clear contents of cluster 2 */
  clt2.clear();
  clt1.unique();
}

void Merge::seek (std::vector<Cluster> &clusters) {
  //! Find clusters with members in common.
  for(int i = 0; i < clusters.size(); i++)
    if(clusters[i].mem.size() > 0)
      for(int j = 0; j < clusters.size(); j++)
	if(clusters[j].mem.size() > 0 && i != j)
	  if(check_mem(clusters[i], clusters[j])) {
	    assimilate(clusters[i], clusters[j]);
	    j = 0;
	  }
}

void Merge::destroy (std::vector<Cluster> &clusters) {
  //! Function to erase empty Cluster instances.
  std::vector<int> remove_list;
  /**< Loop through clusters */
  for(int i = 0; i < clusters.size(); i++) {
    /**< Check if cluster is empty */
    if(clusters[i].mem.empty())
      remove_list.push_back(i);
  }
  /**< Loop backwards through list of items to be removed */
  for(int i = remove_list.size(); i --> 0;)
    /**< Erase empty cluster */
    clusters.erase(clusters.begin() + remove_list[i]);
}
