/**
 * @file galaxy_class.hpp
 *
 * @author Samuel Farrens
 */

#ifndef GALAXY_CLASS_H
#define GALAXY_CLASS_H

/**
 * @class Galaxy
 *
 * @brief Class for storing galaxy properties.
 *
 * This class calculates and stores Galaxy properties.
 */

#include <math.h>
#include <string>
#include "astro.hpp"
#include "cosmo.hpp"
#include "exceptions.hpp"
#include <iostream>

class UnionFind{
//DBG private:
public:
    UnionFind* parent;

public:
    UnionFind(): parent(nullptr){}
    UnionFind * find(){
        if (parent == nullptr)
            parent = this;
        if (parent != this)
            parent = parent->find();
  //      std::cout << "uf " << (long long) parent << std::endl;
        return parent;
    }

    void join(UnionFind* u){
        UnionFind* a = find();
        UnionFind* b = u->find();
        if(a != b)
            a->parent = b;
    }
    bool is_singlethon(){
        return parent == nullptr;
    }


};

class Galaxy { //! Class structure for galaxy properties

public:

    UnionFind uf;

    /// Number associated to Galaxy instance.
    int num;

    /// Zbin instance corresponding to Galaxy instance.
    int bin;

    /// coordinates of the Galaxy instance: the entries corresponds to Right ascension and Declination respectively
    Point P;

    /// Redshift of Galaxy instance.
    double z;

    /// Photometric redshift error of Galaxy instance.
    double dz;

    /// Angular diameter distance of Galaxy instance.
    double da;

    /// Velocity of Galaxy instance.
    double v;

    /// ID of Galaxy instance.
    unsigned long id;

    /// Vector of flags indicating if the Galaxy instance is a member
    /// of a Cluster instance for a given Zbin instance.
    std::vector<bool> in_cluster;

    /**
     * Initialise Galaxy instance. [FoF mode: "spec"]
     * @param[in] num_val Integer value.
     * @param[in] id_val Galaxy ID.
     * @param[in] ra_val Galaxy right ascension.
     * @param[in] dec_val Galaxy declination.
     * @param[in] z_val Galaxy spectroscopic redshift.
     */
    Galaxy(int num_val, unsigned long id_val, double ra_val, double dec_val,
            double z_val) {
        if (z_val < 0)
            throw BadArgumentException("Galaxy", "z_val", ">= 0.0");
        num = num_val;
        id = id_val;
        P.P[0] = ra_val;
        P.P[1] = dec_val;
        z = z_val;
        v = z / (1 + z);
        da = 0;
        bin = 0;
    };

    /**
     * Initialise Galaxy instance. [FoF mode: "phot"]
     * @param[in] num_val Integer value.
     * @param[in] id_val Galaxy ID.
     * @param[in] ra_val Galaxy right ascension.
     * @param[in] dec_val Galaxy declination.
     * @param[in] z_val Galaxy photometric redshift.
     * @param[in] dz_val Galaxy photometric redshift error.
     */
    Galaxy(int num_val,  unsigned long id_val, double ra_val, double dec_val,
            double z_val, double dz_val) {
        if (z_val <= 0)
            throw BadArgumentException("Galaxy", "z_val", "> 0.0");
        if (dz_val <= 0)
            throw BadArgumentException("Galaxy", "dz_val", "> 0.0");
        num = num_val;
        id = id_val;
        P.P[0] = ra_val;
        P.P[1] = dec_val;
        z = z_val;
        dz = dz_val;
        da = 0;
        bin = 0;
    };

    /**
     * This method calculates the angular diameter distance of a
     * Galaxy instance for a given cosmology.
     * @param[in] c Speed of light [km/s].
     * @param[in] H0 Hubble parameter [km/s/Mpc].
     * @param[in] Omega_M Matter density.
     * @param[in] Omega_L Dark energy density.
     */
    void assign_dist (double, double, double, double);

    /**
     * This method assigns the Zbin instance corresponding to
     * the Galaxy instance.
     * @param[in] min_value Minimum value in redshift range.
     * @param[in] bin_size Redshift bin size.
     */
    void assign_bin (double, double);

    /**
     * This method sets the initial Cluster instance membership
     * of the Galaxy instance to False.
     * @param[in] nbins Number of redshift bins.
     */
    void set_cluster_status (int);

    friend bool operator== (const Galaxy &gal1, const Galaxy &gal2);
    friend bool operator< (const Galaxy &gal1, const Galaxy &gal2);

private:

    /// Include Astro class.
    Astro astro;

    /// Include Cosmo class.
    Cosmo cosmo;

};

/**
 * Bool == operator for Galaxy class. Compares the ID between two Cluster 
 * instances.
 */
inline bool operator== (const Galaxy &gal1, const Galaxy &gal2) {
    return gal1.id == gal2.id;
}

/**
 * Bool < operator for Galaxy class. Compares the ID between two Cluster 
 * instances.
 */
inline bool operator< (const Galaxy& gal1, const Galaxy& gal2) {
    return gal1.id < gal2.id;
}

#endif // GALAXY_CLASS_H
