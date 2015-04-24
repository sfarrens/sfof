/*Class for file input and output*/

#include "fileio_class.hpp"
#include "exceptions.hpp"

void Fileio::set_up (int id_col_val, int ra_col_val, int dec_col_val, 
		     int z_col_val) {
  if (id_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "id_col_val", "> 0");
  if (ra_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "ra_col_val", "> 0");
  if (dec_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "dec_col_val", "> 0");
  if (z_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "z_col_val", "> 0");
  id_col = id_col_val - 1;
  ra_col = ra_col_val - 1;
  dec_col = dec_col_val - 1;
  z_col = z_col_val - 1;
}

void Fileio::set_up (int id_col_val, int ra_col_val, int dec_col_val, 
		     int z_col_val, int dz_col_val) {
  if (id_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "id_col_val", "> 0");
  if (ra_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "ra_col_val", "> 0");
  if (dec_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "dec_col_val", "> 0");
  if (z_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "z_col_val", "> 0");
  if (dz_col_val <= 0)
    throw BadArgumentException("Fileio::set_up", "dz_col_val", "> 0");
  id_col = id_col_val - 1;
  ra_col = ra_col_val - 1;
  dec_col = dec_col_val - 1;
  z_col = z_col_val - 1;
  dz_col = dz_col_val - 1;
}

void Fileio::split (const std::string &str, std::vector<std::string> &tokens, 
		    const std::string &delimiter) {
  // Function to split a string read in from a file into columns.
  if (str.empty())
    throw BadArgumentException("Fileio::split", "str", "a valid string");
  if (delimiter.empty())
    throw BadArgumentException("Fileio::split", "delimiter", "a valid string");
  std::string::size_type lastPos, pos;      
  lastPos = str.find_first_not_of(delimiter, 0); /* pos = find first "non-delimiter" */
  pos = str.find_first_of(delimiter, lastPos);
  while (std::string::npos != pos || std::string::npos != lastPos){
    tokens.push_back(str.substr(lastPos, pos-lastPos)); /* Found a token, add it to the vector. */     
    lastPos = str.find_first_not_of(delimiter, pos); /* Skip delimiters. Note the "not_of" */         
    pos=str.find_first_of(delimiter, lastPos); /* Find next "non-delimiter" */            
  }
}

void Fileio::read_ascii (const std::string &fname, const std::string &mode, double z_min, 
			 double z_max, double dz_max, std::vector<Galaxy> &gals) { 
  // Function to read in an ASCII file and store the contents in a vector of Galaxy instances.
  if (mode != "spec" && mode != "phot")
    throw BadArgumentException("Fileio::read_ascii", "mode", "a valid option [spec/phot]");
  if (z_min < 0)
    throw BadArgumentException("Fileio::read_ascii", "z_min", ">= 0.0");
  if (z_max <= 0)
    throw BadArgumentException("Fileio::read_ascii", "z_max", "> 0.0");
  if (dz_max <= 0)
    throw BadArgumentException("Fileio::read_ascii", "dz_max", "> 0.0");
  std::ifstream read_file(fname.c_str()); /* open file */
  if (!read_file.good())
    throw BadArgumentException("Fileio::read_ascii", "fname", "a valid file name");
  int count = 0;
  unsigned long id;
  double ra, dec, z, dz;
  std::string line;
  std::vector<std::string> cols; 
  while (std::getline(read_file, line)) { /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      split(line, cols, " "); /* split line into columns */
      id = strtoul(cols[id_col].c_str(), NULL, 0);
      ra = atof(cols[ra_col].c_str());
      dec = atof(cols[dec_col].c_str());
      z = atof(cols[z_col].c_str());
      if (z >= z_min && z <= z_max) { /* check if galaxy is within redshift limits*/
	if(mode == "spec") {
	  Galaxy spec_gal(count, id, ra, dec, z); /* intialise spec Galaxy */
	  gals.push_back(spec_gal); /* store spec Galaxy instance in vector */
	  count++;
	}
	else {
	  dz = atof(cols[dz_col].c_str());	  
	  if (dz <= dz_max) { /* check if photo-z error is below accepted threshold */
	    Galaxy phot_gal(count, id, ra, dec, z, dz); /* intialise phot Galaxy */
	    gals.push_back(phot_gal); /* store phot Galaxy instance in vector */
	    count++;
	  }	  
	}
      }
      cols.clear(); /* clear column vector */
    }
  }
  read_file.close(); /* close file */
  std::cout<<"Reading ASCII file with "<<gals.size()<<" galaxies."<<std::endl;
  std::cout<<" * only accepting galaxies with:"<<std::endl;
  std::cout<<"   - ("<<z_min<<" <= z <= "<<z_max<<")"<<std::endl;
  if(mode == "phot") std::cout<<"   - (dz <= "<<dz_max<<")"<<std::endl;
}

