#include <iostream>
#include <fstream>

#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "../matrix/matrix.hpp"
#include "spline.hpp"

spline::spline(){build();}

void spline::build(){
  lenght=0;
  size_max=100;
  xdat=tools::dvector(1,size_max);
  ydat=tools::dvector(1,size_max);
  sdat=tools::dvector(1,size_max);
  sxdat=tools::dvector(1,size_max);
  armed_x = false; armed_y = false; order = true;
  for (int i = 1; i <= size_max; i++)   ydat[i] = 0;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
}

spline::spline(const spline& s) {
  lenght=s.lenght;
  size_max=s.size_max;
  xdat=tools::dvector(1,size_max);
  ydat=tools::dvector(1,size_max);
  sdat=tools::dvector(1,size_max);
  sxdat=tools::dvector(1,size_max);
  armed_x=s.armed_x; armed_y=s.armed_y; order=s.order;
  for (int i = 1; i <= lenght; i++){
    xdat[i]=s.xdat[i]; ydat[i]=s.ydat[i]; 
    sdat[i]=s.sdat[i]; sxdat[i]=s.sxdat[i];
  }
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
}

spline::spline(std::string name){
  double X,Y; char tmp;
  std::ifstream save_file;
  save_file.open(name.c_str());
  save_file>>tmp>>lenght;
  save_file>>tmp>>armed_x; armed_x=false;
  save_file>>tmp>>armed_y; armed_y=false;
  save_file>>tmp>>order;
  size_max=lenght;
  xdat=tools::dvector(1,size_max);
  ydat=tools::dvector(1,size_max);
  sdat=tools::dvector(1,size_max);
  sxdat=tools::dvector(1,size_max);
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  
  for (int k =1; k<=lenght; k++) {
    save_file>>X>>Y;
    xdat[k]=X;ydat[k]=Y;
    if (k>1) {if (xdat[k]<xdat[k-1]) order=false;}
  }
  save_file.close();
}

spline::spline(double(*func)(double),double a, double b, 
	       int n, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,func(x_now));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,func(x_now));x_now=log(x_now);x_now+=(log(b)-log(a))/(n-1);
      x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {
      set(x_now,func(x_now));x_now=pow(e_log,x_now);
      x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (int i=1; i<=n; i++) {set(x_now,func(x_now));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_single f, math_object *mo, double a, double b, 
	       int n, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x_now));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now));x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (int i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_double f, math_object *mo, double x1,
	       double a, double b, int n, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x1,x_now));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now));x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_double f, math_object *mo, double a, double b, 
	       int n, double x2, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x_now,x2));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2));x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_triple f, math_object *mo, double x1, double x2, 
	       double a, double b, int n, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x2,x_now));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x1,x2,x_now));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x2,x_now));
    x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x2,x_now));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_triple f, math_object *mo, double x1, double a, double b, 
	       int n, double x3, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now,x3));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x1,x_now,x3));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now,x3));
    x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x1,x_now,x3));x_now+=(b-a)/(n-1);}
  }
}

spline::spline(mo_triple f, math_object *mo, double a, double b, 
	       int n, double x2, double x3, std::string key){
  double e_log=2.71828182846; int i; step_key which;
  lenght=0;
  size_max=n;
  xdat=tools::dvector(1,n);
  ydat=tools::dvector(1,n);
  sdat=tools::dvector(1,n);
  sxdat=tools::dvector(1,n);
  armed_x = false; armed_y = false; order = true;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  double x_now=a;
  which=which_step_key(key);
  switch (which) {
  case dx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2,x3));x_now+=(b-a)/(n-1);}
    break;
  case dlnx:
    for (i=1; i<=n; i++) {
      set(x_now,(mo->*f)(x_now,x2,x3));x_now=log(x_now);
      x_now+=(log(b)-log(a))/(n-1);x_now=pow(e_log,x_now);
    }
    break;
  case dexpx:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2,x3));
    x_now=pow(e_log,x_now);
    x_now+=(pow(e_log,b)-pow(e_log,a))/(n-1);x_now=log(x_now);
    }
    break;
  default:
    for (i=1; i<=n; i++) {set(x_now,(mo->*f)(x_now,x2,x3));x_now+=(b-a)/(n-1);}
  }
}

