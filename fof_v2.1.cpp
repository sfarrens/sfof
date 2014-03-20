//************************************************************************************************//
//******************************************FOF v2.1**********************************************//
//************************************************************************************************//
//***Friends-of-Friends Cluster Finder written by Samuel Farrens (2007).                       ***//
//************************************************************************************************//
//************************************LAST UPDATE: 07-01-2014*************************************//
//************************************************************************************************//
//***Method follows that described in Botzler et al. (2003), intially coded by Eduardo Cypriano***//
//***with significant contributions made by Filipe Abdalla.                                    ***//
//************************************************************************************************//
//***Contact Details: farrens@ieec.uab.es, fba@star.ucl.ac.uk, cypriano@astro.iag.usp.br       ***//
//************************************************************************************************//

#include "./include.hpp"  //*Include C++ packages and cosmology routines*//

#include "./fof.hpp"

typedef std::vector<int> intvec;            /*Define integer vector for structures*/
typedef std::vector<double> doublevec;      /*Define double vector for structures*/
typedef std::vector<std::string> stringvec; /*Define string vector for structures*/

struct galaxy_clust{                //***Define Structues for Galaxies, Protoclusters & Clusters***//
  galaxy_clust(int nfrinds){for(int i=0;i<nfrinds;i++) friends.push_back(-1);}
  int num;                          /*Galaxy Number assigned by code*/
  std::string id;                   /*Galaxy ID from input catalogue*/
  double ra;                        /*Galaxy Right Ascension from input catalogue*/
  double dec;                       /*Galaxy Declination from input catalogue*/
  double sindec;                    /*Sine of galaxy Declination assigned by code*/
  double cosdec;                    /*Cosine of galaxy Declination assigned by code*/
  float z;                          /*Galaxy Photometric Redshift from input catalogue*/
  float z_err;                      /*Galaxy Photometric Redshift Error from input catalogue*/
  intvec friends;                   /*Number of friends of galaxy assigned by code*/
  std::string mock_halo_id;         /*ID of halo to which galaxy belongs (calibration mode only)*/
  double mock_halo_mass;            /*MASS of halo to which galaxy belongs (calibration mode only)*/
  int mock_halo_rich;               /*Richness of halo to which galaxy belongs (calibration mode only)*/
};
struct protocluster{
  int id;                           /*Protocluster ID*/
  int zslice;                       /*Number of Redhsift Slice at whcih Protocluster is found*/
  intvec member_num;                /*Galaxy Number of Protocluster member*/
  doublevec zmem,ramem,decmem;      /*Galaxy z, ra & dec of Protocluster member*/
};  
struct cluster{
  int id;                           /*Cluster ID*/
  intvec member_num;                /*Galaxy Number of Cluster member*/
  doublevec zmem,ramem,decmem;      /*Galaxy z, ra & dec of Cluster member*/
  float z;                          /*Cluster Redshift*/
  double ra;                        /*Cluster Right Ascension*/
  double dec;                       /*Cluster Declination*/
  double std;                       /*Cluster Velocity Dispersion (km/s)*/
  double size;                      /*Cluster Diameter (Mpc)*/
  double mass;                      /*Cluster Mass (10^13 M_solar)*/
};

class cluster_finder{               //***Define class with FoF variables & subroutines***//
private:
  class kdtree tree_cluster;        /*Load kdtree class*/
  class spline R_fr;                /*Load spline class*/
  std::vector<protocluster> prtclt; /*Protocluster Structure Vector*/
  std::vector<galaxy_clust> gal;    /*Galaxy Structure Vector*/
  std::vector<float> v_0,R_friend;  /*Linking Parameters*/
  std::vector<double> z_sliced;     /*Redshift Bins*/
public:
  int Nslices,k;                    /*Number of z bins & Protrocluster Count*/
  std::vector<cluster> clt;         /*Cluster Structure Vector*/
  std::vector< std::vector<std::string> > test_vec,test_vec2;
  /*INPUT PARAMETERS*/
  std::string file_name,file_type,param_file,calibrate,type,out_cat,progress,r_as_z,profiles,rad_or_deg,linking_method,log_file,
    log_file_name,mps;
  int kdtree_depth,min_gal,max_gal,id_col,ra_col,dec_col,z_col,zerr_col,hid_col,hmass_col,hrich_col; 
  double mps_val,linking_length,linking_z,r_at_z,v_at_z,ref_z,frndrad,dist,cluz,H0,OmegaM,OmegaL,z_min,z_max,delta_z,MaxErr;
  void make_kdtree(std::string,std::string);
  void skip_comments(std::ifstream& fstr);
  void split(const std::string &str,std::vector<std::string> &tokens,const std::string &delimiter);
  void whileEOF(std::ifstream &inputfile,std::vector<std::string> &header,std::vector<std::string> &values,
		const std::string &comment_str);
  void read_param_file(const std::string &fname);
  void open_log_file();
  void read_data_file(const std::string &fname);
  void read_ascii(const std::string &fname);
  void read_fits(const std::string &fname);
  void selection_link();
  void create_protoclusters_kdtree();
  void create_protoclusters(int o);
  double check_node(int gali, int node_nb);
  void communicate();
  void communicate(int i,int j);
  void merge_protoclusters();
  void cluster_properties();
  void output_files();
  void mean_particle_separation();
};

void cluster_finder::skip_comments(std::ifstream& fstr){  //***Skip all lines begining with # symbol***//
  char a;
  fstr>>a;
  if(a=='#'){
    fstr.ignore(2147483647,'\n');
    skip_comments(fstr);
  } else fstr.unget();
}

void cluster_finder::split(const std::string &str,std::vector<std::string> &tokens,const std::string &delimiter){
  std::string::size_type lastPos,pos;      
  lastPos=str.find_first_not_of(delimiter,0); /* pos = find first "non-delimiter" */
  pos=str.find_first_of(delimiter,lastPos);
  while (std::string::npos!=pos || std::string::npos!=lastPos){
    tokens.push_back(str.substr(lastPos, pos-lastPos)); /* Found a token, add it to the vector. */     
    lastPos=str.find_first_not_of(delimiter, pos); /* Skip delimiters. Note the "not_of" */         
    pos=str.find_first_of(delimiter, lastPos); /* Find next "non-delimiter" */            
  }
}
  
void cluster_finder::whileEOF(std::ifstream &inputfile,std::vector<std::string> &header,std::vector<std::string> &values,
			const std::string &comment_str){
  std::string line;
  while(!inputfile.eof()){ /* While not the end of the file */
    std::getline(inputfile,line); /* Read each line */
    if(line.length() >= 1){ /* For lines with length > 1 (i.e., skip lines with no length = empty lines) */
      int hash=line.find(comment_str); /* Find lines that start with a # - indicating header information */
      if(hash!=std::string::npos) /* If you find a line starting with comment_str */
	header.push_back(line); /* Read the headers here and push to 'header' container */
      else
	values.push_back(line); /* Read the values here and push to 'values' container */
    }
  }
}

