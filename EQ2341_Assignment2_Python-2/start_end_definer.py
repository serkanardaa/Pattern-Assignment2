from tkinter import *
import numpy as np
import time 

def start_end_definer(points):
    #In this function we are removing samples where b=0 before the start of first stroke and after the end of last stroke
    b_values = points[2,:]
    indices = np.where(b_values==1)
    indices_array = indices[0]
    start = indices_array[0]
    end = indices_array[-1]
    output = points[:,start:end + 1]
    return output

