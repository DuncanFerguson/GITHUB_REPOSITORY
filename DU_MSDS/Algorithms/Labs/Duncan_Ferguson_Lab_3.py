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
    """This is the second Function"""
    num = int(2**n * random.random())  # Random Number n bits long
    if isPrime(num) == True:
        print("Prime", num)
    else:
        nBitPrime(n)
    #
    # if num >= 2:
    #     print(num)
    # return




def factor(pq):
    """Som other Function"""
    return

    # if p == #TODO prime:
    #     return True
    # else:
    #     return False

print(isPrime(11))
nBitPrime(8)

# Polynomial Curve fit