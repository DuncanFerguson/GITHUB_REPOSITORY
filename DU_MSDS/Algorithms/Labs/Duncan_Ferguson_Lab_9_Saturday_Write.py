# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 9
# Date 8/10/2021

import icecream as ic

def extractMin(verts):
    minIndex = 0
    for v in range(1,len(verts)):
        print("ExtractMin Vert", verts[v])
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)

# Dijkstra's shortest path algorithm
def MST(g):
# Create a list of vertices and their current shortest distances
# from vertex 0
# [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    # Start at vertex 0 - it has a current shortest distance of -1 unto it self
    vertsToProcess[0][1] = 0
    # Start with an empty list of processed edges
    vertsProcessed = []
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        print("U", u)
        vertsProcessed.append(u)
        for v in enumerate(vertsToProcess):
            # Only care about the ones that are adjacent to u
            print('verts 2', v[1])
            print(g[u[0]][v[1][0]])
            if u[1] + g[u[0]][v[1][0]] < v[1][1] and g[u[0]][v[1][0]] > 0:
                g[u[0]][v[1][0]] = u[1]
                v[1][1] = g[u[0]][v[0]]

                # vertsToProcess[1][1] = g[u[0]][v[1][0]]
                print('New vert[v]', g[u[0]][v[1][0]])
                print('New parent[v]', u[1])
                print("to process:",vertsToProcess)
                print(" processed:",vertsProcessed)

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
