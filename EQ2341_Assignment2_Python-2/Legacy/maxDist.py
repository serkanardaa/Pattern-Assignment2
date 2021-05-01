from math import sqrt
 
# Function calculates distance
# between two points
# source: https://www.geeksforgeeks.org/maximum-distance-between-two-points-in-coordinate-plane-using-rotating-calipers-method/ 

# MODIFIED to take np.array.shape == (2,L)

# !!!!!!!OBS!!!!!! Gives very suspicious answers! Too low?? 
def dist(p1, p2):
     
    x0 = p1[0] - p2[0]
    y0 = p1[1] - p2[1]
    return x0 * x0 + y0 * y0
 
# Function to find the maximum
# distance between any two points
def maxDist(p):
 
    n = len(p[0])
    maxm = 0
 
    # Iterate over all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
             
            # Update maxm
            maxm = max(maxm, dist([p[0][i],p[1][i]], [p[0][j],p[1][j]]))
 
    # Return actual distance
    return sqrt(maxm)
