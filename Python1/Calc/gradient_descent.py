import math
import numpy as np

def vecLength(v):
    """"This Function is taking the... """
    tempSum =0.0
    for x in v:
        tempSum += x[0]**2
    print("Temp Sum = ", tempSum)
    return math.sqrt(tempSum)

def f( A, b, x, y):
    """ Label What this function is doing"""
    temp = np.matrix([[x],[y]])
    return np.matric(np.dot(a,)