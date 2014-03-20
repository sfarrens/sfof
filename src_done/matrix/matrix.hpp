#ifndef _MATRIX_HPP_
#define _MATRIX_HPP_

#include <iostream>
 
#include "../tools/tools.hpp"
#include "../vector/vector.hpp"

class matrix{
private:
  static const int DEFAULT_ALLOC=2;
  static void error(char error_text[]){
    double error_matrix;
    fprintf(stderr,"Run-time error in matrix...\n");
    fprintf(stderr,"%s\n",error_text);
    fprintf(stderr,"...now exiting to system...\n");
    std::cin>>error_matrix;
    exit(1);
  }

  class vector_class *mtrx;
  int *n_row,*n_col;
public:
  // Constructors and Destructors

  matrix();
  matrix(int row, int col);
  matrix(const matrix &s);
  matrix(double **mat, int row, int col);
  matrix(std::string name);
  ~matrix();


  // Save and retrieve matrix to file
  void save(std::string name);
  void retrieve(std::string name);

  void matrix_init(int a, int b);
  void matrix_init(double **mat, int a, int b);


  // Matrix operators
  matrix& operator =(const matrix& s);
  vector_class& operator[](const int i);
  vector_class operator*(const vector_class&);
  friend matrix operator*(const double&, const matrix&);
  friend matrix operator*(const matrix&, const double&);
  matrix operator*(const matrix& a);
  matrix operator+(const matrix& a);
  matrix operator-(const matrix& a);
  matrix transpose();
  //matrix inverse();

  // Set retrieve values manually
  void set(double val, int a, int b) {mtrx[a-1][b]=val;};
  double value(int a, int b){return mtrx[a-1][b];};
  int row_no(){return *n_row;};
  int col_no(){return *n_col;};

  // Print matrix to screen
  void print();
  static void print(double **mat, int a, int b);

  // Trace and Det of matrix.
  double trace();
  double det();
  double ln_det();
  double mat_det(double **mat,int n_row);
  void adjoint(double **adj);

  static void mult(double **a, int ac, int ar, 
		   double **b, int bc, int br, double **tmp);

  // Simple routines for 2x2 matrices
  static void invert_two(double **m,double **m_inv);
  static void subt_two(double **m_a,double **m_b,double **m_ab); 
  static void mult_two(double **m_a,double **m_b,double **m_ab);
  static double det_two(double **m);
  static double trace_two(double **m);

  // Matrix LU decompositions
  static void gauss_jordan(double **a, int n, double **b, int m);
  static void lu_decomp(double **a, int n, int *indx, double *d);
  static void lu_back_sub(double **a, int n, int *indx, double *b);
  static void lu_inverse(double **a, int n);
  static double lu_det(double **a, int n);
  static double lu_ln_det(double **a, int n);
  static void lu_improve(double **a, double *b, int n, double *x);

  // Matrix SVD decompositions
  static void svd_decomp(double **a, double *w, double **v, int m, int n);
  static void svd_back_sub(double **u, double *w, double **v, 
			   int m, int n, double *b, double *x);
  static double pythag(double a, double b);

  // Matrix QR decompositions
  static void qr_decomp(double **a, int n, double *c, double *d, int *sing);
  static void qr_back_sub(double **a,int n,double *c,double *d,double *b);
  static void qr_update(double **r, double **qt, int n, double *u, double *v);
  static void rsolv(double **a, int n, double *d, double *b);
  static void rotate(double **r,double **qt,int n,int i,double a,double b);

  // Matrix eigenvectors stuff
  static void balance(double **a, int n);
  static void hess_red(double **a, int n);
  static void hess_eigen(double **a, int n, double *wr, double *wi);
  static void eigen(double **a, int n, double *wr, double *wi);

  // Matrix catalogue
  static void myludcmp(double **a, int n,int *indx, double *d);
  static void mylubksb(double **a, int n, int *indx, double *b);
  static void cat_ludcmp(double **a, int n,int *indx, double *d);
  static void cat_lubksb(double **a, int n, int *indx, double *b);
  static void invertmatrix(double **a, double **ainv, int n);

  // Matrix data_nd
  static void weightedsvdlsq(double **p, double *y,double *sig, int ndata, 
			     double *a, int ma, double *chisq, 
			     double *maxoff, int *nuse, double TOL,
			     bool verbose);
  static void svdlsq(double **p, double *y, int ndata, double *a, int ma, 
		     double *chisq, double *maxoff, int *nuse,
		     double TOL,bool verbose);

  // Contingency tables
  static void cntab1(int **nn, int ni, int nj, double *chisq, double *df, 
		     double *prob,double *cramrv, double *ccc);
  static void cntab2(int **nn,int ni,int nj,
		     double *h,double *hx,double *hy,double *hygx,double *hxgy,
		     double *uygx,double *uxgy,double *uxy);
  double contin_cramer();
  double contin_c();
  double contin_prob();
  double contin_entropy();

  friend class mcmc;
};

#endif
