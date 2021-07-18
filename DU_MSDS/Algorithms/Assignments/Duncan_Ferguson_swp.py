# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 1
# Date 7/19/2021

from collections import deque
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
import numpy as np


""" This file takes in a file labeled edges. This file is a list of edges. From there
The test function calls load graph. This function loads the edges file and 
return an adjacency list representation of the corresponding undirected 
graph. This adjacency list is then used to run BFS(G,s) using a MyQueue, an returns a list
that contains the distance from s to every other vertex in the graph. The function
distanceDistribution(G) computes the distribution of all distances in G. All the code
is run through the test code. The resulting distribution is then printed in dictionary form
and also graphed. There is a final statement at the end explaining the extent to which this 
satisfies the small world phenomenon"""


class MyQueue(object):
    """ 3). Creating Queue Class. Enqueue enters an integer to the end of the queue.
    Dequeue removes the last item from the queue. Front wills show the front of the queue."""
    def __init__(self, type_var):
        self.elemType = type_var
        self.state = deque()  # This stores the queue

    def __str__(self):
        """Printing out the state as a string"""
        return str(self.state)

    def enqueue(self, elem):
        """Adding an element to the queue"""
        assert type(elem) == self.elemType
        self.state.append(elem)

    def dequeue(self):
        """Removing an element from the queue"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state.popleft()

    def empty(self):
        """True if queue is empty. False if not empty"""
        return len(self.state) == 0

    def front(self):
        """Returns the front of the queue. Which just so happens to be the last item on the list"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state[0]


def loadGraph(edgeFilename):
    """ 2). This function reads in the file of edge data. Note that edgeFileName is a strong storing
    the name of the edge data file.
    This function returns an adjacency list representation of the corresponding undirected graph
    A list of vertex Ids is not explicitly given but instead can be inferred from the edge data"""
    df = pd.read_csv(edgeFilename, sep=" ", header=None)  # Importing the txt file into a dataframe
    rows = df.values.tolist()  # Turning Dataframe into list of lists

    # Produces a dictionary with the node as a key and any nodes adjacency to it stored in the value list
    graph = dict()
    for row in range(len(rows)):
        if rows[row][0] not in graph.keys():
            graph[rows[row][0]] = [rows[row][1]]
        elif rows[row][0] in graph.keys():
            graph[rows[row][0]].append(rows[row][1])
        else:
            print("\n \n \n \n \n BREAK \n \n \n \n \n")  # Should never get to here

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

    # Convert to List of Lists to create an adjacency list
    adj_list = [sorted_dict[key] for key in sorted_dict]

    # print(adj_list)  # Uncomment to see the adjacency list
    return adj_list


def BFS(G, s):
    """ 4). Runs a breadth-first search (BFS) algorithm outlined in the Slides.
    It should run a BFS starting with source vertex s element of V.
    You should use your queue class implementation in the implementation of this function.
    Should return a list that contains the distance from s to every other vertex v in the graph.
    That is the distant Vertex 5 would be stored in slot 5 of the list.
    The graph will be passed using the adjacency list representation from step 2"""

    # print("Searching ", s)  # Printing out which s is being searched. Uncomment to see the code run
    q = MyQueue(int)  # Initializing the q
    q.enqueue(s)  # Setting the start value for the queue
    distances = {s: 0}  # adding the first value to the distance dict

    while not q.empty():  # While the queue is not empty
        vertex = q.dequeue()  # take the value from the front of the queue
        for neighbour in G[vertex]:  # For each neighbor to the node
            if neighbour not in distances.keys():  # Checking to see if a neighbour has already been added
                q.enqueue(neighbour)  # Add to the queue
                distances[neighbour] = distances[vertex] + 1  # adding a new distance plus 1

    # Making it come out like a list
    d_list = [value for key, value in sorted(distances.items())]

    # print(d_list)  # Prints out the Adjacency List
    return d_list


