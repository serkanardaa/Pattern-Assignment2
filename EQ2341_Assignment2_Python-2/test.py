from tkinter import *
import numpy as np
import time 
from DrawCharacter import DrawCharacter
from start_end_definer import *
from strokeDivider import *




#-------------- TEST FOR INPUT DRAWING
dc = DrawCharacter()
dc.run()

get1 = dc.get_xybpoints()

print(get1[2,:])

get1_clean = start_end_definer(get1)

print("start end definer result")
print(get1_clean)

stroke_list = strokeDivider(get1_clean)
print("stroke list elements")
print(stroke_list)

#--------------- Normal Test Area
# array1 = np.array([1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1])

# indices = np.where(array1==1)

# indices_array = indices[0]

# diff_indices = np.diff(indices_array)

# indices2 = np.where(diff_indices != 1)

# indices_array2 = indices2[0]


# print(indices_array)
# print(diff_indices)
# print(indices_array2)

# indices_list = []

# for i in range(len(indices_array2)):
#     if i == 0:
#         stroke_index = indices_array[0:indices_array2[i] + 1]
#     else:
#         stroke_index = indices_array[indices_array2[i-1] + 1 : indices_array2[i] + 1]
#     indices_list.append(stroke_index)
#     if i == len(indices_array2) - 1:
#         last_stroke_index = indices_array[indices_array2[i] + 1:]
#         indices_list.append(last_stroke_index)
    
    
# print(indices_list)
        

# stroke_list  = []

# for s_i in range(len(indices_list)):
#     stroke = array1[indices_list[s_i]]
#     stroke_list.append(stroke)
    
# print(stroke_list)

