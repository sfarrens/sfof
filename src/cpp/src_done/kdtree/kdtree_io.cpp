#include <iostream>
#include <fstream>
#include "./treenode.hpp"

void TreeNode::writeBoundaries(const class string_safe &filename_here) {
  class string_safe filename;filename=filename_here;
  FILE *f = fopen(filename.c_str(), "w");
  if (f == NULL)
    error(const_cast<char *>("File open failed: filename in TreeNode::writeBoundaries"));
  writeBoundaries(f);
  fclose(f);
}

void TreeNode::writeBoundaries(FILE *file) {
  //Assume: the file *file has been opened properly
  if (LV == maxLV) {
    for(int j=0; j<NM; ++j) {
      fprintf(file, "%lf %lf ", min[j], max[j]);
    }
    fprintf(file, "\n");
  } else {
    low->writeBoundaries(file);
    high->writeBoundaries(file);
  }
}
