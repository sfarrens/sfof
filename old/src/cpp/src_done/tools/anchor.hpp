#include <map>
#include <iostream>
#include <string>

#ifndef _ANCHOR_HPP_
#define _ANCHOR_HPP_

class anchor_enabled;

class anchor{
private:
  map<anchor_enabled*,anchor_enabled*> obj;
public:
  static int count;
  ~anchor() {kill();}
  void add(anchor_enabled* s) {obj[s]=s; count++;}
  void remove(anchor_enabled* s) {obj.erase(obj.find(s));count--;}
  void kill();
  void print_status(ostream &o=cout);
};

class anchor_enabled{
public:
  anchor *MyAnchor;
  anchor_enabled(anchor* a) : MyAnchor(a) {if (a) a->add(this);};
  virtual ~anchor_enabled() {if (MyAnchor) {MyAnchor->remove(this);}}
};

int anchor::count = 0;
void anchor::kill() {while (!obj.empty()) {delete obj.begin()->second;}}
void anchor::print_status(ostream &o){
  o << "anchor content " << endl;
  for (map<anchor_enabled*,anchor_enabled*>::iterator i = obj.begin(); i != obj.end(); i++) o << i->first <<"\t"<< i->second << endl;
  o << "===== end of anchor == (total count in class: "<< count << ")" << endl;
}

#endif
