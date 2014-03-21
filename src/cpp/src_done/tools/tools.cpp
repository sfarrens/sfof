#include <iostream>
#include <fstream>
#include "./tools.hpp"

std::string tools_var::dir="";

void tools::error(char error_text[]){
  double a;
  fprintf(stderr,"Standard run-time error...\n");
  fprintf(stderr,"%s\n",error_text);
  fprintf(stderr,"...now exiting to system...\n");
  std::cin>>a; exit(1);
}

float *tools::fvector(int nl, int nh){
  float *v;
  v=(float *)malloc((size_t) ((nh-nl+1+1)*sizeof(float)));
  if (!v) tools::error((char *)"allocation failure in tools::fvector()");
  return v-nl+1;
}

int *tools::ivector(int nl, int nh){
  int *v;
  v=(int *)malloc((size_t) ((nh-nl+1+NR_END1)*sizeof(int)));
  if (!v) tools::error((char *)"allocation failure in tools::ivector()");
  return v-nl+NR_END1;
}

unsigned char *tools::cvector(int nl, int nh){
  unsigned char *v;
  v=(unsigned char *)malloc((size_t) ((nh-nl+1+NR_END1)*sizeof(unsigned char)));
  if (!v) tools::error((char *)"allocation failure in tools::cvector()");
  return v-nl+NR_END1;
}

char *tools::chvector(int nl, int nh){
  char *v;
  v=(char *)malloc((size_t) ((nh-nl+1+NR_END1)*sizeof(char)));
  if (!v) tools::error((char *)"allocation failure in tools::cvector()");
  return v-nl+NR_END1;
}

unsigned long *tools::lvector(int nl, int nh){
  unsigned long *v;
  v=(unsigned long *)malloc((size_t) ((nh-nl+1+1)*sizeof(unsigned long)));
  if (!v) tools::error((char *)"allocation failure in tools::lvector()");
  return v-nl+1;
}

double *tools::dvector(int nl, int nh){
  double *v;
  //static int i;
  //i++;
  //std::cout<<"nl is\t"<<nl<<"nh is\t"<<nh<<"\t"<<i<<"\t"<<v<<"\n"<<std::flush;
  v=(double *)malloc((size_t) ((nh-nl+1+NR_END1)*sizeof(double)));
  //v = new double [nh+1];
  //if (!v) tools::error((char *)"allocation failure in tools::dvector()");
  return v-nl+NR_END1;
 
  //return v;
}

bool *tools::bvector(int nl, int nh){
  bool *v;
  v=(bool *)malloc((size_t) ((nh-nl+1+NR_END1)*sizeof(bool)));
  //v = new double [nh+1];
  if (!v) tools::error((char *)"allocation failure in tools::dvector()");
  return v-nl+NR_END1;
  //return v;
}

void tools::free_fvector(float *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}
void tools::free_ivector(int *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}
void tools::free_cvector(unsigned char *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}
void tools::free_chvector(char *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}
void tools::free_lvector(unsigned long *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}
void tools::free_dvector(double *v, int nl, int nh){
  free((char*) (v+nl-NR_END1));
  //std::cout<<v<<"\n"<<std::flush;
  //delete[] v;
}
void tools::free_bvector(bool *v, int nl, int nh)
{free((char*) (v+nl-NR_END1));}

float **tools::fmatrix(int nrl, int nrh, int ncl, int nch){
  int i, nrow=nrh-nrl+1,ncol=nch-ncl+1;
  float **m;
  m=(float **) malloc((size_t)((nrow+NR_END1)*sizeof(float*)));
  if (!m) tools::error((char *)"allocation failure 1 in tools::fmatrix()");
  m += NR_END1;
  m -= nrl;
  m[nrl]=(float *) malloc((size_t)((nrow*ncol+NR_END1)*sizeof(float)));
  if (!m[nrl]) 
    tools::error((char *)"allocation failure 2 in tools::fmatrix()");
  m[nrl] += NR_END1;
  m[nrl] -= ncl;
  for(i=nrl+1;i<=nrh;i++) m[i]=m[i-1]+ncol;
  return m;
}

double **tools::dmatrix(int nrl, int nrh, int ncl, int nch){
  int i, nrow=nrh-nrl+1,ncol=nch-ncl+1;
  double **m;
  m=(double **) malloc((size_t)((nrow+NR_END1)*sizeof(double*)));
  if (!m) tools::error((char *)"allocation failure 1 in tools::dmatrix()");
  m += NR_END1;
  m -= nrl;
  m[nrl]=(double *) malloc((size_t)((nrow*ncol+NR_END1)*sizeof(double)));
  if (!m[nrl]) tools::error((char *)"allocation failure 2 in tools::dmatrix()");
  m[nrl] += NR_END1;
  m[nrl] -= ncl;
  for(i=nrl+1;i<=nrh;i++) m[i]=m[i-1]+ncol;
  return m;
}

