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




def main():
    graph = [[False, True, False, False, False, True],
             [True, False, True, False, False, True],
             [False, True, False, True, True, False],
             [False, False, True, False, True, False],
             [False, False, True, True, False, True],
             [True, True, False, False, True, False]]
    colors = ['r', 'g', 'b']
    graphColoring(graph, colors)



if __name__ == '__main__':
    main()