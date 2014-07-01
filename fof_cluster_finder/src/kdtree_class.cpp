/*Class for storing kdtree properties*/

#include "kdtree_class.hpp"
#include <algorithm>
#include <iostream>

void Kdtree::set_kdtree (std::vector<Galaxy> &gals, int max_depth_val) {
    //! Set up a Kdtree instance.
    max_depth = max_depth_val;
//  build_kdtree(gals, 0);
    gaps_ptrs.reserve(gals.size());
    unsigned long long size = gals.size();
    Galaxy* ptr = gals.data();
    for(auto i=0; i<size; ++i)
        gaps_ptrs.push_back(ptr++);
    unsigned long long elems = gaps_ptrs.end() - gaps_ptrs.begin();
    std::cout << "elems " << elems << std::endl;
    build_kdtree2(gaps_ptrs.begin(),gaps_ptrs.end(),0);
    unsigned long long check = 0;
    for(auto& node : node_list)
        check += node.members.size();
    std::cout << "check " << check << std::endl;
};

void Kdtree::build_kdtree (const std::vector<Galaxy> &gals, int depth) {
    //! Build kd-tree.
    int axis = depth % 2;
    if (depth <= max_depth) {
        if (depth == max_depth) {
            Kdtree_node node(gals);
            node_list.push_back(node);
        }
        std::vector<Galaxy> gals_left, gals_right;
        std::vector<double> ra_list, dec_list;
        for (int i = 0; i < gals.size(); i++) {
            ra_list.push_back(gals[i].ra);
            dec_list.push_back(gals[i].dec);
        }
        double median_val;
        for (int i = 0; i < gals.size(); i++) {
            if (axis == 1){
                median_val = astro.median(ra_list);
                if (ra_list[i] <= median_val)
                    gals_left.push_back(gals[i]);
                else
                    gals_right.push_back(gals[i]);
            }
            else {
                median_val = astro.median(dec_list);
                if (dec_list[i] <= median_val)
                    gals_left.push_back(gals[i]);
                else
                    gals_right.push_back(gals[i]);
            }
        }
        build_kdtree(gals_left, depth + 1);
        build_kdtree(gals_right, depth + 1);
    }
}


void Kdtree::build_kdtree2(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end,
        int depth){
    unsigned long long elems = end - begin;
    if(elems == 0) return;
    if (elems == 1 || depth == max_depth){
        Kdtree_node node(begin,end);
        node_list.push_back(node);
    }else{
        int axis = depth % 2;
        if (axis == 1){
            std::sort(begin,end,
                    [](Galaxy* a, Galaxy* b)->bool{
                return a->ra < b->ra;
            }
            );
        }else{
            std::sort(begin,end,
                    [](Galaxy* a,Galaxy*  b)->bool{
                return a->dec < b->dec;
            }
            );

        }
        unsigned long long half = elems/2;
        build_kdtree2(begin,begin+half, depth + 1);
        build_kdtree2(begin+half,end, depth + 1);
    }
}
