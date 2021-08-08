import sys

# Prim's MST greedy algorithm

def extractMin(key):
    minIndex = 0
    min = float('inf')
    for v in range(1, len(key)):
        if key[v] < min:
            min = key[v]
            minIndex = v
    # print("Return", minIndex, key)
    return minIndex

def mst(g):
    nVerts = len(g)
    key = [float("inf")] * nVerts
    p = [None] * nVerts
    key[0] = 0
    p[0] = -1

    for _ in range(nVerts):
        u = extractMin(key)
        for v in range(nVerts):
            if g[u][v] > 0 and key[v] > g[u][v]:
                key[v] = g[u][v]
                p[v] = u

        result = []
        for i in range(nVerts):
            edge = [i, p[i]]
            result.append(edge)

    print(result)

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9],
         [0, 12, 0, 6, 0, 0, 0, 0],
         [0, 5, 6, 0, 14, 8, 0, 0],
         [0, 0, 0, 14, 0, 3, 0, 0],
         [10, 0, 0, 8, 3, 0, 0, 0],
         [15, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0]]

mst(graph)