spline::~spline(){
  if (xdat!=NULL) tools::free_dvector(xdat,1,size_max);
  if (ydat!=NULL) tools::free_dvector(ydat,1,size_max);
  if (sdat!=NULL) tools::free_dvector(sdat,1,size_max);
  if (sxdat!=NULL) tools::free_dvector(sxdat,1,size_max);
}

void spline::set(double x, double y) {
  if (lenght>=size_max) resize();
  lenght++;
  xdat[lenght]=x; ydat[lenght]=y;
  if (lenght>1) {if (xdat[lenght]<xdat[lenght-1]) order=false;}
  armed_x=false; armed_y=false;
}

void spline::resize(){
  double *tmp_xdat,*tmp_ydat; int i;
  tmp_xdat = tools::dvector(1,2*size_max);
  tmp_ydat = tools::dvector(1,2*size_max);
  for (i =1; i<= size_max; i++) {tmp_xdat[i]=xdat[i];tmp_ydat[i]=ydat[i];}
  tools::free_dvector(xdat,1,size_max);tools::free_dvector(ydat,1,size_max);
  xdat=tmp_xdat; ydat=tmp_ydat;
  tools::free_dvector(sdat,1,size_max); tools::free_dvector(sxdat,1,size_max);
  sdat = tools::dvector(1,2*size_max);
  sxdat = tools::dvector(1,2*size_max);
  size_max*=2;
}

void spline::dump(std::string name){
  int k;
  std::ofstream local_file(name.c_str());
  local_file.setf(std::ios::scientific);
  for (k = 1; k <= lenght; k++) {local_file<<xdat[k]<<"\t"<<ydat[k]<<"\n";}
  local_file.close();
}

void spline::save(std::string name){
  double X,Y;
  std::ofstream save_file;
  save_file.open(name.c_str());
  save_file.setf(std::ios::scientific);
  save_file<<"#"<<lenght<<"\n";
  save_file<<"#"<<armed_x<<"\n";
  save_file<<"#"<<armed_y<<"\n";
  save_file<<"#"<<order<<"\n";
  for (int k =1; k<=lenght; k++) {
    X=xdat[k];Y=ydat[k];
    save_file<<X<<"\t"<<Y<<"\n";
  }
  save_file.close();
}

void spline::retrieve(std::string name){
  double X,Y; char tmp;
  std::ifstream save_file;

  if (xdat!=0) tools::free_dvector(xdat,1,size_max);
  if (ydat!=0) tools::free_dvector(ydat,1,size_max);
  if (sdat!=0) tools::free_dvector(sdat,1,size_max);
  if (sxdat!=0) tools::free_dvector(sxdat,1,size_max);

  save_file.open(name.c_str());
  save_file>>tmp>>lenght;
  save_file>>tmp>>armed_x; armed_x=false;
  save_file>>tmp>>armed_y; armed_y=false;
  save_file>>tmp>>order;
  size_max=lenght;
  xdat=tools::dvector(1,size_max);
  ydat=tools::dvector(1,size_max);
  sdat=tools::dvector(1,size_max);
  sxdat=tools::dvector(1,size_max);
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
  
  for (int k =1; k<=lenght; k++) {
    save_file>>X>>Y;
    xdat[k]=X;ydat[k]=Y;
    if (k>1) {if (xdat[k]<xdat[k-1]) order=false;}
  }
  save_file.close();
}

void spline::clear(){
  if (xdat!=0) tools::free_dvector(xdat,1,size_max);
  if (ydat!=0) tools::free_dvector(ydat,1,size_max);
  if (sdat!=0) tools::free_dvector(sdat,1,size_max);
  if (sxdat!=0) tools::free_dvector(sxdat,1,size_max);
  lenght=0;
  size_max=1000;
  xdat=tools::dvector(1,1000);
  ydat=tools::dvector(1,1000);
  sdat=tools::dvector(1,1000);
  sxdat=tools::dvector(1,1000);
  armed_x = false; armed_y = false; order = true;
  for (int i = 1; i <= 1000; i++)   ydat[i] = 0;
  if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0) 
    error((char *)"no memory in creation of spline");
}

