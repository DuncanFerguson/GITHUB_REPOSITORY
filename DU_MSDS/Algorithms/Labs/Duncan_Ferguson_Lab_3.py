# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 2
# Date 6/22/2021

import random

def isPrime(p):
    """This function takes a number, p, and returns true if it is prime and false otherwise"""
    if p > 1:
        for i in range(2,p,1):
            if (p % i) == 0:
                return False
            else:
                return True
    else:
        return False

def nBitPrime(n):
    """Creating a Random Prime Number n-bits long"""
    num = int(2**n * random.random())  # Random Number n bits long
    if num >= 2:
        if isPrime(num):
            return int(num)
        else:
            nBitPrime(n)
    else:
        nBitPrime(n)

def factor(pq):
    """ Factoring out Pq"""
    for i in range(2,pq,1):
        if (p % i) == 0:
            print("Prime!")

pq = nBitPrime(20) * nBitPrime(20)
print(pq)



#
# pq = nBitPrime(20) * nBitPrime(20)