void Fileio::read_fits (const std::string &fname, const std::string &mode, double z_min,
			double z_max, double dz_max, std::vector<Galaxy> &gals) { 
  // Function to read in an FITS file and store the contents in a vector of Galaxy instances.
  if (mode != "spec" && mode != "phot")
    throw BadArgumentException("Fileio::read_fits", "mode", "a valid option [spec/phot]");
  if (z_min < 0)
    throw BadArgumentException("Fileio::read_fits", "z_min", ">= 0.0");
  if (z_max <= 0)
    throw BadArgumentException("Fileio::read_fits", "z_max", "> 0.0");
  if (dz_max <= 0)
    throw BadArgumentException("Fileio::read_fits", "dz_max", "> 0.0");
  std::ifstream read_file(fname.c_str()); /* open file */
  if (!read_file.good())
    throw BadArgumentException("Fileio::read_fits", "fname", "a valid file name");
  read_file.close();
  unsigned long id;
  double ra, dec, z, dz;
  fitsfile *fptr;
  int count = 0, n_cols, status = 0, hdunum, hdutype, anynul, typecode;
  long n_rows, repeat, width;
  char *val, nullstr[] = "*";
  std::vector<std::string> cols; /* column vector */
  val = new char[1000];
  if(!fits_open_file(&fptr, fname.c_str(), READONLY, &status)){ /* open FITS file */
    if(fits_get_hdu_num(fptr, &hdunum) == 1) fits_movabs_hdu(fptr, 2, &hdutype, &status);
    else fits_get_hdu_type(fptr, &hdutype, &status);
    if(hdutype == IMAGE_HDU) /* check if the FITS file contains an image */
      throw DomainException("Fileio::read_fits", "This code only read FITS tables, not images.");
    else{
      fits_get_num_rows(fptr, &n_rows, &status); /* get number of rows in FITS table */
      fits_get_num_cols(fptr, &n_cols, &status); /* get number of columns in FITS table */
      for(int i = 1; i <= n_rows && !status; i++){
	for(int j = 1; j <= n_cols; j++){
	  fits_get_coltype(fptr, j, &typecode, &repeat, &width, &status);
	  for(int k = 1; k <= repeat; k++){
	    if(fits_read_col_str(fptr, j, i, k, 1, nullstr, &val, &anynul, &status)) break;
	    cols.push_back(val);
	  }
	}
	id = strtoul(cols[id_col].c_str(), NULL, 0);
	ra = atof(cols[ra_col].c_str());
	dec = atof(cols[dec_col].c_str());
	z = atof(cols[z_col].c_str());
	if (z >= z_min && z <= z_max) { /* check if galaxy is within redshift limits*/
	  if(mode == "spec") {
	    Galaxy spec_gal(count, id, ra, dec, z); /* intialise spec Galaxy */
	    gals.push_back(spec_gal); /* store spec Galaxy instance in vector */
	    count++;
	  }
	  else {
	    dz = atof(cols[dz_col].c_str());
	    if (dz <= z_max) { /* check if photo-z error is below accepted threshold */
	      Galaxy phot_gal(count, id, ra, dec, z, dz); /* intialise phot Galaxy */
	      gals.push_back(phot_gal); /* store phot Galaxy instance in vector */
	      count++;
	    }
	  }
	}
	cols.clear(); /* clear column vector */
      }      
    }
    fits_close_file(fptr, &status); /* close FITS file */
  }
  if(status) fits_report_error(stderr, status); /*print any error message*/
  std::cout<<"Reading FITS file with "<<gals.size()<<" objects."<<std::endl;
  std::cout<<" * only accepting galaxies with:"<<std::endl;
  std::cout<<"   - ("<<z_min<<" <= z <= "<<z_max<<")"<<std::endl;
  if(mode == "phot") std::cout<<"   - (dz <= "<<dz_max<<")"<<std::endl;
}

