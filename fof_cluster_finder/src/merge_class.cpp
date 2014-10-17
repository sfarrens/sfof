/*Class for merge clusters*/

#include "merge_class.hpp"
#include <map>
#include <iostream>

bool Merge::gal_in_clt (const Galaxy &gal, const Cluster &clt) {
    // Function to check if a Galaxy instance is a member of a Cluster instance.
    return std::find(clt.mem.begin(), clt.mem.end(), gal) != clt.mem.end();
}

bool Merge::check_mem (const Cluster &clt1, const Cluster &clt2) {
    // Funciton to check if two Cluster instances share any Galaxy instances.
    /* Loop through cluster 1 members */
    for(int i = 0; i < clt1.mem.size(); i++)
        /* Check if member i is in cluster 2 */
        if(gal_in_clt(clt1.mem[i], clt2))
            return true;
    return false;
}

void Merge::assimilate (Cluster &clt1, Cluster &clt2) {
    // Function to assimilate members from one Cluster instance into another.
    /* Loop through cluster 2 members */
    for(int i = 0; i < clt2.mem.size(); i++)
        /* Add member i to cluster 1 */
        clt1.add_gal(clt2.mem[i]);
    /* Clear contents of cluster 2 */
    clt2.clear();
    clt1.unique();
}

void Merge::seek (std::vector<Cluster> &clusters) {
    // Find clusters with members in common.
    for(int i = 0; i < clusters.size(); i++)
        if(clusters[i].mem.size() > 0)
            for(int j = 0; j < clusters.size(); j++)
                if(clusters[j].mem.size() > 0 && i != j)
                    if(check_mem(clusters[i], clusters[j])) {
                        assimilate(clusters[i], clusters[j]);
                        j = 0;
                    }
}

bool first_time=true;

void Merge::join_uf(std::vector<Cluster> &clusters){
    for(int i = 0; i < clusters.size(); i++){
        if(first_time){
            for(int j=1; j<clusters[i].mem.size(); j++)
                std::cout << "gal_id "<< clusters[i].mem[j].id
                << " uf: " << (long long) clusters[i].mem[j].uf.parent << std::endl;
        }
        for(int j=1; j<clusters[i].mem.size(); j++){
            clusters[i].mem[j].uf.join(&clusters[i].mem[0].uf);
        }
        //  std::cout << "merged cluster " << clusters[i].mem.size() << " wide" << std::endl;
        if(first_time){
            std::cout << std::endl;
            for(int j=1; j<clusters[i].mem.size(); j++)
                std::cout << "gal_id "<< clusters[i].mem[j].id
                << " uf: " << (long long) clusters[i].mem[j].uf.parent << std::endl;
            first_time=false;
        }
    }

}

void Merge::rearrange_clusters(std::vector<Galaxy>& gals, std::vector<Cluster>& clus_vec){
    typedef std::vector<Galaxy>::iterator gal_it;
    typedef std::map<UnionFind*,Cluster>::iterator map_it;

    std::cout << std::endl;
    for(int j=1; j<clus_vec[0].mem.size(); j++)
        std::cout << "gal_id "<< clus_vec[0].mem[j].id
        << " uf: " << (long long) clus_vec[0].mem[j].uf.parent << std::endl;


    std::map<UnionFind*,Cluster> m;
    std::cout << "gals tot=" << gals.size() << std::endl;
    for(gal_it it = gals.begin(); it != gals.end(); ++it){
        if(it->uf.is_singlethon())
            continue;
        std::cout << "new map entry!!!" << std::endl;
        m[it->uf.find()].add_gal(*it);
    }
    clus_vec.clear();
    clus_vec.reserve(m.size());
    std::cout << "total real clusters:" << m.size() << std::endl;
    unsigned long long i=0;
    for(map_it it=m.begin(); it != m.end(); ++it){
        it->second.num=i;
        clus_vec.push_back(std::move(it->second));
        ++i;
    }
}

void Merge::destroy (std::vector<Cluster> &clusters) {
    // Function to erase empty Cluster instances.
    std::vector<int> remove_list;
    /* Loop through clusters */
    for(int i = 0; i < clusters.size(); i++) {
        /* Check if cluster is empty */
        if(clusters[i].mem.empty())
            remove_list.push_back(i);
    }
    /* Loop backwards through list of items to be removed */
    for(int i = remove_list.size(); i --> 0;)
        /* Erase empty cluster */
        clusters.erase(clusters.begin() + remove_list[i]);
}
