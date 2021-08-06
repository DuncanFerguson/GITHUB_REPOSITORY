import sys

# Prim's MST greedy algorithm

def extractMin(verts):
    # print("verts", verts)
    minIndex = 0
    min = float('inf')
    for v in range(1, len(verts)):
        if verts[v] < min:
            min = verts[v]
            minIndex = v
    print("MSTSet", )
    print("Min Before Return", minIndex)
    return minIndex

def mst(g):
    nVerts = len(g)
    verts = [float("inf")] * nVerts
    parent = [None] * nVerts
    verts[0] = 0
    mstSet = [False] * nVerts
    parent[0] = -1

    print("verts", verts)
    print("mst", mstSet)
    print("parent", parent)

    for cout in range(nVerts):
        u = extractMin(verts)
        for v in range(nVerts):
            if g[u][v] > 0 and verts[v] > g[u][v]:
                verts[v] = g[u][v]
                parent[v] = u
        result = []
        for i in range(nVerts):
            edge = [i, parent[i]]
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