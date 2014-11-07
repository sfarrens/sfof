/*Class of astronomy functions*/

#include <algorithm>
#include <cmath>
#include <numeric>
#include "astro.hpp"
#include "exceptions.hpp"

int Astro::find_bin (double value, double min_value, double bin_size) { 
  // Find bin corresponding to the input value given the minimum
  // value in range and the bin size.
  if (bin_size <= 0)
    throw BadArgumentException("Astro::find_bin", "bin_size", "> 0.0");
  if (value < min_value)
    throw BadArgumentException("Astro::find_bin", "value", ">= min_value");
  return floorf((value - min_value) / bin_size);
}

int Astro::num_bins (double min_value, double max_value, double bin_size) {
  // Find number of bins in a given range for a given bin size.
  if (bin_size <= 0)
    throw BadArgumentException("Astro::num_bins", "bin_size", "> 0.0");
  if (max_value <= min_value)
    throw BadArgumentException("Astro::num_bins", "max_value", "> min_value");
  return floorf((max_value - min_value) / bin_size);
}

bool Astro::within (double value, double min_value, double max_value) {
  // Deterimine whether or not a value is within the limits 
  // provided.
  if (max_value <= min_value)
    throw BadArgumentException("Astro::within", "max_value", "> min_value");
  return (value >= min_value && value < max_value);
}

double Astro::deg2rad (double angle) {
  // Function that converts angle from degrees to radians.
  return angle * M_PI / 180.0;
}

double Astro::rad2deg (double angle) {
  // Function that converts angle from radians to degrees.
  return angle * 180.0 / M_PI;
}


double Astro::angsep (const Point &P1, const Point &P2) {
  //! Function that returns the angular separation (in radians) between two points.
  if (P1.P[0] < 0 || P1.P[0] > 360)
    throw BadArgumentException("Astro::angsep", "ra1", "in the range 0 <= ra1 <= 360");
  if (P2.P[0] < 0 || P2.P[0] > 360)
    throw BadArgumentException("Astro::angsep", "ra2", "in the range 0 <= ra2 <= 360");
  if (P1.P[1] < -90 || P1.P[1] > 90)
    throw BadArgumentException("Astro::angsep", "dec1", "in the range -90 <= dec1 <= 90");
  if (P2.P[1] < -90 || P2.P[1] > 90)
    throw BadArgumentException("Astro::angsep", "dec2", "in the range -90 <= dec2 <= 90");
  if(P1.P[0] == P2.P[0] && P1.P[1] == P2.P[1])
    return 0.0;
  else
    return acos(sin(deg2rad(P1.P[1])) * sin(deg2rad(P2.P[1])) + cos(deg2rad(P1.P[1])) * 
		cos(deg2rad(P2.P[1])) * cos(deg2rad(P1.P[0]) - deg2rad(P2.P[0])));
}

double Astro::angsep (double ra1, double dec1, double ra2, double dec2) {
  // Function that returns the angular separation (in radians) between two points.
  if (ra1 < 0 || ra1 > 360)
    throw BadArgumentException("Astro::angsep", "ra1", "in the range 0 <= ra1 <= 360");
  if (ra2 < 0 || ra2 > 360)
    throw BadArgumentException("Astro::angsep", "ra2", "in the range 0 <= ra2 <= 360");
  if (dec1 < -90 || dec1 > 90)
    throw BadArgumentException("Astro::angsep", "dec1", "in the range -90 <= dec1 <= 90");
  if (dec2 < -90 || dec2 > 90)
    throw BadArgumentException("Astro::angsep", "dec2", "in the range -90 <= dec2 <= 90");
  if(ra1 == ra2 && dec1 == dec2)
    return 0.0;
  else
    return acos(sin(deg2rad(dec1)) * sin(deg2rad(dec2)) + cos(deg2rad(dec1)) * 
		cos(deg2rad(dec2)) * cos(deg2rad(ra1) - deg2rad(ra2)));
}

double Astro::mean (const std::vector<double> &elements) {
  // Function that computes the mean value of a vector of doubles.
  if (elements.empty())
    throw BadArgumentException("Astro::mean", "elements", "not empty");
  double sum = std::accumulate(elements.begin(), elements.end(), 0.0);
  return sum / double(elements.size());
}

double Astro::median (std::vector<double> elements) {
  // Function that computes the median value of a vector of doubles.
  // Pass vector by value to leave original vector unaltered.
  if (elements.empty())
    throw BadArgumentException("Astro::median", "elements", "not empty");
  int size = elements.size();
  double median;
  std::sort(elements.begin(), elements.end());
  if (size % 2 == 0)
    median = (elements[size / 2 - 1] + elements[size / 2]) / 2;
  else
    median = elements[size / 2];
  return median;
}

double Astro::variance (const std::vector<double> &elements) {
  // Function that computes the variance of a vector of doubles.
  double sum = 0;
  double mean_val = mean(elements);
  for (int i = 0; i < elements.size(); i++)
    sum += pow((elements[i] - mean_val), 2);
  return sum / double(elements.size());
}

double Astro::stdev (const std::vector<double> &elements) {
  // Function that computes the standard deviation of a vector of doubles.
  return pow(variance(elements), 0.5);
}

double Astro::stderr_mean (const std::vector<double> &elements) {
  // Function that computes the standard error of the mean
  // of a vector of doubles.
  return stdev(elements) / pow(double(elements.size()), 0.5);
}

double Astro::stderr_median (const std::vector<double> &elements) {
  // Function that computes the standard error of the median of a 
  // vector of doubles.
  return 1.253 * stderr_mean(elements);
}

double Astro::min (const std::vector<double> &elements) {
  // Function that computes the minimum value of a vector of doubles.
  if (elements.empty())
    throw BadArgumentException("Astro::min", "elements", "not empty");
  return *std::min_element(elements.begin(), elements.end());
}

double Astro::max (const std::vector<double> &elements) {
  // Function that computes the maximum value of a vector of doubles.
  if (elements.empty())
    throw BadArgumentException("Astro::max", "elements", "not empty");
  return *std::max_element(elements.begin(), elements.end());
}
