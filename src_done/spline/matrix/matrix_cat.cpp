#include <iostream>
#include <fstream>
 
#include "../tools/tools.hpp"
#include "./matrix.hpp"

void matrix::myludcmp(double **a, int n,int *indx, double *d){
  int	i;
  for (i = 0; i < n; i++) a[i]--;
  cat_ludcmp(a - 1, n, indx - 1, d);
  for (i = 0; i < n; i++) a[i]++;
}

void matrix::mylubksb(double **a, int n, int *indx, double *b){
  int	i;
  for (i = 0; i < n; i++) a[i]--;
  cat_lubksb(a - 1, n, indx - 1, b - 1);
  for (i = 0; i < n; i++) a[i]++;
}

void matrix::cat_ludcmp(double **a, int n, int *indx, double *d){
  int i,imax,j,k;
  double big,dum,sum,temp,TINY=1.0e-20;
  double *vv,*dvector();
  void nrerror(),free_dvector();
  vv=tools::dvector(1,n);
  *d=1.0;
  for (i=1;i<=n;i++) {
    big=0.0;
    for (j=1;j<=n;j++)
      if ((temp=fabs(a[i][j])) > big) big=temp;
    if (big == 0.0) error("Singular matrix in routine CAT_LUDCMP");
    vv[i]=1.0/big;
  }
  for (j=1;j<=n;j++) {
    for (i=1;i<j;i++) {
      sum=a[i][j];
      for (k=1;k<i;k++) sum -= a[i][k]*a[k][j];
      a[i][j]=sum;
    }
    big=0.0;
    for (i=j;i<=n;i++) {
      sum=a[i][j];
      for (k=1;k<j;k++)
	sum -= a[i][k]*a[k][j];
      a[i][j]=sum;
      if ( (dum=vv[i]*fabs(sum)) >= big) {
	big=dum;
	imax=i;
      }
    }
    if (j != imax) {
      for (k=1;k<=n;k++) {
	dum=a[imax][k];
	a[imax][k]=a[j][k];
	a[j][k]=dum;
      }
      *d = -(*d);
      vv[imax]=vv[j];
    }
    indx[j]=imax;
    if (a[j][j] == 0.0) a[j][j]=TINY;
    if (j != n) {
      dum=1.0/(a[j][j]);
      for (i=j+1;i<=n;i++) a[i][j] *= dum;
    }
  }
  tools::free_dvector(vv,1,n);
}

void matrix::cat_lubksb(double **a, int n, int *indx, double *b){
  int i,ii=0,ip,j;
  double sum;
  for (i=1;i<=n;i++) {
    ip=indx[i];
    sum=b[ip];
    b[ip]=b[i];
    if (ii)
      for (j=ii;j<=i-1;j++) sum -= a[i][j]*b[j];
    else if (sum) ii=i;
    b[i]=sum;
  }
  for (i=n;i>=1;i--) {
    sum=b[i];
    for (j=i+1;j<=n;j++) sum -= a[i][j]*b[j];
    b[i]=sum/a[i][i];
  }
}				

/* non destructuve inverse */
void matrix::invertmatrix(double **a, double **ainv, int n){
  int	i, j, *indx;
  double d, **A, **B;
  /* allocate internal arrays */
  indx = (int *) calloc(n, sizeof(int));
  A = (double **) calloc(n, sizeof(double *));
  B = (double **) calloc(n, sizeof(double *));
  A[0] = (double *) calloc(n * n, sizeof(double));
  B[0] = (double *) calloc(n * n, sizeof(double));
  for (i = 1; i < n; i++) {
    A[i] = A[0] + i * n;
    B[i] = B[0] + i * n;
  }
  /* make copy of input array a[][] */
  for (i = 0; i < n; i++) 
    for (j = 0; j < n; j++) A[i][j] = a[i][j];
  /* make tranpose of inverse B[][] */
  myludcmp(A, n, indx, &d);
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) B[i][j] = 0.0;
    B[i][i] = 1.0;
    mylubksb(A, n, indx, B[i]);
  }
  /* copy transpose B[][] to ainv[][] */
  for (i = 0; i < n; i++) 
    for (j = 0; j < n; j++) ainv[i][j] = B[j][i];
  /* free the internal arrays */
  free(indx);
  free(A[0]);
  free(B[0]);
  free(A);
  free(B);
}
