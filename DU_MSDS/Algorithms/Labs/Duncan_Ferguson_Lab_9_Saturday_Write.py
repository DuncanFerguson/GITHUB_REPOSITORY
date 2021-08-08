# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 9
# Date 8/10/2021

import icecream as ic

def extractMin(key):
    print("key1", key)
    minIndex = 0
    min = float('inf')
    for v in range(1, len(key)):
        print("inside1",key[v])
        if key[v] < min:
            min = key[v]
            minIndex = v
    return minIndex

def extractMin2(key):
    print("key2", key)
    minIndex = 0
    min = float('inf')
    for v in range(1, len(key)):
        print("inside2", key[v][1])
        if key[v][1] < min:
            min = key[v][1]
            minIndex = v
    return minIndex


def mst(g):
    nVerts = len(g)
    key = [float("inf")] * nVerts
    p = [None] * nVerts
    vertsToProcess = [[None, float("inf")] for i in range(nVerts)]

    # The First node is -1, starting on 0
    vertsToProcess[0] = [-1, 0]
    key[0] = 0
    p[0] = -1

    print("V2P-Start", vertsToProcess)
    print("K2P-Start",list(zip(p, key)))

    for _ in range(nVerts):
        u = extractMin(key)
        # print("U1", u)
        for v in range(nVerts):
            if g[u][v] > 0 and key[v] > g[u][v]:
                key[v] = g[u][v]
                p[v] = u
                print("hit1", u, g[u][v])

    print("K2P-Finish", list(zip(p, key)))
    result = []
    for i in range(nVerts):
        edge = [i, p[i]]
        result.append(edge)

    for _ in range(nVerts):
        u2 = extractMin2(vertsToProcess)
        # print("U2", u2)
        for v in range(nVerts):
            if g[u2][v] > 0 and vertsToProcess[v][1] > g[u2][v]:
                vertsToProcess[v] = [u2, g[u2][v]]
                print("hit2", u2, g[u2][v])

    print("V2P-Finish", vertsToProcess)
    result2 = []
    for i in range(nVerts):
        edge2 = [i, vertsToProcess[i][0]]
        result2.append(edge2)

    print(result)
    print(result2)

def main():
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
             [7, 0, 12, 5, 0, 0, 0, 9],
             [0, 12, 0, 6, 0, 0, 0, 0],
             [0, 5, 6, 0, 14, 8, 0, 0],
             [0, 0, 0, 14, 0, 3, 0, 0],
             [10, 0, 0, 8, 3, 0, 0, 0],
             [15, 0, 0, 0, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0]]

    mst(graph)

if __name__ == '__main__':
    main()
