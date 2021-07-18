# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 1
# Date 7/19/2021

import pandas as pd
import queue
# import matplotlib.pyplot as plt
# from time import time
import numpy as np


class MyQueue(object):
    """ 3). Creating Queue Class. Enqueue enters an integer to the end of the queue.
     Dequeue removes the last item from the queue.
      Front wills show the front of the queue. Which just so happens to be the last item on the list."""
    def __init__(self, type_var):
        self.elemType = type_var
        self.state = []  # This stores the queue

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
    df = pd.read_csv(edgeFilename, sep=" ", header=None)  # Importing the txt file into a dataframe
    rows = df.values.tolist()  # Turning Dataframe into list of lists

    print(rows)
    # Produces a dictionary with the node and the adjacency of the lists next to it
    # TODO Maybe look at making this a bit quicker
    graph = dict()
    for row in range(len(rows)):
        if rows[row][0] not in graph.keys():
            graph[rows[row][0]] = [rows[row][1]]
        elif rows[row][0] in graph.keys():
            graph[rows[row][0]].append(rows[row][1])

    for row in range(len(rows)):
        if rows[row][1] not in graph.keys():
            graph[rows[row][1]] = [rows[row][0]]
        elif rows[row][1] in graph.keys():
            graph[rows[row][1]].append(rows[row][0])
        else:
            print("\n \n \n \n \n BREAK \n \n \n \n \n")  # Should never get to here

    # Sorting the Graph Dictionary
    sorted_dict = dict()
    for i in sorted(graph.keys()):
        sorted_dict[i] = sorted(graph[i])

    # Convert to List of Lists
    adj_list = []
    for key in sorted_dict:
        adj_list.append(sorted_dict[key])

    print(adj_list)
    return adj_list


def BFS(G, s):
    """ 4). Runs a breadth-first search (BFS) algorithm outlined in the Slides.
    It should run a BFS starting with source vertex s element of V.
    You should use your queue class implementation in the implementation of this function.
    Should return a list that contains the distance from s to every other vertex v in the graph.
    That is the distant Vertex 5 would be stored in slot 5 of the list.
    The graph will be passed using the adjacency list representation from step 2"""

    q = MyQueue(int)  # Initializing the q
    q.enqueue(s)  # Setting the start value for the queue
    distances = {s: 0}  # adding the first value to the distance dict
    # TODO write out the logic more
    while not q.empty():  # While the queue is not empty
        vertex = q.dequeue()
        for neighbour in G[vertex]:
            if neighbour not in distances.keys():
                q.enqueue(neighbour)
                distances[neighbour] = distances[vertex] + 1  # adding a new distance

    # Making it come out like a list
    d_list = []
    for key, value in sorted(distances.items()):
        d_list.append(value)

    print(d_list)
    return d_list


def distanceDistribution(G):
    """ 5). Computes the distribution of all distances in G.
     The function returns a dictionary that maps positive distances to frequency of occurances.
     Specifically, the frequencies should be stored in percentage form.
     That is, 24.4% of all distances are three apart. Note that this might take a few minutes to run.
     So you might want to print out values every once in a while to show progress"""

    dmatrix = []
    # total_time = 0

    for row in enumerate(G):
        # t1 = time()
        dmatrix.append(BFS(G, row[0]))
        # t2 = time()
        # running_time = t2-t1
        # total_time += running_time
        # print(row[0], " Line Run: ", running_time, "Total Run: ", total_time)
    # print(total_time)
    # df = pd.DataFrame(dmatrix)
    # loadlist = df.to_csv("Loadlist.csv", header=False, index=False)  # This was a lot faster to use for the graphs etc

    # TODO write out the logic, and double check
    # matrix = df.to_numpy()
    matrix = np.array(dmatrix)

    # Putting all the unique values into a dictionary and returning their counts
    unique, counts = np.unique(matrix, return_counts=True)
    frequency_dict = dict(zip(unique, counts))

    s = sum(frequency_dict.values())
    for k, v in frequency_dict.items():
        frequency_dict[k] = v * 100.0 / s
    print(frequency_dict)


def test():
    """Testing code that prints out the final distribution dictionary"""
    # graphit = loadGraph('edges.txt')
    graphit = loadGraph('edgesshort.txt')
    distanceDistribution(graphit)


def main():
    """Standard Main pointing to test queue"""
    test()


if __name__ == '__main__':
    main()

"""" 7). To what extent does this network satisfy the small world phenomenon? 
Please put a comment section at the bottom of your code that answer this question"""

# This makes sens in satisfying the small world phenomenon in that it looks at how far apart people are actually
# From each other. In the example of Kevin Bacon, the saying is that there is 6 degrees of separation.
# In this case we can see the percentage that people are x a mount of people away from each other.
# Kevin bacon would have to have a 100% of total people knowing him adding up through his 6th degree.
# Looking at the numbers here. People are actuall located X amount from each other.
# TODO CLEAN UP THIS ANSWER
