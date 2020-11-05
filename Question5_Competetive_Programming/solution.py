#!/usr/bin/env python

import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('/home/hk/Qualifiers/Question5_Competetive_Programming/points.csv', delimiter=',')
if my_data[63][1] == 1.0:
    print("A")
else :
    print("B")






