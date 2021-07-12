# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

class MyQueue(object):
    """Creating Queue Class. Enqueue enters an integer to the end of the queue. Dequeue removes the last item from the
    queue. Front wills show the front of the queue. Which just so happens to be the last item on the list."""
    def __init__(self, type_var):
        self.elemType = type_var
        self.state = []

    def __str__(self):
        """Printing out the state as a string"""
        return str(self.state)

    def enqueue(self, elem):
        """Adding an element to the queue"""
        self.state.insert(0, elem)

    def dequeue(self):
        """Removing an element from the queue"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state.pop()

    def empty(self):
        """True if queue is empty. False if not empty"""
        return len(self.state) == 0

    def front(self):
        """Returns the front of the queue. Which just so happens to be the last item on the list"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state[-1]


def test_queue():
    """This is for testing.txt the queue"""
    q = MyQueue(int)
    print(q.empty())
    q.enqueue(5)
    q.enqueue(8)
    print(q.dequeue())
    q.enqueue(3)
    print(q.empty())
    print(q.front())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())  # should generate an error


def main():
    """Standard Main pointing to test queue"""
    test_queue()


if __name__ == '__main__':
    main()
