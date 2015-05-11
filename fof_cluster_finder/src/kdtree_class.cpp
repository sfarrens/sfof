/*Class for storing kdtree properties*/

#include <fstream>
#include <iomanip>
#include <iostream>
#include "kdtree_class.hpp"


void Kdtree::Kdtree_node::print_node_info(class Kdtree_node *node, const std::vector<Galaxy> &myAllG)
{
  if(node->Gal == NULL)
    std::cout << "\t NODE: split at " << node->center.P[node->axis] << " on axis " << node->axis << " [ " << node->Ngalaxies << "]" << std::endl;
  else
    std::cout << "\t\t GAL [" << node->Gal - myAllG.data() << "] :: ra: " << (node->Gal)->P.P[0] << " dec: " << (node->Gal)->P.P[1] << std::endl;
  return;
}

node_to_galaxy Kdtree::Kdtree_node::check_node(Point &origin, double sradius, int num)
    // check for rectangular intersection
    // note: radius[0] is expected to be the linking length, while radius[1] is
    // expected to be the squared linking length
    {
      double distance;
      //sradius *= FLTC;
      if(Gal != NULL) // it is a leaf
        {
          if(Gal->num == num)
            return External;
          distance = astro.angsep(Gal->P, origin);
          if(distance <= sradius)
            return Internal;
          else
            return External;
        }
      else // it is a node
        {
          distance = astro.angsep(center, origin);
          if(distance - radius > sradius)
            return External;
          if(distance + radius <= sradius)
            return Internal;
          else
            return Intersects;
        }
    }
    
void Kdtree::write_Kdtree(const std::string &output_file) {
  std::ofstream kdtree_file (output_file);
  kdtree_file << std::fixed << std::setprecision(6);
  for(int i = NNodes-1; i >= 0; i--) {
    if(Nodes[i].Gal == NULL){
      double xdelta = (Nodes[i].top_right.P[0] - Nodes[i].bottom_left.P[0]) / 2;
      double ydelta = (Nodes[i].top_right.P[1] - Nodes[i].bottom_left.P[1]) / 2;
      // writes the # of the node
      kdtree_file << i << " ";
      // writes coordiantes: center, xdelta, ydelta, radius
      kdtree_file << Nodes[i].center.P[0] << " " << Nodes[i].center.P[1] << " " 
		  << xdelta << " " << ydelta << " " << Nodes[i].radius << " ";
      // writes the splitting axis and the ratio of maximum side over the minimum side
      kdtree_file << Nodes[i].axis << " " << std::max(xdelta, ydelta) / std::min(xdelta, ydelta) 
		  << std::endl;
    }
  }
  kdtree_file.close();
}

void Kdtree::set_Kdtree(std::vector<Galaxy> &Gals, double max_inq = 0.3) {
    
  std::vector<Galaxy*>::iterator itr;
  Point box[2];
#ifdef TIMING
  clock_t t0, t1;
#endif
  SETPERIODIC(0, 360);
  AllG = Gals;
  max_axis_inequality = max_inq;
  Galaxy *G = Gals.data();
  GalPtrs.reserve(Gals.size());

  NNodes = 0;
  NLeaves = 0;

  for(int i=0; i < Gals.size(); i++)
    GalPtrs.push_back(G++);
  
  NMaxNodes = Gals.size()*2 + 1;
  Nodes = new Kdtree_node [NMaxNodes];

  box[0] = Gals[0].P;
  box[1] = Gals[0].P;
  itr = GalPtrs.begin() + 1;
  while(itr != GalPtrs.end()) {
    for(int i = 0; i < 2; i++) {
      if( (*itr)->P.P[i] < box[i].P[0] )
	box[i].P[0] = (*itr)->P.P[i];
      else if( (*itr)->P.P[i] > box[i].P[1] )
	box[i].P[1] = (*itr)->P.P[i];
    }
    itr++;
  }
          
#ifdef TIMING    
  for( int i = 0; i < N_TIMING; i++)
    timing[i] = 0;
#endif
#ifdef TIMING      
  t0 = clock();
#endif                
  root = build_kdtree(GalPtrs.begin(), GalPtrs.end(), box, 0);
#ifdef TIMING
  t1 = clock();
  timing[TREE_CONSTRUCTION] += GET_SECS(t1, t0);
#endif

  // KD-Tree Sample Area
  sample_area = std::abs(root->bottom_left.P[0] - root->top_right.P[0]) *
    std::abs(root->bottom_left.P[1] - root->top_right.P[1]);      
  
  std::cout << "   - with " << NNodes << " nodes and " << NLeaves << " leaves." << std::endl;
  std::cout << "   - [xmin, ymin][xmax, ymax] are : [" << root->bottom_left.P[0] << ", " 
	    << root->bottom_left.P[1] << "][" << root->top_right.P[0] <<", " << root->top_right.P[1] 
	    << "]" << std::endl;
  std::cout << "   - sample area: " << sample_area << " deg^2." << std::endl;
  return;
};