void cluster_finder::read_param_file(const std::string &fname){  //***Read in parameter file values***//
  std::ifstream file(fname.c_str());
  std::vector<std::string> header,lines,values;
  whileEOF(file,header,lines,"#");
  file.close();
  for(int i=0;i<lines.size();++i){
    values.clear();
    split(lines[i],values," "); 
    if(values[0]=="speed_of_light") cluz=atof(values[1].c_str());
    if(values[0]=="hubble_constant") H0=atof(values[1].c_str());
    if(values[0]=="matter_density") OmegaM=atof(values[1].c_str());
    if(values[0]=="dark_energy_density") OmegaL=atof(values[1].c_str());
    if(values[0]=="minimum_redshift") z_min=atof(values[1].c_str());
    if(values[0]=="maximum_redshift") z_max=atof(values[1].c_str());
    if(values[0]=="redshift_bin_size") delta_z=atof(values[1].c_str());
    if(values[0]=="maximum_photoz_error") MaxErr=atof(values[1].c_str());
    if(values[0]=="ref_z") ref_z=atof(values[1].c_str());
    if(values[0]=="rad_or_deg") rad_or_deg=values[1];
    if(values[0]=="minimum_richness") min_gal=atoi(values[1].c_str());
    if(values[0]=="maximum_richness") max_gal=atoi(values[1].c_str());
    if(values[0]=="kdtree_depth") kdtree_depth=atoi(values[1].c_str());
    if(values[0]=="calibrate_mode") calibrate=values[1];
    if(values[0]=="fof_mode") type=values[1];
    if(values[0]=="linking_method") linking_method=values[1];
    if(values[0]=="linking_length") linking_length=atof(values[1].c_str());
    if(values[0]=="linking_z") linking_z=atof(values[1].c_str());
    if(values[0]=="ouput_catalogues") out_cat=values[1];
    if(values[0]=="print_progress") progress=values[1];
    if(values[0]=="log_file") log_file=values[1];
    if(values[0]=="mean_particle_separation") mps=values[1];
    if(values[0]=="ouput_R_friend(z)") r_as_z=values[1];
    if(values[0]=="ouput_profiles") profiles=values[1];
    if(values[0]=="galaxy_catalogue") file_name=values[1];
    if(values[0]=="file_type") file_type=values[1];
    if(values[0]=="galaxy_id") id_col=atoi(values[1].c_str())-1;
    if(values[0]=="galaxy_ra") ra_col=atoi(values[1].c_str())-1;
    if(values[0]=="galaxy_dec") dec_col=atoi(values[1].c_str())-1;
    if(values[0]=="galaxy_z") z_col=atoi(values[1].c_str())-1;
    if(values[0]=="galaxy_z_err") zerr_col=atoi(values[1].c_str())-1;
    if(values[0]=="halo_id") hid_col=atoi(values[1].c_str())-1;
    if(values[0]=="halo_mass") hmass_col=atoi(values[1].c_str())-1;
    if(values[0]=="halo_rich") hrich_col=atoi(values[1].c_str())-1;
  }
}

void cluster_finder::open_log_file(){
  struct tm *current;
  time_t now;
  time(&now);
  current=localtime(&now);
  log_file_name="fof_log_file.txt";
  std::ofstream outfile;
  outfile.open(log_file_name.c_str());
  outfile<<"#----------------------------------------------------------------------------------------------#\n"<<std::flush;
  outfile<<"#---   FOF LOG FILE CREATED "<<std::setw(2)<<std::setfill('0')<<current->tm_mday<<"/"<<std::setw(2)
	 <<std::setfill('0')<<current->tm_mon+1<<"/"<<std::setw(2)<<std::setfill('0')<<current->tm_year+1900
	 <<" AT "<<std::setw(2)<<std::setfill('0')<<current->tm_hour<<":"<<std::setw(2)<<std::setfill('0')<<current->tm_min
	 <<":"<<std::setw(2)<<std::setfill('0')<<current->tm_sec<<"    -----------------------------------------#\n"<<std::flush;
  outfile<<"#----------------------------------------------------------------------------------------------#\n"<<std::flush;
  outfile<<" FoF Mode:"<<std::flush;
  if(!strcmp(type.c_str(),"phot")) outfile<<" [PHOTOMETRIC]"<<std::flush;
  else if(!strcmp(type.c_str(),"spec")) outfile<<" [SPECTROSCOPIC]"<<std::flush;
  outfile<<"\n"<<std::flush;
  if(!strcmp(calibrate.c_str(),"on")) outfile<<" [CALIBRATION]"<<std::flush;
  outfile<<" FoF Linking Parameters: "<<"[R("<<ref_z<<")="<<linking_length<<"] [z0="<<linking_z<<"] "<<std::flush;
  if(!strcmp(linking_method.c_str(),"dynamic")) outfile<<"[DYNAMIC]\n"<<std::flush;
  else if(!strcmp(linking_method.c_str(),"fixed")) outfile<<"[FIXED]\n"<<std::flush;
  outfile.close();
}

void cluster_finder::read_ascii(const std::string &fname){ //***Read ASCII File***//
  int n_rows=0,n_cols=0;
  std::ifstream save_file(fname.c_str()); 
  std::vector<std::string> header,lines,values;
  whileEOF(save_file,header,lines,"#");
  split(lines[0],values," "); 
  n_rows = lines.size();
  n_cols = values.size();
  if(n_cols<4){
    std::cerr<<"[FOF ERROR] PROBLEM READING FILE: "<<fname<<"\n"<<std::flush;
    if(!strcmp(log_file.c_str(),"yes")){
      std::ofstream outlogfile;
      outlogfile.open(log_file_name.c_str(),std::ios_base::app);
      outlogfile<<"[FOF ERROR] PROBLEM READING FILE: "<<fname<<"\n"<<std::flush;
      outlogfile<<"- FOF ABORTED...\n"<<std::flush;
      outlogfile.close();
    }
    exit(-1);
  }
  for(int i=0;i<n_cols;i++){
    test_vec.push_back(std::vector<std::string>());
    test_vec2.push_back(std::vector<std::string>());
  }
  for(int i=0;i<lines.size();i++){
    values.clear();
    split(lines[i],values," "); 
    for(int j=0;j<n_cols;j++) test_vec[j].push_back(values[j]);
  }
  save_file.close();
  std::cout<<" Reading ASCII file with "<<n_cols<<" columns and "<<n_rows<<" rows:\tDone\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Reading ASCII file with "<<n_cols<<" columns and "<<n_rows<<" rows:\tDone\n"<<std::flush;
    outlogfile.close();
  }
  if(!strcmp(type.c_str(),"phot")){
    for(int i=0;i<test_vec[0].size();i++){
      if(atof(test_vec[z_col][i].c_str())>=z_min && atof(test_vec[z_col][i].c_str())<=z_max &&
	 atof(test_vec[zerr_col][i].c_str())<=MaxErr){
	for(int j=0;j<test_vec.size();j++){
	  test_vec2[j].push_back(test_vec[j][i]);
	}
      }
    }
    std::cout<<"   - Using only the "<<test_vec2[0].size()<<" objects between z="<<z_min<<" and z="<<z_max<<" with z_err <= "<<
      MaxErr<<"\n"<<std::flush;
  }
  else if(!strcmp(type.c_str(),"spec")){
    for(int i=0;i<test_vec[0].size();i++){
      if(atof(test_vec[z_col][i].c_str())>=z_min && atof(test_vec[z_col][i].c_str())<=z_max){
	for(int j=0;j<test_vec.size();j++){
	  test_vec2[j].push_back(test_vec[j][i]);
	}
      }
    }
    std::cout<<"   - Using only the "<<test_vec2[0].size()<<" objects between z="<<z_min<<" and z="<<z_max<<"\n"<<std::flush;
  }
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<"   - Using only the "<<test_vec2[0].size()<<" objects between z="<<z_min<<" and z="<<z_max<<"\n"<<std::flush;
    outlogfile.close();
  }
  test_vec.clear();
}

