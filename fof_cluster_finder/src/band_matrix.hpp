/*
 * @file spline.hpp
 *
 * @author Tino Kluge, Samuel Farrens
 */

#ifndef BAND_MATRIX_H
#define BAND_MATRIX_H

/**
 * @class Band_Matrix
 *
 * @brief Band Martix solver for cubic spline
 * interpolation.
 *
 */

#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

// band matrix solver
class Band_Matrix {
private:
  std::vector< std::vector<double> > m_upper;  // upper band
  std::vector< std::vector<double> > m_lower;  // lower band
public:
  Band_Matrix() {};                             // constructor
  Band_Matrix(int dim, int n_u, int n_l) {
    resize(dim, n_u, n_l);
  }
  ~Band_Matrix() {};                            // destructor
  void resize(int dim, int n_u, int n_l);      // init with dim,n_u,n_l
  int dim() const;                             // matrix dimension
  int num_upper() const {
    return m_upper.size() - 1;
  }
  int num_lower() const {
    return m_lower.size() - 1;
  }
  // access operator
  double & operator () (int i, int j);            // write
  double   operator () (int i, int j) const;      // read
  // we can store an additional diogonal (in m_lower)
  double & saved_diag(int i);
  double  saved_diag(int i) const;
  void lu_decompose();
  std::vector<double> r_solve(const std::vector<double>& b) const;
  std::vector<double> l_solve(const std::vector<double>& b) const;
  std::vector<double> lu_solve(const std::vector<double>& b,
			       bool is_lu_decomposed=false);
};

#endif // BAND_MATRIX_H
