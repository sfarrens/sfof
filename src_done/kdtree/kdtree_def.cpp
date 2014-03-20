#include "./treenode.hpp"
#include <float.h>

TreeNode::TreeNode() {
  LV = 0;
  BN = 0;
  maxLV = 0;
  NOBJ = 0;
  obj = NULL;
  min = NULL;
  max = NULL;
  mmin = NULL;
  mmax = NULL;
  NUSE = 0;
}

TreeNode::TreeNode(int L, int mL, int N, int nm, 
		   int nt, int bn, int nus) {
  LV = L;
  BN = bn;
  maxLV = mL;
  NOBJ = N;
  NT = nt;
  NC = nm+NT;
  NM = nm;
  NUSE = nus;
  obj = new Object_kdtree[NOBJ];
  for(int i=0; i<NOBJ; ++i) {
    obj[i].m = new double[NM];
    obj[i].m_orig = new double[NM];
    obj[i].trues = new double[NT];
    for(int j=0; j<NM; ++j) {
      obj[i].m[j] = 0.0;
      obj[i].m_orig[j] = 0.0;
    }
    for(int j=0; j<NT; ++j) {obj[i].trues[j] = 0.0;}
  }
  min = new double[NM];
  max = new double[NM];
  mmin = new double[NM];
  mmax = new double[NM];
  for(int j=0; j<NM; ++j) {
    min[j] = -FLT_MAX;
    max[j] = FLT_MAX;
    mmin[j] = -FLT_MAX;
    mmax[j] = FLT_MAX;
  }
  low=NULL;
  high=NULL;
}

TreeNode::~TreeNode() {clear();}

void TreeNode::delete_stuff() {
  if (obj != NULL) {
    for(int i=0; i<NOBJ; ++i){
      if (obj[i].m != NULL) {delete [] obj[i].m; obj[i].m=NULL;}
      if (obj[i].m_orig != NULL) {delete [] obj[i].m_orig;obj[i].m_orig=NULL;}
      if (obj[i].trues != NULL) {delete [] obj[i].trues;obj[i].trues=NULL;}
    }
    delete [] obj; obj=NULL;
  }
}

void TreeNode::clear(){
  if (this != NULL) {
    delete_stuff();
    if (min != NULL) {delete [] min; min=NULL;}
    if (max != NULL) {delete [] max; max=NULL;}
    if (mmin != NULL) {delete [] mmin; mmin=NULL;}
    if (mmax != NULL) {delete [] mmax; mmax=NULL;}
    if (low != NULL) {low->clear(); low=NULL;}
    if (high != NULL) {high->clear(); high=NULL;}
  }
}
