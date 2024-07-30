import numpy as np
import pandas as pd
f = open('C:/Users/Hanby/Documents/Python Scripts/hw1x.dat', mode='r')
X = []
line = None
while line != ' ':
    line = f.readline()
    X.append(line)
print("test")
print(X)
f.close()