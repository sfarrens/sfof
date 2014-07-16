/*Class header for Zbin*/

#ifndef ZBIN_CLASS_H
#define ZBIN_CLASS_H

class Zbin { //! Class structure for redshift bin properties.
public:
  int num, count;
  double z, dz, da, dvdz, dndz, dndv, link_r, rfriend;
  Zbin(int num_val, double z_val, double z_bin_size) { 
    /**< Initialise Zbin instance. */
    num = num_val;
    z = z_val;
    dz = z_bin_size;
    count = 0;
  };
  void assign_dist (double, double, double, double);
  void assign_rfriend (double);
  void assign_fixed_rfriend (double);
};

#endif /* ZBIN_CLASS_H */
