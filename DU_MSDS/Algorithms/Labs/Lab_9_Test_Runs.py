import sys

# Prim's MST greedy algorithm

def extractMin(verts):
    minIndex = 0
    min = float('inf')
    for v in range(1, len(verts)):
        print("ExtractMin Vert", verts)
        # print("verts:", verts[v], "Min:", min)
        if verts[v] < min:
            min = verts[v]
            minIndex = v
            print("min", min)
            print("Vers Min Index", minIndex)
    return minIndex

def mst(g):
    INF = float("inf")
    nVert= len(g)
    selected = [0]*nVert
    no_edge = 0
    selected[0] = True

    while (no_edge < nVert - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(nVert):
            if selected[i]:
                for j in range(nVert):
                    if ((not selected[j]) and g[i][j]):
                        if minimum > g[i][j]:
                            minimum = g[i][j]
                            x = i
                            y = j
        print(str(x)+"-"+str(y)+":"+str(g[x][y]))
        selected[y] = True
        no_edge += 1

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9],
         [0, 12, 0, 6, 0, 0, 0, 0],
         [0, 5, 6, 0, 14, 8, 0, 0],
         [0, 0, 0, 14, 0, 3, 0, 0],
         [10, 0, 0, 8, 3, 0, 0, 0],
         [15, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0]]

mst(graph)