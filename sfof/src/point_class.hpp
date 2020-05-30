
#ifndef CLASS_POINT
#define CLASS_POINT

//#include "astro.hpp"

#define DIMENSIONS 2

extern int PERIODIC[DIMENSIONS];
extern double BoxSize[DIMENSIONS], BoxHalf[DIMENSIONS];

#define SETPERIODIC( D, L) {PERIODIC[(D)] = 1; BoxSize[(D)] = (L); BoxHalf[(D)] = (L)/2.0;}
#define PDISTANCE( mydist, D) ((!PERIODIC[D])? (mydist) : (((mydist) > BoxHalf[D])?( (mydist) - BoxSize[D] ) : ( ((mydist) < -BoxHalf[D])? ((mydist) + BoxSize[D]) : (mydist) ) ))
#define NOPERIODIC {for(int i = 0; i < DIMENSIONS; i++) PERIODIC[i] = 0;};



class Point {
public:
  double P[DIMENSIONS];

  double sqdistance(const Point& S)
  {
    if (this == &S)
      return 0;
    double sqdist = 0; 
    for(int i = 0; i < DIMENSIONS; i++)
      sqdist += (P[i] - S.P[i]) * (P[i] - S.P[i]);
    return sqdist;
  }

  double distance(const Point& S, int D)
  {
    if (this == &S)
      return 0;
    double dist = 0; 
    dist = P[D] - S.P[D];
    return dist;
  }

  double psqdistance(const Point& S)
  {
    if (this == &S)
      return 0;
    double dist, sqdist = 0; 
    for(int i = 0; i < DIMENSIONS; i++) {
      dist = PDISTANCE((P[i] - S.P[i]), i);
      sqdist += dist * dist;
    }
    return sqdist;
  }
  
  Point();
  Point(double, double);
  Point(double *);
  Point(const Point& );
  Point& operator=(const Point& );
  Point& operator-(const Point& );
  Point& operator+(const Point& );
  
};

inline Point::Point() {};

inline Point::Point(double S0, double S1) {
  P[0] = S0;
  P[1] = S1;
}

inline Point::Point(double *S) {
  for(int i = 0; i < DIMENSIONS; i++)
    P[i] = *(S+i);
}

inline Point::Point(const Point& S) {
  for(int i = 0; i < DIMENSIONS; i++)
    P[i] = S.P[i];
}

inline Point& Point::operator=(const Point& S) {
  if (this != &S)
    for(int i = 0; i < DIMENSIONS; i++)
      P[i] = S.P[i];
  return *this;
}

inline Point& Point::operator+(const Point& S) {
  if (this != &S)
    for(int i = 0; i < DIMENSIONS; i++)
      P[i] += S.P[i];
  return *this;
}

inline Point& Point::operator-(const Point& S) {
  if (this != &S)
    for(int i = 0; i < DIMENSIONS; i++)
      P[i] -= S.P[i];
  return *this;
}


#endif
