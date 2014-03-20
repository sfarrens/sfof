#ifndef _KDTREE_STRUCT_HPP_
#define _KDTREE_STRUCT_HPP_

// This is a structure that holds most important information about a galaxy. 
typedef struct Object_kdtree *ObjectPtr_kdtree;
struct Object_kdtree {
  int NG;        //number of galaxies in branch number BN
  int BN;        //branch number
  int NT;        //number of trues in true vector
  int NM;        //number of magnitudes in the magnitude vector
  double *trues; //vector of trues
  double *m;     //magnitude vector
  double *m_orig;//magnitude original, if matrix non-diag
  int id;
};

#endif
