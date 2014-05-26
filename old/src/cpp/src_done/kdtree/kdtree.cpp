#include "./kdtree.hpp"
//#include "../healpix/healpix.hpp"


kdtree::kdtree(){
  galaxy_sep=NULL;trunk=NULL;galaxies=NULL;nb_leaf=NULL;nb_leaf_2=NULL;
  tNR=0;tNC=0;pNR=0;pNC=0;tNM=0;pNM=0;tNT=0;pNT=0;BN=0;
}

kdtree::~kdtree(){
  if (galaxy_sep != NULL)
    for (int i=0; i<(int)pow(2.0,(MAX_DEPTH));i++) {
      for(int j=0; j<nb_leaf[i]; ++j) {
	if (galaxy_sep[i][j].m != NULL) 
	  {delete [] galaxy_sep[i][j].m;galaxy_sep[i][j].m=NULL;}
	if (galaxy_sep[i][j].m_orig != NULL) 
	  {delete [] galaxy_sep[i][j].m_orig;galaxy_sep[i][j].m_orig=NULL;}
	if (galaxy_sep[i][j].trues != NULL) 
	  {delete [] galaxy_sep[i][j].trues;galaxy_sep[i][j].trues=NULL;}
      }
      if (galaxy_sep[i] != NULL) 
	{delete [] galaxy_sep[i];galaxy_sep[i]=NULL;}
    }
  if (galaxy_sep != NULL) {delete [] galaxy_sep;galaxy_sep=NULL;}
  trunk->clear();
  if (trunk != NULL) {delete trunk;trunk=NULL;}
  if (galaxies != NULL)
    for(int i=0; i<pNR; ++i) {
      if (galaxies[i].m != NULL) 
	{delete [] galaxies[i].m;galaxies[i].m=NULL;}
      if (galaxies[i].m_orig != NULL) 
	{delete [] galaxies[i].m_orig;galaxies[i].m_orig=NULL;}
      if (galaxies[i].trues != NULL) 
	{delete [] galaxies[i].trues;galaxies[i].trues=NULL;}
    }
  if (galaxies != NULL) {delete [] galaxies;galaxies=NULL;}
  if (nb_leaf != NULL) 
    {tools::free_ivector(nb_leaf,0,(int)pow(2.0,(MAX_DEPTH)));nb_leaf=NULL;}
  if (nb_leaf_2 != NULL) {
    tools::free_ivector(nb_leaf_2,0,(int)pow(2.0,(MAX_DEPTH)));
    nb_leaf_2=NULL;
  }
}

void kdtree::set_depth(int N){
  MAX_DEPTH = N;
  NCUT = 1 << (MAX_DEPTH-1);
  nb_leaf=tools::ivector(0,(int)pow(2.0,(MAX_DEPTH)));
  nb_leaf_2=tools::ivector(0,(int)pow(2.0,(MAX_DEPTH)));
}

void kdtree::set_tag(const class string_safe &file){tag_here=file;}
void kdtree::set_train(const class string_safe &file){trainfile=file;}
void kdtree::set_test(const class string_safe &file){testfile=file;}
void kdtree::set_matrix(const class string_safe &file){
  class string_safe file_here_here;file_here_here=file;
  std::string file_here=file_here_here.c_str();
  mat_here.retrieve(file_here);
}

void kdtree::set_kdtree(int nus){
  tools::find_NR_NC(trainfile, tNR, tNC);
  tools::find_NR_NC(testfile, pNR, pNC);
  tNM = mat_here.row_no(); pNM = mat_here.row_no();
  tNT = tNC-tNM; pNT = pNC-pNM; BN = 0; NUSE_HERE=nus;
  trunk = new TreeNode(0, MAX_DEPTH, tNR, tNM, tNT, 0, NUSE_HERE);
}

void kdtree::set_kdtree(int nus, 
			int NC_train, int NR_train, 
			int NC_test, int NR_test){
  tNR=NR_train;
  tNC=NC_train;
  pNR=NR_test;
  pNC=NC_test;
  tNM = mat_here.row_no(); pNM = mat_here.row_no();
  tNT = tNC-tNM; pNT = pNC-pNM; BN = 0; NUSE_HERE=nus;
  trunk = new TreeNode(0, MAX_DEPTH, tNR, tNM, tNT, 0, NUSE_HERE);
}


void kdtree::add_train_data(){
  kdtree::read_data(trunk->getObjects(), trainfile, tNR, tNC, tNT);
}

void kdtree::add_train_data(int id, double *mag_orig, double *trues){
  double temp;
  int NM = (tNC-tNT);
  //read matrix here
  class matrix mag_here(NM,1);
  class matrix mag_use(NM,1);
  (trunk->getObjects())[id].id=id;
  for(int i=0; i<NM; ++i) {
    temp=mag_orig[i];
    (trunk->getObjects())[id].m_orig[i]=temp;
    mag_here.set(temp,i+1,1);
  }
  mag_use=mat_here*mag_here;
  for(int i=0; i<NM; ++i) {(trunk->getObjects())[id].m[i]=mag_use.value(i+1,1);}
  for (int i=0; i<tNT; ++i)
    (trunk->getObjects())[id].trues[i]=trues[i];
}


void kdtree::set_branch(){trunk->branch(0);}

