import numpy as np
# Functions used
from DrawCharacter import *
from sampler import sampler
from norm_dist_slope import norm_dist_slope
from removeZero import removeZero

def featureExtractor(symbol,thr):
    xyb_values = symbol.get_xybpoints()
    xyb_cleaned = removeZero(xyb_values)
    sampled_symbol = sampler(xyb_cleaned, thr)
    feature_symbol = norm_dist_slope(sampled_symbol,thr)
    
    return feature_symbol, sampled_symbol
