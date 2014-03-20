#include <iostream>
 
#include "./matrix.hpp"

void matrix::gauss_jordan(double **a, int n, double **b, int m){
  int *indxc,*indxr,*ipiv;
  int i,icol,irow,j,k,l,ll;
  double big,dum,pivinv,temp;
  
  indxc=tools::ivector(1,n);
  indxr=tools::ivector(1,n);
  ipiv=tools::ivector(1,n);
  for (j=1;j<=n;j++) ipiv[j]=0;
  for (i=1;i<=n;i++) {
    big=0.0;
    for (j=1;j<=n;j++)
      if (ipiv[j] != 1)
	for (k=1;k<=n;k++) {
	  if (ipiv[k] == 0) {
	    if (fabs(a[j][k]) >= big) {
	      big=fabs(a[j][k]);
	      irow=j;
	      icol=k;
	    }
	  } else if (ipiv[k] > 1) 
	    error((char *)"matrix::gauss_jordan Singular Matrix-1");
	}
    ++(ipiv[icol]);
    if (irow != icol) {
      for (l=1;l<=n;l++) 
	{temp=(a[irow][l]);(a[irow][l])=(a[icol][l]);(a[icol][l])=temp;}
      for (l=1;l<=m;l++) 
	{temp=(b[irow][l]);(b[irow][l])=(b[icol][l]);(b[icol][l])=temp;}
    }
    indxr[i]=irow;
    indxc[i]=icol;
    if (a[icol][icol] == 0.0) 
      error((char *)"matrix::gauss_jordan Singular Matrix-2");
    pivinv=1.0/a[icol][icol];
    a[icol][icol]=1.0;
    for (l=1;l<=n;l++) a[icol][l] *= pivinv;
    for (l=1;l<=m;l++) b[icol][l] *= pivinv;
    for (ll=1;ll<=n;ll++)
      if (ll != icol) {
	dum=a[ll][icol];
	a[ll][icol]=0.0;
	for (l=1;l<=n;l++) a[ll][l] -= a[icol][l]*dum;
	for (l=1;l<=m;l++) b[ll][l] -= b[icol][l]*dum;
      }
  }
  for (l=n;l>=1;l--) {
    if (indxr[l] != indxc[l])
      for (k=1;k<=n;k++){
	temp=(a[k][indxr[l]]);
	(a[k][indxr[l]])=(a[k][indxc[l]]);(a[k][indxc[l]])=temp;
      }
  }
  tools::free_ivector(ipiv,1,n);
  tools::free_ivector(indxr,1,n);
  tools::free_ivector(indxc,1,n);
}

void matrix::lu_decomp(double **a, int n, int *indx, double *d){
  int i,imax,j,k;
  double big,dum,sum,temp,tiny=1.0e-20;
  double *vv;
  
  vv=tools::dvector(1,n);
  *d=1.0;
  for (i=1;i<=n;i++) {
    big=0.0;
    for (j=1;j<=n;j++)
      if ((temp=fabs(a[i][j])) > big) big=temp;
    if (big == 0.0) 
      error((char *)"Singular matrix in routine matrix::lu_decomp");
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
    if (a[j][j] == 0.0) a[j][j]=tiny;
    if (j != n) {
      dum=1.0/(a[j][j]);
      for (i=j+1;i<=n;i++) a[i][j] *= dum;
    }
  }
  tools::free_dvector(vv,1,n);
}