void cluster_finder::read_fits(const std::string &fname){ //***Read FITS File***//
  fitsfile *fptr;
  int n_cols,status=0,hdunum,hdutype,anynul,typecode,x;
  long n_rows,repeat,width;
  char *val,nullstr[]="*";
  val = new char[1000];
  if(!fits_open_file(&fptr,fname.c_str(),READONLY,&status)){
    if(fits_get_hdu_num(fptr,&hdunum)==1) fits_movabs_hdu(fptr,2,&hdutype,&status);
    else fits_get_hdu_type(fptr,&hdutype,&status);
    if(hdutype==IMAGE_HDU) std::cout<<"Error: this program only displays tables, not images.\n"<<std::flush;
    else{
      fits_get_num_rows(fptr,&n_rows,&status);
      fits_get_num_cols(fptr,&n_cols,&status);
      for(int i=0;i<n_cols;i++) test_vec.push_back(std::vector<std::string>());
      for(int i=1;i<=n_rows && !status;i++){
	for(int j=1;j<=n_cols;j++){
	  fits_get_coltype(fptr,j,&typecode,&repeat,&width,&status);
	  for(int k=1;k<=repeat;k++){
	    x=j+k-2;
	    if(fits_read_col_str(fptr,j,i,k,1,nullstr,&val,&anynul,&status)) break;
	    test_vec[x].push_back(val);
	  }
	}
      }
    }
  }
  delete [] val;
  std::cout<<" Reading FITS file with "<<n_cols<<" columns and "<<n_rows<<" rows:\tDone\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Reading FITS file with "<<n_cols<<" columns and "<<n_rows<<" rows:\tDone\n"<<std::flush;
    outlogfile.close();
  }
}

void cluster_finder::read_data_file(const std::string &fname){  //***Read in data file and calculate R_friend(z)***//
  int i_temp;
  double r_temp;
  std::vector<int> slice;
  std::vector<double> dslice,dcmv;
  for(int i=0;i<Nslices;i++){
    slice.push_back(0);
    z_sliced.push_back(z_min+i*delta_z);
    dcmv.push_back(dcomvoldz(z_sliced[i],OmegaM,OmegaL));
  }
  std::string dummy; /*dummy string to push back all gal structure vectors*/
  if(!strcmp(file_type.c_str(),"ascii")) read_ascii(fname);
  else if(!strcmp(file_type.c_str(),"fits")) read_fits(fname);
  for(int i=0;i<test_vec2[0].size();i++){
    struct galaxy_clust dummy_gal(Nslices);
    dummy_gal.num=i;
    dummy_gal.id=test_vec2[id_col][i];
    if(!strcmp(rad_or_deg.c_str(),"deg")){
      dummy_gal.ra=atof(test_vec2[ra_col][i].c_str())*(M_PI/180);
      dummy_gal.dec=atof(test_vec2[dec_col][i].c_str())*(M_PI/180);
    }
    else if(!strcmp(rad_or_deg.c_str(),"rad")){
      dummy_gal.ra=atof(test_vec2[ra_col][i].c_str());
      dummy_gal.dec=atof(test_vec2[dec_col][i].c_str());
    }
    else {
      std::cout<<"RA and DEC units must be in radians or degrees.\n"<<std::flush;
      if(!strcmp(log_file.c_str(),"yes")){
	std::ofstream outlogfile;
	outlogfile.open(log_file_name.c_str(),std::ios_base::app);
	outlogfile<<"RA and DEC units must be in radians or degrees.\n"<<std::flush;
	outlogfile.close();
      }
      exit(-1);
    }
    dummy_gal.sindec=sin(dummy_gal.dec);
    dummy_gal.cosdec=cos(dummy_gal.dec);
    dummy_gal.z=atof(test_vec2[z_col][i].c_str());
    if(!strcmp(type.c_str(),"phot"))
      dummy_gal.z_err=atof(test_vec2[zerr_col][i].c_str());
    else if(!strcmp(type.c_str(),"spec"))
      dummy_gal.z_err=0;
    if(!strcmp(calibrate.c_str(),"on")){
      dummy_gal.mock_halo_id=test_vec2[hid_col][i];
      dummy_gal.mock_halo_mass=atof(test_vec2[hmass_col][i].c_str());
      dummy_gal.mock_halo_rich=atoi(test_vec2[hrich_col][i].c_str());
    }
    int o=int(floor(((dummy_gal.z-z_min)/delta_z)+0.5));
    slice[o]++;
    for(int m=0;m<Nslices;m++) dummy_gal.friends[m]=-1;
    gal.push_back(dummy_gal);
  }
  /*Find mean particle separation*/
  mean_particle_separation();
  /*Detemering Linking Length for Redshift Range*/
  if(!strcmp(linking_method.c_str(),"dynamic")){
    for(int i=0;i<Nslices;i++) dslice.push_back((double)slice[i]);
    for(int i=0;i<Nslices;i++) R_fr.set(z_sliced[i],dslice[i]);
    R_fr.arm_y();
    std::stringstream rf_filename;
    std::ofstream outrz;
    rf_filename<<file_name<<"_r_friends_data_"<<std::setw(2)<<std::setfill('0')<<linking_length<<"_"<<std::fixed<<std::setprecision(1)
	     <<linking_z<<"_"<<type<<".dat";
    if(!strcmp(r_as_z.c_str(),"yes")){
      outrz.open(rf_filename.str().c_str());
      outrz<<"#z_bin\tR("<<ref_z<<")\tR_friend\tz\tdN\tdV/dz\t\tdN/dV\n"<<std::flush;
    }
    i_temp=int(ceil((ref_z-z_min)/delta_z)); /*Reference redshift bin*/
    double konst;
    if(!strcmp(mps.c_str(),"yes"))
      konst = linking_length*mps_val;
    else
      konst = linking_length;
    r_temp=konst*pow((double)((R_fr.y(z_sliced[i_temp])/delta_z)*(1/dcmv[i_temp])),(double)0.5); /*R Constant*/
    for(int i=0;i<Nslices;i++){
      R_friend.push_back(r_temp*pow((double)((R_fr.y(z_sliced[i])/delta_z)*(1/dcmv[i])),(double)-0.5));
      v_0.push_back((linking_z)/(1+z_sliced[i]));
      if(R_fr.y(z_sliced[i])==0) R_friend[i]=FLT_MAX;
      if(!strcmp(r_as_z.c_str(),"yes")){ 
	outrz<<std::fixed<<std::setprecision(0)<<i<<"\t"<<std::fixed<<std::setprecision(4)<<linking_length<<"\t"
	     <<std::scientific<<std::setprecision(5)<<R_friend[i]
	     <<"\t"<<std::fixed<<std::setprecision(2)<<std::setw(4)<<std::setfill('0')<<std::left<<z_sliced[i]<<"\t"
	     <<std::setprecision(0)<<std::setw(6)<<std::setfill('0')<<std::right<<R_fr.y(z_sliced[i])<<"\t"
	     <<std::setprecision(9)<<std::setw(11)<<std::setfill('0')<<std::left<<dcmv[i]<<"\t"<<std::setprecision(2)
	     <<std::setw(11)<<std::setfill('0')<<std::right<<(double)((R_fr.y(z_sliced[i])/delta_z)*(1/dcmv[i]))
	     <<"\n"<<std::flush;
      }
      if(z_sliced[i]>ref_z-delta_z && z_sliced[i]<ref_z+delta_z){
	r_at_z=R_friend[i];
	v_at_z=v_0[i]*cluz;
      }
    }
    if(!strcmp(r_as_z.c_str(),"yes")) outrz.close();
    std::cout<<" Calculating linking length for redshift range:\t\tDone\n"<<std::flush;
    std::cout<<"   - R_friend at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t"<<std::fixed
	     <<std::setprecision(6)<<r_at_z<<" Mpc/h\n"<<std::flush; 
    if(!strcmp(type.c_str(),"spec")) 
      std::cout<<"   - v at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t\t"<<std::fixed<<std::setprecision(6)
	       <<v_at_z<<" km/s\n"<<std::flush;
    if(!strcmp(log_file.c_str(),"yes")){
      std::ofstream outlogfile;
      outlogfile.open(log_file_name.c_str(),std::ios_base::app);
      outlogfile<<" Calculating linking length for redshift range:\t\tDone\n"<<std::flush;
      outlogfile<<"   - R_friend at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t"<<std::fixed
		<<std::setprecision(6)<<r_at_z<<" Mpc/h\n"<<std::flush;
      if(!strcmp(type.c_str(),"spec")) 
	outlogfile<<"   - v at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t\t"<<std::fixed<<std::setprecision(6)
		  <<v_at_z<<" km/s\n"<<std::flush;
      outlogfile.close();
    }
  }
  else if(!strcmp(linking_method.c_str(),"fixed")){
    R_friend.push_back(linking_length*mps_val);
    v_0.push_back((linking_z)/(1+ref_z));
    r_at_z=R_friend[0];
    v_at_z=v_0[0]*cluz;
    std::cout<<"   - R_friend at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t"<<std::fixed
	     <<std::setprecision(6)<<r_at_z<<" Mpc/h\n"<<std::flush; 
    if(!strcmp(type.c_str(),"spec")) 
      std::cout<<"   - v at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t\t"<<std::fixed<<std::setprecision(6)
	       <<v_at_z<<" km/s\n"<<std::flush;
    if(!strcmp(log_file.c_str(),"yes")){
      std::ofstream outlogfile;
      outlogfile.open(log_file_name.c_str(),std::ios_base::app);
      outlogfile<<"   - R_friend at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t"<<std::fixed
		<<std::setprecision(6)<<r_at_z<<" Mpc/h\n"<<std::flush; 
      if(!strcmp(type.c_str(),"spec")) 
	outlogfile<<"   - v at z="<<std::fixed<<std::setprecision(3)<<ref_z<<":\t\t"<<std::fixed<<std::setprecision(6)
		  <<v_at_z<<" km/s\n"<<std::flush;
      outlogfile.close();
    }
  }
  slice.clear();
  dslice.clear();
  dcmv.clear();
  test_vec2.clear();
}

