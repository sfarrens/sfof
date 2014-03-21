#ifndef _CLEANVECTOR_HPP_
#define _CLEANVECTOR_HPP_

#include <vector>
#include <iostream>

/*!
  A slight modification of the standard vector. The added
  functionality is automatic deleting of all data. Hence, clean_vector
  only makes sense to store pointers.
*/

template <class T> class clean_vector : public std::vector<T> {
public:
  typedef typename std::vector<T>::iterator vector_iterator;
  clean_vector<T>() : std::vector<T>() {}
  clean_vector<T>(const int i) : std::vector<T>(i) {}
  ~clean_vector() {
    //cout << "+++++++++++++++++++++ CLEANVECTOR DESTRUCTION +++++++"<<endl;
    clear();
    //cout << "++ACCOMPLISHED"<<endl;
  }
  
  void clear() {
    for (vector_iterator i=begin();i!=end();i++) {if ((*i)!=0) delete (*i);}
    std::vector<T>::clear();
  }
  
  static void clear(std::vector<T> &v) {v.clear();}

  void resize(size_t neu) {
    if (neu < size() && neu >0) {
      for (unsigned int i = neu; i < size(); i++) {
	T now  = ((*this)[i]);
	if (now  != 0) delete now;
      } 
    }
    std::vector<T>::resize(neu);
  }
  
  void print_status() {
    int count =0;
    for (vector_iterator i = begin() ; i != end() ;i++) 
      cout << count++ <<  "   " << *i << endl;	
  }  
};

#endif

