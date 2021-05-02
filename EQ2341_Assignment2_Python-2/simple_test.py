import numpy as np
import time 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from DrawCharacter import DrawCharacter
from legacy.removeZero import removeZero
from functions.start_end_definer import *
from functions.strokeDivider import *
from functions.relativeDistance import *
from functions.scaleData import *
from functions.dist_and_slope import *
from functions.centerData import centerData

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
    get1_clean = removeZero(get1)
    #Cleaning of symbol-2 data from b=0
    get2_clean = removeZero(get2)

    center_clean1 = centerData(get1_clean)
    center_clean2 = centerData(get2_clean)

    scale = 100
    feature_vector1 = scaleData(center_clean1, scale)
    feature_vector2 = scaleData(center_clean2, scale)

    stroke_dist1 = feature_vector1
    stroke_dist2 = feature_vector2

    print(stroke_dist1.shape)

    # x-wise distance ,y-wise distance, and t for symbol-1
    t1 = np.array(range(0,stroke_dist1.shape[1]))
    x1 = stroke_dist1[0]
    y1 = stroke_dist1[1]
    # x-wise distance ,y-wise distance, and t for symbol-2
    t2 = np.array(range(0,stroke_dist2.shape[1]))
    x2 = stroke_dist2[0]
    y2 = stroke_dist2[1]

    # Original drawing
    # combined pixel values of all strokes for symbol-1
    comb_stroke_list1 = get1_clean
    # combined pixel values of all strokes for symbol-2
    comb_stroke_list2 = get2_clean


    
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