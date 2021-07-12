# Python3 program to implement
# the above approach

# Function to insert vertices
# to adjacency list
def insert(adj, u, v):
    # Insert a vertex v to vertex u
    adj[u].append(v)
    return


# Function to display adjacency list
def printList(adj, V):
    for i in range(V):
        print(i, end='')

        for j in adj[i]:
            print(' --> ' + str(j), end='')

        print()

    print()


# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):
    # Initialize a matrix
    matrix = [[0 for j in range(V)]
              for i in range(V)]

    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1

    return matrix


# Function to display adjacency matrix
def printMatrix(adj, V):
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end=' ')

        print()

    print()


# Driver code
if __name__ == '__main__':
    V = 11
    adjList = [[] for i in range(V)]

    # Inserting edges
    insert(adjList, 0, 1)
    insert(adjList, 0, 2)
    insert(adjList, 0, 3)
    insert(adjList, 1, 0)
    insert(adjList, 1, 2)
    insert(adjList, 1, 4)
    insert(adjList, 2, 0)
    insert(adjList, 2, 1)
    insert(adjList, 2, 3)
    insert(adjList, 2, 4)
    insert(adjList, 2, 5)
    insert(adjList, 2, 10)
    insert(adjList, 3, 0)
    insert(adjList, 3, 2)
    insert(adjList, 3, 5)
    insert(adjList, 4, 1)
    insert(adjList,4, 2)
    insert(adjList,4, 5)
    insert(adjList,5, 2)
    insert(adjList,5, 3)
    insert(adjList,5, 4)
    insert(adjList,5, 6)
    insert(adjList,6, 5)
    insert(adjList,6, 7)
    insert(adjList,7, 6)
    insert(adjList,7, 8)
    insert(adjList,8, 7)
    insert(adjList,9, 10)
    insert(adjList, 10,2)
    insert(adjList,10,9 )


    # Display adjacency list
    print("Adjacency List: ")
    printList(adjList, V)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adjList, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)