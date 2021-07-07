# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 5
# Date 7/13/2021

from collections import deque

# TODO check out geeks  for geeks deque website
# https://www.geeksforgeeks.org/deque-in-python/

class MyQueue(object):
    def __init__(self, type):
        self.elemType = type
        self.state = []

    def __str__(self):
        """Printing out the state as a string"""
        return str(self.state)
        # string_queue = ""
        # for i in range(len(self.state)):
        #     string_queue += " " + str(self.state[i])
        # return string_queue.lstrip()

    def enqueue(self, elem):
        """Adding an element to the queue"""
        self.state.insert(0, elem)

    def dequeue(self):
        """Removing an element from the queue"""
        return self.state.pop()

    def empty(self):
        """True if queue is empty"""
        return len(self.state) == 0

    def front(self):
        """Returns the front of the queue"""
        if self.empty():
            raise ValueError("Requested queue is empty")
        else:
            return self.state[0]

def test_queue():
    """This is for testing the queue"""
    q = MyQueue(int)
    print(q.empty())
    q.enqueue(5)
    q.enqueue(8)
    print(q)
    print(q.dequeue())
    q.enqueue(3)
    print(q.empty())
    print(q.front())
    print("This is the q", q)
    print(q.dequeue())
    print(q.dequeue())
    # print(q.dequeue())  # should generate an error