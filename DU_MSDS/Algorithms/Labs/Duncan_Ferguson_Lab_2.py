# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 2
# Date 6/22/2021

from time import time
import random
import pandas as pd

def merge(A,B):
    out = []
    I,J = 0,0
    while I < len(A) and J < len(B):
        if A[I] < B[J]:
            out.append(A[I])
            I += 1
        else:
            out.append(B[J])
            J += 1
    while I < len(A):
        out.append(A[I])
        I += 1
    while J < len(B):
        out.append(B[J])
        J += 1
    return out


def mergeSort(L):
    """ Merge Sort Taken from class notes"""
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)


def insertionSort(L):
    """Code Taken From Class Slides"""
    for i in range(len(L)):
        key = L[i]
        j = i-1
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = key
    return L


def bubbleSort(L):
    """ On A single Bubble pass, run through all the elements in your list from front to back.
    At each index you compare it's value to the next one
    """
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


# Setting up increments
start = 100
stop = 5000
increment = 100

# Columns Result table
results = []

# Setting up results table
for n in range(start,stop+1,increment):
    A = [i for i in range(n)]

    # Merge Sort
    random.shuffle(A)
    t1 = time()
    m_Sort = mergeSort(A)
    t2 = time()
    mtime = (t2-t1)*1000

    # insertion Sort
    random.shuffle(A)
    t3 = time()
    m_Sort = insertionSort(A)
    t4 = time()
    itime = (t4-t3)*1000

    # Bubble Sort
    random.shuffle(A)
    t5 = time()
    m_Sort = bubbleSort(A)
    t6 = time()
    btime = (t6-t5)*1000

    results.append([n, round(mtime, 1), round(itime, 1), round(btime, 1)])

# Converting results to a dataframe and printing the results
panda = pd.DataFrame(results, columns=['N', 'Merge', 'Insert', 'Bubble'])
print(panda.to_string(index=False))