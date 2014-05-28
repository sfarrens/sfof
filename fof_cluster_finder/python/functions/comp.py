###########################
# COMPUTATIONAL FUNCTIONS #
###########################

import numpy as np

def find_bin(value, min_value, bin_size):
    """
    Fine corresponding bin of a given value.
    """
    return np.floor(round((value - min_value) / bin_size, 8)).astype('int')

def num_bins(min_value, max_value, bin_size):
    """
    Find number of bins in given range for a given bin size.
    """
    return np.floor(round((max_value - min_value) / bin_size, 8)).astype('int')

def within(value, min_value, max_value):
    """
    Deterimine whether or not a values is within the
    limits provided.
    """
    return (value >= min_value and value < max_value)

def nan2one(array):
   """
   Convert nan values to 1.0
   """
   array[np.isnan(array)] = 1.0

def nan2zero(array):
   """
   Convert nan values to 1.0
   """
   array[np.isnan(array)] = 0.0

def sort_data(data,col):
   """
   Function that returns a numpy array sorted by a given column.
   """
   sorted_data = data[:,np.array(data[col,:],dtype='f').argsort()[::-1]]
   return sorted_data

def data_var(data, cols, types):
   """
   Function that returns specified variable arrays from data.
   """
   values = []
   for i in range(len(cols)):
      values.append(np.array(data[cols[i],:], dtype = types[i]))
   return np.array(values)
