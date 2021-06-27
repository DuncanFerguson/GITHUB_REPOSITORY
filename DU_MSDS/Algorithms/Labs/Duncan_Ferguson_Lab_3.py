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
    while not isPrime(num):
        num = int(2 ** n * random.random())
    return num


def factor(pq):
    """ Factoring out Pq"""
    for i in range(2,pq,1):
        if (pq % i) == 0 and isPrime(i) and isPrime(int(pq/i)):
            p = i
            q = pq/p
            return(p,q)

bit = 8
p = nBitPrime(bit)
q = nBitPrime(bit)
print("P", p)
print("Q", q)


# pq = nBitPrime(bit) * nBitPrime(bit)
pq = p*q
print("pq",pq)
keys = factor(pq)
print("P", keys[0], "Q", keys[1])



#
# pq = nBitPrime(20) * nBitPrime(20)
