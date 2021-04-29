from tkinter import *
import numpy as np
import time 
from DrawCharacter import DrawCharacter

dc = DrawCharacter()
dc.run()

get1 = dc.get_xybpoints()

print(get1[0,:])
print(get1[1,:])