def distanceDistribution(G):
    """ 5). Computes the distribution of all distances in G.
     The function returns a dictionary that maps positive distances to frequency of occurances.
     Specifically, the frequencies should be stored in percentage form.
     That is, 24.4% of all distances are three apart. Note that this might take a few minutes to run.
     So you might want to print out values every once in a while to show progress"""

    # Using list comprehension to run through the each vertex in the Graph. Then using BFS(G,s)
    # To return the adjacency list for that vertex
    dmatrix = [BFS(G, row[0]) for row in enumerate(G)]

    # # The two lines below load the dmatrix into a csv. Use when wanting to work on graph or percentage distribution
    # df = pd.DataFrame(dmatrix)
    # loadlist = df.to_csv("Loadlist.csv", header=False, index=False)  # This was a lot faster to use for the graphs etc

    # Turning dmatrix into an array to easily find the unique numbers and their counts
    matrix = np.array(dmatrix)

    # Putting all the unique values into a dictionary and returning their counts
    unique, counts = np.unique(matrix, return_counts=True)
    frequency_dict = dict(zip(unique, counts))

    # Iterating over the dictionary and turning values into percentages
    s = sum(frequency_dict.values())
    for key, val in frequency_dict.items():
        frequency_dict[key] = val * 100.0 / s

    # print(frequency_dict)  # Uncomment to see the returned frequency dictionary
    return frequency_dict


def test():
    """Testing code that prints out the final distribution dictionary.
    You can uncomment graphit for either edges or edgesshort. This test codes also
    prints off the dictionary of the distrance distribution. There are two graphs that are included
    one is a bar chart. The other is a Pie graph just to give it another look."""
    graphit = loadGraph('edges.txt')  # Loading the file
    # graphit = loadGraph('edgesshort.txt')  # Loading the file
    distribution_dict = distanceDistribution(graphit)  # Sending off to gather the distribution dictionary
    print(distribution_dict)  # Printing the distribution dictionary

    # Turning Dictionary in Dataframe so that it's easier to map
    df_dist = pd.DataFrame(list(distribution_dict.items()), columns=["Distance", "Distribution Percentage '%'"])

    # Graphing with a barplot
    sns.set(style='whitegrid')
    sns.barplot(x="Distance", y="Distribution Percentage '%'",
                data=df_dist).set_title("Distribution of shortest path length")
    plt.show()

    # Graphing with a pie graph to help answer question 7. Uncomment below to see
    # labels, size = list(distribution_dict.keys()), list(distribution_dict.values())
    # explode = [0]*len(labels)
    # explode[6] = .05  # Exploding the 6th degree
    # explode = tuple(explode)
    # plt.pie(size, explode=explode, labels=labels, autopct='%.0f%%')
    # plt.title("Distribution of shortest path length")
    # plt.show()


def main():
    """Standard Main pointing to test queue"""
    test()


if __name__ == '__main__':
    main()

"""" 7). To what extent does this network satisfy the small world phenomenon? 
Please put a comment section at the bottom of your code that answer this question"""

# This network comes close to satisfying the small world phenomenon of exactly 6 degrees.
# There is a very small amount of nodes that are more than 6 degrees of separation away from themselves
# 7: 1.933757893222438, 8: 0.0957487963511985
# Meaning that not all people are 6 degrees apart from eachother. But there is a really high percentage of people that
# Are 6 or less degrees from each other.
# By looking at the distribution most people are actually located about 4 degrees of separation from each other
# 35.930685962889314 percentage of people are that many degrees away from eachother.
# In the example of Kevin Bacon, the saying is that there is 6 degrees of separation between him and
# Everyone else in hollywood makes some sense. Because it represents a smaller subset of people, like in edgeshort.
# To dive further into this question it would be interesting to look at which nodes have the most connections
# and determine if removing them changes the distribution. Essentially looking at the local clustering of nodes.
# The BFS algorithm lets us find this distribution rather fast so that we can conduct this analysis

