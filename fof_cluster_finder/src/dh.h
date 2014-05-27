#ifndef DH_HPP
#define DH_HPP

#ifdef __cplusplus
extern "C" {
#endif


  double angdidis(double z,double OmegaM,double OmegaL);
  double angdidis2(double z1,double z2,double OmegaM,double OmegaL);
  double comdis(double z,double OmegaM,double OmegaL);
  double comvol(double z,double OmegaM,double OmegaL);
  double dcomdisdz(double z,double OmegaM,double OmegaL);
  double dcomvoldz(double z,double OmegaM,double OmegaL);
  double dlookbackdz(double z,double OmegaM,double OmegaL);
  double doptdepthdz(double z,double OmegaM,double OmegaL);
  double dpropmotdisdz(double z,double OmegaM,double OmegaL);
  double intcomvol(double z,double OmegaM,double OmegaL);
  double lookback(double z,double OmegaM,double OmegaL);
  double lumdis(double z,double OmegaM,double OmegaL);
  double optdepth(double z,double OmegaM,double OmegaL);
  double propmotdis(double z,double OmegaM,double OmegaL);

#ifdef __cplusplus
}
#endif
#endif
