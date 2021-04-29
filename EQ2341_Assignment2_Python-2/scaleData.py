# Scales the data down by normalizing based on greatest distance between two points


import numpy as np
from maxDist import *
#from scipy.spatial import ConvexHull
#from scipy.spatial.distance import cdist

def scaleData(strokes, size):
    
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

    # Scale data:

    #   Upscale or downscale?
    #   Discrete or continous in the end?
    return data
