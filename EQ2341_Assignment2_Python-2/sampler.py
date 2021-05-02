import numpy as np

def sampler(coordinates,thr):
# Removes all samples for which the distance from the previous point is less than a given threshold
#
# Input:    coordinates         clean data from DrawCharacter with only x,y (2,L)
#           thr                 lower threshold bound for distances when removing samples
#
# Output:   sampled_coordinates sampled data (2,L-removed_samples)      

    rel_dist = np.diff(coordinates)
    #calculating absolute distances between each sample
    abs_dist = np.sqrt(    np.square(rel_dist[0,:]) + np.square(rel_dist[1,:])    )
    #vector for indices of output samples. Starting with keeping the first sample
     rel_dist = np.diff(coordinates)
    #calculating absolute distances between each sample
    abs_dist = np.sqrt(    np.square(rel_dist[0,:]) + np.square(rel_dist[1,:])    )
    #vector for indices of output samples. Starting with keeping the first sample
    remain_sample_indices = [0]
    #keep the samples where their distances between each other is higher than the given threshold
    temp_dist = 0
    for i in range(abs_dist.size):
        temp_dist = temp_dist + abs_dist[i] 
        if temp_dist > thr:
            temp_dist = 0
            remain_sample_indices.append(i + 1)
    #getting x,y values of the samples for corresponding indices
    sampled_coordinates = coordinates[:,remain_sample_indices]
    return sampled_coordinates