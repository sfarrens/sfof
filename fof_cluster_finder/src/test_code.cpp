#include <cmath>
#include <limits>
#include <iostream>

int main(int argc, char* argv[]) {
  
  double OmegaM_val = atof(argv[1]);
  double OmegaL_val = atof(argv[2]);

  std::cout<<OmegaM_val<<" "<<OmegaL_val<<" "<<abs(1.0 - OmegaM_val - OmegaL_val)<<" "
	   <<std::numeric_limits<double>::epsilon()<<std::endl;

  if (std::abs(1.0 - OmegaM_val - OmegaL_val) > std::numeric_limits<double>::epsilon())
    std::cout<<"True!"<<std::endl;
  else
    std::cout<<"False!"<<std::endl;
  
  return 0;
}
