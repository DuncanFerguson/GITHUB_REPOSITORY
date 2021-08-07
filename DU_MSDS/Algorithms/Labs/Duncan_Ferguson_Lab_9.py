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
    print("vertsE", verts)
    minIndex = 0
    min = float("inf")
    for v in range(1, len(verts)):
        # print("verts: ", verts[v][1], "Min:", min)
        # print("Vert", verts[v])
        if verts[v][1] < min:
            min = verts[v][1]
            minIndex = v

    print("Return", verts[minIndex])
    return verts.pop(minIndex)


def MST(g):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    key = [float("inf")]*nVerts
    key[0] = 0
    P = [None] * nVerts
    P[0] = -1

    # print("Key", key)
    # print("P", P)

    # Start at vertex 0 - it has a current shortest distance of 0
    vertsToProcess[0][1] = 0
    # print("V2P", vertsToProcess[0][1])
    # vertsProcessed = []
    # while len(vertsToProcess) > 0:
    #     u = extractMin(vertsToProcess)
    #     vertsProcessed.append(u)
    #     print("U", u[1])
    #     # print("to process:",vertsToProcess)
    #     # print(" processed:",vertsProcessed)
    #     # Examine all potential verts remaining
    #     for v in vertsToProcess:
    #         # Update the distances if necessary
    #         if g[u[0]][v[0]] > 0 and v[1] > g[u[0]][v[0]]:
    #             print("Checking", g[u[0]][v[0]], v[0])
    #             print("Old V", v)
    #             v = [g[u[0]][v[0]], u[0]]
    #             print("New V",v)
    #             # P[v]
    #             P[0] = u[1]
    # print(P)

                # Start with an empty list of processed edges
    vertsProcessed = []
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        vertsProcessed.append(u)
        print("U", u[1])
        for v in range(len(vertsToProcess)):
            print("Verts", vertsToProcess, v)
            if g[u[0]][v] > 0 and vertsToProcess[v][0] < g[u[0]][v]:
                print("Checking", g[u[0]][v], v)
                # vertsToProcess[v][0] = g[u[0]][v]
                # vertsToProcess[v][1] = u[1]

        # print("to process:", vertsToProcess)
        # print(" processed:", vertsProcessed)

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


