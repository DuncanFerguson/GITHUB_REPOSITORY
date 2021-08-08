import sys

# https://www.codespeedy.com/demonstrate-prims-minimum-spanning-tree-algorithm-in-python/
def min_key2(mstSet, verts):
    min = float('inf')
    minIndex = 0
    for v in range(len(verts)):
        # print("Key2", verts[v][1])
        # if verts[v][1] < min and mstSet[v] == False:
        if verts[v][1] < min:
            min = verts[v][1]
            minIndex = v
    # print(verts[minIndex])
    return verts.pop(minIndex)

# def min_Key(key, mstSet, nVerts):
#     min = float('inf')
#     for v in range(nVerts):
#         print("key1", key[v])
#         if key[v] < min and mstSet[v] == False:
#             min = key[v]
#             min_index = v
#     return min_index

def prim(g):
    nVerts = len(g)
    key = [float('inf')] * nVerts
    parent = [None] * nVerts
    key[0] = 0
    mstSet = [False] * nVerts

    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]
    vertsToProcess[0][1] = -1
    parent[0] = -1

    p = [[0, -1]]
    vertsProcessed = []
    edgelist = []
    minimum = float("inf")
    while len(vertsToProcess) > 0:
        u2 = min_key2(mstSet, vertsToProcess)
        vertsProcessed.append(u2)
        # mstSet[u2[0]] = True
        for v in range(len(vertsToProcess)):
            # print("V2P", vertsToProcess[v][1])
            print("G", g[u2[0]][v], "v", v, "u", u2[0])
            if g[u2[0]][v] > 0 and g[u2[0]][v] not in edgelist and minimum > g[u2[0]][v]:
            # if g[u2[0]][v] > 0 and g[u2[0]][v] and vertsToProcess[v][1] > g[u2[0]][v]:
                minimum = g[u2[0]][v]
                x, y = g[u2[0]][v], v
                # vertsToProcess[v][1] = u2[0]
            # print("Edge List", edgelist)
        edgelist.append([y, x])

    print(x, "-", y, "\t", minimum)
    print(edgelist)


    # for cout in range(nVerts):
    #     u = min_Key(key, mstSet, nVerts)
    #     print("U_Back", u, cout)
    #     u2 = min_key2(mstSet, vertsToProcess)
    #     print("U2", u2, cout)
    #     mstSet[u] = True
    #     for v in range(nVerts):
    #         if g[u][v] > 0 and mstSet[v] == False and key[v] > g[u][v]:
    #             key[v] = g[u][v]
    #             parent[v] = u
    #             vertsToProcess[v][0] = g[u][v]
    #             vertsToProcess[v][1] = u

    # for i in range(1, nVerts):
    #     print(parent[i], "-", i, "\t", g[i][parent[i]])
    #     p.append([i, parent[i]])
    #
    # print(p)

g = [[0, 7, 0, 0, 0, 10, 15, 0],
     [7, 0, 12, 5, 0, 0, 0, 9],
     [0, 12, 0, 6, 0, 0, 0, 0],
     [0, 5, 6, 0, 14, 8, 0, 0],
     [0, 0, 0, 14, 0, 3, 0, 0],
     [10, 0, 0, 8, 3, 0, 0, 0],
     [15, 0, 0, 0, 0, 0, 0, 0],
     [0, 9, 0, 0, 0, 0, 0, 0]]

prim(g)