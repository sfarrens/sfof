##############################
# FILE INPUT/OUPUT FUNCTIONS #
##############################

import math
import numpy as np
from astropy.io import fits

def read_ascii(file):
    """
    Function reads an ASCII file and
    returns a numpy array of strings.
    """
    data = np.genfromtxt(file, unpack = True, dtype="S")
    return data

def read_fits(file):
    """
    Function reads a FITS file and
    returns a numpy array of strings.
    """
    fits_data = fits.open(file)[1].data    
    data = []
    for i in range(len(fits_data[0])):
        data.append(fits_data.field(i))
    data = np.array(data)
    return data
