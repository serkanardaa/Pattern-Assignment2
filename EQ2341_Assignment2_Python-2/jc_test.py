from tkinter import *
import numpy as np
import time 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from DrawCharacter import DrawCharacter
from start_end_definer import *
from strokeDivider import *
from relativeDistance import *
from scaleData import *

def main():
    
    #Get symbol-1
    dc1 = DrawCharacter()
    dc1.run()
    #Get symbol-2
    dc2 = DrawCharacter()
    dc2.run()
    
    get1 = dc1.get_xybpoints()
    get2 = dc2.get_xybpoints()
    """
    
    get1 = np.load("small_o.npy")
    get2 = np.load("big_o.npy")
    """
    #Cleaning of symbol-1 data from b=0
    get1_clean = start_end_definer(get1)
    #Cleaning of symbol-2 data from b=0
    get2_clean = start_end_definer(get2)

    print(get1.shape)

    #strokes are returned as a list
    stroke_list1 = strokeDivider(get1_clean)
    stroke_list2 = strokeDivider(get2_clean)

    print(len(stroke_list1))

    print(stroke_list1[0].shape)

    
    scale = 200
    stroke_list1 = scaleData(stroke_list1, scale)
    stroke_list2 = scaleData(stroke_list2,scale)
    
    
    #strokes are combined and relative distances are calculated
    stroke_dist1 = relativeDistance(stroke_list1)
    stroke_dist2 = relativeDistance(stroke_list2)

    print(stroke_dist1.shape)

    # x-wise distance ,y-wise distance, and t for symbol-1
    t1 = np.array(range(0,stroke_dist1.shape[1]))
    x1 = stroke_dist1[0]
    y1 = stroke_dist1[1]
    # x-wise distance ,y-wise distance, and t for symbol-2
    t2 = np.array(range(0,stroke_dist2.shape[1]))
    x2 = stroke_dist2[0]
    y2 = stroke_dist2[1]
    # combined pixel values of all strokes for symbol-1
    comb_stroke_list1 = np.concatenate(stroke_list1,axis = 1)
    # combined pixel values of all strokes for symbol-2
    comb_stroke_list2 = np.concatenate(stroke_list2,axis = 1)



    f, axarr = plt.subplots(3, 2)
    f.suptitle('Character Check', fontsize=20)
    #Drawing of symbol-1
    axarr[0, 0].scatter(comb_stroke_list1[0], comb_stroke_list1[1])
    axarr[0, 0].set_title('Symbol-1')
    axarr[0, 0].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
    axarr[0, 0].set_xlim([0,210])
    axarr[0, 0].set_ylim([0,210])

    #Drawing of symbol-2
    axarr[0, 1].scatter(comb_stroke_list2[0], comb_stroke_list2[1])
    axarr[0, 1].set_title('Symbol-2')
    axarr[0, 1].set(xlabel = "X-Coordinate", ylabel = "Y-Coordinate")
    axarr[0, 1].set_xlim([0,210])
    axarr[0, 1].set_ylim([0,210])

    #X-wise distance plot of symbol-1
    axarr[1, 0].plot(t1, x1)
    #axarr[1, 0].set_title('Symbol-1 X-Wise Distance')
    axarr[1, 0].set(xlabel = "Time", ylabel = "X-wise distance")

    #X-wise distance plot of symbol-2
    axarr[1, 1].plot(t2, x2)
    #axarr[1, 1].set_title('Symbol-2 X-Wise Distance')
    axarr[1, 1].set(xlabel = "Time", ylabel = "X-wise distance")

    #Y-wise distance plot of symbol-1
    axarr[2, 0].plot(t1, y1)
    #axarr[2, 0].set_title('Symbol-1 Y-Wise Distance')
    axarr[2, 0].set(xlabel = "Time", ylabel = "Y-wise distance")

    #Y-wise distance plot of symbol-2
    axarr[2, 1].plot(t2, y2)
    #axarr[2, 1].set_title('Symbol-2 Y-Wise Distance')
    axarr[2, 1].set(xlabel = "Time", ylabel = "Y-wise distance")

    plt.show()


if __name__ == "__main__":
    main()
