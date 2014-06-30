#include "galaxy_class.hpp"
#include "cluster_class.hpp"
#include "merge_class.hpp"

#include <iostream>
#include <sstream>

int main (int argc, char *argv[]) {
  
  std::cout<<"THIS IS TEST CODE:"<<std::endl;
  
  Galaxy gal1 (0, 200135060, 42.088, -1.911, 0.866);
  Galaxy gal2 (1, 1270026, 40.730, -1.474, 0.387);
  Galaxy gal3 (2, 1600017, 40.729, -1.487, 0.559);
  Galaxy gal4 (3, 16000017, 42.099, -1.908, 0.489);
  Galaxy gal5 (4, 872389798, 40.725, -1.481, 0.420);
  Galaxy gal6 (5, 9890480, 40.746, -1.497, 0.414);
  Galaxy gal7 (6, 33, 44.729, -1.487, 0.559);

  Cluster cl1 (0);
  cl1.add_gal(gal1);
  cl1.add_gal(gal2);
  cl1.add_gal(gal3);
  cl1.add_gal(gal4);
  cl1.add_gal(gal7);

  Cluster cl2 (0);
  cl2.add_gal(gal3);
  cl2.add_gal(gal5);
  cl2.add_gal(gal6);
  cl2.add_gal(gal2);
  cl2.add_gal(gal7);

  cl1.unique();
  cl1.assign_props();

  cl2.unique();
  cl2.assign_props();

  std::vector<Cluster> list_of_clusters;

  list_of_clusters.push_back(cl1);
  list_of_clusters.push_back(cl2);

  Merge merge_clusters(list_of_clusters);

  for (int i = 0; i < list_of_clusters.size(); i++) {
    list_of_clusters[i].unique();
    list_of_clusters[i].assign_props();
    for (int j = 0; j < list_of_clusters[i].mem.size(); j++)
      std::cout<<list_of_clusters[i].ngal<<" "<<list_of_clusters[i].mem[j].id<<" "
	       <<list_of_clusters[i].mem[j].ra<<std::endl;
  }
}