void cluster_finder::mean_particle_separation(){
  int count=0;
  double xxx;
  double sum_dist=0;
  for(int i=0;i<gal.size();i++){ 
    if(gal[i].z>ref_z-delta_z && gal[i].z<ref_z+delta_z){
       for(int j=i+1;j<gal.size();j++){ 
	 if(gal[j].z>ref_z-delta_z && gal[j].z<ref_z+delta_z){
	   count++;
	   sum_dist+=proj_dist(gal[j].ra,gal[i].ra,gal[j].sindec,gal[i].sindec,gal[j].cosdec,gal[i].cosdec);
	 }
       }
    }
  }
  mps_val=(sum_dist/(double)count)*angdidis(ref_z,OmegaM,OmegaL)*(cluz/H0) ;
  std::cout<<" Mean Particle Separation ("<<std::fixed<<std::setprecision(3)<<ref_z<<"): "<<mps_val<<" Mpc/h"<<std::flush;
  if(!strcmp(mps.c_str(),"yes"))
    std::cout<<"[MPS USED]"<<std::flush;
  std::cout<<"\n"<<std::flush;
}

void cluster_finder::make_kdtree(std::string mat, std::string tag_here){  //***Divide catalogue into branches***//
  tree_cluster.set_matrix(mat);
  tree_cluster.set_depth(5);
  tree_cluster.set_tag(tag_here);
  int NCol,NRow;
  NCol=3;
  NRow=gal.size();  
  tree_cluster.set_kdtree_train(2,NCol,NRow);
  double *vec_a,*vec_b;
  vec_a=new double[2];
  vec_b=new double[2];
  for(int i=0;i<NRow;i++){
    vec_a[0]=gal[i].ra;
    vec_a[1]=gal[i].dec;
    vec_b[0]=gal[i].z;
    tree_cluster.add_train_data(i,vec_a,vec_b);
  }
  tree_cluster.set_branch();
  tree_cluster.set_kdtree_test(NCol,NRow);
  tree_cluster.set_separate();
  for(int i=0;i<NRow;i++){
    vec_a[0]=gal[i].ra;
    vec_a[1]=gal[i].dec;
    vec_b[0]=gal[i].z;
    tree_cluster.add_data(i,vec_a,vec_b);
  }
  tree_cluster.do_separate();
  delete [] vec_a;
  delete [] vec_b;
  std::cout<<" Making kdtree:\t\t\t\t\t\tDone\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Making kdtree:\t\t\t\t\t\tDone\n"<<std::flush;
    outlogfile.close();
  }
}

double cluster_finder::check_node(int gali, int node_nb){  //***Find distance between a galaxy and neighbouring branches***//
  double diag,dist,dist3,cent0,cent1;
  TreeNode *pointer_to_node;
  int level_here=tree_cluster.MAX_DEPTH;
  pointer_to_node=tree_cluster.trunk->getLeefwithBN(level_here,node_nb);
  cent0=(pointer_to_node->max[0]+pointer_to_node->min[0])/2.0;
  cent1=(pointer_to_node->max[1]+pointer_to_node->min[1])/2.0;
  diag=acos(sin(cent1)*sin(pointer_to_node->min[1])+cos(cent1)*cos(pointer_to_node->min[1])*cos(cent0-pointer_to_node->min[0]));
  dist=acos(sin(cent1)*gal[gali].sindec+cos(cent1)*gal[gali].cosdec*cos(cent0-gal[gali].ra));
  dist3=dist-diag;
  return dist3;
}

