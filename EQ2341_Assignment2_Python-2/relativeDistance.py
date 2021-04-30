from tkinter import *
import numpy as np
import time 

def relativeDistance(stroke_in, return_start_end = False):
    if isinstance(stroke_in, np.ndarray): # if the input is ndarray, the relative distance is directly calculated
        rel_dist = np.diff(stroke_in)
        return rel_dist
    elif type(stroke_in) == list: # case for the input is list
        if len(stroke_in) > 1: # if the list has multiple strokes
            comb_strokes = np.concatenate(stroke_in,axis = 1) #we concatenate strokes by column
            rel_dist = np.diff(comb_strokes)
            if return_start_end == True: #This parameter contains specifically the start-end point differences between strokes
                start_end_diff_list = []
                temp_index = -1 #starts from -1 because python inputs starts from 0
                for i in range(len(stroke_in) -1):
                    stroke = stroke_in[i]
                    stroke_len = stroke.shape[1]
                    temp_index = temp_index + stroke_len #step by step, the indices of distances between start-end points are found
                    start_end_diff = rel_dist[:,temp_index] #corresponding values for start-end point distance index is called
                    start_end_diff_list.append(start_end_diff) #each start-end point distance values are added to the list
                return rel_dist, start_end_diff_list #returns both the relative distance for combined strokes and specific start-end point distance values between strokes
            else:
                return rel_dist # if return_start_end is defined false( default is false) then return only relative distance for combined strokes
        elif len(stroke_in) == 1:
            return relativeDistance(stroke_in[0]) #if the input is list but it contains only 1 element, then calculate relative distance for contained array
        else:
            print("input is empty")
    
        


                
            
        
        