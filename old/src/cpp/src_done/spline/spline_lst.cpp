#include <iostream>
 
#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "./spline.hpp"

void spline::pick_sort(double *arr, unsigned long n){
  unsigned long i,j;
  double a;
  for (j=2;j<=n;j++) {
    a=arr[j]; i=j-1;
    while (i>0 && arr[i]>a){arr[i+1]=arr[i]; i--;}
    arr[i+1]=a;
  }
}

void spline::pick_sort(double *arr, double *brr, unsigned long n){
  unsigned long i,j;
  double a,b;
  for (j=2;j<=n;j++) {
    a=arr[j]; b=brr[j]; i=j-1;
    while (i>0 && arr[i]>a){arr[i+1]=arr[i]; brr[i+1]=brr[i]; i--;}
    arr[i+1]=a; brr[i+1]=b;
  }
}

void spline::shell_sort(double *arr, unsigned long n){
  unsigned long i,j,inc;
  double v;
  inc=1;
  do {inc *= 3; inc++;} while (inc <= n);
  do {
    inc /= 3;
    for (i=inc+1;i<=n;i++) {
      v=arr[i]; j=i;
      while (arr[j-inc] > v) {
	arr[j]=arr[j-inc];
	j -= inc;
	if (j <= inc) break;
      }
      arr[j]=v;
    }
  } while (inc > 1);
}

void spline::heap_sort(double *arr, unsigned long n){
  unsigned long i,ir,j,l;
  double rra;
  if (n < 2) return;
  l=(n >> 1)+1; ir=n;
  for (;;) {
    if (l>1){
      rra=arr[--l];
    } else {
      rra=arr[ir]; arr[ir]=arr[1];
      if (--ir == 1) {
	arr[1]=rra;
	break;
      }
    }
    i=l; j=l+l;
    while (j <= ir) {
      if (j < ir && arr[j] < arr[j+1]) j++;
      if (rra < arr[j]) {
	arr[i]=arr[j];
	i=j;
	j <<= 1;
      } else j=ir+1;
    }
    arr[i]=rra;
  }
}

void spline::quick_sort(double *arr,unsigned long n){
  unsigned long i,ir=n,j,k,l=1,M=7;
  int jstack=0,*istack,NSTACK=50;
  double a,temp;
  istack=tools::ivector(1,NSTACK);
  for (;;) {
    if (ir-l < M) {
      for (j=l+1;j<=ir;j++) {
	a=arr[j];
	for (i=j-1;i>=1;i--) {
	  if (arr[i] <= a) break;
	  arr[i+1]=arr[i];
	}
	arr[i+1]=a;
      }
      if (jstack == 0) break;
      ir=istack[jstack--];
      l=istack[jstack--];
    } else {
      k=(l+ir) >> 1;
      temp=arr[k];arr[k]=arr[l+1];arr[l+1]=temp;
      if (arr[l] > arr[ir]) {temp=arr[l];arr[l]=arr[ir];arr[ir]=temp;}
      if (arr[l+1] > arr[ir]) {temp=arr[l+1];arr[l+1]=arr[ir];arr[ir]=temp;}
      if (arr[l] > arr[l+1]) {temp=arr[l];arr[l]=arr[l+1];arr[l+1]=temp;}
      i=l+1;
      j=ir;
      a=arr[l+1];
      for (;;) {
	do i++; while (arr[i] < a);
	do j--; while (arr[j] > a);
	if (j < i) break;
	temp=arr[i];arr[i]=arr[j];arr[j]=temp;
      }
      arr[l+1]=arr[j];
      arr[j]=a;
      jstack += 2;
      if (jstack > NSTACK) error((char *)"NSTACK too small in spline::sort.");
      if (ir-i+1 >= j-l) {istack[jstack]=ir;istack[jstack-1]=i;ir=j-1;}
      else {istack[jstack]=j-1;istack[jstack-1]=l;l=i;}
    }
  }
  tools::free_ivector(istack,1,NSTACK);
}

