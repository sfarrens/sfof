#include "./vector.hpp"

void vector_class::zero(){for(int i=0;i<*len;i++) data[i]=(double)0;}
int vector_class::length() const {return *len;}

double& vector_class::operator[](int i)const{
  assert(i > 0 && i <= *len);
  return data[i-1];
}

vector_class::vector_class(){
  len=tools::ivector(0,0);
  data = new double[DEFAULT_ALLOC];
  assert(data!=0);
  *len=  DEFAULT_ALLOC;
}

vector_class::vector_class(int n){
  len=tools::ivector(0,0);
  data = new double[*len=n];
  assert(data!=0);
}

vector_class::vector_class(const vector_class& v){
  len=tools::ivector(0,0);
  data=new double[*len=*(v.len)];
  assert(data!=0);
  for(int i=0;i<*len;i++) data[i]=v.data[i];
}

vector_class& vector_class::operator =(const vector_class &original){
  if(this != &original) {
    if (len!=0) tools::free_ivector(len,0,0);
    delete [] data;
    len=tools::ivector(0,0);
    data= new double[*len=*(original.len)];
    assert(data!=0);
    for(int i=0;i<*len;i++) data[i]=original.data[i];
  }
  return *this;
}

vector_class vector_class::operator+(const vector_class& v){
  vector_class sum(*len);
  for(int i=0;i<*len;i++) sum[i] = data[i]+v.data[i];
  return sum;
}

vector_class vector_class::operator-(const vector_class& v){
  vector_class sum(*len);
  for(int i=0;i<*len;i++) sum[i] = data[i]-v.data[i];
  return sum;
}

void  vector_class::rprint() const {
  int i;
  std::cout << "VECTOR_CLASS: ";
  std::cout << "(";
  for(i=0;i<*len-1;i++) std::cout << data[i] << ",";
  std::cout << data[*len-1] << ")" << std::endl;
  return;
}

void vector_class::resize(int n){
  delete[]data;
  data = new double[*len=n];
  assert(data !=0);
}

int vector_class::operator==(const vector_class& v)const{
  if(*len != *(v.len)) return 0;
  for(int i=0;i<*len;i++) if(data[i]!=v.data[i]) return 0;
  return 1;
}

vector_class operator*(double c,vector_class& v ){
  vector_class ans(*(v.len));
  for(int i=0;i<*(v.len);i++) ans[i]=c*v[i];
  return ans;
}

vector_class operator*(vector_class& v,double c ){
  vector_class ans(*(v.len));
  for(int i=0;i<*(v.len);i++) ans[i]=c*v[i];
  return ans;
}
