# Hello world!

# Hello world!

from DrawCharacter import *


# Input: 
#   data (3,L) matrix from DrawCharacter
#       has values 0-200 in row 1,2 and binary row 3
# Output: K dimensional feature vector
# Functionality:
#   1. Cleans data from leading and trailing b=0
#   2. Normalizes the

# Clean data from leading and trailing b = 0
def cleanData(data):

    b_data = data[2,:]
    i = 0
    for d in data:
        if d = 1:
            start = i
        i+=1
        break

    b_data = b_data[start:]
    
    prev_1 = True
    i = 0
    for d in data:
        if d = 1:
            prev_1 = True
            end = i
        if d = 0 and prev_1:
            prev_1 = False
        i+=1

    # start: first b = 1
    # end: last b = 1
    # Remove all points before or after
    pass

def featureExtractor(data):
    print(data)
    L = data.shape[1]  # length of the input data
    

