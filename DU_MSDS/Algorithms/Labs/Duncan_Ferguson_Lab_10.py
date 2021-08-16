# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 10
# Date 8/17/2021

class MyStack(object):
    def __init__(self, type):  # Creates an empty list
        self.elemType = type
        self.state = []  # Empty List

    def __str__(self):
        """For printing"""
        return str(self.state)

    def empty(self):
        return len(self.state) == 0

    def push(self, elem):
        """Adds an element to the top of a stack"""
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):
        """Removes an element from the top of a stack"""
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()

    def top(self):
        """Returns the top of a nonempty stack"""
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]


def nQueens(n):
    # Each state will include only the queens that have  been placed so far
    initialState = []  # Initial empty state
    s = MyStack(list)  # For a depth first search
    s.push(initialState)  # Push the initial state onto the Stack

    # While we still have states to explore
    while not s.empty():
        currentState = s.pop()  # Grab the next state
        currentCol = len(currentState)

        # See if we fond a solved state at a lead node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState)  # Display the solution
        else:
            # Produce the state's children (if they are feasible)
            # Note Children are produced backward so they come off the stack later left to right
            for currentRow in range(n, 0, -1):
                # Check horizontal
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or \
                            abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState)  # Push child onto data structure


def graphColoring(graph, colors):
    """This is a backgracking Coloring. Depth first search through a space tree.
    This should create a list of nodes that have been colored so far. Finished when it's reached all the nodes
    """
    initialState = []  # Initial empty state
    solutions = []
    s = MyStack(list)  # For a depth first search
    s.push(initialState)  # Push the initial state onto the Stack

    n = len(graph)

    # See if we fond a solved state at a lead node
    # That is, we have filled in every column with a queen
    while not s.empty():
        currentState = s.pop()
        currentCol = len(currentState)
        if currentCol == n:
            solutions.append(currentState)  # Adding a solution to the list
            # TODO this is where the return is
        else:
            for color in colors:
                feasible = True
                for node in range(currentCol):
                    if graph[currentCol][node] and currentState[node] == color:
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState)  # Push child onto data structure
    return solutions[-1]


def main():
    """Main Function that runs both nQueens and prints one answer for graphing colors"""
    # Testing code (check 4,5,6,7)
    for n in range(4, 5):
        print("Here")
        nQueens(n)

    # graph = [[False, True, False, False, False, True],
    #          [True, False, True, False, False, True],
    #          [False, True, False, True, True, False],
    #          [False, False, True, False, True, False],
    #          [False, False, True, True, False, True],
    #          [True, True, False, False, True, False]]
    # colors = ['r', 'g', 'b']
    # print(graphColoring(graph, colors))

    # nQueens()


if __name__ == '__main__':
    main()
