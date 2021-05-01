# Hello world!

# Hello world!

from DrawCharacter import *
from start_end_definer import *
from removeZero import *
from centerData import *
from scaleData import *

# Input: 
#   self.data (3,L) matrix from DrawCharacter
#       has values 0-200 in row 1,2 and binary row 3
# Output: K dimensional feature vector
# Functionality:
#   1. Divide into strokes 
#   2. Cleans self.data from all b = 0
#   2. Centers the start position
#   3. Scales the self.data to the same size TODO


# Clean self.data from leading and trailing b = 0

class CharacterFeatureExtractor:
    def __init__(self,data):
        self.data = self.data 

    def extract(self):
        data_clean = self.start_end_definer(self.data)
        strokes = strokeDivider(data_clean)  # TODO divides the self.data into strokes
        scale = 200
        strokes = scaleData(strokes,scale)  # TODO: remove or interpolate datapoints in the middle of strokes.
        strokes = relativeDistance(strokes)  # TODO converts the self.data to relative distances

        feature_vector = strokes  # are we done here?
        """ Old workflow
        self.data = removeZero(self.data)  # removes all b = 0 from self.data
        print(self.data)
        self.data = centerData(self.data)  # centers the self.data to make it start invariant
        print(self.data)
        self.data = resizeData(self.data)  # scale all self.data to same size patterns
        print(self.data)
        """
        return feature_vector
    
    def start_end_definer(self):
        b_values = self.data[2,:]
        indices = np.where(b_values==1)
        indices_array = indices[0]
        start = indices_array[0]
        end = indices_array[-1]
        print("starts at: " + str(start) + " and ends at: " + str(end))
        output = self.data[:,start:end + 1]
        return output

    def strokeDivider(self):
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