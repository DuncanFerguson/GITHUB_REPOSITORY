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
    """This function takes in an adjacency matrix and a list of colors. The function is a depth-first search
    through a state space tree. This function creates a list of solutions that contains
    a list of solutions where nodes have been colored."""

    initialState = []  # Initial empty state
    solutions_list = []  # Blank Solutions List
    s = MyStack(list)  # For a depth first search
    s.push(initialState)  # Push the initial state onto the Stack

    n = len(graph)  # Grabbing the number of nodes in the graph

    # See if we fond a solved state at a lead node
    # That is, we have filled in every column with a queen
    while not s.empty():
        currentState = s.pop()  # Grabbing the next state
        currentCol = len(currentState)
        # See if we have found a solved state at a leaf node
        # That is, we have filled in every node with a color
        if currentCol == n:
            solutions_list.append(currentState)  # Adding a solution to the list and continuing to find more solutions
            break  # stopping after the first solution, uncomment for all solutions
        else:
            for color in colors:  # Going through all the different colors
                feasible = True
                for node in range(currentCol):
                    if graph[currentCol][node] and currentState[node] == color:  # Checking to see if feasible
                        feasible = False
                if feasible:
                    # Create child by making a copy and appending new color
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState)  # Push child onto data structure
    return solutions_list  # Returning a list of the solutions


def main():
    """Main Function that runs both nQueens and prints one answer for graphing colors"""
    # Testing code (check 4,5,6,7)
    print("\nRunning nQueens Test")
    for n in range(4, 5):
        nQueens(n)

    graph = [[False, True, False, False, False, True],
             [True, False, True, False, False, True],
             [False, True, False, True, True, False],
             [False, False, True, False, True, False],
             [False, False, True, True, False, True],
             [True, True, False, False, True, False]]

    colors = ['r', 'g', 'b']

    solution_list = graphColoring(graph, colors)
    print("\nPrinting out the first Solution")
    print(solution_list[0])

    # print("\nPrinting last graphColoring Solution")
    # print(solution_list[-1])  # Printing out the last solution
    #
    # print("\nPrinting all the Solutions")
    # for sol in solution_list:
    #     print(sol)


if __name__ == '__main__':
    main()
