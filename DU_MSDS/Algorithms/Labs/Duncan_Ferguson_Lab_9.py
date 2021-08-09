# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 9
# Date 8/10/2021

def mst(g):
    nVerts = len(g)
    key = [None for _ in range(nVerts)]  # Creating an array to track vertex's that have been selected
    no_edge = 0  # Starting at Edge 0
    key[0] = True  # Checking the first key to show that we represented it above
    P = [[no_edge, -1]]  # First Vertex is -1 to itself

    # Going through the number edge
    while no_edge < nVerts - 1:
        # print("Looking at", no_edge)
        minimum = float("inf")  # Setting the Current Min Start
        for i in range(nVerts):  # Looping the amount of vertices
            if key[i] == True:  # If the Key is true look to update
                for j in range(nVerts):
                    # If the key is not already selected and there is an edge and the min is greater adj then update
                    if key[j] == None and g[i][j] and minimum > g[i][j]:
                        minimum = g[i][j]  # Updating the minimum
                        x, y = i, j  # Grabbing location of adjacency

        P.append([y, x])  # Adding The Edge to the list
        key[y] = True  # Marking the key as checked true
        no_edge += 1  # Indexing to go through the next edge

    return P


def main():
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
             [7, 0, 12, 5, 0, 0, 0, 9],
             [0, 12, 0, 6, 0, 0, 0, 0],
             [0, 5, 6, 0, 14, 8, 0, 0],
             [0, 0, 0, 14, 0, 3, 0, 0],
             [10, 0, 0, 8, 3, 0, 0, 0],
             [15, 0, 0, 0, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0]]
    print(mst(graph))


if __name__ == '__main__':
    main()
