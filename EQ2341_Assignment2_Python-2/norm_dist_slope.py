import numpy as np

def norm_dist_slope(coordinates,thr):
# Calculates a metric for scale of the symbol which is used to normalize large distances between two samples.
# Adds the large distance to the remaining values.
# Calculates the polar coordinates (absolute distance and slope) of the input coordinates and adds random noise to avoid zero variance.
#  
# 
# Input:    coordinates         sampled data (2,L-removed_samples)
#           thr                 threshold used to downsample, used to calculate "large" distances
# 
# Output:   dist_slope          polar coordinates with distance increased at each large distance increment
   
    #Calculation of maximum distance in the symbol to get an idea about scale of it
    init_coor = coordinates[:,0]
    init_coor = init_coor.reshape((init_coor.size,1))
    origin_coor = coordinates-init_coor
    distances = np.sqrt(    np.square(origin_coor[0,:]) + np.square(origin_coor[1,:])    )
    max_dist = np.max(distances)
    
    #Finding the distance values between strokes ending and starting far from each other and normalizing them to make them similar for
    #different scaled similar symbols
    rel_dist = np.diff(coordinates)
    abs_dist = np.sqrt(    np.square(rel_dist[0,:]) + np.square(rel_dist[1,:])    )
    #if absolute distance between two points is higher than 2 times threshold ( which means there is certainly a jump between strokes) then normalize that distance value
    bigjump_indices = np.where(abs_dist > 2*thr)
    abs_dist[bigjump_indices] = (abs_dist[bigjump_indices] / max_dist) * 5 * thr
    
    #indices of distance values where we have big jumps between strokes
    bigjump_array = bigjump_indices[0]
    
    #when we have a jump in distance value, we keep that in the same level for remaining distance values coming after that and we apply it for each jumps
    for jump in bigjump_array:
        shift = abs_dist[jump] - abs_dist[jump - 1]
        remaining = jump + 1
        abs_dist[remaining:] += shift
        
    #setting data type to float for both distance vectors
    abs_dist = abs_dist.astype(float)
    rel_dist = rel_dist.astype(float)
    
    #we calculate the degrees for each slope between consecutive samples. For cases x = 0 we set x to 0.0001 so that y/x will bi divisible
    zerox_indices = np.where(rel_dist[0,:] == 0)
    rel_dist[0,zerox_indices] = 0.0001
    slope = np.divide(rel_dist[1,:] , rel_dist[0,:] )
    slope_inf_indices = np.where(np.absolute(slope) > 1000)
    slope_angle = np.arctan(slope)
    #we set the corresponding angle of the slopes where we were supposed to have infinite to 90 degrees
    slope_angle[slope_inf_indices] = np.deg2rad(90)
    
    #reshaping arrays for concatenating properly
    abs_dist = np.reshape(abs_dist,(1,abs_dist.size))
    slope_angle = np.reshape(slope_angle,(1,slope_angle.size))

    # converts radian values to degrees
    slope_angle = np.rad2deg(slope_angle)
    
    #adding random noise for not having 0 variance in features
    abs_dist = abs_dist + np.random.rand(1)/100 
    slope_angle = slope_angle + np.random.rand(1)/100
    #returns feature matrix of size (2 x number of samples -1)
    dist_slope = np.concatenate((abs_dist,slope_angle),axis=0)

    
    return dist_slope