#if __cplusplus >= 201103L
  
inline void mynth( int N, int ax,
                     std::vector<Galaxy*>::iterator begin,
                     std::vector<Galaxy*>::iterator end) {
std::nth_element(begin, begin+N/2, end,
                   [&](Galaxy *G1, Galaxy *G2)->bool {return G1->P.P[ax] < G2->P.P[ax];});
}

inline std::vector<Galaxy*>::iterator mymax( int ax,
                                               std::vector<Galaxy*>::iterator begin,
                                               std::vector<Galaxy*>::iterator end) {
return std::max_element(begin, end,
                          [&](Galaxy *G1, Galaxy *G2)->bool {return G1->P.P[ax] < G2->P.P[ax];});
}

#else

class GalaxyCompCoord{
private:
    int ax_;
public:
GalaxyCompCoord(int ax):ax_(ax){}
bool operator()(Galaxy* A, Galaxy* B) const{
return A->P.P[ax_] < B->P.P[ax_];
}
};

inline void mynth( int N, int ax,
                     std::vector<Galaxy*>::iterator begin,
                     std::vector<Galaxy*>::iterator end) {
std::nth_element(begin, begin+N/2, end, GalaxyCompCoord(ax));
}

inline std::vector<Galaxy*>::iterator mymax( int ax,
                   std::vector<Galaxy*>::iterator begin,
                   std::vector<Galaxy*>::iterator end) {
return std::max_element(begin, end, GalaxyCompCoord(ax));
}


#endif

Kdtree::Kdtree_node* Kdtree::build_kdtree(std::vector<Galaxy*>::iterator begin,
                                          std::vector<Galaxy*>::iterator end,
                                          Point box[2],
                                          int depth)
{
  unsigned long long elems = end - begin;
  unsigned long long half;
  double split_value;
  
  if(elems == 0) {
    std::cout << "kdtree building error" << std::endl;
    exit(3);
  }
  
  if(elems == 1)
    {
      Nodes[NNodes].Gal = (*begin);
      Nodes[NNodes].left = NULL;
      Nodes[NNodes].right = NULL;
      Nodes[NNodes].bottom_left = (*begin)->P;
      Nodes[NNodes].top_right = (*begin)->P;
      Nodes[NNodes].Ngalaxies = 1;
      NLeaves++;       
    }
  else
    {
      Point mylengths, mybox[2];
      int axis;
      std::vector<Galaxy*>::iterator itr, half_node;

      mylengths.P[0] = (box[0].P[1] - box[0].P[0]); // length of axis 0
      mylengths.P[1] = (box[1].P[1] - box[1].P[0]); // length of axis 0
      
      if( fabs(mylengths.P[0] - mylengths.P[1]) / (std::max(mylengths.P[0], mylengths.P[1])) > max_axis_inequality)
        axis = (mylengths.P[1] > mylengths.P[0]);
      else
        axis = depth % 2;
      
      //std::nth_element(begin, begin+elems/2, end, [&](Galaxy *G1, Galaxy *G2)->bool {return G1->P.P[axis] < G2->P.P[axis];});
      mynth(elems, axis, begin, end);

      half_node = begin+elems/2;
      split_value = (*half_node)->P.P[axis];

      mybox[!axis] = box[!axis];

      //itr = std::max_element(begin, half_node, [&](Galaxy *G1, Galaxy *G2)->bool {return G1->P.P[axis] < G2->P.P[axis];});
      itr = mymax(axis, begin, half_node);
      
      mybox[axis].P[0] = box[axis].P[0];
      mybox[axis].P[1] = (*itr)->P.P[axis];
      Kdtree::Kdtree_node* leftN = Kdtree::build_kdtree(begin, half_node, mybox, depth+1);

      mybox[axis].P[0] = split_value;
      mybox[axis].P[1] = box[axis].P[1];
      Kdtree::Kdtree_node* rightN = Kdtree::build_kdtree(half_node, end, mybox, depth+1);
      

      Nodes[NNodes].Gal = NULL;
      Nodes[NNodes].left = leftN;
      Nodes[NNodes].right = rightN;
      Nodes[NNodes].axis = axis;
      Nodes[NNodes].Ngalaxies = elems;

      Nodes[NNodes].bottom_left.P[axis] = box[axis].P[0];
      Nodes[NNodes].bottom_left.P[!axis] = box[!axis].P[0];
      Nodes[NNodes].top_right.P[axis] = box[axis].P[1];
      Nodes[NNodes].top_right.P[!axis] = box[!axis].P[1];

      Nodes[NNodes].center.P[0] = (Nodes[NNodes].top_right.P[0] + Nodes[NNodes].bottom_left.P[0]) / 2.0;
      Nodes[NNodes].center.P[1] = (Nodes[NNodes].top_right.P[1] + Nodes[NNodes].bottom_left.P[1]) / 2.0;
      Nodes[NNodes].radius = astro.angsep(Nodes[NNodes].center, Nodes[NNodes].top_right);
    }
  
  NNodes++;
  if(NNodes > NMaxNodes)
    {
      std::cout << "reallocating Nodes from " << NMaxNodes << " to " << NMaxNodes*1.1 << std::endl;
      NMaxNodes *= 1.1;
      Nodes = (Kdtree_node*)realloc(Nodes, NMaxNodes * sizeof(Kdtree_node));
    }


  return &Nodes[NNodes-1];  
}


