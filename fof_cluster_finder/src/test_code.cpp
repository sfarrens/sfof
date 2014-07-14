#include "astro.hpp"

#include <iostream>
#include <sstream>

int main (int argc, char *argv[]) {
  
  std::cout<<"THIS IS TEST CODE:"<<std::endl;
  
  Astro astro;
  std::vector<double> stuff;

  for (int i = 0; i < 10; i++)
    stuff.push_back(i * 0.5);

  std::cout<<astro.mean(stuff)<<" "<<astro.median(stuff)<<" "<<astro.variance(stuff)<<" "
	   <<astro.stderr(stuff)<<" "<<astro.stderr_median(stuff)<<std::endl;

}
