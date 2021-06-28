# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 3
# Date 6/28/2021

import random
from time import time
import pandas as pd


def isPrime(p):
    """This Function Checks if a number is prime. If the number is prime the function returns True
    Otherwise, if the number is not prime it returns false."""
    if p > 1:
        for i in range(2, p):
            if (p % i) == 0:
                return False
        else:
            return True
    else:
        return False


def nBitPrime(n):
    """This Function generates a random prime number that is up to n bits long"""
    num = int(random.random()*2**n)
    if num >= 2 and isPrime(num):
        return num
    else:
        return nBitPrime(n)


def factor(pq):
    """This Function finds the prime factors of pq"""
    p, q = 0, 0  # Creating holding values to get replaced
    for i in range(2, pq, 1):  # Starting at 2 because 1 is not a prime number
        if pq % i == 0:
            p = i
            break
    q = int(pq/p)
    return p, q


def timeit(n):
    """This Function looks at the amount of time it takes to factor"""
    bit_list = [i for i in range(2, n+1)]
    time_list = []
    for i in bit_list:
        pq = int(nBitPrime(i)*nBitPrime(i))
        t1 = time()
        factor(pq)
        t2 = time()
        time_list.append((t2-t1)*1000)
    time_panda = pd.DataFrame(zip(bit_list, time_list), columns=["Bits", "Time_2_Factor"])
    # print(time_panda.to_string(index=False))
    time_panda.to_csv("Time_Panda.csv", index=False)

bits = 30
time = timeit(bits)

# Excel Curve Fitter Equation y=9E-05e^0.6512x
# Time that it would take to crack 1024 bit key
# 3.5835E+285 in milliseconds or 1.1356E+275 Years