void spline::add(int k, double y) {
  if (k > lenght || k < 0)  error((char *)"spline::add element not in spline");
  ydat[k] += y;
}

void spline::mul(int k, double x) {
  if (k > lenght || k < 0) error((char *)"spline::mul element not available");
  ydat[k] *=x;
}

void spline::arm_y(double yp1,double yp2) {
  if (armed_y) error((char *)"spline already armed");
  if (!order) {sort(xdat,ydat,lenght); order=true;}
  cubic_spline(xdat,ydat,1,lenght,yp1,yp2,sdat);
  armed_y = true;
}

double spline::y (double x)  {
  if (!armed_y) error((char *)"spline::y not armed");
  return cubic_splint(xdat,ydat,sdat,lenght,x);
}

double spline::y_der (double x)  {
  if (!armed_y) error((char *)"spline::y not armed");
  return cubic_splint_der(xdat,ydat,sdat,lenght,x);
}

void spline::smooth(int nl,int nr,int ld,int m){
  double val,*data_here,*c;
  int j,i;
  data_here=tools::dvector(1,lenght);
  c=tools::dvector(1,nl+nr+1);
  sav_gol_coef(c,nl,nr,ld,m);
  for(i=1;i<=lenght;i++){data_here[i]=0.0;}
  for (i=1;i<=lenght;i++){
    for(j=1;j<=nl+nr+1;j++){
      if (j==1) val=c[j]*xdat[j];
      if (j>1 || j<=nl+1)
	{if ((i-j+1)>=1) val=c[j]*xdat[i-j+1]; else val=0;}
      if (j>1 || j<=nl+1)
	{if ((i+2+nl+nr-j)<=lenght) val=c[j]*xdat[i+2+nl+nr-j]; else val=0;}
      data_here[i]+=val;
    }
  }
  for(i=1;i<=lenght;i++){xdat[i]=data_here[i];}
  tools::free_dvector(data_here,1,lenght);
  tools::free_dvector(c,1,nl+nr+1);
}

void spline::sav_gol_coef(double *c,int nl,int nr,int ld,int m){
  int imj,ipj,j,k,kk,mm,*indx,np=nl+nr+1;
  double d,fac,sum,**a,*b;
  
  if (nl < 0 || nr < 0 || ld > m || nl+nr < m) 
    error(const_cast<char *>("bad args in data_vector::sav_gol_coef"));
  indx=tools::ivector(1,m+1);
  a=tools::dmatrix(1,m+1,1,m+1);
  b=tools::dvector(1,m+1);
  for (ipj=0;ipj<=(m << 1);ipj++) {
    sum=(ipj ? 0.0 : 1.0);
    for (k=1;k<=nr;k++) sum += pow((double)k,(double)ipj);
    for (k=1;k<=nl;k++) sum += pow((double)-k,(double)ipj);
    mm=IMIN(ipj,2*m-ipj);
    for (imj = -mm;imj<=mm;imj+=2) a[1+(ipj+imj)/2][1+(ipj-imj)/2]=sum;
  }
  matrix::lu_decomp(a,m+1,indx,&d);
  for (j=1;j<=m+1;j++) b[j]=0.0;
  b[ld+1]=1.0;
  matrix::lu_back_sub(a,m+1,indx,b);
  for (kk=1;kk<=np;kk++) c[kk]=0.0;
  for (k = -nl;k<=nr;k++) {
    sum=b[1];
    fac=1.0;
    for (mm=1;mm<=m;mm++) sum += b[mm+1]*(fac *= k);
    kk=((np-k) % np)+1;
    c[kk]=sum;
  }
  tools::free_dvector(b,1,m+1);
  tools::free_dmatrix(a,1,m+1,1,m+1);
  tools::free_ivector(indx,1,m+1);
}
