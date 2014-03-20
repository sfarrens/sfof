#include <iostream>
#include <fstream>
 
#include "../tools/tools.hpp"
#include "./matrix.hpp"

matrix::matrix(){
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  mtrx = new vector_class[DEFAULT_ALLOC];
  assert(mtrx !=0);
  *n_row=*n_col=DEFAULT_ALLOC;
  for(int i=0;i<*n_row;i++){
    class vector_class v;
    mtrx[i]= v;
  }
}

matrix::matrix(int row, int col){
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  mtrx = new vector_class[row];
  assert(mtrx != 0);
  *n_row=row; *n_col=col;
  for(int i=0;i<row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
}

matrix::matrix(const class matrix &s){
  int i;
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  *n_row=*(s.n_row);
  mtrx = new vector_class[*n_row];
  assert(mtrx!=0);
  *n_col =*(s.n_col);
  for(i=0;i<*n_row;i++){mtrx[i]=s.mtrx[i];}
}

matrix::matrix(double **mat, int row, int col){
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  mtrx = new vector_class[row];
  assert(mtrx != 0);
  *n_row=row; *n_col=col;
  for(int i=0;i<row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
  for (int i=1;i<=*n_row;i++)
    for(int j=1;j<=*n_col;j++) mtrx[i-1][j]=mat[i][j]; 
}

matrix::matrix(std::string name){
  char tmp;
  std::ifstream save_file;
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  save_file.open(name.c_str());
  save_file>>tmp>>*n_row>>*n_col;
  mtrx = new vector_class[*n_row];
  assert(mtrx != 0);
  for(int i=0;i<*n_row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
  for(int i=1;i<=*n_row;i++)
    for (int j=1;j<=*n_col;j++)
      save_file>>mtrx[i-1][j];
  save_file.close();
}

matrix::~matrix(){
  if (n_row!=0) tools::free_ivector(n_row,0,0);
  if (n_col!=0) tools::free_ivector(n_col,0,0);
  delete [] mtrx;
}

void matrix::save(std::string name){
  std::ofstream save_file(name.c_str(),std::ios::out);
  if (save_file.is_open()){
    save_file.setf(std::ios::scientific);
    save_file<<"#"<<*n_row<<"\t"<<*n_col<<"\n";
    for (int i=1;i<=*n_row;i++){
      for(int j=1;j<=*n_col;j++) {save_file<<mtrx[i-1][j]<<"\t";}
      save_file<<"\n";
    }
    save_file<<"\n";
    save_file.close();
  } else error((char*)"Error in matrix::save, could not open file.");
}

void matrix::retrieve(std::string name){
  if (n_row!=0) tools::free_ivector(n_row,0,0);
  if (n_col!=0) tools::free_ivector(n_col,0,0);
  delete [] mtrx;
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  *n_row=2;
  *n_col=2;
  mtrx = new vector_class[*n_row];
  assert(mtrx != 0);
  for(int i=0;i<*n_row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
  mtrx[0][1]=1;
  mtrx[0][2]=0;
  mtrx[1][1]=0;
  mtrx[1][2]=1;
}

void matrix::matrix_init(int row, int col){
  if (n_row!=0) tools::free_ivector(n_row,0,0);
  if (n_col!=0) tools::free_ivector(n_col,0,0);
  delete [] mtrx;
  mtrx = new vector_class[row];
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  assert(mtrx != 0);
  *n_row=row; *n_col=col;
  for(int i=0;i<row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
};

void matrix::matrix_init(double **mat, int row, int col){
  if (n_row!=0) tools::free_ivector(n_row,0,0);
  if (n_col!=0) tools::free_ivector(n_col,0,0);
  delete [] mtrx;
  mtrx = new vector_class[row];
  n_row=tools::ivector(0,0);
  n_col=tools::ivector(0,0);
  assert(mtrx != 0);
  *n_row=row; *n_col=col;
  for(int i=0;i<row;i++){
    class vector_class v(*n_col);
    mtrx[i]=v;
  }
  for (int i=1;i<=*n_row;i++)
    for(int j=1;j<=*n_col;j++) mtrx[i-1][j]=mat[i][j]; 
};

matrix& matrix::operator =(const matrix &s){
  if(this != &s) {
    if (n_row!=0) tools::free_ivector(n_row,0,0);
    if (n_col!=0) tools::free_ivector(n_col,0,0);
    delete []mtrx;
    n_row=tools::ivector(0,0);
    n_col=tools::ivector(0,0);
    *n_row= *(s.n_row);
    *n_col=*(s.n_col);
    mtrx = new vector_class[*n_row];
    assert(mtrx !=0);
    for(int i=0;i<*n_row;i++) mtrx[i]=s.mtrx[i];
  }
  return *this;
}

vector_class& matrix::operator[](const int i){
  assert(i>0 && i <= *n_row);
  return mtrx[i-1];
}

vector_class matrix::operator*(const vector_class& v){
  int i,j;
  assert(*n_col == *(v.len));
  vector_class ans(*n_row);
  for(i=0;i<*n_row;i++){
    ans.data[i]=0.0;
    for(j=0;j<*n_col;j++) ans.data[i] += mtrx[i][j+1]*v.data[j];
  }
  return ans;
}

matrix operator*(const double& x,const matrix& s){
  class matrix ans(*(s.n_row),*(s.n_col));
  for(int i=0;i<*(ans.n_row);i++){ans.mtrx[i]= x*s.mtrx[i]; }
  return ans;
}

matrix operator*(const matrix& s,const double& x){
  matrix ans(*(s.n_row),*(s.n_col));
  for(int i=0;i<*(ans.n_row);i++){ans.mtrx[i]= x*s.mtrx[i];}
  return ans;
}

matrix matrix::operator*(const matrix& a){
  assert(*n_col == *(a.n_row));
  matrix ans(*n_row,*(a.n_col));
  for(int i=0;i<*n_row;i++){
    for(int j=0;j<*(a.n_col);j++){
      ans.mtrx[i][j+1]=0.0;
      for(int k=0;k<*n_col;k++){ans.mtrx[i][j+1]+=mtrx[i][k+1]*a.mtrx[k][j+1];}
    }
  }
  return ans;
}

matrix matrix::operator+(const matrix& a){
  int i,j;
  assert(*n_row == *(a.n_row));
  assert(*n_col == *(a.n_col));
  matrix ans(*(a.n_row),*(a.n_col));
  for(i=0;i<*(a.n_row);i++){
    for(j=0;j<*(a.n_col);j++){ans.mtrx[i][j+1] = 
				mtrx[i][j+1] + a.mtrx[i][j+1];}
  }
  return ans;
}

matrix matrix::operator-(const matrix& a){
  int i,j;
  assert(*n_row == *(a.n_row));
  assert(*n_col == *(a.n_col));
  matrix ans(*(a.n_row),*(a.n_col));
  for(i=0;i<*(a.n_row);i++){
    for(j=0;j<*(a.n_col);j++)
      {ans.mtrx[i][j+1] = mtrx[i][j+1] - a.mtrx[i][j+1];}
  }
  return ans;
}

matrix matrix::transpose(){
  class matrix ans(*n_col,*n_row);
  for(int i=0;i<*n_row;i++)
    for(int j=0;j<*n_col;j++) ans.mtrx[j+1][i]=mtrx[i][j+1];
  return ans;
}

void matrix::print(){
  for (int i=1;i<=*n_row;i++) {
    for(int j=1;j<=*n_col;j++) {std::cout<<mtrx[i-1][j]<<"\t";} 
    std::cout<<"\n";
  }
  std::cout<<"\n";
}

void matrix::print(double **mat, int a, int b){
  int i,j;
  for (i=1;i<=a;i++){
    for(j=1;j<=b;j++) {std::cout<<mat[i][j]<<"\t";}
    std::cout<<"\n";
  }
  std::cout<<"\n";
}

void matrix::mult(double **a, int ac, int ar, 
		  double **b, int bc, int br, double **tmp){
  int i,j,k;
  if (ac!=br) 
    error((char *)"Two matrices cannot be multiplied in matrix::matrix_mult.");
  for (i=1;i<=ar;i++) for (j=1;j<=ar;j++) tmp[i][j]=0;
  for (i=1;i<=ar;i++)
    for (j=1;j<=ar;j++)
      for (k=1;k<=ar;k++)
	tmp[i][j]+=a[i][k]*b[k][j];
}


double matrix::trace(){
  double value=0.0;
  if (*n_col != *n_row) error((char *)"Only sq matrix allowed matrix::trace.");
  for (int i=1;i<=*n_col;i++) value+=mtrx[i-1][i];
  return value;
}

double matrix::det(){
  double **matrix_here,value=0.0;
  if (*n_col != *n_row) error((char *)"Only sq matrix allowed matrix::det.");
  matrix_here=tools::dmatrix(1,*n_row,1,*n_row);
  for (int i=1;i<=*n_col;i++)
    for (int j=1;j<=*n_col;j++) matrix_here[i][j]=mtrx[i-1][j];
  value=lu_det(matrix_here,*n_row);
  tools::free_dmatrix(matrix_here,1,*n_row,1,*n_row);
  return value;
}

double matrix::ln_det(){
  double **matrix_here,value=0.0;
  if (*n_col != *n_row) error((char *)"Only sq matrix allowed matrix::det.");
  matrix_here=tools::dmatrix(1,*n_row,1,*n_row);
  for (int i=1;i<=*n_col;i++)
    for (int j=1;j<=*n_col;j++) matrix_here[i][j]=mtrx[i-1][j];
  value=lu_ln_det(matrix_here,*n_row);
  tools::free_dmatrix(matrix_here,1,*n_row,1,*n_row);
  return value;
}

double matrix::mat_det(double **mat,int n_row){
  double **matrix_here,value=0.0;
  matrix_here=tools::dmatrix(1,n_row,1,n_row);
  for (int i=1;i<=n_row;i++)
    for (int j=1;j<=n_row;j++) matrix_here[i][j]=mat[i][j];
  value=lu_det(matrix_here,n_row);
  tools::free_dmatrix(matrix_here,1,n_row,1,n_row);
  return value;
}  

void matrix::adjoint(double **adj){
  double **matrix_here,value=0.0;
  if (*n_col != *n_row) error((char *)"Only sq matrix allowed matrix::adj.");
  matrix_here=tools::dmatrix(1,*n_row,1,*n_row);
  for (int i=1;i<=*n_col;i++)
    for (int j=1;j<=*n_col;j++){
      for(int i0=1;i0<=*n_col;i0++)
	for (int j0=1;j0<=*n_col;j0++){
	  matrix_here[i0][j0]=mtrx[i0-1][j0];
	  if(j0==j || i0==i) matrix_here[i0][j0]=0.;
	  if(j0==j && i0==i) matrix_here[i0][j0]=1.;
	}
      adj[i][j]=mat_det(matrix_here,*n_row);
    } 
  tools::free_dmatrix(matrix_here,1,*n_row,1,*n_row);
}       
