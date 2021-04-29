from tkinter import *
import numpy as np
import time 

def strokeDivider(data):
    b_values = data[2,:] #Extracts only be values
    indices_list = [] # each element of this list will include indices of a stroke separated from indices of other strokes
    stroke_list  = [] #each element of this list will include exactly the strokes separately which were in the input data
    
    indices = np.where(b_values==1) #Indices of b values where b = 1
    indices_array = indices[0] #indices was a tuple so we get the first element which is the array of indices
    
    diff_indices = np.diff(indices_array) # calculates the difference between each consecutive index
    
    j_indices = np.where(diff_indices != 1) # Getting the indices of positions where there is a jump which means diff != 1
    j_indices_array = j_indices[0] #array conversion as we did in indices_array
    if len(j_indices_array) == 0:
        stroke = data[:,indices_array]
        stroke_list.append(stroke[0:2,:])  # adds x,y and removes b
        return stroke_list
    else:
        for i in range(len(j_indices_array)):
            if i == 0: #indices for first stroke 
                stroke_index = indices_array[0:j_indices_array[i] + 1]
                indices_list.append(stroke_index)
            else: #indices for strokes in the middle
                stroke_index = indices_array[j_indices_array[i-1] + 1 : j_indices_array[i] + 1]
                indices_list.append(stroke_index)
            if i == len(j_indices_array) - 1: #indices for last stroke
                last_stroke_index = indices_array[j_indices_array[i] + 1:]
                indices_list.append(last_stroke_index)
        
        for s_i in range(len(indices_list)):
            stroke = data[:,indices_list[s_i]] # getting the stroke values by using indices of each corresponding stroke
            stroke_list.append(stroke[0:2,:])  # adds x,y and removes b
            
        return stroke_list
    
    
    
    
