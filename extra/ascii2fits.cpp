//*************************************************//
//***ascii2fits written by Samuel Farrens (2012)***//
//*************************************************//
//***********LAST UPDATE: 02-08-2012***************//
//*************************************************//
#include "/Users/Rowen/Documents/Library/include.hpp"
#include "/Users/Rowen/Documents/Library/fits.hpp" //*Include FITSIO packages*//

class do_stuff{
private:
public: 
  int n_cols; 
  std::string in_file_name,out_file_name;
  std::vector<std::string> ttype_vec,tform_vec;
  std::vector< std::vector<std::string> > test_vec;
  void skip_comments(std::ifstream& fstr);
  void count_cols(const std::string &fname);
  void set_vector(int n);
  void read_ascii_file(const std::string &fname);
  void write_fits_file();
  void merge_fits(const std::string &fname,int &new_cols);
};

void do_stuff::skip_comments(std::ifstream& fstr){
  char a;
  fstr>>a;
  if(a=='#'){
    fstr.ignore(2147483647,'\n');
    skip_comments(fstr);
  } else fstr.unget();
}

void do_stuff::count_cols(const std::string &fname){
  std::string line,temp;
  std::vector<std::string> col_count;
  std::ifstream test_file(fname.c_str());
  skip_comments(test_file);
  getline(test_file,line);
  std::stringstream line_stream(line,std::stringstream::in);
  test_file.close();
  while(!line_stream.eof()){
    line_stream>>temp;
    col_count.push_back(temp);
    line_stream>>std::ws;
  }
  n_cols=col_count.size();
  line.clear();
  temp.clear();
  line_stream.str("");
  col_count.clear();
  set_vector(n_cols);
}

void do_stuff::set_vector(int n){
  for(int i=0;i<n;i++) test_vec.push_back(std::vector<std::string>());
}

void do_stuff::read_ascii_file(const std::string &fname){
  std::string s_var;
  std::ifstream read_file(fname.c_str());
  skip_comments(read_file);
  for(;;){
    read_file>>s_var;
    if(read_file.eof()) break;
    test_vec[0].push_back(s_var);
    for(int i=1;i<n_cols;i++){
      read_file>>s_var;
      test_vec[i].push_back(s_var);
    }
  }
  read_file.close();
}

void do_stuff::write_fits_file(){
  fitsfile *fptr;
  int tint,status=0;
  double tdouble;
  const int tfields=test_vec.size();
  char *ttype[ttype_vec.size()],*tform[tform_vec.size()],*tstring;
  for(int i=0;i<ttype_vec.size();i++){
    ttype[i]=const_cast<char *>(ttype_vec[i].c_str());
    tform[i]=const_cast<char *>(tform_vec[i].c_str());
  }
  fits_create_file(&fptr,out_file_name.c_str(),&status); /*create new FITS file*/
  if(status!=0){
    std::cout<<"Error! Cannot create FITS file.\n"<<std::flush;
    exit(-1);
  }
  fits_create_tbl(fptr,BINARY_TBL,0,tfields,ttype,tform,NULL,NULL,&status); /*create new FITS table*/ 
  for(int j=1;j<=test_vec[0].size();j++){
    for(int i=1;i<=test_vec.size();i++){
      if(tform_vec[i-1].find("V")!=std::string::npos){
	tint=atoi(test_vec[i-1][j-1].c_str());
	fits_write_col(fptr,TUINT,i,j,1,1,&tint,&status);
      }
      else if(tform_vec[i-1].find("E")!=std::string::npos || tform_vec[i-1].find("D")!=std::string::npos){
	tdouble=atof(test_vec[i-1][j-1].c_str());
	fits_write_col(fptr,TDOUBLE,i,j,1,1,&tdouble,&status);
      }
      else if(tform_vec[i-1].find("A")!=std::string::npos){
	tstring=const_cast<char *>(test_vec[i-1][j-1].c_str());
	fits_write_col(fptr,TSTRING,i,j,1,1,&tstring,&status); 
      }
    }
  }
  fits_close_file(fptr,&status); /*close FITS file*/
  ttype_vec.clear();
  tform_vec.clear();
  test_vec.clear();
}

void help();
void error1();
void error2();
void error3();
void error4();
void error5();
void error6();

