import numpy as np

# Centers data to the middle of a virtual palette 
#
# Input: data, in this case already cleaned from zeroes
# Output: centered_data, data which starts in the defined origin point of the virtual palette
#
# TODO Data an be less than 0! Solve how?

def centerData(data):
    L = data.shape[1]  # length of data
    width = 100  
    height = 100
    origin = np.array([width,height])  # defines the origin of the centered palette
    start_xy = np.array([data[0,0], data[1,0]])  # extracts start of data
    offset_xy = origin - start_xy  # offset used to center data
    offset_x = np.full(L,offset_xy[0])  # to make matrix addition possible
    offset_y = np.full(L,offset_xy[1])
    centered_data = data + np.array([offset_x, offset_y])
    return centered_data
    