int **tools::imatrix(int nrl, int nrh, int ncl, int nch){
  int i, nrow=nrh-nrl+1,ncol=nch-ncl+1;
  int **m;
  m=(int **) malloc((size_t)((nrow+NR_END1)*sizeof(int*)));
  if (!m) tools::error((char *)"allocation failure 1 in tools::imatrix()");
  m += NR_END1;
  m -= nrl;
  m[nrl]=(int *) malloc((size_t)((nrow*ncol+NR_END1)*sizeof(int)));
  if (!m[nrl]) 
    tools::error((char *)"allocation failure 2 in tools::imatrix()");
  m[nrl] += NR_END1;
  m[nrl] -= ncl;
  for(i=nrl+1;i<=nrh;i++) m[i]=m[i-1]+ncol;
  return m;
}

float **tools::submatrix(float **a, int oldrl, int oldrh, 
			 int oldcl, int oldch, int newrl, int newcl){
  int i,j,nrow=oldrh-oldrl+1,ncol=oldcl-newcl;
  float **m;
  m=(float **) malloc((size_t) ((nrow+NR_END1)*sizeof(float*)));
  if (!m) tools::error((char *)"allocation failure in tools::submatrix()");
  m += NR_END1;
  m -= newrl;
  for(i=oldrl,j=newrl;i<=oldrh;i++,j++) m[j]=a[i]+ncol;
  return m;
}

float **tools::convert_matrix(float *a, int nrl, int nrh, 
			      int ncl, int nch){
  int i,j,nrow=nrh-nrl+1,ncol=nch-ncl+1;
  float **m;
  m=(float **) malloc((size_t) ((nrow+NR_END1)*sizeof(float*)));
  if (!m) 
    tools::error((char *)"allocation failure in tools::convert_matrix()");
  m += NR_END1;
  m -= nrl;
  m[nrl]=a-ncl;
  for(i=1,j=nrl+1;i<nrow;i++,j++) m[j]=m[j-1]+ncol;
  return m;
}

void tools::free_fmatrix(float **m, int nrl, int nrh, int ncl, int nch){
  free((char *) (m[nrl]+ncl-1));
  free((char *) (m+nrl-1));
}

void tools::free_dmatrix(double **m, int nrl, int nrh, int ncl, int nch){
  free((char *) (m[nrl]+ncl-NR_END1));
  free((char *) (m+nrl-NR_END1));
}

void tools::free_imatrix(int **m, int nrl, int nrh, int ncl, int nch){
  free((char *) (m[nrl]+ncl-NR_END1));
  free((char *) (m+nrl-NR_END1));
}

void tools::free_submatrix(float **b, int nrl, int nrh, int ncl, int nch){
  free((char *) (b+nrl-NR_END1));
}

void tools::free_convert_matrix(float **b, int nrl, int nrh, 
				int ncl, int nch){
  free((char *) (b+nrl-NR_END1));
}

float ***tools::f3tensor(int nrl, int nrh, int ncl, 
			 int nch, int ndl, int ndh){
  int i,j,nrow=nrh-nrl+1,ncol=nch-ncl+1,ndep=ndh-ndl+1;
  float ***t;
  t=(float ***) malloc((size_t)((nrow+NR_END1)*sizeof(float**)));
  if (!t) tools::error((char *)"allocation failure 1 in tools::f3tensor()");
  t += NR_END1;
  t -= nrl;
  t[nrl]=(float **) malloc((size_t)((nrow*ncol+NR_END1)*sizeof(float*)));
  if (!t[nrl]) 
    tools::error((char *)"allocation failure 2 in tools::f3tensor()");
  t[nrl] += NR_END1;
  t[nrl] -= ncl;
  t[nrl][ncl]=(float *) 
    malloc((size_t)((nrow*ncol*ndep+NR_END1)*sizeof(float)));
  if (!t[nrl][ncl]) 
    tools::error((char *)"allocation failure 3 in tools::f3tensor()");
  t[nrl][ncl] += NR_END1;
  t[nrl][ncl] -= ndl;
  for(j=ncl+1;j<=nch;j++) t[nrl][j]=t[nrl][j-1]+ndep;
  for(i=nrl+1;i<=nrh;i++) {
    t[i]=t[i-1]+ncol;
    t[i][ncl]=t[i-1][ncl]+ncol*ndep;
    for(j=ncl+1;j<=nch;j++) t[i][j]=t[i][j-1]+ndep;
  }
  return t;
}

