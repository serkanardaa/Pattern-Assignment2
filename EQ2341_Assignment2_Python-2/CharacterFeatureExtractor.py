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

    data_clean = start_end_definer(data)
    strokes = strokeDivider(data)  # TODO divides the data into strokes
    scale = 200
    strokes = scaleData(strokes,scale)  # TODO: remove or interpolate datapoints in the middle of strokes.
    strokes = relativeDistance(strokes)  # TODO converts the data to relative distances

    feature_vector = strokes  # are we done here?
    """ Old workflow
    data = removeZero(data)  # removes all b = 0 from data
    print(data)
    data = centerData(data)  # centers the data to make it start invariant
    print(data)
    data = resizeData(data)  # scale all data to same size patterns
    print(data)
    """
    return feature_vector