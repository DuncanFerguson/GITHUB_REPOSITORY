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

def insertionSort(array):
    # print("insertion Sort" , L)
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array


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

    results.append([n,round(mtime,1), round(itime,1), round(btime,1)])

# Converting results to a dataframe and printing the results
panda = pd.DataFrame(results, columns=['N','Merge','Insert','Bubble'])
print(panda.to_string(index=False))