void cluster_finder::create_protoclusters_kdtree(){  //***Loop over photometric redshift bins***//
  k=-1;
  int number_of_loops;
  if(!strcmp(type.c_str(),"spec")) number_of_loops=1;
  else if(!strcmp(type.c_str(),"phot")) number_of_loops=Nslices;
  for(int j=0;j<number_of_loops;j++) create_protoclusters(j);
}

void cluster_finder::create_protoclusters(int o){  //***Find protoclusters in spectroscopic mode***//
  time_t start_f,end_f;
  start_f=time(NULL);
  int oint,z_oint,count=0;
  double frndrad,dist,v1,v2,v3,v4,dist_z;
  for(int i=0;i<gal.size();i++){ /*Loop over all galaxies*/
    if(!strcmp(linking_method.c_str(),"dynamic")){
      if(!strcmp(type.c_str(),"spec")){
	oint=(int)((gal[i].z-z_min)/delta_z);
	z_oint=0;
	dist_z=gal[i].z;
      }
      if(!strcmp(type.c_str(),"phot")){
	oint=o;
	z_oint=o;
	dist_z=z_sliced[o];
      }
    }
    else if(!strcmp(linking_method.c_str(),"fixed")){
      if(!strcmp(type.c_str(),"spec")){
	oint=0;
	z_oint=0;
	dist_z=gal[i].z;
      }
      if(!strcmp(type.c_str(),"phot")){
	oint=0;
	z_oint=o;
	dist_z=z_sliced[o];
      }
    }
    if(gal[i].friends[z_oint]==-1){ /*Check that galaxy is not already in a proto-cluster*/
      if(!strcmp(type.c_str(),"spec") || !strcmp(type.c_str(),"phot") && fabs(gal[i].z-z_sliced[o])<=linking_z*gal[i].z_err){
	frndrad=R_friend[oint]/((cluz/H0)*angdidis(dist_z,OmegaM,OmegaL)); /*Calculate friend radius*/
	if(R_friend[oint]==FLT_MAX) frndrad=0.0;
	v1=(gal[i].z)/(1+gal[i].z); /*Calculate velocity of current galaxy*/
	for(int j_node=0;j_node<(int)pow(2.0,(tree_cluster.MAX_DEPTH));j_node++){ /*Loop over kd-tree nodes*/
	  if(check_node(i,j_node)<frndrad){ /*Check for nodes nearby current galaxy*/
	    for(int jj=0;jj<tree_cluster.nb_leaf[j_node];jj++){ /*Loop over nearby node members*/    
	      int j=tree_cluster.galaxy_sep[j_node][jj].id;
	      v2=(gal[j].z)/(1+gal[j].z); /*Calculate velocity of potential friend galaxy*/
	      if(gal[i].id!=gal[j].id && gal[j].friends[0]==-1){  
		if(!strcmp(type.c_str(),"spec") && fabs(v1-v2)<=v_0[oint] || !strcmp(type.c_str(),"phot") 
		   && fabs(gal[j].z-z_sliced[o])<=linking_z*gal[j].z_err){  
		  dist=proj_dist(gal[j].ra,gal[i].ra,gal[j].sindec,gal[i].sindec,gal[j].cosdec,gal[i].cosdec); /*Calculate distance between pair*/
		  if(dist<frndrad){ /*Check that distance is less than threshold*/
		    if(gal[i].friends[z_oint]==-1){ /*Create new proto-cluster*/
		      struct protocluster dummy_prtclt;
		      k++;
		      gal[i].friends[z_oint]=k;
		      gal[j].friends[z_oint]=k;
		      dummy_prtclt.id=k;
		      dummy_prtclt.zslice=oint;
		      dummy_prtclt.member_num.push_back(gal[i].num);
		      dummy_prtclt.member_num.push_back(gal[j].num);
		      dummy_prtclt.zmem.push_back(gal[i].z);
		      dummy_prtclt.ramem.push_back(gal[i].ra);
		      dummy_prtclt.decmem.push_back(gal[i].dec);
		      dummy_prtclt.zmem.push_back(gal[j].z);
		      dummy_prtclt.ramem.push_back(gal[j].ra);
		      dummy_prtclt.decmem.push_back(gal[j].dec);
		      prtclt.push_back(dummy_prtclt);
		    } 
		    else if(gal[i].friends[z_oint]>-1 && prtclt[k].member_num.size()<max_gal){ /*Add galaxy to existing proto-cluster*/
		      gal[j].friends[z_oint]=k;
		      prtclt[k].member_num.push_back(gal[j].num);
		      prtclt[k].zmem.push_back(gal[j].z);
		      prtclt[k].ramem.push_back(gal[j].ra);
		      prtclt[k].decmem.push_back(gal[j].dec);
		    } 
		    //else over_merge_error1(max_gal);
		  } 
		}
	      }
	    } /*End of the loop over node members*/
	  }
	} /*End of loop over kd-tree nodes*/
	if(gal[i].friends[z_oint]>-1){ /*Check if galaxy is now in a proto-cluster*/
	  for(int ii=0;ii<prtclt[k].member_num.size();ii++){ /*Loop over proto-cluster members*/
	    v3=(gal[prtclt[k].member_num[ii]].z)/(1+gal[prtclt[k].member_num[ii]].z); /*Calculate veloctity of proto-cluster member*/
	    for(int j_node=0;j_node<(int)pow(2.0,(tree_cluster.MAX_DEPTH));j_node++){ /*Loop over kd-tree nodes*/
	      if(check_node(prtclt[k].member_num[ii],j_node)<frndrad){
		for(int jjj=0;jjj<tree_cluster.nb_leaf[j_node];jjj++){ /*Loop over node members*/
		  int jj=tree_cluster.galaxy_sep[j_node][jjj].id;
		  v4=(gal[jj].z)/(1+gal[jj].z); /*Calculate velocity of potential friend-of-friend galaxy*/
		  if(gal[prtclt[k].member_num[ii]].id!=gal[jj].id && gal[jj].friends[z_oint]==-1){  
		    if(!strcmp(type.c_str(),"spec") && fabs(v3-v4)<=v_0[oint] || !strcmp(type.c_str(),"phot") 
		       && fabs(gal[jj].z-z_sliced[o])<=linking_z*gal[jj].z_err){
		      dist=proj_dist(gal[jj].ra,gal[prtclt[k].member_num[ii]].ra,gal[jj].sindec,gal[prtclt[k].member_num[ii]].sindec,
				     gal[jj].cosdec,gal[prtclt[k].member_num[ii]].cosdec); /*Calculate distance between pair*/
		      if(dist<frndrad){ /*Check that distance is less than threshold*/
			if(prtclt[k].member_num.size()<max_gal){ /*Add galaxy to existing proto-cluster*/
			  gal[jj].friends[z_oint]=k;
			  prtclt[k].member_num.push_back(gal[jj].num);
			  prtclt[k].zmem.push_back(gal[jj].z);
			  prtclt[k].ramem.push_back(gal[jj].ra);
			  prtclt[k].decmem.push_back(gal[jj].dec);
			}
			//else over_merge_error2(max_gal);
		      }  
		    }
		  } 
		} /*End of loop over node members*/
	      }
	    } /*End of loop over kd-tree nodes*/
	  } /*End of loop over proto-cluster members*/
	}
	if(gal[i].friends[z_oint]>-1 && prtclt[k].member_num.size()<min_gal){ /*Destroy proto-cluster if it doesn't have enough members*/
	  for(int jj=0;jj<prtclt[k].member_num.size();jj++) gal[prtclt[k].member_num[jj]].friends[z_oint] = -2; 
	  prtclt.pop_back();
	  k--;
	}
      }
    } /*End of field flag skip*/
    if(!strcmp(progress.c_str(),"yes") && !strcmp(type.c_str(),"spec")) std::cout<<"!Creating Protoclusters: "<<std::fixed<<std::setprecision(3)
										 <<((double)(i+1)/gal.size())*100.0<<" %\r"<<std::flush;
  }/*End of the loop over all  i galaxies*/
  end_f=time(NULL);
  int ngalprtclt=0;
  for(int i=0;i<prtclt.size();i++) ngalprtclt+=prtclt[i].member_num.size();
  if(!strcmp(type.c_str(),"phot")){ 
    std::cout<<" Creating Protoclusters:\t z = "<<std::fixed<<std::setprecision(2)<<std::setw(4)<<std::left<<std::setfill('0')
	     <<z_sliced[o]<<std::resetiosflags(std::ios::fixed)<<"\tNprtclt = "<<std::setw(6)<<std::right
	     <<std::setfill('0')<<prtclt.size()<<"  Ngalprtclt = "<<std::setw(7)<<std::right<<std::setfill('0')
	     <<ngalprtclt<<"\tTime: "<<(end_f-start_f)<<" s\n"<<std::flush;
  }
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Creating Protoclusters:\t\t\t\tDone\n"<<std::flush;
    outlogfile.close();
  }
}

