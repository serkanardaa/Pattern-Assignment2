# Hello world!

# Hello world!

from DrawCharacter import *
from start_end_definer import *
from removeZero import *
from centerData import *
from scaleData import *

# Input: 
#   data (3,L) matrix from DrawCharacter
#       has values 0-200 in row 1,2 and binary row 3
# Output: K dimensional feature vector
# Functionality:
#   1. Cleans data from all b = 0
#   2. Centers the start position
#   3. Scales the data to the same size TODO


# Clean data from leading and trailing b = 0

def featureExtractor(data):
    L_total = data.shape[1]  # length of the input data
    data = removeZero(data)  # removes all b = 0 from data
    print(data)
    data = centerData(data)  # centers the data to make it start invariant
    print(data)
    data = scaleData(data)  # scale all data to same size patterns
    print(data)
    return data



# LEGACY FUNCTIONS

def cleanData_old(data):
    b_data = data[2,:]
    i = 0
    for d in data:
        if d == 1:
            start = i
        i+=1
        break
    b_data = b_data[start:]
    
    prev_1 = True
    i = 0
    for d in data:
        if d == 1:
            prev_1 = True
            end = i
        if d == 0 and prev_1:
            prev_1 = False
        i+=1

    # start: first b = 1
    # end: last b = 1
    # Remove all points before or after
    pass
