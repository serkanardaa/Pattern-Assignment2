from tkinter import *
import numpy as np
import time 
from DrawCharacter import *
from start_end_definer import *
from strokeDivider import *
from sampler import *
from norm_dist_slope import *


def featureExtractor(symbol,thr):
    xyb_values = symbol.get_xybpoints()
    xyb_cleaned = start_end_definer(xyb_values)
    stroke_list = strokeDivider(xyb_cleaned)
    sampled_symbol = sampler(stroke_list, thr)
    feature_symbol = norm_dist_slope(sampled_symbol,thr)
    
    return feature_symbol, sampled_symbol
