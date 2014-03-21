#include <iostream>
#include <fstream>
#include <map>
 
#include "../tools/math_object.hpp"
#include "../tools/tools.hpp"
#include "spline.hpp"
#include "spline_web.hpp"

spline_web::spline_web(){
  lenght_x1=0;lenght_x2=0;
  size_max_x1=1000;size_max_x2=1000;
  x1dat=tools::dvector(1,1000);
  x2dat=tools::dvector(1,1000);
  ydat=tools::dmatrix(1,1000,1,1000);
  y1dat=tools::dmatrix(1,1000,1,1000);y2dat=tools::dmatrix(1,1000,1,1000);
  y12dat=tools::dmatrix(1,1000,1,1000);
  y2x1dat=tools::dmatrix(1,1000,1,1000);y2x2dat=tools::dmatrix(1,1000,1,1000);
  armed_x1=false;armed_x2=false;armed_x12=false;order_x1=true;order_x2=true;
  for (int i = 1; i <= 1000; i++)
    for (int j = 1; j <= 1000; j++) ydat[i][j] = 0;
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error((char *)"no memory in creation of spline_web");
}

spline_web::spline_web(const spline_web& s) {
  lenght_x1=s.lenght_x1;lenght_x2=s.lenght_x2;
  size_max_x1=s.size_max_x1;size_max_x2=s.size_max_x2;
  x1dat=tools::dvector(1,size_max_x1);
  x2dat=tools::dvector(1,size_max_x2);
  ydat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y12dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  armed_x1=s.armed_x1;armed_x2=s.armed_x2;armed_x12=s.armed_x12;
  order_x1=s.order_x1;order_x2=s.order_x2;
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error((char *)"no memory in creation of spline_web");
  for (int i = 1; i <= lenght_x1; i++){x1dat[i]=s.x1dat[i];}
  for (int i = 1; i <= lenght_x2; i++){x2dat[i]=s.x2dat[i];}
  for (int i = 1; i <= lenght_x1; i++)
    for (int j = 1; j <= lenght_x2; j++){
      ydat[i][j]=s.ydat[i][j];y1dat[i][j]=s.y1dat[i][j];
      y2dat[i][j]=s.y2dat[i][j];y12dat[i][j]=s.y12dat[i][j];
      y2x1dat[i][j]=s.y2x1dat[i][j];y2x2dat[i][j]=s.y2x2dat[i][j];
    }
}

spline_web::spline_web(std::string name){
  double X; char tmp; int ca,cs;
  ifstream save_file;
  save_file.open(name.c_str());
  save_file>>tmp>>lenght_x1>>lenght_x2;
  save_file>>tmp>>armed_x1>>armed_x2>>armed_x12;
  save_file>>tmp>>order_x1>>order_x2;
  armed_x1=false; armed_x2=false; armed_x12=false;
  size_max_x1=lenght_x1; size_max_x2=lenght_x2;
  x1dat=tools::dvector(1,size_max_x1);
  x2dat=tools::dvector(1,size_max_x2);
  ydat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y12dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error((char *)"no memory in creation of spline_web");
  for (int k =1; k<=lenght_x1; k++){
    save_file>>X;
    x1dat[k]=X;
    if (k>1) {if (x1dat[k]<x1dat[k-1]) order_x1=false;}
  }
  for (int k =1; k<=lenght_x2; k++){
    save_file>>X;
    x2dat[k]=X;
    if (k>1) {if (x2dat[k]<x2dat[k-1]) order_x2=false;}
  }
  for (int k =1; k<=lenght_x1; k++)
    for (int l =1; l<=lenght_x2; l++){
      save_file>>X;
      ydat[k][l]=X;
    }
  save_file.close();
}

