# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 8
# Date 8/3/2021

class MyStack(object):
    def init(self, type):
        self.elemType = type
        self.state = []

    def str(self):  # for print
        return str(self.state)

    def empty(self):
        return len(self.state) == 0

    def push(self, elem):  # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):  # Removes an element from the top of a stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")

    def top(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def nQueens(n):
    # Each state will include only the queens that have  been placed so far
    initialState = []  # Initial empty state
    s = MyStack(list)  # For a depth first search
    s.push(initialState)  # Push the initial state onto the Stack

    #While we still have states to explore
    while not s.empty():
        currentState = s.pop()
        currentCol = len(currentState)

        # See if we fond a solved state at a lead node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState)
        else:
            # Produce the state's children (if they are feasible)
            # Note Children are produced backward so they come off the stack later left to right
            for currentRow in range(n, 0 -1):
                # Check horizontal
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol == currentRow]) or abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState)  # Push child onto data structure
    # Testing code (check 4,5,6,7)
    for n in range(4,8):
        nQueens(n)


def graphColoring(graph, colors):
    """This is a backgracking Coloring. Depth first search through a space tree.
    This should create a list of nodes that have been colored so far. Finished when it's reached all the nodes
    """
    initialState = []
    s = MyStack(list())
    s.push(initialState)

    n = len(graph)
    while not s.empty():
        currentState = s.pop()
        currentNode = len(currentState)
        if currentNode == n:
            print(currentState)
            break
        else:
            for color in colors:
                feasible = True
                for node in range(currentNode):
                    if graph[currentNode][node] == True and currentState[node] == color:
                        feasible = False
                        break
                if feasible:
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState)


def main():
    graph = [[False, True, False, False, False, True],
             [True, False, True, False, False, True],
             [False, True, False, True, True, False],
             [False, False, True, False, True, False],
             [False, False, True, True, False, True],
             [True, True, False, False, True, False]]
    colors = ['r', 'g', 'b']
    graphColoring(graph, colors)
    # nQueens()



if __name__ == '__main__':
    main()