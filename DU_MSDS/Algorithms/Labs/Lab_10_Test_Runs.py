class MyStack(object):
    def __init__(self, type):
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
        else:
            return self.state.pop()

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

    # While we still have states to explore
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


def main():
    graph = [[False, True, False, False, False, True],
             [True, False, True, False, False, True],
             [False, True, False, True, True, False],
             [False, False, True, False, True, False],
             [False, False, True, True, False, True],
             [True, True, False, False, True, False]]
    # colors = ['r', 'g', 'b']
    # print(graphColoring(graph, colors))
    # for n in range(4,8):
    #     nQueens(n)
    for n in range(4, 8):
        # print(n)
        nQueens(n)

    # nQueens()



if __name__ == '__main__':
    main()