# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 2
# Date 6/10/2021

from time import time
import random
import pandas as pd

def mergeSort(L):
    # print("Merge Sort", L)
    L.sort()
    return L

def insertionSort(L):
    # print("insertion Sort" , L)
    x = 1123412349867*23452345234523452345234523
    return L


def bubbleSort(L):
    """Will have to code Bubble Sort"""
    """ ON A single Bubble pass, run through all the elements in your list from front to back.
    At each index you compare it's value to the next one
    https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
    """
    n = len(L)
    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]  # Swapping Values if it is greater
                already_sorted = False
        # the array is already sorted, and you can terminate
        if already_sorted:
            break
    return L


# Setting up increments
start = 100
stop = 5000000
increment = 100

# Columns Result table
results = []

# Setting up results table
for n in range(start,stop+1,increment):
    A = [i for i in range(n)]
    random.shuffle(A)

    # Merge Sort
    t1 = time()
    m_Sort = mergeSort(A)
    t2 = time()
    mtime = (t2-t1)*1000

    # insertion Sort
    t3 = time()
    m_Sort = insertionSort(A)
    t4 = time()
    itime = (t4-t3)*1000

    # Bubble Sort
    t5 = time()
    m_Sort = bubbleSort(A)
    t6 = time()
    btime = (t6-t5)*1000

    results.append([n,round(mtime,2), round(itime,2), round(btime,2)])

cols = ['N','Merge','Insert','Bubble']  # Setting Up columns for data frame
panda = pd.DataFrame(results, columns=cols)  # Changing the List into a dataframe
print(panda.to_string(index=False))

