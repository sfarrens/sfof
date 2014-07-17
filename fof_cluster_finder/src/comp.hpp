/**
 * @file comp.hpp
 *
 * @author Samuel Farrens
 */

#ifndef COMP_H
#define COMP_H

/**
 * @class Comp
 *
 * @brief Class containing basic functions used in generic codes.
 */

#include <iostream>
#include <math.h>
#include <time.h>
#include <stdio.h>

class Comp { // Class structure for computational functions

public:

  /**
   * This method sets the start walltime.
   */
  void start_time();

  /**
   * This method sets the end walltime.
   */
  void end_time();

  /**
   * This method prints the elapsed walltime.
   */
  void print_time();

private:
  
  /// Start walltime
  time_t start;

  /// End walltime
  time_t end;
  
  /**
   * This method converts the walltime to days, hours, miutes and seconds.
   * @param time Input walltime.
   * @param days Placeholder for numbers of days.
   * @param hours Placeholder for numbers of hours.
   * @param minutes Placeholder for numbers of minutes.
   * @param seconds Placeholder for numbers of seconds.
   */
  void d_h_m_s(double, double &, double &, double &, double &);

};

#endif // COMP_H
