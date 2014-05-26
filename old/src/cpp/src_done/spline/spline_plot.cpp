#include <iostream>
#include <fstream>

#include "../pgplot/cpg/cpgplot.h"

#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "../plot/plot_struct.hpp"
#include "./spline.hpp"

void spline::plot(){
  float *num,*xdat_here;
  int a,i;

  if (1!=cpgbeg(0,plot_device.c_str(),1,1)) 
    error("Pgplot failed in data_vector::plot()");
  cpgslw(plot_lwidth);
  cpgsch(plot_charheight);
  cpgscf(plot_chartype);  
  num=tools::fvector(1,lenght);xdat_here=tools::fvector(1,lenght);
  plot_x1=xdat[1];
  plot_x2=xdat[1];
  plot_y1=ydat[1];
  plot_y2=ydat[1];
  num[0]=(float)xdat[1];
  xdat_here[0]=(float)ydat[1];
  for (i=1;i<=lenght;i++) {
    num[i]=(float)xdat[i];
    xdat_here[i]=(float)ydat[i];
    if (plot_x1 >= xdat[i]) plot_x1=xdat[i];
    if (plot_x2 <= xdat[i]) plot_x2=xdat[i];
    if (plot_y1 >= ydat[i]) plot_y1=ydat[i];
    if (plot_y2 <= ydat[i]) plot_y2=ydat[i];
  } 
  cpgenv(plot_x1,plot_x2,plot_y1,plot_y2,0,0);
  cpglab(this->plot_xlabel.c_str(),this->plot_ylabel.c_str(),
	 this->plot_plotlabel.c_str());

  cpgline(lenght,num,xdat_here);
  cpgclos();
  tools::free_fvector(num,1,lenght);
  tools::free_fvector(xdat_here,1,lenght);
}
