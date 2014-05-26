#ifndef _STRING_SAVE_HPP_
#define _STRING_SAVE_HPP_

#include <string>


class string_safe{
private:
  int size; int number_this;
  char *tag_here;
public:
  static int number;
  string_safe(){number++;number_this=number;size=1;tag_here=(char *)calloc(1,1);    std::cout<<"Tag here start\t"<<tag_here<<"\n"<<std::flush; 
}
  string_safe(std::string name){   
    size=name.size()+1;number++;number_this=number;
    std::cout<<"Tag here start\t"<<size<<"\n"<<std::flush; 
    double aa;std::cin>>aa;
    tag_here=(char *)calloc(size,1);
    char char_here;
    for (int i=0;i<size;i++) {char_here=name[i];tag_here[i]=char_here;}
  }
  ~string_safe(){
    std::cout<<"Tag die\t"<<size<<"\t"<<tag_here<<"\t"<<number_this<<"\n"<<std::flush; 
    double aa;std::cin>>aa;
    if (tag_here!=NULL) free(tag_here);
  }
  void set_size(int size_here){
    if (tag_here!=NULL) free(tag_here); 
    tag_here=(char *)calloc(size_here,1);
    size=size_here;
  }
  void set_char(int i, char *value){tag_here[i]=value[0];}
  void set_char(int i, char value){tag_here[i]=value;}
  char char_val(const int i)
  {char char_here;char_here=tag_here[i];return char_here;}
  char& operator[](int i) const {return tag_here[i];}
  void set(std::string name){
    size=name.size();
    free(tag_here);
    tag_here=(char *)calloc(size,1);
    char char_here;
    for (int i=0;i<size;i++) {char_here=name[i];tag_here[i]=char_here;}
    std::cout<<"Tag here set\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush; 
  }
  string_safe& operator =(const string_safe &s){
    if(this != &s) {
      std::cout<<"Tag here before eq1\t"<<size<<"\t"<<s.size<<"\t"<<tag_here<<"\t"<<s.tag_here<<"\n"<<std::flush; 
      size=s.size;
      if (tag_here!=NULL) free(tag_here);
      tag_here=(char *)calloc(size,1);
      for (int i=0;i<size;i++) set_char(i,s[i]);
      std::cout<<"Tag here eq1\t"<<size<<"\t"<<s.size<<"\t"<<tag_here<<"\t"<<s.tag_here<<"\n"<<std::flush; 
    }
    return *this;
  }
  string_safe& operator =(const std::string &s){
    class string_safe test(s);
    *this=test;    
    std::cout<<"Tag here eq2\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush; 
    return *this;
  }
  string_safe operator+(const string_safe& a){
    std::cout<<"Tag here pre pl1\t"<<size<<"\t"<<a.size<<"\n"<<std::flush;     
    class string_safe ans;
    ans.set_size(size+a.size);
    char tag_char;
    for (int i=0;i<size;i++) ans.set_char(i,tag_here[i]);
    for (int i=size;i<a.size+size;i++) {
      tag_char=a[i-size];
      std::cout<<tag_char<<"\t";
      ans.set_char(i,tag_char);
    }
    std::cout<<"\n";
    std::cout<<"Tag here pl1\t"<<ans.size<<"\t"<<ans.tag_here<<"\n"<<std::flush;     
    std::cout<<"Tag here pl1\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush;     
    return ans;
  }
  string_safe operator+(const std::string &s){
    class string_safe test(s),test2;
    test2=(*this)+test;
    std::cout<<"Tag here pl2\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush; return test;
  }
  string_safe& operator +=(const string_safe& a){
    std::cout<<"Tag here pre peq\t"<<size<<"\t"<<a.size<<"\n"<<std::flush;     
    set_size(size+a.size);
    char tag_char;
    for (int i=0;i<size;i++) set_char(i,tag_here[i]);
    for (int i=size;i<a.size+size;i++) {
      tag_char=a[i-size];
      std::cout<<tag_char<<"\t";
      set_char(i,tag_char);
    }
    std::cout<<"Tag here peq\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush;     
   return *this;
  }
  string_safe& operator +=(std::string a){
    std::cout<<"Tag here pre peq2\t"<<size<<"\t"<<a.size()<<"\n"<<std::flush;     
    set_size(size+a.size());
    char tag_char;
    for (int i=0;i<size;i++) set_char(i,tag_here[i]);
    for (int i=size;i<a.size()+size;i++) {
      tag_char=a[i-size];
      std::cout<<tag_char<<"\t";
      set_char(i,tag_char);
    }
    std::cout<<"Tag here peq\t"<<size<<"\t"<<tag_here<<"\n"<<std::flush;     
   return *this;
  }

  const char *c_str(){return tag_here;}
  char *cn_str(){return tag_here;}
};
 
#endif
