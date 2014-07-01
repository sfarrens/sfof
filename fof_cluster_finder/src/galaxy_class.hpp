/*Class header for Galaxy*/

#ifndef GALAXY_CLASS_H
#define GALAXY_CLASS_H

#include <string>
#include "astro.hpp"

class Galaxy { //! Class structure for galaxy properties
private:
    Astro astro;
public:
    int num, bin;
    double ra, dec, z, dz, da, v;
    unsigned long id;
    std::vector<bool> in_cluster;
    Galaxy(int num_val, unsigned long id_val, double ra_val, double dec_val,
            double z_val) {
        /**< Initialise Galaxy instance in spec mode */
        num = num_val;
        id = id_val;
        ra = ra_val;
        dec = dec_val;
        z = z_val;
        v = z / (1 + z);
    };
    Galaxy(int num_val,  unsigned long id_val, double ra_val, double dec_val,
            double z_val, double dz_val) {
        /**< Initialise Galaxy instance in phot mode */
        num = num_val;
        id = id_val;
        ra = ra_val;
        dec = dec_val;
        z = z_val;
        dz = dz_val;
    };
    void assign_dist (double, double, double, double);
    void assign_bin (double, double);
    void set_cluster_status (int);
    friend bool operator== (const Galaxy &gal1, const Galaxy &gal2);
    friend bool operator< (const Galaxy &gal1, const Galaxy &gal2);
};

inline bool operator== (const Galaxy &gal1, const Galaxy &gal2) {
    //! Bool == operator for Galaxy class.
    return gal1.id == gal2.id;
}

inline bool operator< (const Galaxy& gal1, const Galaxy& gal2) {
    //! Bool < operator for Galaxy class.
    return gal1.id < gal2.id;
}

#endif /* GALAXY_CLASS_H */
