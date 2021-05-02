from tkinter import *
import numpy as np
import time 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

<<<<<<< HEAD
# from DrawCharacter import DrawCharacter
# from start_end_definer import *
# from strokeDivider import *
# from relativeDistance import *
# from dist_and_slope import *
# from sampler import *
# from norm_dist_slope import *
from CharacterFeatureExtractor import *
=======
from DrawCharacter import DrawCharacter
from start_end_definer import *
from strokeDivider import *
from relativeDistance import *
from dist_and_slope import *
>>>>>>> afa820fab537fb97b77ec1d84fca43f34a835fef




#NEW TEST!!!!!!!!
#Get symbol-1
dc1 = DrawCharacter()
dc1.run()
#Get symbol-2
dc2 = DrawCharacter()
dc2.run()
#Cleaning of symbol-1 data from b=0
get1 = dc1.get_xybpoints()
get1_clean = start_end_definer(get1)
#Cleaning of symbol-2 data from b=0
get2 = dc2.get_xybpoints()
get2_clean = start_end_definer(get2)

#strokes are returned as a list
org_stroke_list1 = strokeDivider(get1_clean)
org_stroke_list2 = strokeDivider(get2_clean)

<<<<<<< HEAD
=======
#strokes are combined and relative distances are calculated
# stroke_dist1 = relativeDistance(stroke_list1)
# stroke_dist2 = relativeDistance(stroke_list2)

stroke_dist1 = dist_and_slope(stroke_list1[0])
stroke_dist2 = dist_and_slope(stroke_list2[0])

# stroke_dist1 = dist_and_slope(np.concatenate(stroke_list1,axis = 1) )
# stroke_dist2 = dist_and_slope(np.concatenate(stroke_list2,axis = 1) )
>>>>>>> afa820fab537fb97b77ec1d84fca43f34a835fef

thr = 9 # threshold for sampling and distance normalization



# #Feature vectors are returned
feature_symbol1, sampled_symbol1 = featureExtractor(dc1,thr)
feature_symbol2, sampled_symbol2 = featureExtractor(dc2,thr)



# normalized distance ,slope, and t for symbol-1
f1_symbol1 = feature_symbol1[0]
f2_symbol1 = feature_symbol1[1]
t1 = np.array(range(0,feature_symbol1.shape[1]))



# normalized distance ,slope, and t for symbol-2
f1_symbol2 = feature_symbol2[0]
f2_symbol2 = feature_symbol2[1]
t2 = np.array(range(0,feature_symbol2.shape[1]))

# combined pixel values of all strokes for original symbol-1
comb_stroke_list1 = np.concatenate(org_stroke_list1,axis = 1)
# combined pixel values of all strokes for original symbol-2
comb_stroke_list2 = np.concatenate(org_stroke_list2,axis = 1)



f, axarr = plt.subplots(4, 2)
f.suptitle('Character Check', fontsize=20)

#Drawing of original symbol-1
axarr[0, 0].scatter(comb_stroke_list1[0], comb_stroke_list1[1])
axarr[0, 0].set_title('Symbol-1')
axarr[0, 0].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
axarr[0, 0].set_xlim([0,210])
axarr[0, 0].set_ylim([0,210])

#Drawing of original symbol-2
axarr[0, 1].scatter(comb_stroke_list2[0], comb_stroke_list2[1])
axarr[0, 1].set_title('Symbol-2')
axarr[0, 1].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
axarr[0, 1].set_xlim([0,210])
axarr[0, 1].set_ylim([0,210])




#Drawing of sampled symbol-1
axarr[1, 0].scatter(sampled_symbol1[0], sampled_symbol1[1])
axarr[1, 0].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
axarr[1, 0].set_xlim([0,210])
axarr[1, 0].set_ylim([0,210])

#Drawing of sampled symbol-2
axarr[1, 1].scatter(sampled_symbol2[0], sampled_symbol2[1])
axarr[1, 1].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
axarr[1, 1].set_xlim([0,210])
axarr[1, 1].set_ylim([0,210])

#Absolute distance plot of symbol-1
axarr[2, 0].plot(t1, f1_symbol1)
axarr[2, 0].set(xlabel = "Time", ylabel = "Normalized Distance")
axarr[2, 0].set_ylim([0,np.max(f1_symbol1)])


#Absolute distance plot of symbol-2
axarr[2, 1].plot(t2, f1_symbol2)
axarr[2, 1].set(xlabel = "Time", ylabel = "Normalized Distance")
axarr[2, 1].set_ylim([0,np.max(f1_symbol2)])

#Slope(Degree) plot of symbol-1
axarr[3, 0].plot(t1, f2_symbol1)
axarr[3, 0].set(xlabel = "Time", ylabel = "Slope(Degrees)")
axarr[3, 0].set_ylim([-120,120])

#Slope(Degree) plot of symbol-2
axarr[3, 1].plot(t2, f2_symbol2)
axarr[3, 1].set(xlabel = "Time", ylabel = "Slope(Degrees)")
axarr[3, 1].set_ylim([-120,120])

plt.show()












