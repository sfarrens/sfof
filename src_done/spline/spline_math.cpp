#include <iostream>
 
#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "../misc_math/misc_math.hpp"
#include "spline.hpp"

double spline::integrate(double x1, double x2, double err){
  double value;
  if (!armed_y) error((char *)"spline::integrate not armed");
  math_object *mo; mo=this;
  value=misc_math::integrate((mo_single)&spline::y,mo,x1,x2,err);
  return value;
}

double spline::root(double x1, double x2, double err){
  double value;
  if (!armed_y) error((char *)"spline::root not armed");
  math_object *mo; mo=this;
  value=misc_math::root_safe((mo_derivs)&spline::y_all,mo,x1,x2,err);
  return value;
}

class spline spline::derive(){
  class spline tmp;
  math_object *mo; mo=this;
  double dummy,set_var;
  if (!armed_y) arm_y();
  set_var=misc_math::derivative((mo_single)&spline::y,mo,
				xdat[1]+1e-2*(xdat[2]-xdat[1]),
				1e-3*(xdat[2]-xdat[1]),&dummy);
  tmp.set(xdat[1],set_var);
  if (lenght>2)
    for (int k=2;k<lenght-1; k++) {
      set_var=misc_math::derivative((mo_single)&spline::y,mo,
				    xdat[k],(xdat[k+1]-xdat[k]),&dummy);
      tmp.set(xdat[k],set_var);
    }
  set_var=misc_math::derivative((mo_single)&spline::y,mo,
				xdat[lenght]+1e-2*
				(xdat[lenght]-xdat[lenght-1]),
				1e-3*(xdat[lenght]-xdat[lenght-1]),&dummy);
  if (lenght >= 2) tmp.set(xdat[lenght],set_var);
  return tmp;
}

