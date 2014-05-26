#include <iostream>

#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "./spline.hpp"

void spline::cubic_spline(double *x, double *y, int anf, int n,
			  double yp1, double ypn, double *y2){
  int i,k; double p,qn,sig,un,*u;
  u = tools::dvector(1,n-1);
  if (yp1 > 0.99e30) {y2[anf]=u[anf]=0.0;}
  else {
    y2[anf] = -0.5;
    u[anf]=(3.0/(x[anf+1]-x[anf]))*((y[anf+1]-y[anf])/(x[anf+1]-x[anf])-yp1);
  }
  for (i=anf+1;i<n;i++) {
    sig=(x[i]-x[i-1])/(x[i+1]-x[i-1]);
    p=sig*y2[i-1]+2.0;
    y2[i]=(sig-1.0)/p;
    u[i]=(y[i+1]-y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1]);
    u[i]=(6.0*u[i]/(x[i+1]-x[i-1])-sig*u[i-1])/p;
  }
  if (ypn > 0.99e30) {qn=un=0.0;}
  else {
    qn=0.5;
    un=(3.0/(x[n]-x[n-1]))*(ypn-(y[n]-y[n-1])/(x[n]-x[n-1]));
  }
  y2[n]=(un-qn*u[n-1])/(qn*y2[n-1]+1.0);
  for (k=n-1;k>=anf;k--)
    y2[k]=y2[k]*y2[k+1]+u[k];
  tools::free_dvector(u,1,n-1);
}

double spline::cubic_splint(double *xa, double *ya, double *y2a,
			    int n, double x){
  int klo,khi,k;
  double h,b,a,y;
  klo=1;
  khi=n;
  while (khi-klo > 1)
    {
      k=(khi+klo) >> 1;
      if (xa[k] > x) khi=k;
      else klo=k;
    }
  h=xa[khi]-xa[klo];
  if (h == 0.0) error((char *)"Bad xa input to routine spline::cubic_splint");
  a=(xa[khi]-x)/h;
  b=(x-xa[klo])/h;
  y=a*ya[klo]+b*ya[khi]+((a*a*a-a)*y2a[klo]+(b*b*b-b)*y2a[khi])*(h*h)/6.0;
  return y;
}

double spline::cubic_splint_der(double *xa, double *ya, double *y2a,
				int n, double x){
  int klo,khi,k;
  double h,b,a,y;
  klo=1;
  khi=n;
  while (khi-klo > 1)
    {
      k=(khi+klo) >> 1;
      if (xa[k] > x) khi=k;
      else klo=k;
    }
  h=xa[khi]-xa[klo];
  if (h == 0.0) 
    error((char *)"Bad xa input to routine spline::cubic_splint_der");
  a=(xa[khi]-x)/h;
  b=(x-xa[klo])/h;
  y=((ya[khi]-ya[klo])/(xa[khi]-xa[klo]))
     -(((3.0*a*a-1.0)/(6.0))*(xa[khi]-xa[klo])*y2a[klo])
     +(((3.0*b*b-1.0)/(6.0))*(xa[khi]-xa[klo])*y2a[khi]);
  return y;
}