void kdtree::set_separate(){   
  galaxies = new Object_kdtree[pNR];
  for(int i=0; i<pNR; ++i) {
    galaxies[i].m = new double[pNM];
    galaxies[i].m_orig = new double[pNM];
    galaxies[i].trues = new double[pNT];
    for(int j=0; j<pNM; ++j) {
      galaxies[i].m[j] = 0.0;
      galaxies[i].m_orig[j] = 0.0;
    }
    for(int j=0; j<pNT; ++j) {
      galaxies[i].trues[j] = 0.0;
    }
  }
}

void kdtree::add_data(){
  kdtree::read_data(galaxies, testfile, pNR, pNC, pNT);
}

void kdtree::add_data(int id, double *mag_orig, double *trues){
  double temp;
  int NM = (tNC-tNT);
  //read matrix here
  class matrix mag_here(NM,1);
  class matrix mag_use(NM,1);
  galaxies[id].id=id;
  for(int i=0; i<NM; ++i) {
    temp=mag_orig[i];
    galaxies[id].m_orig[i]=temp;
    mag_here.set(temp,i+1,1);
  }
  mag_use=mat_here*mag_here;
  for(int i=0; i<NM; ++i) {galaxies[id].m[i]=mag_use.value(i+1,1);}
  for (int i=0; i<tNT; ++i)
    galaxies[id].trues[i]=trues[i];
}

void kdtree::set_separate2(){   
  //int nb_leaf[(int)pow(2.0,(MAX_DEPTH))];
  for (int i=0; i<(int)pow(2.0,(MAX_DEPTH)); ++i) {nb_leaf[i]=0;}
  for (int i=0; i<pNR; ++i) {
    tp = trunk->getLeefContaining(&galaxies[i]); 
    if (tp == NULL) {  
      error("galaxy not found in the training kdtree");
    } else {nb_leaf[tp->BN]=nb_leaf[tp->BN]+1;}
  }
  galaxy_sep = new ObjectPtr_kdtree[(int)pow(2.0,(MAX_DEPTH))];
  for (int i=0; i<(int)pow(2.0,(MAX_DEPTH));i++) {
    galaxy_sep[i] = new Object_kdtree[nb_leaf[i]];
    for(int j=0; j<nb_leaf[i]; ++j) {
      galaxy_sep[i][j].m = new double[pNM];
      galaxy_sep[i][j].m_orig = new double[pNM];
      galaxy_sep[i][j].trues = new double[pNT];
      for(int k=0; k<pNM; ++k) {
	galaxy_sep[i][j].m[k] = 0.0;
	galaxy_sep[i][j].m_orig[k] = 0.0;
      }
      for(int k=0; k<pNT; ++k) {galaxy_sep[i][j].trues[k] = 0.0;}
    }
  }
  for (int i=0; i<(int)pow(2.0,(MAX_DEPTH)); ++i) {nb_leaf_2[i]=0;}
  for (int i=0; i<pNR; ++i) {
    tp = trunk->getLeefContaining(&galaxies[i]); 
    if (tp == NULL) {  
      error("galaxy not found in the training kdtree");
    } else {      
      for(int k=0; k<pNM; ++k) {
	galaxy_sep[tp->BN][nb_leaf_2[tp->BN]].m[k]=galaxies[i].m[k];
	galaxy_sep[tp->BN][nb_leaf_2[tp->BN]].m_orig[k]=galaxies[i].m_orig[k];
      }
      for(int k=0; k<pNT; ++k) {
	galaxy_sep[tp->BN][nb_leaf_2[tp->BN]].trues[k] = galaxies[i].trues[k];
      }
      galaxy_sep[tp->BN][nb_leaf_2[tp->BN]].id = galaxies[i].id;
      nb_leaf_2[tp->BN]=nb_leaf_2[tp->BN]+1;
    }
  }
}

void kdtree::set_dump_files(){
  for (int i=0; i<(int)pow(2.0,(MAX_DEPTH)); ++i) {
    buffer=tag_here+"."+intToString(i,5)+".kdtree";
    FILE *output = fopen(buffer.c_str(), "w");
    for (int j=0; j<nb_leaf_2[i]; ++j) {
      for (int k=0; k<pNM; ++k)
	fprintf(output, "%lf ",galaxy_sep[i][j].m_orig[k]);	
      for (int k=0; k<pNT; ++k) 
	fprintf(output, "%lf \n", galaxy_sep[i][j].trues[k]);
    }
    fclose(output);
  }
  buffer=tag_here+".bound.kdtree";
  trunk->writeBoundaries(buffer);
}


void kdtree::read_data(Object_kdtree *data, 
		       const class string_safe &filename_here, 
		       const int NR, const int NC, const int NT) {
  class string_safe filename;filename=filename_here;
  double temp;
  int NM = (NC-NT);
  //read matrix here
  class matrix mag_here(NM,1);
  class matrix mag_use(NM,1);
  std::ifstream ss;
  ss.open(filename.c_str());
  for (int k=0; k<NR; ++k) {
    data[k].id=k;
    for(int i=0; i<NM; ++i) {
      if (ss >> temp) {
	data[k].m_orig[i]=temp;
	mag_here.set(temp,i+1,1);
      } else {error("ERROR 1: Bad input data int kdtree::read_data");}
    }
    mag_use=mat_here*mag_here;
    for(int i=0; i<NM; ++i) {data[k].m[i]=mag_use.value(i+1,1);}
    if (ss >> temp) {
      data[k].trues[0] = temp;
      for (int i=1; i<NT; ++i) {
	if (ss >> temp) {
	  data[k].trues[i]=temp;
	} else {error("ERROR 1: Bad input data int kdtree::read_data");}
      }
    }
  }
  ss.close();
}
