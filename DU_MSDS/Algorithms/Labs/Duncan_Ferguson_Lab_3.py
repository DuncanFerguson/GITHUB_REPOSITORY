# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 3
# Date 6/28/2021

import random
from time import time
import pandas as pd
import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

def isPrime(p):
    """This function takes a number, p, and returns true if it is prime and false otherwise"""
    if p > 1:
        for i in range(2, int(p/2)+1):
            if (p % i) == 0:
                return False
        else:
            return True
    else:
        return False


def nBitPrime(n):
    """Creating a Random Prime Number n-bits long"""
    num = int(2**n * random.random())  # Random Number n bits long
    while not isPrime(num):
        num = int(2 ** n * random.random())
    return num


def factor(pq):
    """Finding the Factors of PG"""
    for i in range(2, pq, 1):
        if isPrime(int(pq/i)) and (pq % i) == 0:
            q, p = int(pq / i), int(i)
            if isPrime(q) and isPrime(p) and p * q == pq:
                return p, q


bit_list = []
time_list = []
for i in range(7, 20, 1):
    print(i)
    bit_list.append(i)
    p, q = nBitPrime(i), nBitPrime(i)
    pq = int(p*q)
    t1 = time()
    factor(pq)
    t2 = time()
    time_list.append((t2-t1)*1000)
predictions = pd.DataFrame(zip(bit_list, time_list), columns=["Bits", "Time to Factor"])
print(predictions)
plt.plot(predictions['Bits'], predictions['Time to Factor'], 'b-', label='data')
plt.xlabel("Time to Factor")
plt.ylabel("Number of Bits")
plt.show()
predictions.to_csv("Predictions.csv")


