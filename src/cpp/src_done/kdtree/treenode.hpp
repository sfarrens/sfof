#ifndef _TREENODE_HPP_
#define _TREENODE_HPP_

#include <iostream>

#include "../tools/tools.hpp"
#include "../spline/spline.hpp"
#include "../matrix/matrix.hpp"
#include "../tools/string_safe.hpp"
#include "./kdtree_struct.hpp"

typedef struct TreeNode *TreeNodePtr;
class TreeNode {
private:
  static void error(char error_text[]){
    double error_kdtree;
    fprintf(stderr,"Run-time error in TreeNode...\n");
    fprintf(stderr,"%s\n",error_text);
    fprintf(stderr,"...now exiting to system...\n");
    std::cin>>error_kdtree;
    exit(1);
  }
public:
  int NOBJ; //number of galaxies in obj
  int LV;   //level of the tree node
  int maxLV; //maximum level allowed
  int NC;  //number of columns in the data
  int NM;  //number of columns of magnitudes in the data
  int NT;  //number of columns of true outputs in data
  int BN;  //branch number
  int NUSE; //Use how many directions?
  double *min; //lower boundary of this node for column i
  double *max; //upper boundary of this node for column i
  double *mmin; //lower boundary of this node for column i
  double *mmax; //upper boundary of this node for column i
  Object_kdtree *obj;
  TreeNodePtr low;
  TreeNodePtr high;
  TreeNodePtr parent;

  // These are the constructors/destructors.
  // int L => level of the tree node
  // int mL => maximum level that the nodes are allowed to be
  // int N => the number of objects (galaxies) in this node
  // int nm => number of magnitudes in the galaxy structure
  // int nt => number of trues in the galaxy structure
  // int bn => branch number
  // int nus => how many directions?
  TreeNode();
  TreeNode(int L, int mL, int N, int nm, int nt, int bn, int nus);
  ~TreeNode(); 
  void delete_stuff();
  void clear();

  // This is the key routine in the TreeNode data structure.
  // This routine will make a single Kdtree cut in the direction 
  // Make sure that dir does not exceed the number of available columns.
  void branch(int dir);
  
  // Function to write the boundaries to a file
  void writeBoundaries(const class string_safe &filename);
  void writeBoundaries(FILE *file);

  // Function gets the leef node that contains the Galaxy gal.
  // It returns a pointer pointing to the TreeNode containing gal.
  TreeNodePtr getLeefContaining(Object_kdtree *gal);
  TreeNodePtr getLeefwithBN(int level, int branch_nb);

  // Returns the pointer pointing to the array of galaxies in this node.
  Object_kdtree* getObjects();

  // Returns the number of galaxies in this node
  int getNObjects();

  // Returns 1 if it is a leaf and 0 if it is a node.
  int isLeaf();
  
  // These functions get bias/sigma/sigma68 of the objects 
  // contained in this node.
  double getAverage(int i);
  double getSigma(int i, int j);
  double getSigma68(int i,int j);

  // Returns the boundary in i'th direction in dmin, dmax
  void getBoundary(int dir, double &dmin, double &dmax); 
  double getMinDist(double *testpt);
  double getMaxDist(double *testpt);

  // Returns the distance to boundary 
  double getDistanceToBoundary(Object_kdtree *gal);

  // Usefull routine to get binary number for given position
  int get_binary_nb(int number, int position);
  // Useful function to calculate the median of a given vector
  double median(double *vec, unsigned long N);
};

#endif
