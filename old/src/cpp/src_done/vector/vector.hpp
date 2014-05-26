#ifndef _VECTOR_CLASS_HPP_
#define _VECTOR_CLASS_HPP_

#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include "../tools/tools.hpp"

class matrix;

class vector_class{
private:
  static const int DEFAULT_ALLOC=2;
  friend class matrix;
  double *data;
  int *len;
public:
  // Constructors and Destructors
  vector_class();
  vector_class(int n);
  ~vector_class(){kill();}
  vector_class(const vector_class& v) ;
  void kill(){if (len!=0) tools::free_ivector(len,0,0);delete [] data;};
  
  // Operator
  vector_class& operator =(const vector_class &original);
  vector_class operator+(const vector_class& v);
  vector_class operator-(const vector_class&v);
  int operator==(const vector_class& v)const;
  friend vector_class operator*(double c,vector_class& v );
  friend vector_class operator*(vector_class& v,double c );
  double& operator[](int i)const  ;
  
  // Other
  int length() const;
  void zero();
  void rprint() const;  //print entries on a single line
  void resize(int n);
  
};

#endif