spline_web::spline_web(double(*func)(double,double), double a1, double b1, 
		       int n1, std::string key1, double a2, double b2, 
		       int n2, std::string key2){
  double e_log=2.71828182846; int i,j; step_key which1,which2;
  lenght_x1=0;lenght_x2=0;
  size_max_x1=n1;size_max_x2=n2;
  x1dat=tools::dvector(1,size_max_x1);
  x2dat=tools::dvector(1,size_max_x2);
  ydat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y12dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  armed_x1=false;armed_x2=false;armed_x12=false;order_x1=true;order_x2=true;
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error((char *)"no memory in creation of spline_web");
  double x1_now,x2_now=a2;
  which1=which_step_key(key1);
  which2=which_step_key(key2);
  switch (which2) {
  case dx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));
	  x1_now=log(x1_now);x1_now+=(log(b1)-log(a1))/(n1-1);
	  x1_now=pow(e_log,x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now)); x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
    }
    break;
  case dlnx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
    }
    break;
  case dexpx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
    }
    break;
  default:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,func(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
    }
  }
}

spline_web::spline_web(mo_double f, math_object *mo, double a1, double b1, 
		       int n1, std::string key1,double a2, double b2, 
		       int n2, std::string key2){
  double e_log=2.71828182846; int i,j; step_key which1,which2;
  lenght_x1=0;lenght_x2=0;
  size_max_x1=n1;size_max_x2=n2;
  x1dat=tools::dvector(1,size_max_x1);
  x2dat=tools::dvector(1,size_max_x2);
  ydat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y12dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x1dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  y2x2dat=tools::dmatrix(1,size_max_x1,1,size_max_x2);
  armed_x1=false;armed_x2=false;armed_x12=false;order_x1=true;order_x2=true;
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error((char *)"no memory in creation of spline_web");
  double x1_now=a1,x2_now=a2;
  which1=which_step_key(key1);
  which2=which_step_key(key2);
  switch (which2) {
  case dx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
    }
    break;
  case dlnx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=log(x2_now);x2_now+=(log(b2)-log(a2))/(n2-1);
	x2_now=pow(e_log,x2_now);
      }
    }
    break;
  case dexpx:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now=pow(e_log,x2_now);x2_now+=(pow(e_log,b2)-pow(e_log,a2))/(n2-1);
	x2_now=log(x2_now);
      }
    }
    break;
  default:
    switch(which1){
    case dx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dlnx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=log(x1_now);
	  x1_now+=(log(b1)-log(a1))/(n1-1);x1_now=pow(e_log,x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    case dexpx:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now=pow(e_log,x1_now);
	  x1_now+=(pow(e_log,b1)-pow(e_log,a1))/(n1-1);x1_now=log(x1_now);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
      break;
    default:
      for (i=1; i<=n2; i++){
	x1_now=a1;
	for (j=1; j<=n1; j++) {
	  set(x1_now,x2_now,(mo->*f)(x1_now,x2_now));x1_now+=(b1-a1)/(n1-1);
	}
	x2_now+=(b2-a2)/(n2-1);
      }
    }
  }
}

spline_web::~spline_web(){
  if (x1dat!=0) tools::free_dvector(x1dat,1,size_max_x1);
  if (x2dat!=0) tools::free_dvector(x2dat,1,size_max_x2);
  if (ydat!=0) tools::free_dmatrix(ydat,1,size_max_x1,1,size_max_x2);
  if (y1dat!=0) tools::free_dmatrix(y2dat,1,size_max_x1,1,size_max_x2);
  if (y2dat!=0) tools::free_dmatrix(y1dat,1,size_max_x1,1,size_max_x2);
  if (y12dat!=0) tools::free_dmatrix(y12dat,1,size_max_x1,1,size_max_x2);
  if (y2x1dat!=0) tools::free_dmatrix(y2x1dat,1,size_max_x1,1,size_max_x2);
  if (y2x2dat!=0) tools::free_dmatrix(y2x2dat,1,size_max_x1,1,size_max_x2);
}

