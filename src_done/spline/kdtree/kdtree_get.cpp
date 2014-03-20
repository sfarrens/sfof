#include <float.h>
#include "./treenode.hpp"

void TreeNode::getBoundary(int dir, double &dmin, double &dmax) 
{dmin = min[dir]; dmax = max[dir];}

double TreeNode::getMinDist(double *testpt) {
  int outside = 1;
  double dmin=0;
  double dist_min;
  for(int i=0;i<NUSE;i++){
    if((testpt[i]-max[i])*(testpt[i]-min[i]) > 0) outside *=0;
    dist_min=tools::d_min(fabs((testpt[i]-max[i])),fabs((testpt[i]-min[i])));
    dmin+=dist_min*dist_min;
  }
  dmin=sqrt(dmin);
  if (!outside) dmin = 0; 
  return dmin;
}

double TreeNode::getMaxDist(double *testpt) {
  int outside = 1;
  double dmax=0;
  double dist_max;
  for(int i=0;i<NUSE;i++){
    if((testpt[i]-max[i])*(testpt[i]-min[i]) > 0) outside *=0;
    dist_max=tools::d_max(fabs(testpt[i]-max[i]),fabs(testpt[i]-min[i]));
    dmax+=dist_max*dist_max;
  }
  dmax=sqrt(dmax);
  return dmax;
}

double TreeNode::getDistanceToBoundary(Object_kdtree *gal) {
  double r = FLT_MAX;
  for(int i=0; i<NM; ++i) {
    if ((double)abs((int)(gal->m[i]-min[i])) < r)
      r = (double)abs((int)(gal->m[i]-min[i]));
    if ((double)abs((int)(gal->m[i]-max[i])) < r)
      r = (double)abs((int)(gal->m[i]-max[i]));
  }
  return r;
}

//this function gets the leef node that contains the Galaxy gal 
TreeNodePtr TreeNode::getLeefContaining(Object_kdtree *gal) {
  int isOut = 0;
  for (int i=0; i<NM; ++i)
    isOut = isOut + (gal->m[i] < mmin[i]) + (gal->m[i] > mmax[i]);
  if (isOut > 0) return NULL;
  if (LV == maxLV) return this;
  TreeNodePtr p = low->getLeefContaining(gal);
  if (p != NULL) return p;
  return high->getLeefContaining(gal);
}

int TreeNode::get_binary_nb(int number, int position){
  if (pow(2.0,position-1) > number) return 0;
  int number_in=number, what_goes, remainder;
  for (int i=1;i<=position;i++){
    what_goes=number_in/2;
    remainder=number_in%2;
    number_in=what_goes;
  }
  return remainder;
}

TreeNodePtr TreeNode::getLeefwithBN(int level, int branch_nb) {
  TreeNodePtr p;
  p=this;
  for (int i=level; i>=1;i--){
    if (get_binary_nb(branch_nb,i) == 0){p=p->low;}
    if (get_binary_nb(branch_nb,i) == 1){p=p->high;}
  }
  return p;
}

//this function gets bias/sigma/sigma68 of the objects contained in this node 
double TreeNode::getAverage(int j) {
  double b = 0.0;
  for (int i=0; i<NOBJ; ++i) b += obj[i].trues[j];
  b = b / (double)NOBJ;
  return b;
}

double TreeNode::getSigma(int j, int jj) {
  double s = 0.0;
  for (int i=0; i<NOBJ; ++i) 
    s += (obj[i].trues[j] - obj[i].trues[jj])*
      (obj[i].trues[j] - obj[i].trues[jj]);
  s = sqrt(s / (double)NOBJ);
  return s;
}

double TreeNode::getSigma68(int j, int jj) {
  double s68 = 0.0;
  double *dd; dd=tools::dvector(1,NOBJ);
  for (int i=1; i<=NOBJ; ++i) dd[i] = fabs(obj[i].trues[j] - obj[i].trues[jj]);
  spline::sort(dd,NOBJ);
  s68 = dd[(2*NOBJ)/3];
  tools::free_dvector(dd,1,NOBJ);
  return s68;
}

Object_kdtree* TreeNode::getObjects() {return obj;}
int TreeNode::getNObjects() {return NOBJ;}

int TreeNode::isLeaf(){
  if(low == NULL && high == NULL) return 1;
  else return 0;
}
