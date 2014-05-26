/*Class header for Astro*/

#ifndef ASTRO_H
#define ASTRO_H

#include <algorithm>
#include <math.h>
#include <numeric>
#include <vector>

class Astro { //! Class structure for astronmy functions
public:
  int find_bin (double, double, double);
  int num_bins (double, double, double);
  bool within (double, double, double);
  double deg2rad (double);
  double rad2deg (double);
  double angsep (double, double, double, double);
  double mean (const std::vector<double> &);
  double median (std::vector<double>);
  double min (const std::vector<double> &);
  double max (const std::vector<double> &);
};

#endif /* ASTRO_H */
