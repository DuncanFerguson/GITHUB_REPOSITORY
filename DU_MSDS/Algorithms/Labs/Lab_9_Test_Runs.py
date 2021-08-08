

def mst(g):
    nVerts= len(g)
    key = [None]*nVerts  # Creating an array to track vertex's that have been selected
    no_edge = 0  # Starting at Edge 0
    key[0] = True  # Checking the first key to show that we represented it above
    P = [[no_edge, -1]]  # First Vertex is -1 to itself

    # Going through the number edge
    while no_edge < nVerts - 1:
        minimum = float("inf")  # Setting the Current Min
        for i in range(nVerts):  # Looping the amount of vertices
            if key[i] == True:
                # print("MIN IN", minimum)
                for j in range(nVerts):
                    # If not already selected and there is an edge and the min is greater adj then update
                    if key[j] == None and g[i][j] and minimum > g[i][j]:
                        minimum = g[i][j]
                        x = i
                        y = j
                        print("Edge",x,y,"Weight",minimum)

        print("Add", x,y)
        P.append([x, y]) # Adding The Edge to the list
        key[y] = True  # Marking the key as checked true
        no_edge += 1  # Indexing to go through the next edge

    print(P)


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






