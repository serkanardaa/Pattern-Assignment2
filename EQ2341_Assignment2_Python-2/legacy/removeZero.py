# Removes all data points where b = 0 from data array
#
# Input: data from DrawCharacter (3,L) 
# Output clean_data (2,L-num_zero)
#
# By: Jonas Cederberg

import numpy as np

def removeZero(data):
    b = data[2,:]
    index_ones = b==1
    x = data[0,:][index_ones]
    y = data[1,:][index_ones]
    clean_data = np.array([x, y])
    return clean_data