void cluster_finder::merge_protoclusters(){    //***Merge protoclusters with shared galaxies into clusters***//
  if(!strcmp(progress.c_str(),"yes") && !strcmp(type.c_str(),"spec")) std::cout<<"\n"<<std::flush;
  std::cout<<" Merging in Progress...\n"<<std::flush;
  int m=0;
  for(int n=0;n<prtclt.size();n++){
    if(prtclt[n].member_num.size()>0){ /*Initiate a Cluster*/
      struct cluster clt_here;
      add_protocluster_to_cluster(&prtclt[n],&clt_here);
      for(int i=0;i<clt_here.member_num.size();i++){ /*Look for Clusters with Galaxies in common*/
        for(int nn=n+1;nn<prtclt.size();nn++){  
          for(int j=0;j<prtclt[nn].member_num.size();j++){
            if(prtclt[nn].member_num.size()>0 && prtclt[nn].member_num[j]==clt_here.member_num[i]){
              add_protocluster_to_cluster(&prtclt[nn],&clt_here);
	      clean_repetitions(&clt_here);
            }
          }
        }
      }
      clt_here.id = m;
      m++; 
      clt.push_back(clt_here);
    } /* Finish cluster m */
  } /*Finish loop over all protoclusters */
  int ngalcl=0;
  for(int i=0;i<clt.size();i++) ngalcl+=clt[i].member_num.size();
  std::cout<<" Merging protoclusters into clusters:\t\t\tDone\n"<<std::flush;
  std::cout<<"\t\t- Number of Clusters:\t\t\t"<<clt.size()<<"\n"<<std::flush;
  std::cout<<"\t\t- Number of Galaxies in Clusters:\t"<<ngalcl<<"\n"<<std::flush;
  std::cout<<"\t\t- Number of Protoclusters:\t\t"<<prtclt.size()<<"\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Merging protoclusters into clusters:\t\t\tDone\n"<<std::flush;
    outlogfile<<"\t\t- Number of Clusters:\t\t\t"<<clt.size()<<"\n"<<std::flush;
    outlogfile<<"\t\t- Number of Galaxies in Clusters:\t"<<ngalcl<<"\n"<<std::flush;
    outlogfile<<"\t\t- Number of Protoclusters:\t\t"<<prtclt.size()<<"\n"<<std::flush;
    outlogfile.close();
  }
}

void cluster_finder::cluster_properties(){    //***Calculate basic physical properties of each cluster***//
  std::ofstream rad_pro;
  if(!strcmp(profiles.c_str(),"yes")) rad_pro.open("Radial_Profiles.dat");
  for(int mm=0;mm<clt.size();mm++){
    double sumcltz=0,sumcltra=0,sumcltdec=0,sumcltsig=0,cltgaldist=0,cltrad=0,sumcltrad=0;
    double g_sig=0.9,h_ratio,delta_vir,x_vir;
    for(int i=0;i<clt[mm].member_num.size();i++){
      if(clt[mm].ramem[i]*(180./M_PI)>350.0) 
	clt[mm].ramem[i]=(clt[mm].ramem[i]*(180./M_PI)-360)*(M_PI/180.); /*Fix for RA wrapping*/
      sumcltz+=clt[mm].zmem[i];
      sumcltra+=clt[mm].ramem[i]*(180./M_PI);
      sumcltdec+=clt[mm].decmem[i]*(180./M_PI);
      if(clt[mm].ramem[i]*(180./M_PI)<0.0) 
	clt[mm].ramem[i]=(clt[mm].ramem[i]*(180./M_PI)+360)*(M_PI/180.); /*Fix for negative RA*/
    }
    clt[mm].z=(sumcltz)/(clt[mm].member_num.size());
    clt[mm].ra=(sumcltra)/(clt[mm].member_num.size());
    clt[mm].dec=(sumcltdec)/(clt[mm].member_num.size());
    if(clt[mm].ra<0) clt[mm].ra=clt[mm].ra+360; /*Fix for negative average RA*/
    for(int i=0;i<clt[mm].member_num.size();i++){
      sumcltsig+=pow((clt[mm].zmem[i]-clt[mm].z),2);
      cltgaldist=acos(sin(clt[mm].dec*(M_PI/180))*sin(clt[mm].decmem[i])+cos(clt[mm].dec*(M_PI/180))*cos(clt[mm].decmem[i])*
		      cos(clt[mm].ra*(M_PI/180)-clt[mm].ramem[i]));
      if(!strcmp(profiles.c_str(),"yes")) rad_pro<<cltgaldist*angdidis(clt[mm].z,OmegaM,OmegaL)*(cluz/H0)<<"\n"<<std::flush;
      //if(cltgaldist>cltrad) cltrad=cltgaldist;
      sumcltrad+=cltgaldist;
    }
    cltrad=(sumcltrad)/(clt[mm].member_num.size());
    clt[mm].std=pow((double)((sumcltsig)/(clt[mm].member_num.size())),(double)0.5)*(cluz);
    clt[mm].size=(double)(cltrad)*(180/M_PI)*3600;//*angdidis(clt[mm].z,OmegaM,OmegaL)*(cluz/H0);
    h_ratio=pow((OmegaM*pow((1.0+clt[mm].z),3)+OmegaL),-0.5);
    x_vir=((OmegaM*pow((1.0+clt[mm].z),3))*pow(h_ratio,2))-1;
    delta_vir=18*pow(M_PI,2)+82*x_vir-39*pow(x_vir,2);
    clt[mm].mass=log10((pow(clt[mm].std,3)*h_ratio*1e13)/((H0/100)*pow((102.5*g_sig),3)*pow(delta_vir,0.5)));
  }
  if(!strcmp(profiles.c_str(),"yes")) rad_pro.close();
  std::cout<<" Determining cluster properties:\t\t\tDone\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Determining cluster properties:\t\t\tDone\n"<<std::flush;
    outlogfile.close();
  }
}

