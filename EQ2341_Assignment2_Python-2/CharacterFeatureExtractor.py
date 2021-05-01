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
#   1. Divide into strokes 
#   2. Cleans data from all b = 0
#   2. Centers the start position
#   3. Scales the data to the same size TODO


# Clean data from leading and trailing b = 0

def featureExtractor(data):
    L_total = data.shape[1]  # length of the input data
    
    strokes = strokeDivider(data)  # TODO divides the data into strokes
    strokes = relativeDistance(strokes)  # TODO converts the data to relative distances
    K = 300  # Variable for how long the end feature vector will be
    feature_vector = scaleData(strokes,K,scale)  # TODO: remove or interpolate datapoints in the middle of strokes.


    data = removeZero(data)  # removes all b = 0 from data
    print(data)
    data = centerData(data)  # centers the data to make it start invariant
    print(data)
    data = resizeData(data)  # scale all data to same size patterns
    print(data)
    return feature_vector



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
