/*Class of computational functions*/

#include "comp.hpp"

void Comp::start_time () { 
  start = time(NULL);
}

void Comp::end_time () { 
  end = time(NULL);
}

void Comp::d_h_m_s(double time, double &days, double &hours, double &minutes, double &seconds){
  double fdays = 24.0; double fhours = 60.0; double fminutes = 60.0;
  double fracpart = time / (fdays * fhours * fminutes);
  fracpart = modf(fracpart, &days);
  fracpart = modf(fracpart * fdays, &hours);
  fracpart = modf(fracpart * fhours, &minutes);
  fracpart = modf(fracpart * fminutes, &seconds);
}

void Comp::print_time() {		       
  double days, hours, minutes, seconds;
  d_h_m_s(double(end - start), days, hours, minutes, seconds);  
  std::cout<<" Time Elapsed: ["<<(int)days<<" days | "<<(int)hours<<" h | "<<(int)minutes
	   <<" m | "<<(int)seconds<<" s"<<"]"<<std::endl;
}
