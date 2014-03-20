#include <iostream>
#include <fstream>
#include "./treenode.hpp"

void TreeNode::branch(int dir) { //branch using column dir-1
  unsigned long *indx; indx=tools::lvector(1,NOBJ);
  double *toSort; toSort=tools::dvector(1,NOBJ);
  if (LV < maxLV) {  
    //first, create the vector to be sorted
    for(int i=0; i<NOBJ; ++i) {toSort[i+1] = obj[i].m[dir];}
    //sort it
    spline::indexx(toSort, indx, NOBJ);
    spline::sort(toSort, NOBJ);
    double cut = median(toSort, NOBJ);
    if (LV > maxLV-1) {
      std::cout << "LV = " << LV << ", cut = " << cut << ", NOBJ = " 
	   << NOBJ << ", ";
      for (int i=0; i<NM; ++i) {
	std::cout << "min[" << i << "] = " << min[i] << ", max[" 
	     << i << "] = " << max[i] << ",  ";
      }
      std::cout << std::endl;
    }
    int c = NOBJ/2;
    while (toSort[c] <= cut) {c++;  }
    int L = c;
    int R = NOBJ-c;
    int nextdir = (dir+1) % NUSE; //next cut direction
    //create the left branch
    low = new TreeNode(LV+1, maxLV, L, NM, NT, 2*BN, NUSE);
    for(int i=0; i<L; ++i) {
      for(int j=0; j<NM; ++j) {
	low->obj[i].m[j] = obj[(int)indx[i+1]-1].m[j];
	low->obj[i].m_orig[j] = obj[(int)indx[i+1]-1].m_orig[j];
      }
      for(int j=0; j<NT; ++j)
	low->obj[i].trues[j] = obj[(int)indx[i+1]-1].trues[j];
    }

    for(int j=0; j<NM; ++j) {
      low->min[j] = min[j];
      low->max[j] = max[j];
      low->mmin[j] = mmin[j];
      low->mmax[j] = mmax[j];
    }
    low->min[dir] = toSort[1];
    low->max[dir] = cut;
    low->mmax[dir] = cut;
    //create the right branch
    high = new TreeNode(LV+1, maxLV, R, NM, NT, 2*BN+1, NUSE);
    for(int i=0; i<R; ++i) {
      for(int j=0; j<NM; ++j) {
	high->obj[i].m[j] = obj[(int)indx[L+i]-1].m[j];
	high->obj[i].m_orig[j] = obj[(int)indx[L+i]-1].m_orig[j];
      }
      for(int j=0; j<NT; ++j)
	high->obj[i].trues[j] = obj[(int)indx[L+i]-1].trues[j];
    }
    for(int j=0; j<NM; ++j) {
      high->min[j] = min[j];
      high->max[j] = max[j];
      high->mmin[j] = mmin[j];
      high->mmax[j] = mmax[j];
    }
    high->min[dir] = cut;
    high->mmin[dir] = cut;
    high->max[dir] = toSort[NOBJ];
    delete_stuff();
   delete_stuff();
    low->branch(nextdir);  //branch further if necesary
    high->branch(nextdir); //branch further if necesary
  }
  tools::free_lvector(indx,1,NOBJ);
  tools::free_dvector(toSort,1,NOBJ);
  return;
}

double TreeNode::median(double *vec, unsigned long N) {
  //Assume: the vector toSort must be sorted first!!!
  if (N % 2 == 0) return ((vec[N/2-1] + vec[N/2])*0.5);
  else return (vec[N/2]);
}
