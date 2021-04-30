from tkinter import *
import numpy as np
import time 
from DrawCharacter import DrawCharacter
from start_end_definer import *
from strokeDivider import *
from relativeDistance import *




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

stroke_dist = relativeDistance(stroke_list)
stroke_dist, start_ends = relativeDistance(stroke_list,True)
print("stroke element distances")
print(stroke_dist)
print(start_ends)

#--------------- Normal Test Area

# array1 = np.array([[1,2,3],[3,4,5]])
# array2 = np.array([[3,4],[5,6]])
# array3 = np.array([[5,6],[7,9]])

# tuple_ar = (array1,array2,array3)
# list_ar = [array1,array2,array3]


# con = np.concatenate(list_ar,axis = 1)
# condif = np.diff(con)
# print(con)
# print(condif)