void cluster_finder::output_files(){    //***Output properties of clusters and cluster members***//
  double *list_clusters_id, *list_clusters_rich;
  list_clusters_id = new double [clt.size()+1];
  list_clusters_rich = new double [clt.size()+1];
  for(int i=0;i<clt.size();i++){ 
    list_clusters_id[i+1] = (double)clt[i].id;
    list_clusters_rich[i+1] = (double)clt[i].member_num.size();
  }
  spline::quick_sort(list_clusters_rich,list_clusters_id,clt.size());
  std::stringstream filename0,filename1;
  if(!strcmp(type.c_str(),"phot")){
    filename0<<file_name<<"_clusters_"<<std::setw(2)<<std::setfill('0')<<linking_length<<"_"<<std::fixed<<std::setprecision(1)
	     <<linking_z<<"_"<<type<<".dat";
    filename1<<file_name<<"_galaxies_"<<std::setw(2)<<std::setfill('0')<<linking_length<<"_"<<std::fixed<<std::setprecision(1)
	     <<linking_z<<"_"<<type<<".dat";
  }
  else if(!strcmp(type.c_str(),"spec")){
    filename0<<file_name<<"_clusters_"<<std::setw(2)<<std::setfill('0')<<linking_length<<"_"<<std::fixed<<std::setprecision(4)
	     <<linking_z<<"_"<<type<<".dat";
    filename1<<file_name<<"_galaxies_"<<std::setw(2)<<std::setfill('0')<<linking_length<<"_"<<std::fixed<<std::setprecision(4)
	     <<linking_z<<"_"<<type<<".dat";
  }
  std::ofstream outfile0 (filename0.str().c_str());
  std::ofstream outfile1 (filename1.str().c_str());
  outfile0<<"#C_ID\t\tRich\tRA\t\tDec\t\tz\t\tSigma (km/s)\t\tSize (arcsec)\tlog Mass (M_solar)\n"<<std::flush;
  if(!strcmp(calibrate.c_str(),"on")) 
    outfile1<<"#C_ID\t\tC_Rich\tC_Mass\tG_ID\t\tG_RA\t\tG_DEC\t\tG_z\tH_ID\tH_Mass\tH_Rich\n"<<std::flush;
  else outfile1<<"#C_ID\t\tC_Rich\tC_Mass\tG_ID\t\tG_RA\t\tG_DEC\t\tG_z\n"<<std::flush;
  for(int n=1;n<=clt.size();n++){
    int ln=(int)list_clusters_id[clt.size()-(n-1)];
    outfile0<<std::setw(12)<<std::setfill('0')<<clt[ln].id<<"\t"<<std::setw(3)<<std::setfill('0')<<clt[ln].member_num.size()
	    <<"\t"<<std::fixed<<std::setprecision(5)<<std::setw(9)<<std::setfill('0')<<clt[ln].ra<<"\t"<<std::setw(8)
	    <<std::setfill('0')<<std::showpos<<clt[ln].dec<<"\t"<<std::setw(7)<<std::setfill('0')<<std::noshowpos<<clt[ln].z
	    <<"\t\t"<<std::setprecision(2)<<std::setw(8)<<std::setfill('0')<<clt[ln].std<<"\t\t"<<std::setw(6)
	    <<std::setfill('0')<<clt[ln].size<<"\t\t"<<std::setprecision(4)<<std::setw(7)<<std::setfill('0')<<clt[ln].mass
	    <<"\n"<<std::flush;
    if(!strcmp(calibrate.c_str(),"on")) for(int i=0;i<clt[ln].member_num.size();i++){    
	outfile1<<std::setw(12)<<std::setfill('0')<<clt[ln].id<<"\t"<<std::setw(3)<<std::setfill('0')<<clt[ln].member_num.size()
		<<"\t"<<std::fixed<<std::setprecision(3)<<clt[ln].mass<<"\t"<<std::setw(12)<<std::setfill('0')
		<<gal[clt[ln].member_num[i]].id<<"\t"<<std::fixed<<std::setprecision(6)<<std::setw(10)<<std::setfill('0')<<std::right
		<<clt[ln].ramem[i]*(180/M_PI)<<"\t"<<std::setw(9)<<std::setfill('0')<<std::right<<std::showpos
		<<clt[ln].decmem[i]*(180/M_PI)<<"\t"<<std::fixed<<std::setprecision(5)<<std::setw(6)<<std::setfill('0')<<std::right
		<<std::noshowpos<<clt[ln].zmem[i]<<"\t"<<gal[clt[ln].member_num[i]].mock_halo_id<<"\t"
		<<gal[clt[ln].member_num[i]].mock_halo_mass<<"\t"<<gal[clt[ln].member_num[i]].mock_halo_rich<<"\n"<<std::flush;
      }
    else for(int i=0;i<clt[ln].member_num.size();i++){    
	outfile1<<std::setw(12)<<std::setfill('0')<<clt[ln].id<<"\t"<<std::setw(3)<<std::setfill('0')<<clt[ln].member_num.size()
		<<std::fixed<<std::setprecision(3)<<"\t"<<clt[ln].mass<<"\t"<<std::setw(12)<<std::setfill('0')
		<<gal[clt[ln].member_num[i]].id<<"\t"<<std::fixed<<std::setprecision(6)<<std::setw(10)<<std::setfill('0')
		<<std::right<<clt[ln].ramem[i]*(180/M_PI)<<"\t"<<std::setw(9)<<std::setfill('0')<<std::right<<std::showpos
		<<clt[ln].decmem[i]*(180/M_PI)<<"\t"<<std::fixed<<std::setprecision(5)<<std::setw(6)<<std::setfill('0')
		<<std::right<<std::noshowpos<<clt[ln].zmem[i]<<"\n"<<std::flush;
      }
  }
  outfile0.close();
  outfile1.close();
  delete [] list_clusters_rich;
  delete [] list_clusters_id;
  std::cout<<" Outputting files:\t\t\t\t\tDone\n"<<std::flush;
  if(!strcmp(log_file.c_str(),"yes")){
    std::ofstream outlogfile;
    outlogfile.open(log_file_name.c_str(),std::ios_base::app);
    outlogfile<<" Outputting files:\t\t\t\t\tDone\n"<<std::flush;
    outlogfile.close();
  }
}

