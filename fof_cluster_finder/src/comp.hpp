/*Class header for Comp*/

#ifndef COMP_H
#define COMP_H

#include <iostream>
#include <math.h>
#include <time.h>
#include <stdio.h>

class Comp { //! Class structure for computational functions
private:
  time_t start, end;
  void d_h_m_s(double time, double &days, double &hours, 
	       double &minutes, double &seconds);
public:
  void start_time();
  void end_time();
  void print_time();
};

#endif /* COMP_H */
