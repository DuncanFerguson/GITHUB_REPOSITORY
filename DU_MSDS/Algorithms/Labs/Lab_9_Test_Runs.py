import sys

# https://www.codespeedy.com/demonstrate-prims-minimum-spanning-tree-algorithm-in-python/

def min_Key(key, mstSet, nVerts):
    min = float('inf')
    print("key", key)
    print("mst", mstSet)
    for v in range(nVerts):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index

def prim(g):
    nVerts = len(g)
    key = [float('inf')] * nVerts
    parent = [None] * nVerts
    key[0] = 0
    mstSet = [False] * nVerts

    parent[0] = -1

    p = [[0, -1]]
    for cout in range(nVerts):
        u = min_Key(key, mstSet, nVerts)
        mstSet[u] = True
        for v in range(nVerts):
            if g[u][v] > 0 and mstSet[v] == False and key[v] > g[u][v]:
                key[v] = g[u][v]
                parent[v] = u

    for i in range(1, nVerts):
        print(parent[i], "-", i, "\t", g[i][parent[i]])
        p.append([i, parent[i]])

    print(p)

g = [[0, 7, 0, 0, 0, 10, 15, 0],
     [7, 0, 12, 5, 0, 0, 0, 9],
     [0, 12, 0, 6, 0, 0, 0, 0],
     [0, 5, 6, 0, 14, 8, 0, 0],
     [0, 0, 0, 14, 0, 3, 0, 0],
     [10, 0, 0, 8, 3, 0, 0, 0],
     [15, 0, 0, 0, 0, 0, 0, 0],
     [0, 9, 0, 0, 0, 0, 0, 0]]

prim(g)