void Kdtree::WalkTree(class Kdtree_node *start, int mode)
  {
    
    if(start != NULL)
      {
        if(mode & 1)
          start->print_node_info(start, AllG);

        if(start->Gal != NULL)
          {
            if((start->Gal)->P.P[0] < MIN.P[0])
              MIN.P[0] = (start->Gal)->P.P[0];
            if((start->Gal)->P.P[1] < MIN.P[1])
              MIN.P[1] = (start->Gal)->P.P[1];
            if((start->Gal)->P.P[0] > MAX.P[0])
              MAX.P[0] = (start->Gal)->P.P[0];
            if((start->Gal)->P.P[1] > MAX.P[1])
              MAX.P[1] = (start->Gal->P).P[1];
          }
        
        if(start->left != NULL)
          WalkTree(start->left, mode);
        if(start->right != NULL)
          WalkTree(start->right, mode);
      }
  }


int Kdtree::range_search(Point &origin, int num, double link_r, std::deque<Galaxy*> &GalList) const
{
  return range_search_loop(root, origin, num, link_r, Intersects, GalList);
}
  
int Kdtree::range_search(Galaxy &G, double link_r, std::deque<Galaxy*> &GalList) const
{
  return range_search_loop(root, G.P, G.num, link_r, Intersects, GalList);
};

int Kdtree::range_search_loop(Kdtree_node *start, class Point &origin, int num, double radius, node_to_galaxy status, std::deque<Galaxy*> &GalList) const
{
    
    node_to_galaxy lstatus, rstatus;
    int ret = 0;
    
    if(status == External)
      return 1;
    
    if(start -> Gal != NULL) {
      if( ((start->Gal)->num != num) &&
          ((status == Internal) ||
           (start->check_node(origin, radius, num) == Internal) ) )
        GalList.push_back(start->Gal);
      else
        ret = 1;
    }
    else {
      if(status == Internal) {
        lstatus = Internal;
        rstatus = Internal;
      }
      else if(status == Intersects){
        lstatus = (start -> left) -> check_node(origin, radius, num);
        rstatus = (start -> right) -> check_node(origin, radius, num);
      }
      
      if(lstatus > External){
        int save = GalList.size();
        ret = range_search_loop(start->left, origin, num, radius, lstatus, GalList);
        if(GalList.size() == save)
          ret++;
      }
      if(rstatus > External) {
        int save = GalList.size();
        ret = range_search_loop(start->right, origin, num, radius, rstatus, GalList);
        if(GalList.size() == save)
          ret++;
      }
    }
    
    return ret;
  };

