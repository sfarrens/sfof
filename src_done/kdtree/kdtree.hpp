#ifndef _KDTREE_HPP_
#define _KDTREE_HPP_

#include <iostream>
#include <fstream>

#include "../tools/tools.hpp"
#include "../spline/spline.hpp"
#include "../matrix/matrix.hpp"
#include "../tools/string_safe.hpp"
#include "./kdtree_struct.hpp"
#include "./treenode.hpp"

class kdtree {
private:
  static void error(char error_text[]){
    double error_kdtree;
    fprintf(stderr,"Run-time error in kdtree...\n");
    fprintf(stderr,"%s\n",error_text);
    fprintf(stderr,"...now exiting to system...\n");
    std::cin>>error_kdtree;
    exit(1);
  }
public:
  int MAX_DEPTH;
  int NCUT;
  int NUSE_HERE;
  class string_safe trainfile;
  class string_safe testfile;
  class string_safe tag_here;
  class string_safe buffer;  
  int tNR, tNC;
  int pNR, pNC;
  int tNM,pNM,tNT,pNT,BN;
  
  Object_kdtree *galaxies;
  ObjectPtr_kdtree *galaxy_sep;
  TreeNodePtr tp;    
   class matrix mat_here;
 int *nb_leaf,*nb_leaf_2;
  TreeNode *trunk;

  kdtree();~kdtree();
  // In these functions only caching and 
  // setting the names of the files
  void set_depth(int N);
  void set_tag(const class string_safe &file);
  void set_train(const class string_safe &file);
  void set_matrix(const class string_safe &file);
  void set_kdtree_train(int nuse);
  void set_kdtree_train(int nus, int NC_train, int NR_train);
  // Can add trainning set from a file or directly from a command line
  void add_train_data();
  void add_train_data(int id, double *mag_orig, double *trues);
  // Set branch... So we here have made a kdtree...
  void set_branch();

  // Now post processing with the testing objects...
  void set_test(const class string_safe &file);
  void set_kdtree_test();
  void set_kdtree_test(int NC_test, int NR_test);
  void set_separate();
  void set_separate2();
  void add_data();
  void add_data(int id, double *mag_orig, double *trues);
  void do_separate();

  // Other functions
  void dump_files();
  int ret_depth(){return MAX_DEPTH;}
  // Functions used for input / output.
  void read_data(Object_kdtree *data, 
		 const class string_safe &filename, 
		 const int NR, const int NC, const int NT);
  void set_kdtree(int nus);
  void set_kdtree(int nus,int NC_train, int NR_train,int NC_test, int NR_test);
};

#endif
