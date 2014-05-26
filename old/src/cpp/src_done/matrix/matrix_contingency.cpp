#include <iostream>
 
#include "./matrix.hpp"
#include "../spec_fct/spec_fct.hpp"

void matrix::cntab1(int **nn, int ni, int nj, double *chisq, double *df, 
		    double *prob,double *cramrv, double *ccc){
  int nnj,nni,j,i,minij;
  double sum=0.0,expctd,*sumi,*sumj,temp,TINY=1.0e-30;
  sumi=tools::dvector(1,ni);
  sumj=tools::dvector(1,nj);
  nni=ni;nnj=nj;
  for (i=1;i<=ni;i++) {
    sumi[i]=0.0;
    for (j=1;j<=nj;j++) {
      sumi[i] += nn[i][j];
      sum += nn[i][j];
    }
    if (sumi[i] == 0.0) --nni;
  }
  for (j=1;j<=nj;j++) {
    sumj[j]=0.0;
    for (i=1;i<=ni;i++) sumj[j] += nn[i][j];
    if (sumj[j] == 0.0) --nnj;
  }
  *df=nni*nnj-nni-nnj+1;
  *chisq=0.0;
  for (i=1;i<=ni;i++) {
    for (j=1;j<=nj;j++) {
      expctd=sumj[j]*sumi[i]/sum;
      temp=nn[i][j]-expctd;
      *chisq += temp*temp/(expctd+TINY);
    }
  }
  *prob=spec_fct::gamma_q(0.5*(*df),0.5*(*chisq));
  minij = nni < nnj ? nni-1 : nnj-1;
  *cramrv=sqrt(*chisq/(sum*minij));
  *ccc=sqrt(*chisq/(*chisq+sum));
  tools::free_dvector(sumj,1,nj);
  tools::free_dvector(sumi,1,ni);
}

void matrix::cntab2(int **nn,int ni,int nj,
		    double *h,double *hx,double *hy,double *hygx,double *hxgy,
		    double *uygx,double *uxgy,double *uxy){
  int i,j;
  double sum=0.0,p,*sumi,*sumj,TINY=1.0e-30;
  sumi=tools::dvector(1,ni);
  sumj=tools::dvector(1,nj);
  for (i=1;i<=ni;i++) {
    sumi[i]=0.0;
    for (j=1;j<=nj;j++) {
      sumi[i] += nn[i][j];
      sum += nn[i][j];
    }
  }
  for (j=1;j<=nj;j++) {
    sumj[j]=0.0;
    for (i=1;i<=ni;i++) sumj[j] += nn[i][j];
  }
  *hx=0.0;
  for (i=1;i<=ni;i++)
    if (sumi[i]) {
      p=sumi[i]/sum;
      *hx -= p*log(p);
    }
  *hy=0.0;
  for (j=1;j<=nj;j++)
    if (sumj[j]) {
      p=sumj[j]/sum;
      *hy -= p*log(p);
    }
  *h=0.0;
  for (i=1;i<=ni;i++)
    for (j=1;j<=nj;j++)
      if (nn[i][j]) {
	p=nn[i][j]/sum;
	*h -= p*log(p);
      }
  *hygx=(*h)-(*hx);
  *hxgy=(*h)-(*hy);
  *uygx=(*hy-*hygx)/(*hy+TINY);
  *uxgy=(*hx-*hxgy)/(*hx+TINY);
  *uxy=2.0*(*hx+*hy-*h)/(*hx+*hy+TINY);
  tools::free_dvector(sumj,1,nj);
  tools::free_dvector(sumi,1,ni);
}

double matrix::contin_cramer(){
  int **matrix_here;
  matrix_here=tools::imatrix(1,(*n_row),1,(*n_col));
  for (int i=1;i<=*n_row;i++)
    for (int j=1;j<=*n_col;j++)
      matrix_here[i][j]=(int)mtrx[i][j];
  double chisq=0.0,df=0.0,prob=0.0,cramrv=0.0,ccc=0.0;
  cntab1(matrix_here,*n_row,*n_col,&chisq,&df,&prob,&cramrv,&ccc);
  tools::free_imatrix(matrix_here,1,*n_row,1,*n_col);
  return cramrv;
  
}

double matrix::contin_c(){
  int **matrix_here;
  matrix_here=tools::imatrix(1,*n_row,1,*n_col);
  for (int i=1;i<=*n_row;i++)
    for (int j=1;j<=*n_col;j++)
      matrix_here[i][j]=(int)mtrx[i][j];
  double chisq=0.0,df=0.0,prob=0.0,cramrv=0.0,ccc=0.0;
  cntab1(matrix_here,*n_row,*n_col,&chisq,&df,&prob,&cramrv,&ccc);
  tools::free_imatrix(matrix_here,1,*n_row,1,*n_col);
  return ccc;
}

double matrix::contin_prob(){
  int **matrix_here;
  matrix_here=tools::imatrix(1,*n_row,1,*n_col);
  for (int i=1;i<=*n_row;i++)
    for (int j=1;j<=*n_col;j++)
      matrix_here[i][j]=(int)mtrx[i][j];
  double chisq=0.0,df=0.0,prob=0.0,cramrv=0.0,ccc=0.0;
  cntab1(matrix_here,*n_row,*n_col,&chisq,&df,&prob,&cramrv,&ccc);
  tools::free_imatrix(matrix_here,1,*n_row,1,*n_col);
  return prob;
}
 
double matrix::contin_entropy(){
  int **matrix_here;
  matrix_here=tools::imatrix(1,*n_row,1,*n_col);
  for (int i=1;i<=*n_row;i++)
    for (int j=1;j<=*n_col;j++)
      matrix_here[i][j]=(int)mtrx[i][j];
  double h=0.0,hx=0.0,hy=0.0,hygx=0.0,hxgy=0.0,uygx=0.0,uxgy=0.0,uxy=0.0;
  cntab2(matrix_here,*n_row,*n_col,&h,&hx,&hy,&hygx,&hxgy,&uygx,&uxgy,&uxy);
  tools::free_imatrix(matrix_here,1,*n_row,1,*n_col);
  return uxy;
}
