import sys

# Prim's MST greedy algorithm

def extractMin(verts):
    print("vertsE", verts)
    minIndex = 0
    min = float('inf')
    for v in range(1, len(verts)):
        print("verts:", verts[v], "Min:", min)
        if verts[v] < min:
            min = verts[v]
            minIndex = v
    # print("MSTSet", )
    # print("Min Before Return", minIndex)
    return minIndex

def mst(g):
    nVerts = len(g)
    verts = [float("inf")] * nVerts
    parent = [None] * nVerts
    verts[0] = 0
    parent[0] = -1

    # print("verts", verts)
    # print("p", parent)

    for _ in range(nVerts):
        u = extractMin(verts)
        print("u", u)
        for v in range(nVerts):
            # print("verts 2", verts, v)
            if g[u][v] > 0 and verts[v] > g[u][v]:
                print("Checking ", g[u][v], v)
                verts[v] = g[u][v]
                parent[v] = u
                print("Old V", v)
                print("New V", verts[v], parent[v])

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