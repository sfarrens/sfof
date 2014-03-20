#include <iostream>

#include "../tools/tools.hpp"
#include "matrix.hpp"

void matrix::invert_two(double **m,double **m_inv){
  double det=m[1][1]*m[2][2]-m[1][2]*m[2][1];
  m_inv[1][1]= m[2][2]/det;
  m_inv[2][2]= m[1][1]/det;
  m_inv[1][2]=-m[1][2]/det;
  m_inv[2][1]=-m[2][1]/det;
}

void matrix::subt_two(double **m_a,double **m_b,double **m_ab){
  int i, j, k;
  for(i=1;i<=2;i++) for(j=1;j<=2;j++){m_ab[i][j]=m_a[i][j] - m_b[i][j];}
}

void matrix::mult_two(double **m_a,double **m_b,double **m_ab){
  int i, j, k;
  for(i=1;i<=2;i++)
    for(j=1;j<=2;j++){
      m_ab[i][j]=0.;
      for(k=1;k<=2;k++) m_ab[i][j]+= m_a[i][k]*m_b[k][j];
    }
} 

double matrix::det_two(double **m){return (m[1][1]*m[2][2]-m[1][2]*m[2][1]);}
double matrix::trace_two(double **m){return (m[1][1]+m[2][2]);}
