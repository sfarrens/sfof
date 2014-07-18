/**
 * @file astro.hpp
 *
 * @author Samuel Farrens
 */

#ifndef ASTRO_H
#define ASTRO_H

/**
 * @class Astro
 *
 * @brief Class containing basic functions required for astronomy.
 *
 * This class encompasses a selection of functions that perform some
 * basic calculations that often required for astronomy or cosmology.
 */

#include <algorithm>
#include <math.h>
#include <numeric>
#include <vector>

class Astro { // Class structure for astronmy functions

public:

  /**
   * This method finds a bin corresponding to the input value given the
   * minimum value in range and the bin size.
   * @param[in] value Input value.
   * @param[in] min_value Minimum value in the range.
   * @param[in] bin_size Bin size.
   * @return Bin number corresponding to the input value.
   */
  int find_bin (double, double, double);

  /**
   * This method finds the number of bins in a given range for a given
   * bin size.
   * @param[in] min_value Maximum value in the range.
   * @param[in] max_value Minimum value in the range.
   * @param[in] bin_size Bin size.
   * @return Number of bins in the relevant range. 
   */
  int num_bins (double, double, double);

  /**
   * This method deterimines whether or not a value is within the limits 
   * provided.
   * @param[in] value Input value.
   * @param[in] min_value Maximum value in the range.
   * @param[in] max_value Minimum value in the range.
   */
  bool within (double, double, double);

  /**
   * This method converts the input angle from degrees to radians.
   * @param[in] angle Input angle in degrees.
   * @return Angle in radians.
   */
  double deg2rad (double);

  /**
   * This method converts the input angle from radians to degrees.
   * @param[in] angle Input angle in radians.
   * @return Angle in degrees.
   */
  double rad2deg (double);

  /**
   * This method calculates the angular separation in radians between
   * two points.
   * @param[in] ra1 Right ascension of first point.
   * @param[in] dec1 Declination of first point.
   * @param[in] ra2 Right ascension of second point.
   * @param[in] dec2 Declination of second point.
   * @return Anugular separation in radians. 
   */
  double angsep (double, double, double, double);

  /**
   * This method calculates the mean value of a vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Mean value. 
   */
  double mean (const std::vector<double> &);

  /**
   * This method calculates the median value of a vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Median value. 
   */
  double median (std::vector<double>);

  /**
   * This method calculates the variance of a vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Variance. 
   */
  double variance (const std::vector<double> &);

  /**
   * This method calculates the standard deviation of a vector of 
   * doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Standard deviation. 
   */
  double stdev (const std::vector<double> &);

  /**
   * This method calculates the standard error on the mean of a vector  
   * of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Standard error on the mean. 
   */
  double stderr (const std::vector<double> &);

  /**
   * This method calculates the standard error on the median of a   
   * vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Standard error on the median. 
   */
  double stderr_median (const std::vector<double> &);

  /**
   * This method calculates the minimum value of a vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Minimum value. 
   */
  double min (const std::vector<double> &);

  /**
   * This method calculates the maximum value of a vector of doubles.
   * @param[in] elements Vector of double floating point values.
   * @return Maximum value. 
   */
  double max (const std::vector<double> &);

};

#endif // ASTRO_H
