#ifndef _SPLINE_HPP_
#define _SPLINE_HPP_

#include <iostream>
#include <cmath>

#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "../plot/plot_struct.hpp"
#include "./spline.hpp"

class spline: public math_object, public plot_struct {
private:
  static void error(char error_text[]){
    double error_spline;
    fprintf(stderr,"Run-time error in spline...\n");
    fprintf(stderr,"%s\n",error_text);
    fprintf(stderr,"...now exiting to system...\n");
    std::cin>>error_spline;
    exit(1);
  }
  double *xdat,*ydat;
  double *sdat,*sxdat;
  int lenght,size_max;
  bool armed_x,armed_y,order;
  enum step_key {dx,dlnx,dexpx};
  step_key which_step_key(std::string this_key){
    if (!strcmp("dx",this_key.c_str())) return dx;
    if (!strcmp("dlnx",this_key.c_str())) return dlnx;
    if (!strcmp("dexpx",this_key.c_str())) return dexpx;
  }
public:
  spline(); //Creates an empty spline
  spline (const spline& s); //Creates a spline equal to spline s
  spline (std::string name); //Retrieves a spline from the file of name name.
  spline(double(*func)(double),double a, double b, int n, 
	 std::string key=(char *)"dx");
  spline(mo_single f, math_object *mo, double a, double b, 
	 int n, std::string key=(char *)"dx");
  spline(mo_double f, math_object *mo, double x1, 
	 double a, double b, int n, std::string key=(char *)"dx");
  spline(mo_double f, math_object *mo, double a, double b, 
	 int n, double x2, std::string key=(char *)"dx");
  spline(mo_triple f, math_object *mo, double x1, 
	 double x2, double a, double b, int n, std::string key=(char *)"dx");
  spline(mo_triple f, math_object *mo, double x1, double a, double b, 
	 int n, double x3, std::string key=(char *)"dx");
  spline(mo_triple f, math_object *mo, double a, double b, 
	 int n, double x2, double x3, std::string key=(char *)"dx");

  //Creates a spline from function from a to b with n steps and spacing key
  ~spline(); //Destructor
  spline& operator *=(double x) 
  {for (int i=1;i<=lenght;i++) ydat[i] *=x; return *this;}
  spline& operator +=(double x) 
  {for (int i=1;i<=lenght;i++) ydat[i] +=x; return *this;}
  spline& operator =(spline s){
    if (xdat!=0) tools::free_dvector(xdat,1,size_max);
    if (ydat!=0) tools::free_dvector(ydat,1,size_max);
    if (sdat!=0) tools::free_dvector(sdat,1,size_max);
    if (sxdat!=0) tools::free_dvector(sxdat,1,size_max);
    lenght=s.lenght;	size_max=s.size_max;
    xdat=tools::dvector(1,size_max); ydat=tools::dvector(1,size_max);
    sdat=tools::dvector(1,size_max); sxdat=tools::dvector(1,size_max);
    armed_x=s.armed_x; armed_y=s.armed_y; order=s.order;
    for (int i = 1; i <= lenght; i++){
      xdat[i]=s.xdat[i]; ydat[i]=s.ydat[i]; 
      sdat[i]=s.sdat[i]; sxdat[i]=s.sxdat[i];
    }
    if (xdat == 0 || ydat == 0 || sdat == 0 || sxdat == 0)
      error((char *)"no memory in creation of spline");
    return *this;
  }