void spline_web::clear(){
  if (x1dat!=0) tools::free_dvector(x1dat,1,size_max_x1);
  if (x2dat!=0) tools::free_dvector(x2dat,1,size_max_x2);
  if (ydat!=0) tools::free_dmatrix(ydat,1,size_max_x1,1,size_max_x2);
  if (y1dat!=0) tools::free_dmatrix(y2dat,1,size_max_x1,1,size_max_x2);
  if (y2dat!=0) tools::free_dmatrix(y1dat,1,size_max_x1,1,size_max_x2);
  if (y12dat!=0) tools::free_dmatrix(y12dat,1,size_max_x1,1,size_max_x2);
  if (y2x1dat!=0) tools::free_dmatrix(y2x1dat,1,size_max_x1,1,size_max_x2);
  if (y2x2dat!=0) tools::free_dmatrix(y2x2dat,1,size_max_x1,1,size_max_x2);
  lenght_x1=0;lenght_x2=0;
  size_max_x1=1000;size_max_x2=1000;
  x1dat=tools::dvector(1,1000);
  x2dat=tools::dvector(1,1000);
  ydat=tools::dmatrix(1,1000,1,1000);
  y1dat=tools::dmatrix(1,1000,1,1000);y2dat=tools::dmatrix(1,1000,1,1000);
  y12dat=tools::dmatrix(1,1000,1,1000);
  y2x1dat=tools::dmatrix(1,1000,1,1000);y2x2dat=tools::dmatrix(1,1000,1,1000);
  armed_x1=false;armed_x2=false;armed_x12=false;order_x1=true;order_x2=true;
  for (int i = 1; i <= 1000; i++)
    for (int j = 1; j <= 1000; j++) ydat[i][j] = 0;
  if (x1dat == 0 || x2dat == 0 || ydat == 0 || y1dat == 0 || 
      y2dat == 0 || y12dat == 0 || y2x1dat == 0 || y2x2dat==0)
    error("no memory in creation of spline_web");
}

void spline_web::set(double x1, double x2, double y){
  map< double,int,less<double> >::iterator i,j;
  int x1pos, x2pos;
  i=x1grid.find(x1);j=x2grid.find(x2);
  if (i==x1grid.end()) {
    x1grid[x1]=++lenght_x1;x1pos=lenght_x1;x1dat[x1pos]=x1;
  } else {
    x1pos=x1grid[x1];
  }
  if (j==x2grid.end()) {x2grid[x2]=++lenght_x2;x2pos=lenght_x2;x2dat[x2pos]=x2;
  } else {
    x2pos=x2grid[x2];
  }
  if (lenght_x1>=size_max_x1) resize_x1();
  if (lenght_x2>=size_max_x2) resize_x2();
  ydat[x1pos][x2pos]=y;
}

