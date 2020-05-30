/*
 * @file spline.hpp
 *
 * @author Tino Kluge, Samuel Farrens
 */

#ifndef SPLINE_H
#define SPLINE_H

/**
 * @class Spline
 *
 * @brief Class for cubic spline interpolation. 
 *
 * This class performs cubic spline interpolation.
 */

#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

// spline interpolation
class Spline {
private:
  std::vector<double> m_x, m_y; // x,y coordinates of points
  // interpolation parameters
  // f(x) = a*(x-x_i)^3 + b*(x-x_i)^2 + c*(x-x_i) + y_i
  std::vector<double> m_a, m_b, m_c, m_d;
public:
  Spline(){
  };
  void set_points(const std::vector<double>& x, const std::vector<double>& y,
		  bool cubic_spline = true);
  double operator() (double x) const;
};

#endif // SPLINE_H
