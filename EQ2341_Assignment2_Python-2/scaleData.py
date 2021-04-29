# Scales the data down by normalizing based on greatest distance between two points




import numpy as np
from maxDist import *
#from scipy.spatial import ConvexHull
#from scipy.spatial.distance import cdist

def scaleData(data):
    
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

    #### LEGACY
    # Find max points and indexes
    x_max = np.nanmax(data[0])
    i_xmax = np.where(data[0] == x_max)[0]  # [0] to go from tuple to np.array
    x_min = np.nanmin(data[0])
    i_xmin = np.where(data[0] == x_min)[0]
    
    y_max = np.nanmax(data[1])
    i_ymax = np.where(data[1] == y_max)[0]
    y_min = np.nanmin(data[1])
    i_ymin = np.where(data[1] == y_min)[0]
    
    print("X max and min points:", x_max, x_min,". Y max and min points:", y_max, y_min)
    # Compute greatest distance
    
    # Trying out this solution but does not give good results yet
    max_dist = maxDist(data)
    print("Maximum distance:", max_dist)
    
    # Accoding to StackOverflow (but in 3D! Does not work here...)
    """
    # N = 16000000
    # Find a convex hull in O(N log N)
    # points = np.random.rand(N, 3)   # N random points in 3-D

    points = data
    # Returned 420 points in testing
    hull = ConvexHull(points)

    # Extract the points forming the hull
    hullpoints = points[hull.vertices,:]

    # Naive way of finding the best pair in O(H^2) time if H is number of points on
    # hull
    hdist = cdist(hullpoints, hullpoints, metric='euclidean')

    # Get the farthest apart points
    bestpair = np.unravel_index(hdist.argmax(), hdist.shape)

    #Print them

    print([hullpoints[bestpair[0]],hullpoints[bestpair[1]]])
    """

    # Scale data:

    #   Upscale or downscale?
    #   Discrete or continous in the end?
    return data