void Fileio::output_cluster_name (const std::string &fname, const std::string &mode, 
				  const std::string &output, double link_r, double link_z,
				  std::string &cluster_file_name) {
  // Function to set up cluster output file name.
  if (fname.empty())
    throw BadArgumentException("Fileio::output_cluster_name", "fname", "a valid string");
  if (mode != "spec" && mode != "phot")
    throw BadArgumentException("Fileio::output_cluster_name", "mode", "a valid option [spec/phot]");
  if (output != "ascii" && output != "fits")
    throw BadArgumentException("Fileio::output_cluster_name", "output", "a valid option [ascii/fits]");
  std::stringstream cluster_file_stream, member_file_stream;
  if(output == "ascii") 
    cluster_file_stream<<fname<<"_clusters_"<<link_r<<"_"<<link_z<<"_"<<mode<<".dat";
  else if(output == "fits") 
    cluster_file_stream<<fname<<"_clusters_"<<link_r<<"_"<<link_z<<"_"<<mode<<".fits";
  cluster_file_name = cluster_file_stream.str();
}

void Fileio::output_member_name (const std::string &fname, const std::string &mode, 
				 const std::string &output, double link_r, double link_z,
				 std::string &member_file_name) {
  // Function to set up member output file name.
  if (fname.empty())
    throw BadArgumentException("Fileio::output_member_name", "fname", "a valid string");
  if (mode != "spec" && mode != "phot")
    throw BadArgumentException("Fileio::output_member_name", "mode", "a valid option [spec/phot]");
  if (output != "ascii" && output != "fits")
    throw BadArgumentException("Fileio::output_member_name", "output", "a valid option [ascii/fits]");
  std::stringstream cluster_file_stream, member_file_stream;
  if(output == "ascii") 
    member_file_stream<<fname<<"_members_"<<link_r<<"_"<<link_z<<"_"<<mode<<".dat"; 
  else if(output == "fits") 
    member_file_stream<<fname<<"_members_"<<link_r<<"_"<<link_z<<"_"<<mode<<".fits"; 
  member_file_name = member_file_stream.str();
}

void Fileio::write_ascii (const std::vector<Cluster> &cluster_list, const std::string &cluster_file_name, 
			  const std::string &member_file_name) {
  // Funtion to output Cluster intances to an ASCII file.
  if (cluster_list.empty())
    throw BadArgumentException("Fileio::write_ascii", "cluster_list", "a valid vector");
  if (cluster_file_name.empty())
    throw BadArgumentException("Fileio::write_ascii", "cluster_file_name", "a valid string");
  if (member_file_name.empty())
    throw BadArgumentException("Fileio::write_ascii", "member_file_name", "a valid string");
  std::ofstream write_clusters (cluster_file_name.c_str());
  std::ofstream write_members (member_file_name.c_str());
  for(int i = 0; i < cluster_list.size(); i++) {
    write_clusters<<std::fixed<<std::setprecision(5);
    write_clusters<<std::setw(8)<<cluster_list[i].num<<" ";
    write_clusters<<std::setw(9)<<cluster_list[i].ra<<" ";
    write_clusters<<std::setw(7)<<cluster_list[i].ra_err<<" ";
    write_clusters<<std::setw(9)<<std::showpos<<cluster_list[i].dec<<" ";
    write_clusters<<std::setw(7)<<std::noshowpos<<cluster_list[i].dec_err<<" ";
    write_clusters<<std::setw(7)<<cluster_list[i].z<<" ";
    write_clusters<<std::setw(7)<<cluster_list[i].z_err<<" ";
    write_clusters<<std::setw(8)<<cluster_list[i].ngal<<" ";
    write_clusters<<std::setw(10)<<cluster_list[i].sn<<" ";
    write_clusters<<std::setw(7)<<cluster_list[i].size<<" ";
    write_clusters<<std::setw(9)<<cluster_list[i].area<<"\n";
    for(int j = 0; j < cluster_list[i].ngal; j++) {
      write_members<<std::fixed<<std::setprecision(5);
      write_members<<std::setw(8)<<cluster_list[i].num<<" ";
      write_members<<std::setw(8)<<cluster_list[i].ngal<<" ";
      write_members<<std::setw(8)<<cluster_list[i].z<<" ";
      write_members<<std::setw(12)<<cluster_list[i].mem[j]->id<<" ";
      write_members<<std::setw(9)<<cluster_list[i].mem[j]->P.P[0]<<" ";
      write_members<<std::setw(9)<<std::showpos<<cluster_list[i].mem[j]->P.P[1]<<" ";
      write_members<<std::setw(7)<<std::noshowpos<<cluster_list[i].mem[j]->z<<"\n";
    }
  }
  write_clusters.close();
  write_members.close();
}

