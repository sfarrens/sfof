#######################
# COSMOLOGY FUNCTIONS #
#######################

#Taken from David W. Hogg C routines.

import math

def angdidis(z, OmegaM, OmegaL):
    """
    This function calculates the angular diameter distance d_A as a
    function of z, Omega_M and Omega_L in a matter-dominated universe,
    using the function propmotdis().  H0=c=1
    """
    return propmotdis(z, OmegaM, OmegaL) / (1.0 + z)
    
def comdis(z, OmegaM, OmegaL):
    """
    This function calculates the line-of-sight comoving distance d_C as
    a function of z, Omega_M and Omega_L in a matter-dominated
    universe, using dcomdisdz().  H0=c=1.
    """
    dz = z / ((z / 0.01) + 1)
    x = 0.5 * dz
    dC = []
    while x < z:
        dC.append(dz * dcomdisdz(x, OmegaM, OmegaL))
        x += dz
    return sum(dC)

def dcomdisdz(z, OmegaM, OmegaL):
    """
    This function calculates the differential line-of-sight comoving
    distance dD_c/dz as a function of z, Omega_M and Omega_L in a
    matter-dominated universe.  H0=c=1.
    """
    return (1.0 / math.sqrt((1.0 + z) * (1.0 + z) * (1.0 + OmegaM * z) - z * (2.0 + z) * OmegaL))

def dcomvoldz(z, OmegaM, OmegaL):
    """
    This function calculates the one-steradian differential comoving
    volume dV/dz as a function of z, Omega_M and Omega_L in a
    matter-dominated universe.  Formulae from Carrol, Press & Turner,
    1992, Kolb & Turner, 1990, and my own calculation.  H0=c=1.
    """
    OmegaK = 1.0 - OmegaM - OmegaL
    dM = propmotdis(z, OmegaM, OmegaL)
    ddMdz = dpropmotdisdz(z, OmegaM, OmegaL)
    return dM ** 2 * ddMdz / math.sqrt(1.0 + OmegaK * dM ** 2)

def dpropmotdisdz(z, OmegaM, OmegaL):
    """
    This function calculates the derivative of the proper motion
    distance d_M with respect to redshift z as a function of z, Omega_M
    and Omega_L in a matter-dominated universe.  Formula from Carrol,
    Press & Turner, 1992.  This function also requires the function
    propmotdis(). H0=c=1.
    """
    ddMdz = 1.0 / math.sqrt((1.0 + z) ** 2 * (1.0 + OmegaM * z) - z * (2.0 + z) * OmegaL)
    OmegaK = 1.0 - OmegaM - OmegaL
    if OmegaK < 0:
        dM = propmotdis(z, OmegaM, OmegaL) ;
        ddMdz = math.sqrt(1.0 - OmegaK * dM ** 2) * ddMdz
    elif OmegaK > 0:
        dM = propmotdis(z, OmegaM, OmegaL) ;
        ddMdz = math.sqrt(1.0 + OmegaK *dM ** 2) * ddMdz
    return ddMdz

def propmotdis(z, OmegaM, OmegaL):
    """
    This function calculates the proper motion distance d_M as a
    function of z, Omega_M and Omega_L in a matter-dominated universe.
    Formulae from Carrol, Press & Turner, 1992, Kolb \& Turner, 1990,
    and Hogg derivation.  Makes use of comdis().  H0=c=1.
    """
    dM = comdis(z, OmegaM, OmegaL)
    OmegaK = 1.0 - OmegaM - OmegaL
    if OmegaK > 0: dM = math.sin(math.sqrt(OmegaK) * dM) / math.sqrt(OmegaK)
    elif OmegaK < 0: dM = math.sinh(math.sqrt(OmegaK) * dM) / math.sqrt(OmegaK)
    return dM
