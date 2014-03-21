#include "./matrix.hpp"

void matrix::balance(double **a, int n){
  int last,j,i;
  double s,r,g,f,c,sqrdx,RADIX=2.0;
  sqrdx=RADIX*RADIX;
  last=0;
  while (last == 0) {
    last=1;
    for (i=1;i<=n;i++) {
      r=c=0.0;
      for (j=1;j<=n;j++)
	if (j != i) {c += fabs(a[j][i]);r += fabs(a[i][j]);}
      if (c && r) {
	g=r/RADIX;f=1.0;s=c+r;
	while (c<g) {f *= RADIX;c *= sqrdx;}
	g=r*RADIX;
	while (c>g) {f /= RADIX;c /= sqrdx;}
	if ((c+r)/f < 0.95*s) {
	  last=0;
	  g=1.0/f;
	  for (j=1;j<=n;j++) a[i][j] *= g;
	  for (j=1;j<=n;j++) a[j][i] *= f;
	}
      }
    }
  }
}

void matrix::hess_red(double **a, int n){
  int m,j,i;
  double y,x;
  for (m=2;m<n;m++) {
    x=0.0;
    i=m;
    for (j=m;j<=n;j++) {
      if (fabs(a[j][m-1]) > fabs(x)) {
	x=a[j][m-1];
	i=j;
      }
    }
    if (i != m) {
      for (j=m-1;j<=n;j++) {y=a[i][j];a[i][j]=a[m][j];a[m][j]=y;}
      for (j=1;j<=n;j++) {y=a[j][i];a[j][i]=a[j][m];a[j][m]=y;}
    }
    if (x) {
      for (i=m+1;i<=n;i++) {
	if ((y=a[i][m-1]) != 0.0) {
	  y /= x; a[i][m-1]=y;
	  for (j=m;j<=n;j++) a[i][j] -= y*a[m][j];
	  for (j=1;j<=n;j++) a[j][m] += y*a[j][i];
	}
      }
    }
  }
}

void matrix::hess_eigen(double **a, int n, double *wr, double *wi){
  int nn,m,l,k,j,its,i,mmin;
  double z,y,x,w,v,u,t,s,r,q,p,anorm;
  
  anorm=fabs(a[1][1]);
  for (i=2;i<=n;i++) for (j=(i-1);j<=n;j++) anorm += fabs(a[i][j]);
  nn=n;
  t=0.0;
  while (nn >= 1) {
    its=0;
    do {
      for (l=nn;l>=2;l--) {
	s=fabs(a[l-1][l-1])+fabs(a[l][l]);
	if (s == 0.0) s=anorm;
	if ((double)(fabs(a[l][l-1]) + s) == s) break;
      }
      x=a[nn][nn];
      if (l == nn) {
	wr[nn]=x+t;
	wi[nn--]=0.0;
      } else {
	y=a[nn-1][nn-1];
	w=a[nn][nn-1]*a[nn-1][nn];
	if (l == (nn-1)) {
	  p=0.5*(y-x);
	  q=p*p+w;
	  z=sqrt(fabs(q));
	  x += t;
	  if (q >= 0.0) {
	    z=p+SIGN(z,p);
	    wr[nn-1]=wr[nn]=x+z;
	    if (z) wr[nn]=x-w/z;
	    wi[nn-1]=wi[nn]=0.0;
	  } else {
	    wr[nn-1]=wr[nn]=x+p;
	    wi[nn-1]= -(wi[nn]=z);
	  }
	  nn -= 2;
	} else {
	  if (its == 30) 
	    error((char *)"Too many iterations in matrix::hess_eigen");
	  if (its == 10 || its == 20) {
	    t += x;
	    for (i=1;i<=nn;i++) a[i][i] -= x;
	    s=fabs(a[nn][nn-1])+fabs(a[nn-1][nn-2]);
	    y=x=0.75*s;
	    w = -0.4375*s*s;
	  }
	  ++its;
	  for (m=(nn-2);m>=l;m--) {
	    z=a[m][m];
	    r=x-z;
	    s=y-z;
	    p=(r*s-w)/a[m+1][m]+a[m][m+1];
	    q=a[m+1][m+1]-z-r-s;
	    r=a[m+2][m+1];
	    s=fabs(p)+fabs(q)+fabs(r);
	    p /= s;
	    q /= s;
	    r /= s;
	    if (m == l) break;
	    u=fabs(a[m][m-1])*(fabs(q)+fabs(r));
	    v=fabs(p)*(fabs(a[m-1][m-1])+fabs(z)+fabs(a[m+1][m+1]));
	    if ((double)(u+v) == v) break;
	  }
	  for (i=m+2;i<=nn;i++) {
	    a[i][i-2]=0.0;
	    if (i != (m+2)) a[i][i-3]=0.0;
	  }
	  for (k=m;k<=nn-1;k++) {
	    if (k != m) {
	      p=a[k][k-1];
	      q=a[k+1][k-1];
	      r=0.0;
	      if (k != (nn-1)) r=a[k+2][k-1];
	      if ((x=fabs(p)+fabs(q)+fabs(r)) != 0.0) {
		p /= x;
		q /= x;
		r /= x;
	      }
	    }
	    if ((s=SIGN(sqrt(p*p+q*q+r*r),p)) != 0.0) {
	      if (k == m) {
		if (l != m)
		  a[k][k-1] = -a[k][k-1];
	      } else
		a[k][k-1] = -s*x;
	      p += s;
	      x=p/s;
	      y=q/s;
	      z=r/s;
	      q /= p;
	      r /= p;
	      for (j=k;j<=nn;j++) {
		p=a[k][j]+q*a[k+1][j];
		if (k != (nn-1)) {
		  p += r*a[k+2][j];
		  a[k+2][j] -= p*z;
		}
		a[k+1][j] -= p*y;
		a[k][j] -= p*x;
	      }
	      mmin = nn<k+3 ? nn : k+3;
	      for (i=l;i<=mmin;i++) {
		p=x*a[i][k]+y*a[i][k+1];
		if (k != (nn-1)) {
		  p += z*a[i][k+2];
		  a[i][k+2] -= p*r;
		}
		a[i][k+1] -= p*q;
		a[i][k] -= p;
	      }
	    }
	  }
	}
      }
    } while (l < nn-1);
  }
}

void matrix::eigen(double **a, int n, double *wr, double *wi){
  balance(a,n);
  hess_red(a,n);
  hess_eigen(a,n,wr,wi);
}