int main (int argc, char *argv[]){
  class do_stuff do_it;
  if(argc==1) help();
  for(int i=1;i<argc;i++){
    if(argv[i][0]=='-' && std::strlen(argv[i])>1){
      switch(argv[i][1]){
      case 'h' : 
      case 'H' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-help")) help();
	break;
      case 'i' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-int")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') do_it.in_file_name=argv[i+1];
	  else error1();
	  if((i+1)!=(argc-1) && argv[i+2][0]!='-') error4();
	}
	break;
      case 'o' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-out")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') do_it.out_file_name=argv[i+1];
	  else error3();
	  if((i+1)!=(argc-1) && argv[i+2][0]!='-') error4();
	}
	break;
      case 'n' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-name")){
	  for(int j=i+1;j<argc;j++){
	    if(argv[j][0]!='-') do_it.ttype_vec.push_back(argv[j]);
	    else break;
	  }
	  if(do_it.ttype_vec.size()<1) error2();
	}
	break;
      case 'f' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-format")){
	  for(int j=i+1;j<argc;j++){
	    if(argv[j][0]!='-') do_it.tform_vec.push_back(argv[j]);
	    else break;
	  }
	  if(do_it.tform_vec.size()<1) error2();
	}
	break;
      }
    }
  }
  if(do_it.in_file_name.empty()) error1();
  if(do_it.out_file_name.empty()) error3();
  do_it.count_cols(do_it.in_file_name);
  if(do_it.tform_vec.size()<do_it.n_cols || do_it.ttype_vec.size()<do_it.n_cols) error5();
  for(int i=0;i<do_it.tform_vec.size();i++){
    if(do_it.tform_vec[i].find("A")==std::string::npos && do_it.tform_vec[i].find("E")==std::string::npos &&
       do_it.tform_vec[i].find("D")==std::string::npos && do_it.tform_vec[i].find("V")==std::string::npos)
      error6();
  }
  do_it.read_ascii_file(do_it.in_file_name);
  do_it.write_fits_file();
  return 0;
}

void help(){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| This code outputs a FITS binary table from an input ASCII table.                    |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;  
  std::cout<<"| OPTIONS:\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t-h [help]\tDisplays this help page.\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t-i [input]\tAn input file name should be provided as an argument          |\n"<<std::flush;
  std::cout<<"|\t\t        following this option.                                        |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t-o [output]\tAn output file name should be provided as an argument         |\n"<<std::flush;
  std::cout<<"|\t\t        following this option. This option must be used in            |\n"<<std::flush;
  std::cout<<"|\t\t        conjunction with -i.                                          |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t-n [name]\tHeader names for each column should be provided as arguments  |\n"<<std::flush;
  std::cout<<"|\t\t        following this option. The number of header names must match  |\n"<<std::flush;
  std::cout<<"|\t\t        the number of columns in the input file. This option must be  |\n"<<std::flush;
  std::cout<<"|\t\t        used in conjunction with -i.                                  |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t-f [format]\tCFITSIO TFORM codes for each column should be provided as     |\n"<<std::flush;
  std::cout<<"|\t\t        arguments following this option. The number of codes must     |\n"<<std::flush;
  std::cout<<"|\t\t        match the number of columns in the input file. This option    |\n"<<std::flush;
  std::cout<<"|\t\t        must be used in conjunction with -i.                          |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| CFITSIO TFORM CODES:\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\tV [TUINT]\tUnsigned integer value.                                       |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\tE [TFLOAT]\tSingle precision floating-point value.                        |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\tD [TDOUBLE]\tDouble precision floating-point value.                        |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t#A [TSTRING]\tASCII string. # is the number of characters in the string.    |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| EXAMPLES:\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t> ascii2fits -i file.txt -o file.fit -n id x y -f V E E                       |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"| This will read an ASCII file with columns id (int), x (double) and y (double) and   |\n"<<std::flush;
  std::cout<<"| output a FITS file with the same information.                                       |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"|\t> ascii2fits -i file.txt -o file.fit -n string1 string2 -f 8A 16A             |\n"<<std::flush;
  std::cout<<"|\t\t\t\t\t\t\t\t\t\t      |\n"<<std::flush;
  std::cout<<"| This will read an ASCII file with columns string1 (string with 8 characters) and    |\n"<<std::flush;
  std::cout<<"| string2 (string with 16 characters) and output a FITS file with the same            |\n"<<std::flush;
  std::cout<<"| information.                                                                        |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;  
  exit(0);
}

void error1(){
  std::cout<<"ERROR!: Input file name not specified.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}

void error2(){
  std::cout<<"ERROR!: Must specify column names and formats.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}

void error3(){
  std::cout<<"ERROR!: Output file name not specified.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}

void error4(){
  std::cout<<"ERROR!: Only one file name can be specified for input or output.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}

void error5(){
  std::cout<<"ERROR!: The number of column names and formats must match number of columns in the input file.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}

void error6(){
  std::cout<<"ERROR!: Invalid CFITSIO TFORM code.\n"<<std::flush;
  std::cout<<"Use -h option to display help.\n"<<std::flush;
  exit(-1);
}
