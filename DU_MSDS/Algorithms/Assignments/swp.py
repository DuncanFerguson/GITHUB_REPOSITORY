# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Assignment 1
# Date 7/19/2021

import pandas as pd

"""Helpful Links
https://ide.geeksforgeeks.org/9je5j6jJ13
https://www.youtube.com/watch?v=CVq7puhdlFA
https://www.educative.io/edpresso/how-to-implement-a-graph-in-python
https://www.geeksforgeeks.org/graph-and-its-representations/
https://stackoverflow.com/questions/55043492/adjacency-list-to-matrix-pandas
https://www.educative.io/edpresso/how-to-implement-a-graph-in-python
https://www.programiz.com/dsa/graph-adjacency-list
https://www.youtube.com/watch?v=-uR7BSfNJko
https://www.youtube.com/watch?v=m2Elp9ubY3w
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
https://www.geeksforgeeks.org/graph-and-its-representations/
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""

import sys
import matplotlib.pyplot as plt

class MyQueue(object):
    """ 3). Creating Queue Class. Enqueue enters an integer to the end of the queue.
     Dequeue removes the last item from the queue.
      Front wills show the front of the queue. Which just so happens to be the last item on the list."""
    def __init__(self, type_var):
        self.elemType = type_var
        self.state = []  # This stores the queue
        self.visited = []  # This stores all the values that have been in the queue

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
            dequeue_num = self.state.pop()  # Taking the front of the queue
            self.visited.append(dequeue_num)  # Adding the value to the visited list
            return dequeue_num

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

    # Produces a dictionary with the node and the adjacency of the lists next to it
    # TODO Maybe look at putting this into a
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

    return adj_list


def BFS(G, s):
    """ 4). Runs a breadth-first search (BFS) algorithm outlined in the Slides.
    It should run a BFS starting with source vertex s element of V.
    You should use your queue class implementation in the implementation of this function.
    Should return a list that contains the distance from s to every other vertex v in the graph.
    That is the distant Vertex 5 would be stored in slot 5 of the list.
    The graph will be passed using the adjacency list representation from step 2"""

    # Creating the Neighbors Distance List filled in with infinity
    nbrlist = [float(sys.maxsize) for x in G]  # Setting Up Neighbor List

    # Creating a queue for which nodes to look at
    q = MyQueue(int)
    q.enqueue(s)

    # Creating a queue store the distance away a node is
    dq = MyQueue(int)
    distance = 0
    dq.enqueue(distance)

    # Going through the Q
    while not q.empty():
        # In MyQueue I have written in a q.visited. That Way I know if I have looked at that value
        if q.front() not in q.visited:  # Only do this for nodes that have not been visited
            num = q.dequeue()  # Taking the front of the queue
            nbrlist[num] = dq.dequeue()  # Pulling Distance
            for x in G[num]:
                q.enqueue(x)  # Adding to the queue
                dq.enqueue(nbrlist[num]+1)  # Adding distance +1
        else:
            q.dequeue()  # Visited before, throw out
            dq.dequeue()  # Doesn't Matter, throw out

    return nbrlist


def distanceDistribution(G):
    """ 5). Computes the distribution of all distances in G.
     The function returns a dictionary that maps positive distances to frequency of occurances.
     Specifically, the frequencies should be stored in percentage form.
     That is, 24.4% of all distances are three apart. Note that this might take a few minutes to run.
     So you might want to print out values every once in a while to show progress"""

    distance_dict = dict()
    # This returns the list for each of the nodes
    for x in range(len(G)):
        distance_dict[x] = 0

    for node in range(len(G)):
        for nbr in BFS(G, node):
            if nbr == node:
                continue
            else:
                distance_dict[nbr] += 1

    print(distance_dict)


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