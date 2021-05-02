from tkinter import *
import numpy as np
import time 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from CharacterFeatureExtractor import *

#CASE FOR SHOWING THE EFFECT OF SAMPLING
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

#defined new strokes lists to input to sampler so that we can compare with original wones
stroke_list1 = org_stroke_list1 
stroke_list2 = org_stroke_list2

thr = 9 # threshold for sampling and distance normalization

# combined pixel values of all strokes for original symbols
comb_stroke_list1 = np.concatenate(org_stroke_list1,axis = 1)
comb_stroke_list2 = np.concatenate(org_stroke_list2,axis = 1)

#sampled versions of symbols
sampled_symbol1 = sampler(stroke_list1, thr)
sampled_symbol2 = sampler(stroke_list2, thr)


f, axarr = plt.subplots(2, 2)
f.suptitle('Sampling Effect', fontsize=20)

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