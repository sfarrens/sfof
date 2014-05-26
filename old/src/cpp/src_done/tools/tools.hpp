#ifndef _TOOLS_HPP_
#define _TOOLS_HPP_

#include <cmath>
#include <vector>
#include <sstream>
#include <string>
 
#include "./string_safe.hpp"

namespace tools {
  static int NR_END1 = 1;
  void error(char error_text[]);

  // Allocation of vectors[nl..nh] with different types  
  float *fvector(int nl, int nh);
  int *ivector(int nl, int nh);
  unsigned char *cvector(int nl, int nh);
  char *chvector(int nl, int nh);
  unsigned long *lvector(int nl, int nh);
  double *dvector(int nl, int nh);
  bool *bvector(int nl, int nh);
 
  // Deallocation of vectors[nl..nh] with different types 
  void free_fvector(float *v, int nl, int nh);
  void free_ivector(int *v, int nl, int nh);
  void free_cvector(unsigned char *v, int nl, int nh);
  void free_chvector(char *v, int nl, int nh);
  void free_lvector(unsigned long *v, int nl, int nh);
  void free_dvector(double *v, int nl, int nh);
  void free_bvector(bool *v, int nl, int nh);

  // Allocation of matrices[nrl..nrh][ncl..nch] with different types  
  float **fmatrix(int nrl, int nrh, int ncl, int nch);
  double **dmatrix(int nrl, int nrh, int ncl, int nch);
  int **imatrix(int nrl, int nrh, int ncl, int nch);
  float **submatrix(float **a, int oldrl, int oldrh, int oldcl, int oldch,
		    int newrl, int newcl);
  float **convert_matrix(float *a, int nrl, int nrh, int ncl, int nch);

  // Deallocation of matrices[nrl..nrh][ncl..nch] with different types  
  void free_fmatrix(float **m, int nrl, int nrh, int ncl, int nch);
  void free_dmatrix(double **m, int nrl, int nrh, int ncl, int nch);
  void free_imatrix(int **m, int nrl, int nrh, int ncl, int nch);
  void free_submatrix(float **b, int nrl, int nrh, int ncl, int nch);
  void free_convert_matrix(float **b, int nrl, int nrh, int ncl, int nch);

  // Allocation of tensor[nrl..nrh][ncl..nch][ndl..ndh] with different types  
  float ***f3tensor(int nrl, int nrh, int ncl, int nch, 
		    int ndl, int ndh);
  double ***d3tensor(int nrl, int nrh, int ncl, int nch, 
		     int ndl, int ndh);

  // Deallocation of tensor[nrl..nrh][ncl..nch][ndl..ndh] with different types 
  void free_f3tensor(float ***t, int nrl, int nrh, int ncl, int nch,
		     int ndl, int ndh);
  void free_d3tensor(double ***t, int nrl, int nrh, int ncl, int nch,
		     int ndl, int ndh);

  // Basic operations
  static float f_sqr(float a) {return ((a) == 0.0 ? 0.0 : a*a);};
  static double d_sqr(double a) {return ((a) == 0.0 ? 0.0 : a*a);};
  static float f_min(float a, float b){return ((a),(b),(a)<(b)?(a):(b));};
  static float f_max(float a, float b){return ((a),(b),(a)>(b)?(a):(b));};
  static double d_min(double a, double b){return ((a),(b),(a)<(b)?(a):(b));};
  static double d_max(double a, double b){return ((a),(b),(a)>(b)?(a):(b));};
  static long l_min(long a, long b){return ((a),(b),(a)<(b)?(a):(b));};
  static long l_max(long a, long b){return ((a),(b),(a)>(b)?(a):(b));};
  static int i_min(int a, int b){return ((a),(b),(a)<(b)?(a):(b));};
  static int i_max(int a, int b){return ((a),(b),(a)>(b)?(a):(b));};
  double gauss_here(double z, double i);
  void separate_line(const std::string &buffer, 
		     std::vector<std::string> &data);
  // Functions used for input / output.
  void skip_comments(std::ifstream& fstr);
  bool get_next_dataline(std::ifstream& file, std::string& line);
  void find_NR_NC(const class string_safe &filename, int &NR, int &NC);
};

static double dmaxarg1,dmaxarg2;
#define DMAX(a,b) (dmaxarg1=(a),dmaxarg2=(b),(dmaxarg1) > (dmaxarg2) ?\
          (dmaxarg1) : (dmaxarg2))

static double dminarg1,dminarg2;
#define DMIN(a,b) (dminarg1=(a),dminarg2=(b),(dminarg1) < (dminarg2) ?\
        (dminarg1) : (dminarg2))

static int imaxarg1,imaxarg2;
#define IMAX(a,b) (imaxarg1=(a),imaxarg2=(b),(imaxarg1) > (imaxarg2) ?\
        (imaxarg1) : (imaxarg2))

static int iminarg1,iminarg2;
#define IMIN(a,b) (iminarg1=(a),iminarg2=(b),(iminarg1) < (iminarg2) ?\
        (iminarg1) : (iminarg2))

#define SIGN(a,b) ((b) >= 0.0 ? fabs(a) : -fabs(a))
void *km_malloc(size_t size);

class tools_var{
public:
  static std::string dir;
};

#endif

