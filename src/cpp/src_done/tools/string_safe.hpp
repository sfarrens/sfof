#ifndef _STRING_SAVE_HPP_
#define _STRING_SAVE_HPP_

#include <string>

class string_safe{
private:
  int size;
  char *tag_here;
public:
  string_safe(){size=0;tag_here=(char *)calloc(1,1);tag_here[0]='\0';}
  //set_char(size,'\0');}
  string_safe(std::string name){   
    size=name.size();
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,name.c_str());
  }
  string_safe(const string_safe& v){
    size=v.lenght();
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,v.tag_here);tag_here[size]='\0';
    //for(int i=0;i<size;i++) set_char(i,v[i]);
    //set_char(size,'\0');
  }
  ~string_safe(){if (tag_here!=NULL) free(tag_here);}
  int lenght() const {return size;}
  void set_size(int size_here){
    if (tag_here!=NULL) free(tag_here); 
    tag_here=(char *)calloc(size_here+1,1);
    size=size_here;
  }
  //void set_char(int i, const char value){tag_here[i]=value;}
  char char_val(int i) const
  {char char_here;char_here=tag_here[i];return char_here;}
  char& operator[](int i) const {return tag_here[i];}
  char& value(int i) const {return tag_here[i];}
  void set(const std::string name){
    size=name.size();
    free(tag_here);
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,name.c_str());
  }
  string_safe& operator =(const char *s){
    size=strlen(s);
    if (tag_here!=NULL) free(tag_here);
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,s);
    //for (int i=0;i<size;i++) set_char(i,s[i]);
    //set_char(size,'\0');
    return *this;
  }
  string_safe& operator =(const string_safe &s){
    if(this != &s) {
      size=s.size;
      if (tag_here!=NULL) free(tag_here);
      tag_here=(char *)calloc(size+1,1);
      strcpy(tag_here,s.tag_here);
      //for (int i=0;i<size;i++) set_char(i,s[i]);
      //set_char(size,'\0');
    }
    return *this;
  }
  string_safe& operator =(const std::string &s){
    class string_safe test(s);
    *this=test;    
    return *this;
  }
  string_safe operator+(string_safe& a){
    class string_safe ans;
    ans.set_size(size+a.size);
    strcpy(ans.tag_here,tag_here);
    strcat(ans.tag_here,a.c_str());
    //for (int i=0;i<size;i++) ans.set_char(i,tag_here[i]);
    //for (int i=size;i<a.size+size;i++) ans.set_char(i,a[i-size]);
    //ans.set_char(ans.size,'\0');
    return ans;
  }
  string_safe operator+(const std::string& a){
    class string_safe test(a),ans;
    ans.set_size(size+a.size());
    strcpy(ans.tag_here,a.c_str());
    strcat(ans.tag_here,test.c_str());
    //for (int i=0;i<size;i++) ans.set_char(i,tag_here[i]);
    //for (int i=size;i<(a.size()+size);i++) ans.set_char(i,test[i-size]);
    //ans.set_char(ans.size,'\0');
    return ans;
  }
  void add(const std::string name){
    char *new_data,char_here;int size_old=size;
    size=name.size()+size;
    new_data=(char *)calloc(size_old+1,1);
    strcpy(new_data,tag_here);
    free(tag_here);
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,new_data);
    strcat(tag_here,name.c_str());
    free(new_data);
  }
  void add(class string_safe name){
    char *old_data,char_here;int size_old=size;
    size=name.lenght()+size;
    old_data=(char *)calloc(size_old+1,1);
    strcpy(old_data,tag_here);
    free(tag_here);
    tag_here=(char *)calloc(size+1,1);
    strcpy(tag_here,old_data);
    strcat(tag_here,name.c_str());
    free(old_data);
  }
  const char *c_str(){return tag_here;}
  char *cn_str(){return tag_here;}
  int nb_items(){
    char *pch; int i=1;
    pch=strchr(tag_here,' ');
    while (pch!=NULL){
      pch=strchr(pch+1,' '); 
      if (pch-tag_here+1 < size) i++;
    }
    pch=NULL;
    return i;
  }
  class string_safe item_nb(int i){
    class string_safe string_here;
    if(size>0){
      int beg_here=0, end_here=0;
      char *pch; int ii=1;
      pch=strchr(tag_here,' ');
      end_here=pch-tag_here-1;
      for (int iii=1;iii<=i-1;iii++){
	beg_here=end_here+2;
	pch=strchr(pch+1,' ');
	end_here=pch-tag_here-1;
	if (pch==NULL) end_here=size-1;
      }
      string_here.set_size(end_here-beg_here+1);
      strncpy(string_here.tag_here,tag_here+beg_here,end_here-beg_here+1);
      string_here.tag_here[end_here-beg_here+1]='\0';   
      //string_here.set_char(end_here-beg_here+1,'\0');
    }
    return string_here;
  }
  class string_safe item_nb(int i,char char_here){
    class string_safe string_here;
    if(size>0){
      int beg_here=0, end_here=0;
      char *pch; int ii=1;
      pch=strchr(tag_here,char_here);
      end_here=pch-tag_here-1;
      for (int iii=1;iii<=i-1;iii++){
        beg_here=end_here+2;
        pch=strchr(pch+1,char_here);
        end_here=pch-tag_here-1;
        if (pch==NULL) end_here=size-1;
      }
      string_here.set_size(end_here-beg_here+1);
      strncpy(string_here.tag_here,tag_here+beg_here,end_here-beg_here+1);
      string_here.tag_here[end_here-beg_here+1]='\0';
      //string_here.set_char(end_here-beg_here+1,'\0');
    }
    return string_here;
  }
};
 
#endif
