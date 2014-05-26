#ifndef _PLOT_STRUCT_HPP_
#define _PLOT_STRUCT_HPP_
 
class plot_struct{
public:
  std::string plot_xlabel,plot_ylabel,plot_plotlabel;
  std::string plot_device;
  int plot_lwidth, plot_chartype;
  float plot_charheight;
  float	plot_x1, plot_x2, plot_y1, plot_y2; // Range for coords
  float	plot_X1, plot_X2, plot_Y1, plot_Y2; // Range for ticks

  plot_struct(){
    plot_xlabel= (char *)""; 
    plot_ylabel= (char *)""; 
    plot_plotlabel= (char *)"";
    plot_device=(char *)"/xwin";
    plot_chartype = 1;
    plot_lwidth = 1;
    plot_charheight = 1;
  }
  ~plot_struct(){}
};


#endif
