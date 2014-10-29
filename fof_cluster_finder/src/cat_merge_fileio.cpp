/*Class for file input and output*/

#include <algorithm>
#include "cat_merge_fileio.hpp"


bool Merge_Fileio::existing_clt (int id, const std::vector<int> &list) {
  // Function to check if a cluster ID is new.
  return std::find(list.begin(), list.end(), id) != list.end();
}

void Merge_Fileio::read_file_list (const std::string &list, std::vector<Cluster> &cluster_list, 
				   gal_container& gals, const std::string &input_mode) {
  // Function to read a list of files.
  std::cout<<"File List: "<<list<<std::endl;
  std::ifstream read_file(list.c_str()); /* open file */
  if(read_file.fail())
    throw BadArgumentException("Merge_Fileio::read_file_list", "list", "a valid file name");
  if (input_mode != "ascii" && input_mode != "fits")
    throw BadArgumentException("Merge_Fileio::read_file_list", "input_mode", "a valid option [ascii/fits]");
  gal_count = -1;
  clt_count = -1;
  std::string line;
  while( std::getline(read_file, line)) { /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      if(input_mode == "ascii")
	read_ascii(line, cluster_list,gals); /* read each file */
      else
	read_fits(line, cluster_list,gals);
    }
  }
  read_file.close();
}

void Merge_Fileio::read_ascii (const std::string &fname, 
			       std::vector<Cluster> &cluster_list,gal_container& gals) {
  // Function to read in an ASCII file and store the contents in a vector of Cluster instances.
  std::cout<<"Reading: "<<fname<<std::endl;
  std::ifstream read_file(fname.c_str()); /* open file */
  if(read_file.fail())
    throw BadArgumentException("Merge_Fileio::read_ascii", "fname", "a valid file name");
  int clt_id;
  unsigned long id;
  double ra, dec, z;
  std::string line;
  std::vector<int> list_of_ids;
  std::vector<std::string> cols; 
  while(std::getline(read_file, line)) { /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      gal_count++;
      clt_id = atof(cols[0].c_str());
      id = strtoul(cols[2].c_str(), NULL, 0);
      ra = atof(cols[3].c_str());
      dec = atof(cols[4].c_str());
      z = atof(cols[5].c_str());
      auto ref = gals.insert(gal_container::value_type(id,Galaxy(gal_count, id, ra, dec, z)));/* intialise spec Galaxy */
      Galaxy* gal_here =  &ref.first->second;
      if (!existing_clt(clt_id, list_of_ids)) {
	list_of_ids.push_back(clt_id);
	clt_count++;
	Cluster cluster_here(clt_count);
	cluster_list.push_back(cluster_here);
      }
      cluster_list[clt_count].add_gal(gal_here);
      cols.clear(); /* clear column vector */
    }
  }
  read_file.close(); /* close file */
}

void Merge_Fileio::read_fits (const std::string &fname, 
			std::vector<Cluster> &cluster_list,gal_container& gals) {
  // Function to read in an FITS file and store the contents in a vector of Cluster instances.
  std::cout<<"Reading: "<<fname<<std::endl;
  std::ifstream read_file(fname.c_str()); /* open file */
  if(read_file.fail())
    throw BadArgumentException("Merge_Fileio::read_fits", "fname", "a valid file name");
  read_file.close();
  int clt_id;
  unsigned long id;
  double ra, dec, z;
  std::vector<int> list_of_ids;
  fitsfile *fptr;
  int n_cols, status=0, hdunum, hdutype, anynul, typecode;
  long n_rows, repeat, width;
  char *val, nullstr[] = "*";
  std::vector<std::string> cols; /* column vector */
  val = new char[1000];
  if(!fits_open_file(&fptr, fname.c_str(), READONLY, &status)){ /* open FITS file */
    if(fits_get_hdu_num(fptr, &hdunum) == 1) fits_movabs_hdu(fptr, 2, &hdutype, &status);
    else fits_get_hdu_type(fptr, &hdutype, &status);
    if(hdutype == IMAGE_HDU) /* check if the FITS file contains an image */
      std::cout<<"Error: this program only displays tables, not images."<<std::endl;
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
	clt_id = atof(cols[0].c_str());
	id = strtoul(cols[2].c_str(), NULL, 0);
	ra = atof(cols[3].c_str());
	dec = atof(cols[4].c_str());
	z = atof(cols[5].c_str());
      auto ref = gals.insert(gal_container::value_type(id,Galaxy(gal_count, id, ra, dec, z)));/* intialise spec Galaxy */
      Galaxy* gal_here =  &ref.first->second;
	if (!existing_clt(clt_id, list_of_ids)) {
	  list_of_ids.push_back(clt_id);
	  clt_count++;
	  Cluster cluster_here(clt_count);
	  cluster_list.push_back(cluster_here);
	}
	cluster_list[clt_count].add_gal(gal_here);
       	cols.clear(); /* clear column vector */
      }      
    }
    fits_close_file(fptr, &status); /* close FITS file */
  }
}

void Merge_Fileio::output_file_names (const std::string &output, const std::string &output_mode, 
				      std::string &cluster_file_name, std::string &member_file_name) {
  // Function to set up output file names.
  if (output.empty())
    throw BadArgumentException("Merge_Fileio::output_file_names", "output", "a valid string");
  if (output_mode != "ascii" && output_mode != "fits")
    throw BadArgumentException("Merge_Fileio::output_file_names", "output_mode", "a valid option [ascii/fits]");
  std::stringstream cluster_file_stream, member_file_stream;
  if(output_mode == "ascii") {
    cluster_file_stream<<output<<"_clusters.dat";
    member_file_stream<<output<<"_members.dat"; 
  }
  else {
    cluster_file_stream<<output<<"_clusters.fits";
    member_file_stream<<output<<"_members.fits"; 
  }
  cluster_file_name = cluster_file_stream.str();
  member_file_name = member_file_stream.str();
  std::cout<<"Cluster properties being written to: "<<cluster_file_name<<std::endl;
  std::cout<<"Cluster member properties being written to: "<<member_file_name<<std::endl;
}

void Merge_Fileio::read_bg_data (const std::string &file_name, std::vector<double> &z_vals, std::vector<double> &count_vals) {
  // Function to read background data from a file.
  std::cout<<"Reading background data from: "<<file_name<<std::endl;
  std::ifstream read_file(file_name.c_str()); /* open file */
  if(read_file.fail())
    throw BadArgumentException("Merge_Fileio::read_file_list", "file_name", "a valid file name");
  std::string line;
  std::vector<std::string> cols;    
  while(std::getline(read_file, line)) { /* read each line */
    if(line.length() >= 1 && 
       line.find("#") == std::string::npos) { /* skip empty lines and lines starting with # */
      fileio.split(line, cols, " "); /* split line into columns */
      z_vals.push_back(atof(cols[0].c_str()));
      count_vals.push_back(atof(cols[1].c_str()));
      cols.clear(); /* clear column vector */
    }
  }
  read_file.close(); /* close file */
}
