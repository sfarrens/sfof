#ifndef _MATHOBJECT_HPP_
#define _MATHOBJECT_HPP_
 
class  math_object {};

typedef void (math_object::*mo_derivs)(double, double*, double*);  
//! common derivs for Nrecipes ODE

typedef void (math_object::*mo_deriv_jaco)(double, double*, 
					   double*, double **, int);  
//! extra jacobian derivs

typedef double (math_object::*mo_single)(double); 
//! Simple f(x)

typedef double (math_object::*mo_double)(double,double); 
//! Simple f(x,y)

typedef double (math_object::*mo_triple)(double,double,double); 
//! Simple f(x,y,z)

typedef double (math_object::*mo_quad)(double,double,double,double); 
//! Simple f(x,y,z,t)



typedef double (math_object::*mo_open_int_single)(mo_single, math_object*, 
						  double,double,int,char *); 
//! Integral for open integration f(x)

typedef double (math_object::*mo_open_int_double)(mo_double, math_object*, 
						  double,double,double,
						  int,char *); 
//! Integral for open integration f(x,y)

typedef double (math_object::*mo_open_int_triple)(mo_triple, math_object *, 
						  double,double,double,double,
						  int,char *); 
//! Integral for open integration f(x,y,z)



#endif