/*Call to functions*/
float splint(float *,float *,float *,int,float);
void spline(float *,float *,int,float,float,float *);
double dcomvoldz(double,double,double);
double angdidis(double,double,double);
void help();
void param_error();
void cat_error();
void slice_error();
void type_error(std::string);
void out_error(std::string);
void prog_error(std::string);
double proj_dist(double,double,double,double,double,double);
void add_protocluster_to_cluster (struct protocluster *, struct cluster *);
void clean_repetitions (struct cluster *);
void d_h_m_s (double);
void help();
void param_error();
void cat_error();
void slice_error();
void over_merge_error(int);
void type_error(std::string);
void out_error(std::string);
void prog_error(std::string);

/*Beginning of Main*/
int main (int argc, char *argv[]){
  /***************/
  /***BEGIN FOF***/
  /***************/
  time_t start,end;
  start=time(NULL);
  class cluster_finder data_phot;
  /*Assign input parameters*/
  data_phot.param_file="./fof_param.ini";
  /*Check for alternate input parameters*/
  for(int i=1;i<argc;i++){
    if(argv[i][0]=='-' && std::strlen(argv[i])>1){
      switch(argv[i][1]){
      case 'h' : 
      case 'H' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-help")) help();
	break;
      case 'p' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-param")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') data_phot.param_file=argv[i+1];
	}
	break;
      }
    }
  }
  /*Check parameters file*/
  std::ifstream test_file(data_phot.param_file.c_str());
  if(test_file.good()) data_phot.read_param_file(data_phot.param_file);
  else{ 
    param_error(); /*Return FOF ERROR for bad param file*/
    exit(-1);
  }
  test_file.close();
  /*Open parameters file*/
  if(!strcmp(data_phot.log_file.c_str(),"yes"))
    data_phot.open_log_file();
  /*Check for options*/  
  for(int i=1;i<argc;i++){
    if(argv[i][0]=='-' && std::strlen(argv[i])>1){
      switch(argv[i][1]){
      case 'i' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-input")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') data_phot.file_name=argv[i+1];
	}
	break;
      case 'r' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-rlink")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') data_phot.linking_length=atof(argv[i+1]);
	}
	break;
      case 'z' :
	if(std::strlen(argv[i])==2 || (std::strlen(argv[i])>2 && std::string(argv[i])=="-zlink")){
	  if(i!=(argc-1) && argv[i+1][0]!='-') data_phot.linking_z=atof(argv[i+1]);
	}
	break;
      }
    }
  }
  /*Start FoF*/  
  std::cout<<"[:::::::::::::::::::::::FRIENDS-OF-FRIENDS INITIATED:::::::::::::::::::::::]\n"<<std::flush;
  std::cout<<" FoF Mode:"<<std::flush;
  if(strcmp(data_phot.type.c_str(),"spec") && strcmp(data_phot.type.c_str(),"phot")){ 
    type_error(data_phot.type); /*Return FOF ERROR for incorrect type option*/
    exit(-1);
  }
  else if(!strcmp(data_phot.type.c_str(),"phot")) 
    std::cout<<" [PHOTOMETRIC]"<<std::flush;
  else if(!strcmp(data_phot.type.c_str(),"spec")) 
    std::cout<<" [SPECTROSCOPIC]"<<std::flush;
  if(!strcmp(data_phot.calibrate.c_str(),"on"))
    std::cout<<" [CALIBRATION]"<<std::flush;
  std::cout<<"\n"<<std::flush;
  if(strcmp(data_phot.out_cat.c_str(),"yes") && strcmp(data_phot.out_cat.c_str(),"no")){
    out_error(data_phot.out_cat); /*Return FOF ERROR for incorrect output option*/
    exit(-1);
  }
  if(strcmp(data_phot.progress.c_str(),"yes") && strcmp(data_phot.progress.c_str(),"no")){
    prog_error(data_phot.progress); /*Return FOF ERROR for incorrect progress option*/
    exit(-1);
  }
  std::cout<<" FoF Linking Parameters: "<<"[R("<<data_phot.ref_z<<")="<<data_phot.linking_length<<"] [z0="
	   <<data_phot.linking_z<<"] "<<std::flush;
  if(!strcmp(data_phot.linking_method.c_str(),"dynamic")) std::cout<<"[DYNAMIC]\n"<<std::flush;
  else if(!strcmp(data_phot.linking_method.c_str(),"fixed")) std::cout<<"[FIXED]\n"<<std::flush;
  /*Set up FOF*/
  data_phot.Nslices=((int)(((data_phot.z_max-data_phot.z_min)/data_phot.delta_z)+1));
  if(data_phot.Nslices<2){ 
    slice_error();
    exit(-1);
  }
  std::ifstream test_file2(data_phot.file_name.c_str());
  if(test_file2.good()) data_phot.read_data_file(data_phot.file_name);
  else{ 
    cat_error(); /*Return FOF ERROR for bad input catalogue*/
    exit(-1);
  }
  test_file2.close();
  data_phot.make_kdtree("x","tag_cluster");
  data_phot.create_protoclusters_kdtree();
  data_phot.merge_protoclusters();
  data_phot.cluster_properties();  
  if(!strcmp(data_phot.out_cat.c_str(),"yes") && data_phot.clt.size()>0) data_phot.output_files();
  else if(data_phot.clt.size()<=0) std::cout<<" [***NO CLUSTERS FOUND!***]\n"<<std::flush;
  end=time(NULL);
  d_h_m_s(double(end-start));
  std::cout<<"[:::::::::::::::::::::::FRIENDS-OF-FRIENDS COMPLETE:::::::::::::::::::::::]\n"<<std::flush;    
  return 0;
  /***************/
  /***END FOF***/
  /***************/
} 
/*End of Main*/

void add_protocluster_to_cluster(struct protocluster *prtclt, struct cluster *clt){
  for(int i=0;i<prtclt->member_num.size();i++) clt->member_num.push_back(prtclt->member_num[i]);
  for(int i=0;i<prtclt->member_num.size();i++) clt->zmem.push_back(prtclt->zmem[i]);  
  for(int i=0;i<prtclt->member_num.size();i++) clt->ramem.push_back(prtclt->ramem[i]);  
  for(int i=0;i<prtclt->member_num.size();i++) clt->decmem.push_back(prtclt->decmem[i]);  
  prtclt->member_num.clear();
}

void clean_repetitions(struct cluster *clt,int j){
  clt->member_num.erase(clt->member_num.begin()+j);
  clt->zmem.erase(clt->zmem.begin()+j);
  clt->ramem.erase(clt->ramem.begin()+j);
  clt->decmem.erase(clt->decmem.begin()+j);
  clean_repetitions(clt);
  return;  
}

void clean_repetitions(struct cluster *clt){  
  for(int i=0;i<clt->member_num.size()-1;i++)
    for(int j=i+1;j<clt->member_num.size();j++)   
      if(clt->member_num[i]==clt->member_num[j])
	clean_repetitions(clt,j);
  return;
}
