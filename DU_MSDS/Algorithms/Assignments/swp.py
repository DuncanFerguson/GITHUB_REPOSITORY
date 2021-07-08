# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 1
# Date 7/19/2021

import pandas as pd

class MyQueue(object):
    """ 3). Creating Queue Class. Enqueue enters an integer to the end of the queue. Dequeue removes the last item from the
    queue. Front wills show the front of the queue. Which just so happens to be the last item on the list."""
    def __init__(self, type_var):
        self.elemType = type_var
        self.state = []

    def __str__(self):
        """Printing out the state as a string"""
        return str(self.state)

    def enqueue(self, elem):
        """Adding an element to the queue"""
        self.state.insert(0, elem)

    def dequeue(self):
        """Removing an element from the queue"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state.pop()

    def empty(self):
        """True if queue is empty. False if not empty"""
        return len(self.state) == 0

    def front(self):
        """Returns the front of the queue. Which just so happens to be the last item on the list"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state[-1]



def loadGraph(edgeFilename):
    """ 2). This function reads in the file of edge data.
     This function should return an adjacency list representation of the corresponding undirected graph
     A list of vertex Ids is not explicitly given but instead can be inferred from the edge data"""
    # https: // www.geeksforgeeks.org / graph - and -its - representations /
    df = pd.read_csv(edgeFilename, sep=" ", header=None)  # Importing the txt file into a dataframe
    print(df)

def main():
    """Standard Main pointing to test queue"""
    loadGraph('edges.txt')



if __name__ == '__main__':
    main()
