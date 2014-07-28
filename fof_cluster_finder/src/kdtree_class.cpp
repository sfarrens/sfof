/*Class for storing kdtree properties*/

#include "kdtree_class.hpp"
#include <algorithm>
#include <iostream>

void Kdtree::set_kdtree (std::vector<Galaxy> &gals, int max_depth_val) {
  // Set up a Kdtree instance.
  max_depth = max_depth_val;
  gaps_ptrs.reserve(gals.size());
    unsigned long long size = gals.size();
    Galaxy* ptr = gals.data();
    for(size_t i=0; i<size; ++i)
      gaps_ptrs.push_back(ptr++);
    unsigned long long elems = gaps_ptrs.end() - gaps_ptrs.begin();
    std::cout << "elems " << elems << std::endl;
    build_kdtree(gaps_ptrs.begin(),gaps_ptrs.end(),0);
    unsigned long long check = 0;
    for(std::vector<Kdtree_node>::iterator it= node_list.begin(); it != node_list.end(); ++it)
        check += it->members.size();
    std::cout << "check " << check << std::endl;
};

#if __cplusplus >= 201103L
inline void sort_by_ra(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end){
    std::sort(begin,end,
            [](Galaxy* a, Galaxy* b)->bool{
        return a->ra < b->ra;
    }
    );
}

inline void sort_by_dec(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end){
    std::sort(begin,end,
            [](Galaxy* a,Galaxy*  b)->bool{
        return a->dec < b->dec;
    }
    );
}

#else

class GalaxyCompRa{
public:
    GalaxyCompRa(){}
    bool operator()(Galaxy* a,Galaxy*  b) const{
        return a->ra < b->ra;
    }
};

class GalaxyCompDec{
public:
    GalaxyCompDec(){}
    bool operator()(Galaxy* a,Galaxy*  b) const{
        return a->dec < b->dec;
    }
};

inline void sort_by_ra(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end){
    std::sort(begin,end,GalaxyCompRa());
}

inline void sort_by_dec(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end){
    std::sort(begin,end,GalaxyCompDec());
}

#endif


void Kdtree::build_kdtree(
        std::vector<Galaxy*>::iterator begin,
        std::vector<Galaxy*>::iterator end,
        int depth){
  // Build kd-tree.
    unsigned long long elems = end - begin;
    if(elems == 0) return;
    if (elems == 1 || depth == max_depth){
        Kdtree_node node(begin,end);
        node_list.push_back(node);
    }else{
        int axis = depth % 2;
        if (axis == 1)
            sort_by_ra(begin,end);
        else
            sort_by_dec(begin,end);

        unsigned long long half = elems/2;
        build_kdtree(begin,begin+half, depth + 1);
        build_kdtree(begin+half,end, depth + 1);
    }
}