void spline::quick_sort(double *arr, double *brr, unsigned long n){
  unsigned long i,ir=n,j,k,l=1,M=7;
  int *istack,jstack=0,NSTACK=50;
  double a,b,temp;
  istack=tools::ivector(1,NSTACK);
  for (;;) {
    if (ir-l < M) {
      for (j=l+1;j<=ir;j++) {
	a=arr[j];
	b=brr[j];
	for (i=j-1;i>=1;i--) {
	  if (arr[i] <= a) break;
	  arr[i+1]=arr[i];
	  brr[i+1]=brr[i];
	}
	arr[i+1]=a;
	brr[i+1]=b;
      }
      if (!jstack) {
	tools::free_ivector(istack,1,NSTACK);
	return;
      }
      ir=istack[jstack];
      l=istack[jstack-1];
      jstack -= 2;
    } else {
      k=(l+ir) >> 1;
      temp=arr[k];arr[k]=arr[l+1];arr[l+1]=temp;
      temp=brr[k];brr[k]=brr[l+1];brr[l+1]=temp;
      if (arr[l] > arr[ir]) {
	temp=arr[l];arr[l]=arr[ir];arr[ir]=temp;
	temp=brr[l];brr[l]=brr[ir];brr[ir]=temp;
      }
      if (arr[l+1] > arr[ir]) {
	temp=arr[l+1];arr[l+1]=arr[ir];arr[ir]=temp;
	temp=brr[l+1];brr[l+1]=brr[ir];brr[ir]=temp;
      }
      if (arr[l] > arr[l+1]) {
	temp=arr[l];arr[l]=arr[l+1];arr[l+1]=temp;
	temp=brr[l];brr[l]=brr[l+1];brr[l+1]=temp;
      }
      i=l+1;
      j=ir;
      a=arr[l+1];
      b=brr[l+1];
      for (;;) {
	do i++; while (arr[i] < a);
	do j--; while (arr[j] > a);
	if (j < i) break;
	temp=arr[i];arr[i]=arr[j];arr[j]=temp;
	temp=brr[i];brr[i]=brr[j];brr[j]=temp;
      }
      arr[l+1]=arr[j];
      arr[j]=a;
      brr[l+1]=brr[j];
      brr[j]=b;
      jstack += 2;
      if (jstack > NSTACK) 
	error((char *)"NSTACK too small in spline::sort_2.");
      if (ir-i+1 >= j-l) {
	istack[jstack]=ir;
	istack[jstack-1]=i;
	ir=j-1;
      } else {
	istack[jstack]=j-1;
	istack[jstack-1]=l;
	l=i;
      }
    }
  }
  tools::free_ivector(istack,1,NSTACK);
}

void spline::quick_sort(double *arr, double *brr, double *crr,unsigned long n){
  unsigned long j,*iwksp; double *wksp;
  iwksp=tools::lvector(1,n);
  wksp=tools::dvector(1,n);
  indexx(arr,iwksp,n);
  for (j=1;j<=n;j++) wksp[j]=arr[j];
  for (j=1;j<=n;j++) arr[j]=wksp[iwksp[j]];
  for (j=1;j<=n;j++) wksp[j]=brr[j];
  for (j=1;j<=n;j++) brr[j]=wksp[iwksp[j]];
  for (j=1;j<=n;j++) wksp[j]=crr[j];
  for (j=1;j<=n;j++) crr[j]=wksp[iwksp[j]];
  tools::free_dvector(wksp,1,n);
  tools::free_lvector(iwksp,1,n);
}

