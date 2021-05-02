from tkinter import *
import numpy as np
import time 

def dist_and_slope(coordinates):
    rel_dist = np.diff(coordinates)
    abs_dist = np.sqrt(    np.square(rel_dist[0,:]) + np.square(rel_dist[1,:])    )
    rel_dist = rel_dist.astype(float)
    zerox_indices = np.where(rel_dist[0,:] == 0)
    rel_dist[0,zerox_indices] = 0.0001
    slope = np.divide(rel_dist[1,:] , rel_dist[0,:] )
    slope_inf_indices = np.where(np.absolute(slope) > 1000)
    slope_angle = np.arctan(slope)
    slope_angle[slope_inf_indices] = np.deg2rad(90)
    
    abs_dist = np.reshape(abs_dist,(1,abs_dist.size))
    slope_angle = np.reshape(slope_angle,(1,slope_angle.size))

    # slope_angle = np.rad2deg(slope_angle)
    dist_slope = np.concatenate((abs_dist,slope_angle),axis=0)

    
    return dist_slope

    
    
# def dist_and_slope(coordinates):
#     init_coor = coordinates[:,0]
#     init_coor = init_coor.reshape((init_coor.size,1))
#     origin_coor = coordinates-init_coor
#     distances = np.sqrt(    np.square(origin_coor[0,:]) + np.square(origin_coor[1,:])    )
#     max_dist = np.max(distances)
    
#     start_point = origin_coor[:,0]
#     start_point = origin_coor[:,0].reshape((start_point.size,1))
    
#     end_point = origin_coor[:,-1]
#     end_point = origin_coor[:,-1].reshape((end_point.size,1))
    
#     comparison_points = origin_coor[:,0: origin_coor.shape[1] -1]
    
#     start_end_distances =  np.sqrt( np.square(comparison_points[0,:] - start_point[0]) + np.square(comparison_points[1,:] - start_point[1]) ) + \
#         np.sqrt( np.square(comparison_points[0,:] - end_point[0]) + np.square(comparison_points[1,:] - end_point[1]) )
        
#     start_end_distances /= max_dist
    
    
    
    
    
#     rel_dist = np.diff(coordinates)
#     rel_dist = rel_dist.astype(float)
#     zerox_indices = np.where(rel_dist[0,:] == 0)
#     rel_dist[0,zerox_indices] = 0.0001
#     slope = np.divide(rel_dist[1,:] , rel_dist[0,:] )
#     slope_inf_indices = np.where(np.absolute(slope) > 1000)
#     slope_angle = np.arctan(slope)
#     slope_angle[slope_inf_indices] = np.deg2rad(90)
    
#     start_end_distances = np.reshape(start_end_distances,(1,start_end_distances.size))
#     slope_angle = np.reshape(slope_angle,(1,slope_angle.size))

#     slope_angle = np.rad2deg(slope_angle)
#     dist_slope = np.concatenate((start_end_distances,slope_angle),axis=0)

    
#     return dist_slope