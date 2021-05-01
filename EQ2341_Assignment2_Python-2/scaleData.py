# Scales the data down by normalizing based on greatest distance between two points


import numpy as np
from distCalc import totDist 
#from scipy.spatial import ConvexHull
#from scipy.spatial.distance import cdist
from centerData import centerData

def scaleData(strokes, scale):
    
    # Average distance normalization scaling
    #   1. Divide total amount of samples for each stroke proportionally
    #   2. Down/upsample each stroke to the defined length (interpolate for upsample?)
    #       - Remove the very close ones
    #       - Remove lower than average?
    #       - Interpolate?
    #   3. Calculate the average absolute distance in each stroke (ignoring start and end samples)
    #   4. (Redistributing the points s.t. they all lie on the average distance)
    #   5. Scale the average distance s.t. it is the same for all vectors
    #   6. Scaling start and end points s.t. the distance between them is the same for different size
    #   7. Collect the strokes with  in an array as the final feature vector
    
    
    # 1. Size division
    
    # 6. Scale start & end points:
    # Input: strokes list [(2,L1),(2,L2),...,(2,Ln)]  containing n strokes relative distances
    # Output: scale [int] which is a sum of all the distances in the stroke
    tot_d = 0
    for stroke in strokes:
        tot_d = tot_d + totDist(stroke)
    
    rescale = tot_d / scale

    for stroke in range(len(strokes)):
        strokes[stroke] = centerData(strokes[stroke])
        strokes[stroke] = strokes[stroke] / rescale
    return strokes


"""
        for j in range(strokes[stroke].shape[0]):
            strokes[stroke][j] = np.delete(strokes[stroke][j], np.where(strokes[stroke][j+1] - strokes[stroke][j] < threshold))
"""