void spline::indexx(double *arr, unsigned long *indx,unsigned long n){
  unsigned long i,indxt,ir=n,itemp,j,k,l=1,M=7;
  int jstack=0,*istack,NSTACK=50;
  double a;
  istack=tools::ivector(1,NSTACK);
  for (j=1;j<=n;j++) indx[j]=j;
  for (;;) {
    if (ir-l < M) {
      for (j=l+1;j<=ir;j++) {
	indxt=indx[j];
	a=arr[indxt];
	for (i=j-1;i>=1;i--) {
	  if (arr[indx[i]] <= a) break;
	  indx[i+1]=indx[i];
	}
	indx[i+1]=indxt;
      }
      if (jstack == 0) break;
      ir=istack[jstack--];
      l=istack[jstack--];
    } else {
      k=(l+ir) >> 1;
      itemp=indx[k];indx[k]=indx[l+1];indx[l+1]=itemp;
      if (arr[indx[l+1]] > arr[indx[ir]]) {
	itemp=indx[l+1];indx[l+1]=indx[ir];indx[ir]=itemp;
      }
      if (arr[indx[l]] > arr[indx[ir]]) {
	itemp=indx[l];indx[l]=indx[ir];indx[ir]=itemp;
      }
      if (arr[indx[l+1]] > arr[indx[l]]) {
	itemp=indx[l+1];indx[l+1]=indx[l];indx[l]=itemp;
      }
      i=l+1;
      j=ir;
      indxt=indx[l];
      a=arr[indxt];
      for (;;) {
	do i++; while (arr[indx[i]] < a);
	do j--; while (arr[indx[j]] > a);
	if (j < i) break;
	itemp=indx[i];indx[i]=indx[j];indx[j]=itemp;
      }
      indx[l]=indx[j];
      indx[j]=indxt;
      jstack += 2;
      if (jstack > NSTACK) 
	error((char *)"NSTACK too small in spline::indexx.");
      if (ir-i+1 >= j-l) {
	istack[jstack]=ir;
	istack[jstack-1]=i;
	ir=j-1;
      } else {
	istack[jstack]=j-1;
	istack[jstack-1]=l;
	l=i;
      }
    }
  }
  tools::free_ivector(istack,1,NSTACK);
}

unsigned long spline::locate(double *xx, unsigned long n, double x){
  unsigned long ju,jm,jl,value;
  int ascnd;
  jl=0; ju=n+1;
  ascnd=(xx[n] >= xx[1]);
  while (ju-jl > 1) {
    jm=(ju+jl) >> 1;
    if ((x >= xx[jm]) == ascnd)
      jl=jm;
    else
      ju=jm;
  }
  if (x == xx[1]) value=1;
  else if(x == xx[n]) value=n-1;
  else value=jl;
  return value;
}

unsigned long spline::hunt(double *xx, unsigned long n, 
			   double x, unsigned long guess){
  unsigned long jm,jhi,inc,value;
  int ascnd; value=guess;
  ascnd=(xx[n] >= xx[1]);
  if (value <= 0 || value > n) {
    value=0;
    jhi=n+1;
  } else {
    inc=1;
    if ((x >= xx[value]) == ascnd) {
      if (value == n) return value;
      jhi=(value)+1;
      while ((x >= xx[jhi]) == ascnd) {
	value=jhi;
	inc += inc;
	jhi=(value)+inc;
	if (jhi > n) {
	  jhi=n+1;
	  break;
	}
      }
    } else {
      if (value == 1) {
	value=0;
	return value;
      }
      jhi=(value)--;
      while ((x < xx[value]) == ascnd) {
	jhi=(value);
	inc <<= 1;
	if (inc >= jhi) {
	  value=0;
	  break;
	}
	else value=jhi-inc;
      }
    }
  }
  while (jhi-(value) != 1) {
    jm=(jhi+(value)) >> 1;
    if ((x >= xx[jm]) == ascnd)
      value=jm;
    else
      jhi=jm;
  }
  if (x == xx[n]) value=n-1;
  if (x == xx[1]) value=1;
  return value;
}

