/*Class of cosmology functions*/

#include <cmath>
#include <limits>
#include "cosmo.hpp"
#include "exceptions.hpp"

#define TINY     (1.0e-16)
#define MINSTEP  (0.01)

void Cosmo::set_up(double OmegaM_val, double OmegaL_val) {
  if (OmegaM_val < 0 || OmegaM_val > 1.0)
    throw BadArgumentException("Cosmo::set_up", "OmegaM_val", "in the range 0.0 <= OmegaM_val <= 1.0");
  if (OmegaL_val < 0 || OmegaL_val > 1.0)
    throw BadArgumentException("Cosmo::set_up", "OmegaL_val", "in the range 0.0 <= OmegaL_val <= 1.0");
  if (std::abs(1.0 - OmegaM_val - OmegaL_val) > std::numeric_limits<double>::epsilon()) 
    throw DomainException("Cosmo::set_up", "OmegaM_val and OmegaL_val must sum to 1.0");
  OmegaM = OmegaM_val;
  OmegaL = OmegaL_val;
}

/* ----------------------------------------------------------------------------
   angdidis
-------------------------------------------------------------------------------
   This function calculates the angular diameter distance d_A as a
   function of z, Omega_M and Omega_L in a matter-dominated universe,
   using the function propmotdis().  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::angdidis(double z) {
  return propmotdis(z) / (1.0 + z) ;
}

/* ----------------------------------------------------------------------------
   angdidis2
-------------------------------------------------------------------------------
   This function calculates the angular diameter distance d_A from z1
   to z2 as a function of Omega_M and Omega_L in a matter-dominated
   universe, using the function propmotdis().  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::angdidis2(double z1, double z2) {
  if (z2 <= z1)
    throw BadArgumentException("Cosmo::angdidis2", "z2", "> z1");
  double y1, y2, y12, OmegaR;
  OmegaR = 1.0 - OmegaM - OmegaL;
  if(OmegaR <- TINY) printf("WARNING: angdidis2() does not work at Omega_R<0!");
  y1 = propmotdis(z1);
  y2 = propmotdis(z2);
  y12 = y2*sqrt(1.0 + y1 * y1 * OmegaR) - y1 * sqrt(1.0 + y2 * y2 * OmegaR);
  return y12 / (1.0 + z2) ;
}

/* ----------------------------------------------------------------------------
   comdis
-------------------------------------------------------------------------------
   This function calculates the line-of-sight comoving distance d_C as
   a function of z, Omega_M and Omega_L in a matter-dominated
   universe, using dcomdisdz().  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::comdis(double z) {
  if (z < 0.0)
    throw BadArgumentException("Cosmo::comdis", "z", ">= 0.0");
  int nsteps;
  double dz, dC, zz;
  nsteps = ((int) (z / MINSTEP)) + 1;
  dz = z / ((double) nsteps) ;
  dC = 0.0 ;
  for(zz = 0.5 * dz; zz < z; zz += dz) dC += dz * dcomdisdz(zz);
  return dC ;
}

/* ----------------------------------------------------------------------------
   comvol
-------------------------------------------------------------------------------
   This function calculates the all-sky comoving volume V as a
   function of z, Omega_M and Omega_L in a matter-dominated universe.
   Formulae from Carrol, Press & Turner, 1992, and my own calculation.
---------------------------------------------------------------------------- */
double Cosmo::comvol(double z) {
  double V, dM, OmegaK, sqrtOmegaK;
  OmegaK = 1.0 - OmegaM - OmegaL;
  sqrtOmegaK = sqrt(fabs(OmegaK));
  dM = propmotdis(z);
  if(OmegaK < -TINY)
    V = (dM * sqrt(1.0 + OmegaK * dM * dM) - asin(dM * sqrtOmegaK) / sqrtOmegaK)
      / (2.0 * OmegaK);
  else if(OmegaK > TINY)
    V = (dM * sqrt(1.0 + OmegaK * dM * dM) - asinh(dM * sqrtOmegaK) / sqrtOmegaK)
      / (2.0 * OmegaK);
  else
    V = dM * dM * dM / 3.0;
  return 4.0 * M_PI * V;
}

