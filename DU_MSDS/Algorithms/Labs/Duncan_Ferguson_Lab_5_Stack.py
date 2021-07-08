# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

# TODO make sure to write errors for anything that is not an int

class MyStack(object):
    def __init__(self, type):
        self.elemType = type
        self.state = []

    def __str__(self):
        """Printing out the state as a string"""
        return str(self.state)

    def push(self, elem):
        """Adding an element to the top of the stack"""
        self.state.append(elem)

    def empty(self):
        """True iff stack is empty"""
        return len(self.state) == 0

    def pop(self):
        """Removes the top of a nonempty stack"""
        if not self.empty():
            return self.state.pop()
        else:
            raise ValueError("Requested top of an empty stack")

    def top(self):
        """Returns the top of a nonempty stack"""
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]


def test_stack():
    """This function is testing the stack"""
    s = MyStack(int)
    print(s.empty())
    s.push(5)
    s.push(8)
    print(s.pop())
    s.push(3)
    print(s.empty())
    print(s.top())
    print(s.pop())
    print(s.pop())
    print(s.pop())  # should generate an error


def main():
    test_stack()


if __name__ == '__main__':
    main()
