from tkinter import *
import numpy as np
import time 

def start_end_definer(points):
    b_values = points[2,:]
    indices = np.where(b_values==1)
    indices_array = indices[0]
    start = indices_array[0]
    end = indices_array[-1]
    print("starts at: " + str(start) + " and ends at: " + str(end))
    output = points[:,start:end + 1]
    return output

