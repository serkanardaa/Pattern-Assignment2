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

    slope_angle = np.rad2deg(slope_angle)
    dist_slope = np.concatenate((abs_dist,slope_angle),axis=0)

    
    return dist_slope

    
    
    