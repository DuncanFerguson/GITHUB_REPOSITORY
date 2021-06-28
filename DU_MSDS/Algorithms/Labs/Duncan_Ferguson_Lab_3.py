# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 3
# Date 6/28/2021

import random
from time import time
import pandas as pd

def isPrime(p):
    """This function takes a number, p, and returns true if it is prime and false otherwise"""
    if p > 1:
        for i in range(2,int(p/2)+1):
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
            q, p = int(pq /i), int(i)
            if isPrime(q) and isPrime(p) and p * q == pq:
                return p,q


def time_n_loop():
    """ This records the amount of time it takes to break bits"""
    bit_list = []
    time_list = []
    for i in range(21):
        bit_list.append(i)
        p, q = nBitPrime(i), nBitPrime(i)
        print(p)
        # pq = int(p*q)
        t1 = time()
        # factor(pq)
        t2 = time()
        time_list.append((t2-t1))
    predictions = pd.DataFrame(zip(bit_list,time_list), columns=["Bits", "Time to Factor"])
    print(predictions)
time_n_loop()


# bit = 15
# p = nBitPrime(bit)
# q = nBitPrime(bit)
# print("P", p)
# print("Q", q)
# pq = int(p*q)
# print("PQ", pq)
#
# t1 = time()
# keys = factor(pq)
# t2 = time()
#
# print("P", keys[0],"Q",keys[1])
# print(t2-t1)