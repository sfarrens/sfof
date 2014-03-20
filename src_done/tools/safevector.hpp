#ifndef _SAFEVECTOR_HPP_
#define _SAFEVECTOR_HPP_

#include <vector>
#include <iostream>
#include <list>

struct safe_vector_out_of_range {};

/*!
  Safe vector class that does range checking for the [] operator.
  If necessary, it asks vector for resize() 
*/

template <class T> class safe_vector : public std::vector<T> {
public:
  typedef typename std::vector<T>::reference safe_vector_reference;
  typedef typename std::vector<T>::const_reference const_safe_vector_reference;
  typedef typename list<T>::const_reference safe_list_iterator;
  
  safe_vector<T>() : std::vector<T>() {}
  safe_vector<T>(const int i) : std::vector<T>(i) {}
  safe_vector<T>(const list<T>& li) : std::vector<T>(li.size()) {
    for (safe_list_iterator i = li.begin(); i != li.end(); i++) 
      push_back(*i);
  }

  safe_vector_reference operator[](size_t __n) {
    if (__n >= size() ) resize(__n + 1);
    return *(begin() + __n); 
  }
  const_safe_vector_reference  operator[](size_t __n) const  { 
    if (__n >= size() ) throw safe_vector_out_of_range(); // resize(__n + 1);
    return *(begin() + __n); 
  }
};

#endif

