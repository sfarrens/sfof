#include "./kdtree.hpp"


kdtree::kdtree(){
  galaxy_sep=NULL;trunk=NULL;galaxies=NULL;nb_leaf=NULL;nb_leaf_2=NULL;
  tNR=0;tNC=0;pNR=0;pNC=0;tNM=0;pNM=0;tNT=0;pNT=0;BN=0;
}

kdtree::~kdtree(){
  if (galaxy_sep != NULL){
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
    delete [] galaxy_sep;
    galaxy_sep=NULL;
  }
  if (trunk != NULL) {delete trunk; trunk=NULL;}
  if (galaxies != NULL){
    for(int i=0; i<pNR; ++i) {
      if (galaxies[i].m != NULL) 
	{delete [] galaxies[i].m;galaxies[i].m=NULL;}
      if (galaxies[i].m_orig != NULL) 
	{delete [] galaxies[i].m_orig;galaxies[i].m_orig=NULL;}
      if (galaxies[i].trues != NULL) 
	{delete [] galaxies[i].trues;galaxies[i].trues=NULL;}
    }
    delete [] galaxies;
    galaxies=NULL;
  }
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
void kdtree::set_matrix(const class string_safe &file){
  class string_safe file_here_here;file_here_here=file;
  std::string file_here=file_here_here.c_str();
  mat_here.retrieve(file_here);
}

void kdtree::set_kdtree_train(int nus){
  tools::find_NR_NC(trainfile, tNR, tNC);
  tNM = mat_here.row_no(); 
  tNT = tNC-tNM; BN = 0; NUSE_HERE=nus;
  trunk = new TreeNode(0, MAX_DEPTH, tNR, tNM, tNT, 0, NUSE_HERE);
}

void kdtree::set_kdtree_train(int nus, int NC_train, int NR_train){
  tNR=NR_train;
  tNC=NC_train;
  tNM = mat_here.row_no(); 
  tNT = tNC-tNM; BN = 0; NUSE_HERE=nus;
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
