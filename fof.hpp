/*PROJECTED DISTANCE*/

double proj_dist(double ra1,double ra2,double sin_dec1,double sin_dec2,double cos_dec1,double cos_dec2){
  double dist;
  dist=acos(sin_dec1*sin_dec2+cos_dec1*cos_dec2*cos(ra1-ra2));
  if(isnan(dist)) dist=0;
  return dist;
}

/*CODE TIMER*/

void d_h_m_s(double time){
  double fdays,fhours,fminutes,part0,fracpart1,fracpart2,fracpart3,fracpart4,intpart1,intpart2,intpart3,intpart4;
  fdays=24.0;
  fhours=60.0;
  fminutes=60.0;
  part0=time/(fdays*fhours*fminutes);
  fracpart1=modf(part0,&intpart1);
  fracpart2=modf(fracpart1*fdays,&intpart2);
  fracpart3=modf(fracpart2*fhours,&intpart3);
  fracpart4=modf(fracpart3*fminutes,&intpart4);
  std::cout<<" Time Elapsed: ["<<(int)intpart1<<" days | "<<(int)intpart2<<" h | "<<(int)intpart3<<" m | "<<(int)intpart4<<" s"<<"] \n"<<std::flush;
}

/*ERROR MESSAGES*/

void help(){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| ERROR: Too many arguments. Please provide path to fof_param.ini or leave blank.     |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void param_error(){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| ERROR: fof_param.ini not found. Please run set_param.cpp to produce this file.      |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void cat_error(){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| ERROR: Input catalogue invalid or not found. Please update fof_param.ini.           |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void slice_error(){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| ERROR: Insufficient redshift bins to fit spline, code requires at least 2 bins.     |\n"<<std::flush;
  std::cout<<"| Please update redshift_bin_size parameter in fof_param.ini.                         |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void over_merge_error1(int size){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| WARNING: Code attempting to merge clusters larger than "<<size<<" in friends loop.  |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void over_merge_error2(int size){
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
  std::cout<<"| WARNING: Code attempting to merge clusters larger than "<<size<<" in f-o-f loop.    |\n"<<std::flush;
  std::cout<<"|-------------------------------------------------------------------------------------|\n"<<std::flush;
}

void type_error(std::string type){
  std::cout<<"[FOF ERROR] ["<<type<<"] IS NOT A VALID OPTION FOR FOF MODE. PLEASE CHOOSE:\n"<<std::flush;
  std::cout<<"\t    - [spec] SPECTROSCOPIC\n"<<std::flush;
  std::cout<<"\t    - [phot] PHOTOMETRIC\n"<<std::flush;
}

void out_error(std::string out){
  std::cout<<"[FOF ERROR] ["<<out<<"] IS NOT A VALID OPTION FOR FOF OUTPUT. PLEASE CHOOSE:\n"<<std::flush;
  std::cout<<"\t    - [yes] OUTPUT CLUSTER CATALOGUES\n"<<std::flush;
  std::cout<<"\t    - [no] DO NOT OUTPUT CLUSTER CATALOGUES\n"<<std::flush;
}

void prog_error(std::string prog){
  std::cout<<"[FOF ERROR] ["<<prog<<"] IS NOT A VALID OPTION FOR FOF PROGRESS. PLEASE CHOOSE:\n"<<std::flush;
  std::cout<<"\t    - [yes] PRINT CODE PROGRESS\n"<<std::flush;
  std::cout<<"\t    - [no] DO NOT PRINT CODE PROGRESS\n"<<std::flush;
}
