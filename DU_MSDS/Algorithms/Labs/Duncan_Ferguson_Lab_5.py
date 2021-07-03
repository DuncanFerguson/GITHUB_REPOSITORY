# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

class MyStack(object):
    def __init__(self, type):
        self.elemType = type
        self.state = []

    def __str__(self):
        """Printing out the state as a string"""
        string_stack = ""
        for i in range(len(self.state)):
            string_stack += " " + str(self.state[i])
        return string_stack.lstrip()

    def push(self, elem):
        """Adding an element to the top of the stack"""
        self.state.append(elem)

    def empty(self):
        """True iff stack is empty"""
        return len(self.state) == 0

    def pop(self):
        """Removes the top of a nonempty stack"""
        if not self.empty():
            self.state.pop()

    def top(self):
        """Returns the top of a nonempty stack"""
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]



# class MyQueue(object):
#     def __init__(self):


def test_stack():
    """This function is testing the stack"""
    s = MyStack(int)
    print(s.empty())
    s.push(5)
    s.push(8)
    print(s.pop())
    print(s)
    # s.push(3)
    # print(s.empty())
    # print(s.top())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())  # should generate an error

# def test_queue():
#     """This is for testing the queue"""
#     q = MyQueue(int)
#     print(q.empty())
#     q.enqueue(5)
#     q.enqueue(8)
#     print(q.dequeue())
#     q.enqueue(3)
#     print(q.empty())
#     print(q.front())
#     print(q.dequeue())
#     print(q.dequeue())
#     print(q.dequeue())  # should generate an error

def main():
    test_stack()
    # test_queue()

if __name__ == '__main__':
    main()
