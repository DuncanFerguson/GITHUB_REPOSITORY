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
"""

# TODO not sure if the graph class is needed as it can be incorporated into the loadgraph function
class Graph:
    def __init__(self, num_vertex):
        self.adjMatrix = [[-1]*num_vertex for x in range(num_vertex)]
        self.num_vertex = num_vertex
        self.vertices = {}
        self.verticeslist = [0]*num_vertex

    def __str__(self):
        return str(self.adjMatrix)


class MyQueue(object):
    """ 3). Creating Queue Class. Enqueue enters an integer to the end of the queue.
     Dequeue removes the last item from the queue.
      Front wills show the front of the queue. Which just so happens to be the last item on the list."""
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
    rows = df.values.tolist()  # Turning Dataframe into list of lists
    # graph = {'nodes': list(), 'edges': list()}
    graph = dict()  # Creating Blank Dictionary
    graph['nodes'] = list()  # Adding a collection of nodes
    graph['edges'] = list()  # Adding a collection of the edges

    # Creating Graph Dictionary with the nodes and the
    for row in range(len(rows)):
        if rows[row][0] not in graph.keys():
            graph['nodes'].append(rows[row][0])
            graph['edges'].append(rows[row])
        elif rows[row][1] not in graph.keys():
            graph['nodes'].append(rows[row][1])
            graph['edges'].append(rows[row])
        else:
            graph['edges'].append(rows[row])

    # Alternative Way of Creating the dictionary
    # graph2 = dict()
    # for row in range(len(rows)):
    #     if rows[row][0] not in graph2.keys():
    #         graph2[rows[row][0]] = [rows[row][1]]
    #     elif rows[row][0] in graph2.keys():
    #         graph2[rows[row][0]].append(rows[row][1])
    #     elif rows[rows[row][1]] not in graph2.keys():
    #         graph2[rows[row][1]] = [rows[row][0]]
    #     elif rows[rows[row][1]] in graph2.keys():
    #         graph2[rows[row][1]].append(rows[row][0])
    #     else:
    #         print("\n \n \n \n \n BREAK \n \n \n \n \n")

    # Produces a dictionary with the node and the adjacency of the lists next to it
    graph3 = dict()
    for row in range(len(rows)):
        if rows[row][0] not in graph3.keys():
            graph3[rows[row][0]] = [rows[row][1]]
        elif rows[row][0] in graph3.keys():
            graph3[rows[row][0]].append(rows[row][1])

    for row in range(len(rows)):
        if rows[row][1] not in graph3.keys():
            graph3[rows[row][1]] = [rows[row][0]]
        elif rows[row][1] in graph3.keys():
            graph3[rows[row][1]].append(rows[row][0])
        else:
            print("\n \n \n \n \n BREAK \n \n \n \n \n")  # Should never get to here



    # for key in graph2:
    #     print("New Key")
    #     print(key, len(graph2[key]))
    #     print("End Key")
    print(sum(graph3[1]))
    # print(len(graph['nodes']))
    # for key in graph2:
    #     print(graph2[key])


    # TODO Clean up this dictionary to have nodes and the adjecy
    return graph


def BFS(G, s):
    """ 4). Runs a breadth-first search (BFS) algorithm outlined in the Slides.
    It should run a BFS starting with source vertex s element of V.
    You should use your queue class implementation in the implementation of this function.
    Should return a list that contains the distance from s to every other vertex v in the graph.
    That is the distant Vertex 5 would be stored in slot 5 of the list.
    The graph will be passed using the adjacency list representation from step 2"""
    #  https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/



    return


def distanceDistribution(G):
    """ 5). Computes the distribution of all distances in G.
     The function returns a dictionary that maps positive distances to frequency of occurances.
     Specifically, the frequencies should be stored in percentage form.
     That is, 23.6% of all distances are three apart. Note that this might take a few minutes to run.
     So you might want to print out values every once in a while to show progress"""
    return

def test():
    """Testing code that prints out the final distribution dictionary"""
    loadGraph('edges.txt')
    # loadGraph('testing.txt')


def main():
    """Standard Main pointing to test queue"""
    test()


if __name__ == '__main__':
    main()

"""" 7). To what extent does this network satisfy the small world phenomenon? 
Please put a comment section at the bottom of your code that answer this question"""