void spline_web::resize_x1(){
  double *tmp_x1dat,**tmp_ydat; int i,j;
  tmp_x1dat = tools::dvector(1,2*size_max_x1);
  tmp_ydat = tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  for (i =1; i<= size_max_x1; i++){
    tmp_x1dat[i]=x1dat[i];
    for (j =1; j<= size_max_x2; j++){tmp_ydat[i][j]=ydat[i][j];}
  }
  tools::free_dvector(x1dat,1,size_max_x1);
  tools::free_dmatrix(ydat,1,size_max_x1,1,size_max_x2);
  x1dat=tmp_x1dat; ydat=tmp_ydat;
  tools::free_dmatrix(y1dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y12dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2x1dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2x2dat,1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  y2dat=tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  y12dat=tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  y2x1dat=tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  y2x2dat=tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  size_max_x1*=2;
}

void spline_web::resize_x2(){
  double *tmp_x2dat,**tmp_ydat; int i,j;
  tmp_x2dat = tools::dvector(1,2*size_max_x1);
  tmp_ydat = tools::dmatrix(1,2*size_max_x1,1,size_max_x2);
  for (i =1; i<= size_max_x2; i++){
    tmp_x2dat[i]=x2dat[i];
    for (j =1; j<= size_max_x1; j++){tmp_ydat[j][i]=ydat[j][i];}
  }
  tools::free_dvector(x2dat,1,size_max_x2);
  tools::free_dmatrix(ydat,1,size_max_x1,1,size_max_x2);
  x2dat=tmp_x2dat; ydat=tmp_ydat;
  tools::free_dmatrix(y1dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y12dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2x1dat,1,size_max_x1,1,size_max_x2);
  tools::free_dmatrix(y2x2dat,1,size_max_x1,1,size_max_x2);
  y1dat=tools::dmatrix(1,size_max_x1,1,2*size_max_x2);
  y2dat=tools::dmatrix(1,size_max_x1,1,2*size_max_x2);
  y12dat=tools::dmatrix(1,size_max_x1,1,2*size_max_x2);
  y2x1dat=tools::dmatrix(1,size_max_x1,1,2*size_max_x2);
  y2x2dat=tools::dmatrix(1,size_max_x1,1,2*size_max_x2);
  size_max_x2*=2;
}

void spline_web::dump(std::string name){
  int k,l;
  ofstream local_file(name.c_str());
  local_file.setf(ios::scientific);
  for (k = 1; k <= lenght_x1; k++)
    for (l = 1; l <= lenght_x2; l++) {
      local_file<<x1dat[k]<<"\t"<<x2dat[l]<<"\t"<<ydat[k][l]<<"\n";
    }
  local_file.close();
}

void spline_web::save(std::string name){
  double X;
  ofstream save_file;
  save_file.open(name.c_str());
  save_file.setf(ios::scientific);
  save_file<<"#"<<lenght_x1<<"\t"<<lenght_x2<<"\n";
  save_file<<"#"<<armed_x1<<"\t"<<armed_x2<<"\t"<<armed_x12<<"\n";
  save_file<<"#"<<order_x1<<"\t"<<order_x2<<"\n";
  for (int k =1; k<=lenght_x1; k++) {
    X=x1dat[k];
    save_file<<X<<"\t";
  }
  save_file<<"\n";
  for (int k =1; k<=lenght_x2; k++) {
    X=x2dat[k];
    save_file<<X<<"\t";
  }
  save_file<<"\n";
  for (int k =1; k<=lenght_x1; k++){
    for (int l =1; l<=lenght_x2; l++) {
      X=ydat[k][l];
      save_file<<X<<"\t";
    }
    save_file<<"\n";
  }
  save_file.close();
}

void spline_web::add(int k, int l, double y) {
  if (k>lenght_x1 || k<0 || l>lenght_x2 || l<0) 
    error((char *)"spline_web::add element not in spline");
  ydat[k][l] += y;
}

void spline_web::mul(int k, int l, double x) {
  if (k>lenght_x1 || k<0 || l>lenght_x2 || l<0) 
    error((char *)"spline_web::mul element not available");
  ydat[k][l] *=x;
}

void spline_web::do_order_x1(){
  double *wksp,**wk2sp; unsigned long * iwksp;
  wksp=tools::dvector(1,lenght_x1);
  wk2sp=tools::dmatrix(1,lenght_x1,1,lenght_x2);
  iwksp=tools::lvector(1,lenght_x1);
  spline::indexx(x1dat,iwksp,lenght_x1);
  for (int j=1;j<=lenght_x1;j++) wksp[j]=x1dat[j];
  for (int j=1;j<=lenght_x1;j++) x1dat[j]=wksp[iwksp[j]];
  for (int j=1;j<=lenght_x1;j++) x1grid[x1dat[j]]=j;
  for (int i=1;i<=lenght_x1;i++)
    for (int j=1;j<=lenght_x2;j++) wk2sp[i][j]=ydat[i][j];
  for (int i=1;i<=lenght_x1;i++)
    for (int j=1;j<=lenght_x2;j++) ydat[i][j]=wk2sp[iwksp[i]][j];
  tools::free_dvector(wksp,1,lenght_x1);
  tools::free_dmatrix(wk2sp,1,lenght_x1,1,lenght_x2);
  tools::free_lvector(iwksp,1,lenght_x1);
}

void spline_web::do_order_x2(){
  double *wksp,**wk2sp; unsigned long * iwksp;
  wksp=tools::dvector(1,lenght_x2);
  wk2sp=tools::dmatrix(1,lenght_x1,1,lenght_x2);
  iwksp=tools::lvector(1,lenght_x2);
  spline::indexx(x2dat,iwksp,lenght_x2);
  for (int j=1;j<=lenght_x2;j++) wksp[j]=x2dat[j];
  for (int j=1;j<=lenght_x2;j++) x2dat[j]=wksp[iwksp[j]];
  for (int j=1;j<=lenght_x2;j++) x2grid[x2dat[j]]=j;
  for (int i=1;i<=lenght_x1;i++)
    for (int j=1;j<=lenght_x2;j++) wk2sp[i][j]=ydat[i][j];
  for (int i=1;i<=lenght_x1;i++)
    for (int j=1;j<=lenght_x2;j++) ydat[i][j]=wk2sp[i][iwksp[j]];
  tools::free_dvector(wksp,1,lenght_x1);
  tools::free_dmatrix(wk2sp,1,lenght_x1,1,lenght_x2);
  tools::free_lvector(iwksp,1,lenght_x1);
}

void spline_web::arm_x1(double xp1, double xp2){
  double *tmp_ydat,*tmp_y2x1dat;
  if (!order_x1) error((char *)"Cannot spline_web::arm_x12 out of order");
  if (!order_x2) error((char *)"Cannot spline_web::arm_x12 out of order");
  tmp_ydat=tools::dvector(1,lenght_x2);tmp_y2x1dat=tools::dvector(1,lenght_x2);
  if (armed_x1) error((char *)"spline_web already armed");
  if (!order_x1) {do_order_x1(); order_x1=true;}
  for (int i=1;i<=lenght_x1;i++){
    for (int j=1;j<=lenght_x2;j++){tmp_ydat[j]=ydat[i][j];}
    spline::cubic_spline(x1dat,tmp_ydat,1,lenght_x1,xp1,xp2,tmp_y2x1dat);
    for (int j=1;j<=lenght_x2;j++){tmp_y2x1dat[j]=y2x1dat[i][j];}
  }
  armed_x1 = true;
  tools::free_dvector(tmp_ydat,1,lenght_x2);
  tools::free_dvector(tmp_y2x1dat,1,lenght_x2);
}

void spline_web::arm_x2(double xp1, double xp2){
  double *tmp_ydat,*tmp_y2x2dat;
  if (!order_x1) error((char *)"Cannot spline_web::arm_x12 out of order");
  if (!order_x2) error((char *)"Cannot spline_web::arm_x12 out of order");
  tmp_ydat=tools::dvector(1,lenght_x1);tmp_y2x2dat=tools::dvector(1,lenght_x1);
  if (armed_x2) error((char *)"spline_web already armed");
  if (!order_x2) {do_order_x2(); order_x2=true;}
  for (int i=1;i<=lenght_x2;i++){
    for (int j=1;j<=lenght_x1;j++){tmp_ydat[j]=ydat[j][i];}
    spline::cubic_spline(x2dat,tmp_ydat,1,lenght_x2,xp1,xp2,tmp_y2x2dat);
    for (int j=1;j<=lenght_x1;j++){tmp_y2x2dat[j]=y2x2dat[j][i];}
  }
  armed_x2 = true;
  tools::free_dvector(tmp_ydat,1,lenght_x2);
  tools::free_dvector(tmp_y2x2dat,1,lenght_x2);
}

void spline_web::arm_x12(){
  int i,j;
  if(lenght_x1<=1 || lenght_x2<=1) 
    error((char *)"Cannot spline_web::arm_x12 with lenght<=1");
  if (!order_x1) error((char *)"Cannot spline_web::arm_x12 out of order");
  if (!order_x2) error((char *)"Cannot spline_web::arm_x12 out of order");
  for (int i=2;i<=lenght_x1-1;i++)
    for (int j=2;j<=lenght_x2-1;j++) {
      y1dat[i][j]=(ydat[i+1][j]-ydat[i-1][j])/(x1dat[i+1]-x1dat[i-1]);
      y2dat[i][j]=(ydat[i][j+1]-ydat[i][j-1])/(x2dat[j+1]-x2dat[j-1]);
      y12dat[i][j]=(ydat[i+1][j+1]-ydat[i+1][j-1]-
		    ydat[i-1][j+1]+ydat[i-1][j-1])
	/((x1dat[i+1]-x1dat[i-1])*(x2dat[j+1]-x2dat[j-1]));
    }
  for (int i=2;i<=lenght_x1-1;i++){
    y1dat[i][1]=(ydat[i+1][1]-ydat[i-1][1])/(x1dat[i+1]-x1dat[i-1]);
    y2dat[i][1]=(ydat[i][2]-ydat[i][1])/(x2dat[2]-x2dat[1]);
    y12dat[i][1]=(ydat[i+1][2]-ydat[i+1][1]-ydat[i-1][2]+ydat[i-1][1])
      /((x1dat[i+1]-x1dat[i-1])*(x2dat[2]-x2dat[1]));
  }
  for (int i=2;i<=lenght_x1-1;i++){
    y1dat[i][lenght_x2]=(ydat[i+1][lenght_x2]-ydat[i-1][lenght_x2])/
      (x1dat[i+1]-x1dat[i-1]);
    y2dat[i][lenght_x2]=(ydat[i][lenght_x2]-ydat[i][lenght_x2-1])/
      (x2dat[lenght_x2]-x2dat[lenght_x2-1]);
    y12dat[i][lenght_x2]=(ydat[i+1][lenght_x2]-ydat[i+1][lenght_x2-1]-
			  ydat[i-1][lenght_x2]+ydat[i-1][lenght_x2-1])
      /((x1dat[i+1]-x1dat[i-1])*(x2dat[lenght_x2]-x2dat[lenght_x2-1]));
  }
  for (int j=2;j<=lenght_x2-1;j++){
    y1dat[1][j]=(ydat[2][j]-ydat[1][j])/(x1dat[2]-x1dat[1]);
    y2dat[1][j]=(ydat[1][j+1]-ydat[1][j-1])/(x2dat[j+1]-x2dat[j-1]);
    y12dat[1][j]=(ydat[2][j+1]-ydat[2][j+1]-ydat[1][j+1]+ydat[1][j-1])
      /((x1dat[2]-x1dat[1])*(x2dat[j+1]-x2dat[j-1]));
  }
  for (int j=2;j<=lenght_x2-1;j++){
    y1dat[lenght_x1][j]=(ydat[lenght_x1][j]-ydat[lenght_x1-1][j])/
      (x1dat[lenght_x1]-x1dat[lenght_x1-1]);
    y2dat[lenght_x1][j]=(ydat[lenght_x1][j+1]-ydat[lenght_x1][j-1])/
      (x2dat[j+1]-x2dat[j-1]);
    y12dat[lenght_x1][j]=(ydat[lenght_x1][j+1]-ydat[lenght_x1][j+1]-
			  ydat[lenght_x1-1][j+1]+ydat[lenght_x1-1][j-1])
      /((x1dat[lenght_x1]-x1dat[lenght_x1-1])*(x2dat[j+1]-x2dat[j-1]));
  }
  
  y1dat[1][1]=(ydat[2][1]-ydat[1][1])/(x1dat[2]-x1dat[1]);
  y2dat[1][1]=(ydat[1][2]-ydat[1][1])/(x2dat[2]-x2dat[1]);
  y12dat[1][1]=(ydat[2][2]-ydat[2][1]-ydat[1][2]+ydat[1][1])
    /((x1dat[2]-x1dat[1])*(x2dat[2]-x2dat[1]));
  
  y1dat[1][lenght_x2]=(ydat[2][lenght_x2]-ydat[1][lenght_x2])/
    (x1dat[2]-x1dat[1]);
  y2dat[1][lenght_x2]=(ydat[1][lenght_x2]-ydat[1][lenght_x2-1])/
    (x2dat[lenght_x2]-x2dat[lenght_x2-1]);
  y12dat[1][lenght_x2]=(ydat[2][lenght_x2]-ydat[2][lenght_x2-1]-
			ydat[1][lenght_x2]+ydat[1][lenght_x2-1])
    /((x1dat[2]-x1dat[1])*(x2dat[lenght_x2]-x2dat[lenght_x2-1]));
  
  y1dat[lenght_x1][1]=(ydat[lenght_x1][1]-ydat[lenght_x1-1][1])/
    (x1dat[lenght_x1]-x1dat[lenght_x1-1]);
  y2dat[lenght_x1][1]=(ydat[lenght_x1][2]-ydat[lenght_x1][1])/
    (x2dat[2]-x2dat[1]);
  y12dat[lenght_x1][1]=(ydat[lenght_x1][2]-ydat[lenght_x1][1]-
			ydat[lenght_x1-1][2]+ydat[lenght_x1-1][1])
    /((x1dat[lenght_x1]-x1dat[lenght_x1-1])*(x2dat[2]-x2dat[1]));

  y1dat[lenght_x1][lenght_x2]=(ydat[lenght_x1][lenght_x2]-
			       ydat[lenght_x1-1][lenght_x2])/
    (x1dat[lenght_x1]-x1dat[lenght_x1-1]);
  y2dat[lenght_x1][lenght_x2]=(ydat[lenght_x1][lenght_x2]-
			       ydat[lenght_x1][lenght_x2-1])/
    (x2dat[lenght_x2]-x2dat[lenght_x2-1]);
  y12dat[lenght_x1][lenght_x2]=(ydat[lenght_x1][lenght_x2]-
				ydat[lenght_x1][lenght_x2-1]-
				ydat[lenght_x1-1][lenght_x2]+
				ydat[lenght_x1-1][lenght_x2-1])
    /((x1dat[lenght_x1]-x1dat[lenght_x1-1])*
      (x2dat[lenght_x2]-x2dat[lenght_x2-1]));
}

double spline_web::y1(double x1, double x2){
  return cubic_splint_x1_web(x1dat,x2dat,ydat,y2x1dat,
			     lenght_x1,lenght_x2,x1,x2);
}

double spline_web::y2(double x1, double x2){
	return cubic_splint_x2_web(x1dat,x2dat,ydat,y2x1dat,
				   lenght_x1,lenght_x2,x1,x2);
}

double spline_web::y12(double x1, double x2){
  double ansy1,ansy2;
  return bicubic_inter(x1dat,x2dat,ydat,y1dat,y2dat,y12dat,
		       lenght_x1,lenght_x2,x1,x2,&ansy1,&ansy2);
}

double spline_web::cubic_splint_x1_web(double *x1a, double *x2a, 
				       double **ya, double **y2a,
				       int m, int n, double x1, double x2){
  int i,j;
  double *ytmp,*yytmp,*yatmp,*y2atmp,y;
  
  ytmp=tools::dvector(1,n);
  yytmp=tools::dvector(1,n);
  yatmp=tools::dvector(1,m);
  y2atmp=tools::dvector(1,m);
  for (j=1;j<=n;j++){
    for (i=1;i<=m;i++){yatmp[i]=ya[i][j];y2atmp[i]=y2a[i][j];}
    yytmp[j]=spline::cubic_splint(x1a,yatmp,y2atmp,m,x1);
  }
  spline::cubic_spline(x2a,yytmp,1,n,1.0e30,1.0e30,ytmp);
  y=spline::cubic_splint(x2a,yytmp,ytmp,n,x2);
  tools::free_dvector(yytmp,1,m); tools::free_dvector(ytmp,1,m);
  tools::free_dvector(yatmp,1,n); tools::free_dvector(y2atmp,1,n);
  return y;
}

double spline_web::cubic_splint_x2_web(double *x1a, double *x2a, 
				       double **ya, double **y2a,
				       int m, int n, double x1, double x2){
  int i,j;
  double *ytmp,*yytmp,*yatmp,*y2atmp,y;
  
  ytmp=tools::dvector(1,m);
  yytmp=tools::dvector(1,m);
  yatmp=tools::dvector(1,n);
  y2atmp=tools::dvector(1,n);
  for (j=1;j<=m;j++){
    for (i=1;i<=n;i++){yatmp[i]=ya[j][i];y2atmp[i]=y2a[j][i];}
    yytmp[j]=spline::cubic_splint(x2a,yatmp,y2atmp,n,x2);
  }
  spline::cubic_spline(x1a,yytmp,1,m,1.0e30,1.0e30,ytmp);
  y=spline::cubic_splint(x1a,yytmp,ytmp,n,x1);
  tools::free_dvector(yytmp,1,m); tools::free_dvector(ytmp,1,m);
  tools::free_dvector(yatmp,1,n); tools::free_dvector(y2atmp,1,n);
  return y;
}

void spline_web::bcubic_coef(double *y, double *y1, double *y2, double *y12,
			     double d1, double d2, double **c){
  static int wt[16][16]= {
    {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0},
    {-3,0,0,3,0,0,0,0,-2,0,0,-1,0,0,0,0},
    {2,0,0,-2,0,0,0,0,1,0,0,1,0,0,0,0},
    {0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0},
    {0,0,0,0,-3,0,0,3,0,0,0,0,-2,0,0,-1},
    {0,0,0,0,2,0,0,-2,0,0,0,0,1,0,0,1},
    {-3,3,0,0,-2,-1,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,-3,3,0,0,-2,-1,0,0},
    {9,-9,9,-9,6,3,-3,-6,6,-6,-3,3,4,2,1,2},
    {-6,6,-6,6,-4,-2,2,4,-3,3,3,-3,-2,-1,-1,-2},
    {2,-2,0,0,1,1,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,2,-2,0,0,1,1,0,0},
    {-6,6,-6,6,-3,-3,3,3,-4,4,2,-2,-2,-2,-1,-1},
    {4,-4,4,-4,2,2,-2,-2,2,-2,-2,2,1,1,1,1}};
  int l,k,j,i;
  double xx,d1d2,cl[16],x[16];
  
  d1d2=d1*d2;
  for (i=1;i<=4;i++) {
    x[i-1]=y[i];x[i+3]=y1[i]*d1;
    x[i+7]=y2[i]*d2;x[i+11]=y12[i]*d1d2;
  }
  for (i=0;i<=15;i++) {
    xx=0.0;
    for (k=0;k<=15;k++) xx += wt[i][k]*x[k];
    cl[i]=xx;
  }
  l=0;
  for (i=1;i<=4;i++)
    for (j=1;j<=4;j++) c[i][j]=cl[l++];
}

double spline_web::bicubic_inter(double *x1a, double *x2a, double **ya, 
				 double **y1a,double **y2a, 
				 double **y12a, int n, int m,
                                 double x1, double x2,
				 double *ansy1, double *ansy2){
  int jlo,jhi,klo,khi,j,k;
  jlo=1; jhi=n;
  klo=1; khi=m;
  while (jhi-jlo > 1){
    j=(jhi+jlo) >> 1;
    if (x1a[j] > x1) jhi=j;
    else jlo=j;
  }
  while (khi-klo > 1){
    k=(khi+klo) >> 1;
    if (x2a[k] > x2) khi=k;
    else klo=k;
  }
  double t,u,*y,*y1,*y2,*y12,value;
  y=tools::dvector(1,4);y1=tools::dvector(1,4);
  y2=tools::dvector(1,4);y12=tools::dvector(1,4);
  y[1]=ya[jlo][klo];y[2]=ya[jhi][klo];y[3]=ya[jhi][khi];y[4]=ya[jlo][khi];
  y1[1]=y1a[jlo][klo];y1[2]=y1a[jhi][klo];
  y1[3]=y1a[jhi][khi];y1[4]=y1a[jlo][khi];
  y2[1]=y2a[jlo][klo];y2[2]=y2a[jhi][klo];
  y2[3]=y2a[jhi][khi];y2[4]=y2a[jlo][khi];
  y12[1]=y12a[jlo][klo];y12[2]=y12a[jhi][klo];
  y12[3]=y12a[jhi][khi];y12[4]=y12a[jlo][khi];
  double d1,d2,**c;
  double ca1=x1a[jhi],ca2=x1a[jlo],ca3=x2a[khi],ca4=x2a[klo];
  c=tools::dmatrix(1,4,1,4); d1=(x1a[jhi]-x1a[jlo]);d2=(x2a[khi]-x2a[klo]);
  bcubic_coef(y,y1,y2,y12,d1,d2,c);
  if (x1a[jhi] == x1a[jlo] || x2a[khi] == x2a[klo])
    error((char *)"Bad input in routine spline_web::bcubic_interp");
  t=(x1-x1a[jlo])/d1;
  u=(x2-x2a[klo])/d2;
  value=(*ansy2)=(*ansy1)=0.0;
  for (int i=4;i>=1;i--) {
    value=t*(value)+((c[i][4]*u+c[i][3])*u+c[i][2])*u+c[i][1];
    *ansy2=t*(*ansy2)+(3.0*c[i][4]*u+2.0*c[i][3])*u+c[i][2];
    *ansy1=u*(*ansy1)+(3.0*c[4][i]*t+2.0*c[3][i])*t+c[2][i];
  }
  *ansy1 /= d1;
  *ansy2 /= d2;
  tools::free_dmatrix(c,1,4,1,4);
  tools::free_dvector(y,1,4);tools::free_dvector(y1,1,4);
  tools::free_dvector(y2,1,4);tools::free_dvector(y12,1,4);
  return value;
}