  void set(double x, double y); // Sets data x,y
  double x_int(int k){
    if (k>lenght || k<0) {
      std::cout<<k<<" not\n"<<std::flush;
      error((char *)"spline::x element not available"); 
    }
    return xdat[k];
  }
  double y_int(int k){
    if (k>lenght || k<0){ 
      std::cout<<k<<" not\n"<<std::flush;
      error((char *)"spline::y element not available"); 
    }
    return ydat[k];
  }
  double start(){return x_int(1);}
  double stop(){return x_int(lenght);}
  int size() { return lenght;}
  void resize(); //Doubles size of arrays.
  void dump(std::string name); void save(std::string name); 
  void retrieve(std::string name); void clear(); void build();
  //Dumps data to file to plot and saves data to be retrieved
  void add(int k, double x); void mul(int k, double x); 
  //Add or mul value to data no k
  void div(int k, double x) { mul(k,1.0/x);}
  bool in_order() {return order;} //Is x in order?
  bool x_armed() { return armed_x;} //Is x armed?
  bool y_armed() { return armed_y;} //Is y armed?
  bool x_disarm() { armed_x = false; return false;} //Disarm x?
  bool y_disarm() { armed_y = false; return false;} //Disarm y?
  void arm_y(double xp1=1e30,double xp2=1e30); 
  //Arm spline y data arguments are derivatives at ends
  double y(double x); //When armed gives y at that x point
  double y_der(double x); //When armed gives y' at that x point
  double y_d2(double x); //When armed gives y'' at that x point
  void y_all(double x, double *yy, double *yder){*yy=y(x);*yder=y_der(x);}
  double integrate(double x1, double x2, double err);
  double root(double x1, double x2, double err);
  //When armed gives integral x1->x2

  void plot();

  class spline derive(); //Returns the derivative of the spline used 
  
  static void indexx(double *arr, unsigned long *indx,unsigned long n);
  static void pick_sort(double *arr, unsigned long n);
  static void pick_sort(double *arr, double *brr, unsigned long n);
  static void shell_sort(double *arr, unsigned long n);
  static void heap_sort(double *arr, unsigned long n);
  static void quick_sort(double *arr,unsigned long n);
  static void quick_sort(double *arr, double *brr, unsigned long n);
  static void quick_sort(double *arr, double *brr, double *crr, 
			 unsigned long n);
  static void sort(double *arr, unsigned long n){quick_sort(arr,n);};
  static void sort(double *arr, double *brr, unsigned long n){
    quick_sort(arr,brr,n);
  };
  static void sort(double *arr, double *brr, double *crr, 
		   unsigned long n){quick_sort(arr,brr,crr,n);};
  //Sorts table arr[1,n] and brr[1,n] and crr[1,n] acordingly

  static double select(double *arr, unsigned long n, unsigned long k);
  static double selip(double *arr,unsigned long n, unsigned long k);
  static void shell(double *a,unsigned long n);
  // Selects mth larges with and without changing the input vector...

  static unsigned long locate(double *xx, unsigned long n, double x);
  static unsigned long hunt(double *xx, unsigned long n, 
			    double x, unsigned long guess);
  //Locates an int in a n table xx[1..n] such that 
  //xx[j]<x<xx[j+1] 0 or n if x out of range
  
  static void cubic_spline(double *x, double *y, int anf, int n, 
			   double yp1, double ypn, double *y2);
  //Given n:(x,y) data, makes a table from anf->n of the 
  //second derivatives given first derivatives yp1 and ypn
  static double cubic_splint(double *xa, double *ya, double *y2a, 
			     int n, double x);
  //Given n:(xa,ya,y2a) data with second derivatives, interpolates at x
  static double cubic_splint_der(double *xa, double *ya, double *y2a, 
				 int n, double x);
  //Given n:(xa,ya,y2a) data with second derivatives, interpolates the der at x
  static double poly_inter(double *xa, double *ya, int n, 
			   double x, double *dy);
  //Given n pts xa,ya fits a poly of order n-1 and returns P(x) and error dy
  static double rat_inter(double *xa, double *ya, int n, double x, double *dx);
  //Given n pts xa,ya fits a diag rat fct and returns R(x) and error dy
  static void poly_coeff(double *x, double *y, int n, double *cof);
  static void poly_coeff_2(double *xa, double *ya, int n, double *cof);
  //Given data x,y[0,n] rtrn the coef[0,n] for a polynomial of degree n
  static double poly_eval(double *c, int nc, double x, double *pd, int nd);
  //Given data coef[0,nc] rtrn the P(x) and P_derivs[1,nd]

  void cat2spline(std::string name_cat,std::string name_x,std::string name_y);
  
  void sav_gol_coef(double *c,int nl,int nr,int ld,int m);
  void smooth(int nl,int nr,int ld,int m);

  friend class cosmology;
  friend class misc_math;
};

#endif