/* ----------------------------------------------------------------------------
   dcomdisdz
-------------------------------------------------------------------------------
   This function calculates the differential line-of-sight comoving
   distance dD_c/dz as a function of z, Omega_M and Omega_L in a
   matter-dominated universe.  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::dcomdisdz(double z) {
  if (z < 0.0)
    throw BadArgumentException("Cosmo::dcomdisdz", "z", ">= 0.0");
  return (1.0 / sqrt((1.0 + z) * (1.0 + z) * (1.0 + OmegaM * z) - z *
		     (2.0 + z) * OmegaL));
}

/* ----------------------------------------------------------------------------
   dcomvoldz
-------------------------------------------------------------------------------
   This function calculates the one-steradian differential comoving
   volume dV/dz as a function of z, Omega_M and Omega_L in a
   matter-dominated universe.  Formulae from Carrol, Press & Turner,
   1992, Kolb & Turner, 1990, and my own calculation.  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::dcomvoldz(double z) {
  double dM, OmegaK, ddMdz;
  OmegaK = 1.0 - OmegaM - OmegaL;
  dM = propmotdis(z);
  ddMdz = dpropmotdisdz(z);
  return dM * dM * ddMdz / sqrt(1.0 + OmegaK * dM * dM);
}

/* ----------------------------------------------------------------------------
   dlookbackdz
-------------------------------------------------------------------------------
   This function calculates the change in lookback time dt/dz with
   redshift z as a function of z, Omega_M and Omega_L in a
   matter-dominated universe.  Formula from Carrol, Press & Turner,
   1992.  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::dlookbackdz(double z) {
  if (z < 0.0)
    throw BadArgumentException("Cosmo::dlookbackdz", "z", ">= 0.0");
  return 1.0 / ((1.0 + z) * sqrt((1.0 + z) * (1.0 + z) * (1.0 + OmegaM * z) - z * 
				 (2.0 + z) * OmegaL));
}

/* ----------------------------------------------------------------------------
   doptdepthdz
-------------------------------------------------------------------------------
   This function calculates the change in optical depth dtau/dz with
   redshift z as a function of z, Omega_M and Omega_L in a
   matter-dominated universe.  Formula from Peebles, 1993.
   H0=c=sigma=n=1.
---------------------------------------------------------------------------- */
double Cosmo::doptdepthdz(double z) {
  if (z < 0.0)
    throw BadArgumentException("Cosmo::doptdepthdz", "z", ">= 0.0");
  return (1.0 + z) * (1.0 + z) / sqrt((1.0 + z) * (1.0 + z) * (1.0 + OmegaM * z) - 
				      z * (2.0 + z) * OmegaL);
}

/* ----------------------------------------------------------------------------
   dpropmotdisdz
-------------------------------------------------------------------------------
   This function calculates the derivative of the proper motion
   distance d_M with respect to redshift z as a function of z, Omega_M
   and Omega_L in a matter-dominated universe.  Formula from Carrol,
   Press & Turner, 1992.  This function also requires the function
   propmotdis(). H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::dpropmotdisdz(double z) {
  double ddMdz, OmegaK, dM;
  ddMdz = 1.0 / sqrt((1.0 + z) * (1.0 + z) * (1.0 + OmegaM * z) - z *
		     (2.0 + z) * OmegaL);
  OmegaK = 1.0 - OmegaM - OmegaL;
  if(OmegaK < -TINY) {
    dM = propmotdis(z);
    ddMdz = sqrt(1.0 - OmegaK * dM * dM) * ddMdz;
  }
  else if(OmegaK > TINY) {
    dM = propmotdis(z);
    ddMdz = sqrt(1.0 + OmegaK * dM * dM) * ddMdz;
  }
  return ddMdz ;
}

/* ----------------------------------------------------------------------------
   intcomvol
-------------------------------------------------------------------------------
   This function calculates the all-sky comoving volume V as a
   function of z, Omega_M and Omega_L in a matter-dominated universe
   by integrating dcomvoldz().  It was written to test comvol().
---------------------------------------------------------------------------- */
double Cosmo::intcomvol(double z) {
  int nsteps;
  double dz, zz, V;
  nsteps = ((int) (z / MINSTEP)) + 1;
  dz = z / ((double) nsteps);
  V = 0.0;
  for(zz = 0.5 * dz; zz < z; zz += dz) V += dz * dcomvoldz(zz);
  return 4.0 * M_PI * V;
}