void Fileio::write_fits (const std::vector<Cluster> &cluster_list, const std::string &cluster_file_name, 
			  const std::string &member_file_name) {
  // Funtion to output Cluster intances to an FITS file.
  if (cluster_list.empty())
    throw BadArgumentException("Fileio::write_fits", "cluster_list", "a valid vector");
  if (cluster_file_name.empty())
    throw BadArgumentException("Fileio::write_fits", "cluster_file_name", "a valid string");
  if (member_file_name.empty())
    throw BadArgumentException("Fileio::write_fits", "member_file_name", "a valid string");
  fitsfile *fptr1, *fptr2;
  int tint, current_pos = 0, status = 0;
  unsigned long tlong;
  double tdouble;
  const int cluster_fields = 11, member_fields = 7;
  char *cluster_types[cluster_fields], *member_types[member_fields];
  char *cluster_forms[cluster_fields], *member_forms[member_fields];
  cluster_types[0] = const_cast<char *>("NUM");     cluster_forms[0] = const_cast<char *>("J");
  cluster_types[1] = const_cast<char *>("RA");      cluster_forms[1] = const_cast<char *>("E");
  cluster_types[2] = const_cast<char *>("RA_ERR");  cluster_forms[2] = const_cast<char *>("E");
  cluster_types[3] = const_cast<char *>("DEC");     cluster_forms[3] = const_cast<char *>("E");
  cluster_types[4] = const_cast<char *>("DEC_ERR"); cluster_forms[4] = const_cast<char *>("E");
  cluster_types[5] = const_cast<char *>("Z");       cluster_forms[5] = const_cast<char *>("E");
  cluster_types[6] = const_cast<char *>("Z_ERR");   cluster_forms[6] = const_cast<char *>("E");
  cluster_types[7] = const_cast<char *>("NGAL");    cluster_forms[7] = const_cast<char *>("J");
  cluster_types[8] = const_cast<char *>("S/N");     cluster_forms[8] = const_cast<char *>("E");
  cluster_types[9] = const_cast<char *>("SIZE");    cluster_forms[9] = const_cast<char *>("E");
  cluster_types[10] = const_cast<char *>("AREA");   cluster_forms[10] = const_cast<char *>("E");
  member_types[0] = const_cast<char *>("C_NUM");    member_forms[0] = const_cast<char *>("J");
  member_types[1] = const_cast<char *>("C_NGAL");   member_forms[1] = const_cast<char *>("J");
  member_types[2] = const_cast<char *>("C_Z");      member_forms[2] = const_cast<char *>("E");
  member_types[3] = const_cast<char *>("G_ID");     member_forms[3] = const_cast<char *>("J");
  member_types[4] = const_cast<char *>("G_RA");     member_forms[4] = const_cast<char *>("E");
  member_types[5] = const_cast<char *>("G_DEC");    member_forms[5] = const_cast<char *>("E");
  member_types[6] = const_cast<char *>("G_Z");      member_forms[6] = const_cast<char *>("E");
  fits_create_file(&fptr1, cluster_file_name.c_str(), &status); /*create new FITS file*/
  if(status != 0){
    std::cout<<"Error! Cannot create cluster FITS file."<<std::endl;
    exit(-1);
  }
  fits_create_file(&fptr2, member_file_name.c_str(), &status); /*create new FITS file*/
  if(status != 0){
    std::cout<<"Error! Cannot create member FITS file."<<std::endl;
    exit(-1);
  }
  fits_create_tbl(fptr1, BINARY_TBL, 0, cluster_fields, cluster_types, 
		  cluster_forms, NULL, NULL, &status); /*create new FITS table*/ 
  fits_create_tbl(fptr2, BINARY_TBL, 0, member_fields, member_types, 
		  member_forms, NULL, NULL, &status); /*create new FITS table*/ 
  for(int i = 1; i <= cluster_list.size(); i++) {
    tint = cluster_list[i - 1].num;
    fits_write_col(fptr1, TUINT, 1, i, 1, 1, &tint, &status);
    tdouble = cluster_list[i - 1].ra;
    fits_write_col(fptr1, TDOUBLE, 3, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].ra_err;
    fits_write_col(fptr1, TDOUBLE, 3, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].dec;
    fits_write_col(fptr1, TDOUBLE, 4, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].dec_err;
    fits_write_col(fptr1, TDOUBLE, 4, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].z;
    fits_write_col(fptr1, TDOUBLE, 5, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].z_err;
    fits_write_col(fptr1, TDOUBLE, 5, i, 1, 1, &tdouble, &status);
    tint = cluster_list[i - 1].ngal;
    fits_write_col(fptr1, TUINT, 2, i, 1, 1, &tint, &status);
    tdouble = cluster_list[i - 1].sn;
    fits_write_col(fptr1, TDOUBLE, 6, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].size;
    fits_write_col(fptr1, TDOUBLE, 6, i, 1, 1, &tdouble, &status);
    tdouble = cluster_list[i - 1].area;
    fits_write_col(fptr1, TDOUBLE, 7, i, 1, 1, &tdouble, &status);
    for(int j = 1; j <= cluster_list[i - 1].ngal; j++) {
      current_pos++;
      tint = cluster_list[i - 1].num;
      fits_write_col(fptr2, TUINT, 1, current_pos, 1, 1, &tint, &status);
      tint = cluster_list[i - 1].ngal;
      fits_write_col(fptr2, TUINT, 2, current_pos, 1, 1, &tint, &status);
      tlong = cluster_list[i - 1].mem[j - 1]->id;
      fits_write_col(fptr2, TULONG, 3, current_pos, 1, 1, &tlong, &status); 
      tdouble = cluster_list[i - 1].mem[j - 1]->P.P[0];
      fits_write_col(fptr2, TDOUBLE, 4, current_pos, 1, 1, &tdouble, &status);
      tdouble = cluster_list[i - 1].mem[j - 1]->P.P[1];
      fits_write_col(fptr2, TDOUBLE, 5, current_pos, 1, 1, &tdouble, &status);
      tdouble = cluster_list[i - 1].mem[j - 1]->z;
      fits_write_col(fptr2, TDOUBLE, 6, current_pos, 1, 1, &tdouble, &status);
    }
  }
  fits_close_file(fptr1, &status); /*close FITS file*/
  fits_close_file(fptr2, &status); /*close FITS file*/
}

void Fileio::read_nz_data (const std::string &file_name, std::vector<double> &z_vals, 
				 std::vector<double> &count_vals) {
  // Function to read N(z) data from a file.
  std::cout<<"Reading N(z) data from: "<<file_name<<std::endl;
  std::ifstream read_file(file_name.c_str()); /* open file */
  if(read_file.fail())
    throw BadArgumentException("Merge_Fileio::read_file_list", "file_name", "a valid file name");
  std::string line;
  std::vector<std::string> cols;    
  while(std::getline(read_file, line)) { /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      split(line, cols, " "); /* split line into columns */
      z_vals.push_back(atof(cols[0].c_str()));
      count_vals.push_back(atof(cols[1].c_str()));
      cols.clear(); /* clear column vector */
    }
  }
  read_file.close(); /* close file */
}
