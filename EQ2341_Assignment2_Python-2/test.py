from tkinter import *
import numpy as np
import time 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from DrawCharacter import DrawCharacter
from start_end_definer import *
from strokeDivider import *
from relativeDistance import *



def strokeTest():
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

def main():
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
    stroke_list1 = strokeDivider(get1_clean)
    stroke_list2 = strokeDivider(get2_clean)

    #strokes are combined and relative distances are calculated
    stroke_dist1 = relativeDistance(stroke_list1)
    stroke_dist2 = relativeDistance(stroke_list2)



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
