#ifndef _SPLINE_WEB_H_
#define _SPLINE_WEB_H_

#include <map>

#include "../tools/tools.hpp"

class spline_web: public math_object {
private:
  static void error(char error_text[]){
    double error_spline_web;
    fprintf(stderr,"Run-time error in spline_web...\n");
    fprintf(stderr,"%s\n",error_text);
    fprintf(stderr,"...now exiting to system...\n");
    std::cin>>error_spline_web;
    exit(1);
  }
  map<double,int, less<double> > x1grid, x2grid;
  double *x1dat,*x2dat,**ydat;
  double **y1dat,**y2dat,**y12dat;
  double **y2x1dat,**y2x2dat;
  int lenght_x1,lenght_x2,size_max_x1,size_max_x2;
  bool order_x1,order_x2,armed_x1,armed_x2,armed_x12;
  enum step_key {dx,dlnx,dexpx};
  step_key which_step_key(std::string this_key){
    if (!strcmp("dx",this_key.c_str())) return dx;
    if (!strcmp("dlnx",this_key.c_str())) return dlnx;
    if (!strcmp("dexpx",this_key.c_str())) return dexpx;
  }
public:
  spline_web(); //Creates an empty spline_web
  spline_web (const spline_web& s); //Creates a spline_web equal to spline_web s
  spline_web (std::string name); //Retrieves a spline_web from the file of name name.
  spline_web(double(*func)(double,double),double a1, double b1, int n1, 
	     std::string key1,double a2, double b2, int n2, std::string key2);
  spline_web(mo_double f, math_object *mo,double a1, double b1, int n1, 
	     std::string key1,double a2, double b2, int n2, std::string key2);
  //Creates a spline from function from a to b with n steps and spacing key
  ~spline_web(); //Destructor
  void clear();
  spline_web& operator +=(double x){
    for (int i=1;i<=lenght_x1;i++) 
      for (int j=1;j<=lenght_x2;j++) ydat[i][j] +=x;
    return *this;
  }
  spline_web& operator *=(double x){
    for (int i=1;i<=lenght_x1;i++) 
      for (int j=1;j<=lenght_x2;j++) ydat[i][j] *=x;
    return *this;
  }
  spline_web& operator =(spline_web s){
    if (x1dat!=0) tools::free_dvector(x1dat,1,size_max_x1);
    if (x2dat!=0) tools::free_dvector(x2dat,1,size_max_x2);
    if (ydat!=0) tools::free_dmatrix(ydat,1,size_max_x1,1,size_max_x2);
    if (y1dat!=0) tools::free_dmatrix(y2dat,1,size_max_x1,1,size_max_x2);
    if (y2dat!=0) tools::free_dmatrix(y1dat,1,size_max_x1,1,size_max_x2);
    if (y12dat!=0) tools::free_dmatrix(y12dat,1,size_max_x1,1,size_max_x2);
    if (y2x1dat!=0) tools::free_dmatrix(y2x1dat,1,size_max_x1,1,size_max_x2);
    if (y2x2dat!=0) tools::free_dmatrix(y2x2dat,1,size_max_x1,1,size_max_x2);
    lenght_x1=s.lenght_x1;lenght_x2=s.lenght_x2;
    size_max_x1=s.size_max_x1;size_max_x2=s.size_max_x2;
    x1dat=tools::dvector(1,size_max_x1);
    x2dat=tools::dvector(1,size_max_x2);
    ydat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    y1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    y2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    y12dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    y2x1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    y2x2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
    armed_x1=s.armed_x1;armed_x2=s.armed_x2;armed_x12=s.armed_x12;
    order_x1=s.order_x1;order_x2=s.order_x2;
    if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
	y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
      error((char *)"no memory in creation of spline_web");
    for (int i = 1; i <= lenght_x1; i++){x1dat[i]=s.x1dat[i];}
    for (int i = 1; i <= lenght_x2; i++){x2dat[i]=s.x2dat[i];}
    for (int i = 1; i <= lenght_x1; i++)
      for (int j = 1; j <= lenght_x2; j++){
	ydat[i][j]=s.ydat[i][j];y1dat[i][j]=s.y1dat[i][j];
	y2dat[i][j]=s.y2dat[i][j];y12dat[i][j]=s.y12dat[i][j];
	y2x1dat[i][j]=s.y2x1dat[i][j];y2x2dat[i][j]=s.y2x2dat[i][j];
      }
    return *this;
  }
  
  void set(double x1, double x2, double y); // Sets data x,y,z
  double x1_int(int k){
    if (k>lenght_x1 || k<0)
      error((char *)"spline_web::x1_int element not available"); 
    return x1dat[k];
  }
  double x2_int(int k){
    if (k>lenght_x2 || k<0)
      error((char *)"spline_web::x2_int element not available"); 
    return x2dat[k];
  }
  double y_int(int k, int l){
    if (k>lenght_x1 || k<0 || l>lenght_x2 || l<0)
      error((char *)"spline_web::y_int element not available"); 
    return ydat[k][l];
  }
  double x1_max(int k){
    if (k>lenght_x1 || k<0)
      error((char *)"spline_web::x1_int element not available"); 
    double value=ydat[k][1];
    for (int i=1;i<=lenght_x2; i++) if(value<ydat[k][i]) value=ydat[k][i];
    return value;
  }
  double x2_max(int k){
    if (k>lenght_x1 || k<0)
      error((char *)"spline_web::x1_int element not available"); 
    double value=ydat[1][k];
    for (int i=1;i<=lenght_x1; i++) if(value<ydat[i][k]) value=ydat[i][k];
    return value;
  }
  int size_x1() {return lenght_x1;}
  int size_x2() {return lenght_x2;}
  void resize_x1(); //Doubles size of arrays.
  void resize_x2(); //Doubles size of arrays.
  void dump(std::string name); void save(std::string name);
  //Dumps data to file to plot and saves data to be retrieved
  void add(int k, int l, double x); void mul(int k, int l, double x);
  //Add or mul value to data no k
  void div(int k, int l, double x) { mul(k,l,1.0/x);}
  bool in_order_x1() {return order_x1;} //Is x in order?
  bool in_order_x2() {return order_x2;} //Is x in order?
  void do_order_x1();
  void do_order_x2();
  bool x1_armed() { return armed_x1;} //Is x1 armed?
  bool x2_armed() { return armed_x2;} //Is x2 armed?
  bool x12_armed() { return armed_x12;} //Is x12 armed?
  void arm_x1(double xp1=1e30,double xp2=1e30);
  void arm_x2(double xp1=1e30,double xp2=1e30);
  void arm_x12();
  //Arm spline x data arguments are derivatives at ends
  double y1(double x1, double x2); //When armed gives y at that x point
  double y2(double x1, double x2); //When armed gives y at that x point
  double y12(double x1, double x2); //When armed gives y at that x point
  
  double cubic_splint_x1_web(double *x1a, double *x2a, double **ya, 
			     double **y2a,int m, int n, double x1, double x2);
  double cubic_splint_x2_web(double *x1a, double *x2a, double **ya, 
			     double **y2a,int m, int n, double x1, double x2);
  void bcubic_coef(double *y, double *y1, double *y2, double *y12,
		   double d1, double d2, double **c);
  double bicubic_inter(double *x1a, double *x2a, double **ya, double **y1a,
		       double **y2a, double **y12a, int n, int m,
		       double x1, double x2,double *ansy1, double *ansy2);
};

#endif