double ***tools::d3tensor(int nrl, int nrh, int ncl, 
			  int nch, int ndl, int ndh){
  int i,j,nrow=nrh-nrl+1,ncol=nch-ncl+1,ndep=ndh-ndl+1;
  double ***t;
  t=(double ***) malloc((size_t)((nrow+NR_END1)*sizeof(double**)));
  if (!t) tools::error((char *)"allocation failure 1 in tools::d3tensor()");
  t += NR_END1;
  t -= nrl;
  t[nrl]=(double **) malloc((size_t)((nrow*ncol+NR_END1)*sizeof(double*)));
  if (!t[nrl]) 
    tools::error((char *)"allocation failure 2 in tools::d3tensor()");
  t[nrl] += NR_END1;
  t[nrl] -= ncl;
  t[nrl][ncl]=(double *) 
    malloc((size_t)((nrow*ncol*ndep+NR_END1)*sizeof(double)));
  if (!t[nrl][ncl]) 
    tools::error((char *)"allocation failure 3 in tools::d3tensor()");
  t[nrl][ncl] += NR_END1;
  t[nrl][ncl] -= ndl;
  for(j=ncl+1;j<=nch;j++) t[nrl][j]=t[nrl][j-1]+ndep;
  for(i=nrl+1;i<=nrh;i++) {
    t[i]=t[i-1]+ncol;
    t[i][ncl]=t[i-1][ncl]+ncol*ndep;
    for(j=ncl+1;j<=nch;j++) t[i][j]=t[i][j-1]+ndep;
  }
  return t;
}

void tools::free_f3tensor(float ***t, int nrl, int nrh, int ncl, int nch,
		   int ndl, int ndh){
  free((char *) (t[nrl][ncl]+ndl-NR_END1));
  free((char *) (t[nrl]+ncl-NR_END1));
  free((char *) (t+nrl-NR_END1));
}

void tools::free_d3tensor(double ***t, int nrl, int nrh, int ncl, int nch,
		   int ndl, int ndh){
  free((char *) (t[nrl][ncl]+ndl-NR_END1));
  free((char *) (t[nrl]+ncl-NR_END1));
  free((char *) (t+nrl-NR_END1));
}


void *km_malloc(size_t size){
 void *return_pointer;
 if ( (return_pointer=malloc(size)) == NULL ){
   fprintf(stderr,"malloc error - abort\n"); abort();
 }
 return return_pointer;
}

double tools::gauss_here(double z, double i){
  double value;
  double mu, sig;
  sig = 0.005;
  if (i == 1) {mu = 0.009;}
  else  {
    if (i == 2) {mu = 0.017;}
    else {
      if (i == 3) {mu = 0.025;}
      else {if (i == 4) {mu = 0.032;}}
    }
  }
  value=(1.0/sqrt(2*M_PI*sig*sig))*exp(-pow(z-mu,2)/2.0/sig/sig);
  return value;
}

void tools::separate_line(const std::string& buffer, 
			  std::vector<std::string>& data){  
  std::stringstream ss(buffer, std::stringstream::in);
  std::string temp;
  data.clear();
  while (!ss.eof()) {
    ss >> temp;
    data.push_back(temp);
    ss >> std::ws;
  }
}

//void tools::find_NR_NC(const class string_safe &filename_here, 
//		       int &NR, int &NC) {
// class string_safe filename;filename=filename_here;
//Find out the number of rows
// FILE *in = fopen(filename.c_str(), "r");
//char line[1024];
//char *token = NULL;
//fgets(line, 1024, in);
//token = strtok(line, "\t \n");
//NC = 0;
//while (token != NULL) {
//  NC++;
//  token = strtok(NULL, "\t \n");
//}
//Find out the number of rows
// NR = 0;
//while (!feof(in)) {
//  NR++;
//  fgets(line, 1024, in);
//}
//fclose(in);
//}

//-------------------------------------------------
// Skip past comments/ blank lines in a file.
void tools::skip_comments(std::ifstream& fstr){
  // Read the next non-whitespace character on the stream.
  char a;
  fstr >> a;
  // Check whether it's a commenting mark.
  if (a == '#') {
    // Skip to the end of the line.
    // fstr.ignore(numeric_limits<streamsize>::max(), '\n'); 
    // Seems to be incompatible with gcc v2.x
    fstr.ignore(2147483647, '\n');
    // Recurse.
    skip_comments(fstr);
  } else {
    // Step back to the start of the line.
    fstr.unget();
  }
}

// Locate the next non-comment and non-blank line from the given file stream.
bool tools::get_next_dataline(std::ifstream& file, std::string& line) {
  skip_comments(file);
  // Return fail if end of file.
  if (file.eof()) return false;
  // Put the next line in 'line'
  getline(file, line);
  return true;
}

void tools::find_NR_NC(const class string_safe &filename_here,int &NR,int &NC){
  std::ifstream file;
  class string_safe filename;filename=filename_here;
  file.open(filename.c_str());
  std::string buffer;
  std::vector<std::string> data;
  get_next_dataline(file, buffer);
  separate_line(buffer,data);
  NC = data.size(); data.clear();
  NR = 1;
  while (get_next_dataline(file, buffer)){
    separate_line(buffer,data);
    NR++; if (NC != data.size()) NR--;
    data.clear();
  }
}
