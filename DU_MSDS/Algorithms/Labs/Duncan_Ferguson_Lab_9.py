# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 9
# Date 8/10/2021

import icecream as ic
import sys

"""
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""

def extractMin(verts):
    # print("verts", verts)
    minIndex = 0
    min = float("inf")
    for v in range(1, len(verts)):
        print("verts: ", verts[v], "Min:", min)
        # print("Vert", verts[v])
        if verts[v][1] < min:
            min = verts[v]
            minIndex = v
            verts[v][1] = v
    return verts.pop(minIndex)


def MST(g):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    # Start at vertex 0 - it has a current shortest distance of 0
    vertsToProcess[0][1] = 0
    # print("V2P", vertsToProcess[0][1])

    # Start with an empty list of processed edges
    vertsProcessed = []
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        vertsProcessed.append(u)
        print("U", u)
        for v in range(len(vertsToProcess)):
            print("Verts", vertsToProcess, v)
            if g[u[0]][v] > 0 and vertsToProcess[v][0] < g[u[0]][v]:
                print("Checking", g[u[0]][v], v)

        print("to process:", vertsToProcess)
        print(" processed:", vertsProcessed)

    print(vertsProcessed)


def main():
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
             [7, 0, 12, 5, 0, 0, 0, 9],
             [0, 12, 0, 6, 0, 0, 0, 0],
             [0, 5, 6, 0, 14, 8, 0, 0],
             [0, 0, 0, 14, 0, 3, 0, 0],
             [10, 0, 0, 8, 3, 0, 0, 0],
             [15, 0, 0, 0, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0]]

    MST(graph)

if __name__ == '__main__':
    main()