double spline::select(double *arr, unsigned long n, unsigned long k){
  unsigned long i,ir,j,l,mid;
  double a,temp;
  l=1;
  ir=n;
  for (;;) {
    if (ir <= l+1) {
      if (ir == l+1 && arr[ir] < arr[l]) {
	temp=arr[l];arr[l]=arr[ir];arr[ir]=temp;
      }
      return arr[k];
    } else {
      mid=(l+ir) >> 1;
      temp=arr[mid];arr[mid]=arr[l+1];arr[l+1]=temp;
      if (arr[l+1] > arr[ir]) {
	temp=arr[l+1];arr[l+1]=arr[ir];arr[ir]=temp;
      }
      if (arr[l] > arr[ir]) {
	temp=arr[l];arr[l]=arr[ir];arr[ir]=temp;
      }
      if (arr[l+1] > arr[l]) {
	temp=arr[l+1];arr[l+1]=arr[l];arr[l]=temp;
      }
      i=l+1;
      j=ir;
      a=arr[l];
      for (;;) {
	do i++; while (arr[i] < a);
	do j--; while (arr[j] > a);
	if (j < i) break;
	temp=arr[i];arr[i]=arr[j];arr[j]=temp;
      }
      arr[l]=arr[j];
      arr[j]=a;
      if (j >= k) ir=j-1;
      if (j <= k) l=i;
    }
  }
}

double spline::selip(double *arr,unsigned long n, unsigned long k){
  int M=64;
  double BIG=1.0e30;
  unsigned long i,j,jl,jm,ju,kk,mm,nlo,nxtmm,*isel;
  double ahi,alo,sum,*sel;
  if (k < 1 || k > n || n <= 0) error(const_cast<char *>("bad input to selip"));
  isel=tools::lvector(1,M+2);
  sel=tools::dvector(1,M+2);
  kk=k;
  ahi=BIG;
  alo = -BIG;
  for (;;) {
    mm=nlo=0;
    sum=0.0;
    nxtmm=M+1;
    for (i=1;i<=n;i++) {
      if (arr[i] >= alo && arr[i] <= ahi) {
	mm++;
	if (arr[i] == alo) nlo++;
	if (mm <= M) sel[mm]=arr[i];
	else if (mm == nxtmm) {
	  nxtmm=mm+mm/M;
	  sel[1 + ((i+mm+kk) % M)]=arr[i];
	}
	sum += arr[i];
      }
    }
    if (kk <= nlo) {
      tools::free_dvector(sel,1,M+2);
      tools::free_lvector(isel,1,M+2);
	return alo;
    }
    else if (mm <= M) {
      shell(sel,mm);
      ahi = sel[kk];
      tools::free_dvector(sel,1,M+2);
      tools::free_lvector(isel,1,M+2);
      return ahi;
    }
    sel[M+1]=sum/mm;
    shell(sel,M+1);
    sel[M+2]=ahi;
    for (j=1;j<=M+2;j++) isel[j]=0;
    for (i=1;i<=n;i++) {
      if (arr[i] >= alo && arr[i] <= ahi) {
	jl=0;
	ju=M+2;
	while (ju-jl > 1) {
	  jm=(ju+jl)/2;
	  if (arr[i] >= sel[jm]) jl=jm;
	  else ju=jm;
	}
	isel[ju]++;
      }
    }
    j=1;
    while (kk > isel[j]) {
      alo=sel[j];
      kk -= isel[j++];
    }
    ahi=sel[j];
  }
}

void spline::shell(double *a,unsigned long n){
  unsigned long i,j,inc;
  double v;
  inc=1;
  do {
    inc *= 3;
    inc++;
  } while (inc <= n);
  do {
    inc /= 3;
    for (i=inc+1;i<=n;i++) {
      v=a[i];
      j=i;
      while (a[j-inc] > v) {
	a[j]=a[j-inc];
	j -= inc;
	if (j <= inc) break;
      }
      a[j]=v;
    }
  } while (inc > 1);
}