/* ----------------------------------------------------------------------------
   lookback
-------------------------------------------------------------------------------
   This function calculates the lookback time t(0)-t(z) as a function
   of z, OmegaM and OmegaL by integrating the output of dlookbackdz.
---------------------------------------------------------------------------- */
double Cosmo::lookback(double z) {
  int nsteps;
  double t, zz, dz;
  nsteps = ((int) (z / MINSTEP)) + 1;
  dz = z / ((double) nsteps);
  t = 0.0;
  for(zz = 0.5 * dz; zz < z; zz += dz) t += dlookbackdz(zz) * dz;
  return t;
}

/* ----------------------------------------------------------------------------
   lumdis
-------------------------------------------------------------------------------
   This function calculates the luminosity distance d_L as a function
   of z, Omega_M and Omega_L in a matter-dominated universe, using the
   function propmotdis().  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::lumdis(double z) {
  return propmotdis(z) * (1.0 + z);
}

/* ----------------------------------------------------------------------------
   optdepth
-------------------------------------------------------------------------------
   This function calculates the optical depth tau as a function
   of z, OmegaM and OmegaL by integrating the output of doptdepthdz.
   Again, H0=c=sigma=n=1.
---------------------------------------------------------------------------- */
double Cosmo::optdepth(double z) {
  int nsteps;
  double tau, zz, dz;
  nsteps = ((int) (z / MINSTEP)) + 1;
  dz = z / ((double) nsteps);
  tau = 0.0;
  for(zz = 0.5 * dz; zz < z; zz += dz) tau += doptdepthdz(zz) * dz;
  return tau;
}

/* ----------------------------------------------------------------------------
   propmotdis
-------------------------------------------------------------------------------
   This function calculates the proper motion distance d_M as a
   function of z, Omega_M and Omega_L in a matter-dominated universe.
   Formulae from Carrol, Press & Turner, 1992, Kolb \& Turner, 1990,
   and my own derivation.  Makes use of comdis().  H0=c=1.
---------------------------------------------------------------------------- */
double Cosmo::propmotdis(double z) {
  if (z < 0.0)
    throw BadArgumentException("Cosmo::propmotdis", "z", ">= 0.0");
  double dM, q0, OmegaK, sqrtOmegaK;
  if(fabs(OmegaM) < TINY && fabs(OmegaL) < TINY) {
    dM = (z + 0.5 * z * z) / (1.0 + z);
  }
  else if(fabs(OmegaL) < TINY) {
    q0 = 0.5 * OmegaM;
    dM = (z * q0 + (q0 - 1.0) * (sqrt(2.0 * q0 * z + 1.0) - 1.0)) / (q0 * q0 * (1.0 + z));
  }
  else {
    dM = comdis(z);
    OmegaK = 1.0 - OmegaM - OmegaL;
    sqrtOmegaK = sqrt(fabs(OmegaK));
    if(OmegaK < -TINY) dM = sin(sqrtOmegaK * dM) / sqrtOmegaK;
    else if(OmegaK > TINY) dM = sinh(sqrtOmegaK * dM) / sqrtOmegaK;
  }
  return dM;
}