void matrix::lu_back_sub(double **a, int n, int *indx, double *b){
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

void matrix::lu_inverse(double **a, int n){
  double **y,d,*col;
  int i,j,*index;
  col=tools::dvector(1,n);
  index=tools::ivector(1,n);
  y=tools::dmatrix(1,n,1,n);
  lu_decomp(a,n,index,&d);
  for (j=1;j<=n;j++){
    for (i=1;i<=n;i++) col[i]=0.0;
    col[j]=1.0;
    lu_back_sub(a,n,index,col);
    for(i=1;i<=n;i++) y[i][j]=col[i];
  }
  for (j=1;j<=n;j++) for (i=1;i<=n;i++) a[i][j]=y[i][j];
  tools::free_dvector(col,1,n);
  tools::free_ivector(index,1,n);
  tools::free_dmatrix(y,1,n,1,n);
}

double matrix::lu_det(double **a, int n){
  double **y,d;
  int i,j,*index;
  y=tools::dmatrix(1,n,1,n);
  index=tools::ivector(1,n);
  for (i=1;i<=n;i++) for (j=1;j<=n;j++) y[i][j]=a[i][j];
  matrix::lu_decomp(y,n,index,&d);
  for (j=1;j<=n;j++){d*=y[j][j];} 
  tools::free_dmatrix(y,1,n,1,n);
  tools::free_ivector(index,1,n);
  return d;
}
double matrix::lu_ln_det(double **a, int n){
  double **y,d;
  int i,j,*index;
  y=tools::dmatrix(1,n,1,n);
  index=tools::ivector(1,n);
  for (i=1;i<=n;i++) for (j=1;j<=n;j++) y[i][j]=a[i][j];
  matrix::lu_decomp(y,n,index,&d);
  double e=0;
  for (j=1;j<=n;j++){
    e+=log(fabs(y[j][j]));
    d*=fabs(y[j][j])/(y[j][j]);
  }
  tools::free_dmatrix(y,1,n,1,n);
  tools::free_ivector(index,1,n);
  return e;
}

void matrix::lu_improve(double **a, double *b, int n, double *x){
  int j,i,*indx;
  double sdp,*d=0,*r,**alud;
  r=tools::dvector(1,n);
  indx=tools::ivector(1,n);
  alud=tools::dmatrix(1,n,1,n);
  for (i=1;i<=n;i++) for (j=1;j<=n;j++) alud[i][j]=a[i][j];
  lu_decomp(alud,n,indx,d);
  for (i=1;i<=n;i++) {
    sdp = -b[i];
    for (j=1;j<=n;j++) sdp += a[i][j]*x[j];
    r[i]=sdp;
  }
  lu_back_sub(alud,n,indx,r);
  for (i=1;i<=n;i++) x[i] -= r[i];
  tools::free_dmatrix(alud,1,n,1,n);
  tools::free_ivector(indx,1,n);
  tools::free_dvector(r,1,n);
}

void matrix::svd_decomp(double **a, double *w, double **v, int m, int n){
  int flag,i,its,j,jj,k,l,nm;
  double anorm,c,f,g,h,s,scale,x,y,z,*rv1;
  
  rv1=tools::dvector(1,n);
  g=scale=anorm=0.0;
  for (i=1;i<=n;i++) {
    l=i+1;
    rv1[i]=scale*g;
    g=s=scale=0.0;
    if (i <= m) {
      for (k=i;k<=m;k++) scale += fabs(a[k][i]);
      if (scale) {
	for (k=i;k<=m;k++) {a[k][i] /= scale;s += a[k][i]*a[k][i];}
	f=a[i][i];
	g = -SIGN(sqrt(s),f);
	h=f*g-s;
	a[i][i]=f-g;
	for (j=l;j<=n;j++) {
	  for (s=0.0,k=i;k<=m;k++) s += a[k][i]*a[k][j];
	  f=s/h;
	  for (k=i;k<=m;k++) a[k][j] += f*a[k][i];
	}
	for (k=i;k<=m;k++) a[k][i] *= scale;
      }
    }
    w[i]=scale *g;
    g=s=scale=0.0;
    if (i <= m && i != n) {
      for (k=l;k<=n;k++) scale += fabs(a[i][k]);
      if (scale) {
	for (k=l;k<=n;k++) {a[i][k] /= scale;s += a[i][k]*a[i][k];}
	f=a[i][l];
	g = -SIGN(sqrt(s),f);
	h=f*g-s;
	a[i][l]=f-g;
	for (k=l;k<=n;k++) rv1[k]=a[i][k]/h;
	for (j=l;j<=m;j++) {
	  for (s=0.0,k=l;k<=n;k++) s += a[j][k]*a[i][k];
	  for (k=l;k<=n;k++) a[j][k] += s*rv1[k];
	}
	for (k=l;k<=n;k++) a[i][k] *= scale;
      }
    }
    anorm=DMAX(anorm,(fabs(w[i])+fabs(rv1[i])));
  }
  for (i=n;i>=1;i--) {
    if (i < n) {
      if (g) {
	for (j=l;j<=n;j++) v[j][i]=(a[i][j]/a[i][l])/g;
	for (j=l;j<=n;j++) {
	  for (s=0.0,k=l;k<=n;k++) s += a[i][k]*v[k][j];
	  for (k=l;k<=n;k++) v[k][j] += s*v[k][i];
	}
      }
      for (j=l;j<=n;j++) v[i][j]=v[j][i]=0.0;
    }
    v[i][i]=1.0; g=rv1[i]; l=i;
  }
  for (i=IMIN(m,n);i>=1;i--) {
    l=i+1; g=w[i];
    for (j=l;j<=n;j++) a[i][j]=0.0;
    if (g) {
      g=1.0/g;
      for (j=l;j<=n;j++) {
	for (s=0.0,k=l;k<=m;k++) s += a[k][i]*a[k][j];
	f=(s/a[i][i])*g;
	for (k=i;k<=m;k++) a[k][j] += f*a[k][i];
      }
      for (j=i;j<=m;j++) a[j][i] *= g;
    } else for (j=i;j<=m;j++) a[j][i]=0.0;
    ++a[i][i];
  }
  for (k=n;k>=1;k--) {
    for (its=1;its<=30;its++) {
      flag=1;
      for (l=k;l>=1;l--) {
	nm=l-1;
	if ((double)(fabs(rv1[l])+anorm) == anorm) {
	  flag=0;
	  break;
	}
	if ((double)(fabs(w[nm])+anorm) == anorm) break;
      }
      if (flag) {
	c=0.0;s=1.0;
	for (i=l;i<=k;i++) {
	  f=s*rv1[i];
	  rv1[i]=c*rv1[i];
	  if ((double)(fabs(f)+anorm) == anorm) break;
	  g=w[i]; h=pythag(f,g);
	  w[i]=h; h=1.0/h;
	  c=g*h; s = -f*h;
	  for (j=1;j<=m;j++) {
	    y=a[j][nm]; z=a[j][i];
	    a[j][nm]=y*c+z*s; a[j][i]=z*c-y*s;
	  }
	}
      }
      z=w[k];
      if (l == k) {
	if (z < 0.0) {w[k] = -z; for (j=1;j<=n;j++) v[j][k] = -v[j][k];}
	break;
      }
      if (its == 30) error((char *)"no convergence in 30 svdcmp iterations");
      x=w[l]; nm=k-1;
      y=w[nm]; g=rv1[nm];
      h=rv1[k]; f=((y-z)*(y+z)+(g-h)*(g+h))/(2.0*h*y);
      g=pythag(f,1.0);
      f=((x-z)*(x+z)+h*((y/(f+SIGN(g,f)))-h))/x;
      c=s=1.0;
      for (j=l;j<=nm;j++) {
	i=j+1; g=rv1[i];
	y=w[i]; h=s*g;
	g=c*g; z=pythag(f,h);
	rv1[j]=z; c=f/z;
	s=h/z; f=x*c+g*s;
	g = g*c-x*s; h=y*s;
	y *= c;
	for (jj=1;jj<=n;jj++) {
	  x=v[jj][j]; z=v[jj][i];
	  v[jj][j]=x*c+z*s; v[jj][i]=z*c-x*s;
	}
	z=pythag(f,h); w[j]=z;
	if (z) {z=1.0/z;c=f*z;s=h*z;}
	f=c*g+s*y; x=c*y-s*g;
	for (jj=1;jj<=m;jj++) {
	  y=a[jj][j]; z=a[jj][i];
	  a[jj][j]=y*c+z*s; a[jj][i]=z*c-y*s;
	}
      }
      rv1[l]=0.0; rv1[k]=f; w[k]=x;
    }
  }
  tools::free_dvector(rv1,1,n);
}

void matrix::svd_back_sub(double **u, double *w, double **v, 
			  int m, int n, double *b, double *x){
  int jj,j,i;
  double s,*tmp;
  tmp=tools::dvector(1,n);
  for (j=1;j<=n;j++) {
    s=0.0;
    if (w[j]) {
      for (i=1;i<=m;i++) s += u[i][j]*b[i]; 
      s /= w[j];
    }
    tmp[j]=s;
  }
  for (j=1;j<=n;j++) {
    s=0.0;
    for (jj=1;jj<=n;jj++) s += v[j][jj]*tmp[jj];
    x[j]=s;
  }
  tools::free_dvector(tmp,1,n);
}

double matrix::pythag(double a, double b){
  double absa,absb;
  absa=fabs(a);
  absb=fabs(b);
  if (absa > absb) return absa*sqrt(1.0+(absb/absa)*(absb/absa));
  else return (absb == 0.0 ? 0.0 : absb*sqrt(1.0+(absa/absb)*(absa/absb)));
}

void matrix::qr_decomp(double **a, int n, double *c, double *d, int *sing){
  int i,j,k;
  double scale,sigma,sum,tau;
  *sing=0;
  for (k=1;k<n;k++) {
    scale=0.0;
    for (i=k;i<=n;i++) scale=DMAX(scale,fabs(a[i][k]));
    if (scale == 0.0) {
      *sing=1;
      c[k]=d[k]=0.0;
    } else {
      for (i=k;i<=n;i++) a[i][k] /= scale;
      for (sum=0.0,i=k;i<=n;i++) sum += (a[i][k])*(a[i][k]);
      sigma=SIGN(sqrt(sum),a[k][k]);
      a[k][k] += sigma;
      c[k]=sigma*a[k][k];
      d[k] = -scale*sigma;
      for (j=k+1;j<=n;j++) {
	for (sum=0.0,i=k;i<=n;i++) sum += a[i][k]*a[i][j];
	tau=sum/c[k];
	for (i=k;i<=n;i++) a[i][j] -= tau*a[i][k];
      }
    }
  }
  d[n]=a[n][n];
  if (d[n] == 0.0) *sing=1;
}

void matrix::qr_back_sub(double **a, int n, double *c, double *d, double *b){
  int i,j;
  double sum,tau;
  for (j=1;j<n;j++) {
    for (sum=0.0,i=j;i<=n;i++) sum += a[i][j]*b[i];
    tau=sum/c[j];
    for (i=j;i<=n;i++) b[i] -= tau*a[i][j];
  }
  rsolv(a,n,d,b);
}

void matrix::qr_update(double **r, double **qt, int n, double *u, double *v){
  int i,j,k;
  for (k=n;k>=1;k--) {if (u[k]) break;}
  if (k < 1) k=1;
  for (i=k-1;i>=1;i--) {
    rotate(r,qt,n,i,u[i],-u[i+1]);
    if (u[i] == 0.0) u[i]=fabs(u[i+1]);
    else if (fabs(u[i]) > fabs(u[i+1]))
      u[i]=fabs(u[i])*sqrt(1.0+(u[i+1]/u[i])*(u[i+1]/u[i]));
    else u[i]=fabs(u[i+1])*sqrt(1.0+(u[i]/u[i+1])*(u[i]/u[i+1]));
  }
  for (j=1;j<=n;j++) r[1][j] += u[1]*v[j];
  for (i=1;i<k;i++) rotate(r,qt,n,i,r[i][i],-r[i+1][i]);
}

void matrix::rsolv(double **a, int n, double *d, double *b){
  int i,j;
  double sum;
  b[n] /= d[n];
  for (i=n-1;i>=1;i--) {
    for (sum=0.0,j=i+1;j<=n;j++) sum += a[i][j]*b[j];
    b[i]=(b[i]-sum)/d[i];
  }
}

void matrix::rotate(double **r,double **qt,int n,int i,double a,double b){
  int j;
  double c,fact,s,w,y;
  if (a == 0.0) {c=0.0;s=(b >= 0.0 ? 1.0 : -1.0);} 
  else if (fabs(a) > fabs(b)) {
    fact=b/a;
    c=SIGN(1.0/sqrt(1.0+(fact*fact)),a);
    s=fact*c;
  } else {
    fact=a/b;
    s=SIGN(1.0/sqrt(1.0+(fact*fact)),b);
    c=fact*s;
  }
  for (j=i;j<=n;j++){y=r[i][j];w=r[i+1][j];r[i][j]=c*y-s*w;r[i+1][j]=s*y+c*w;}
  for (j=1;j<=n;j++){
    y=qt[i][j];
    w=qt[i+1][j];
    qt[i][j]=c*y-s*w;
    qt[i+1][j]=s*y+c*w;
  }
}
