from collections import deque  # special 

# Queue ADT with deque implementation
class MyQueue(object):
    def __init__(self, type): # Creates an empty deque
        self.elemType = type  # type can be int, str, float, etc...
        self.state = deque()  # Empty deque
    def __str__(self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def enqueue(self, elem): # Adds an element to the end of queue
        assert type(elem) == self.elemType
        self.state.append(elem)
    def dequeue(self): # Removes an element from the front of the queue
        if self.empty():
            raise ValueError("Requested front of an empty queue")
        else:
            return self.state.popleft()
    def front(self): # Returns the front of a nonempty queue
        if self.empty():
            raise ValueError("Requested front of an empty queue")
        else:
            return self.state[0]

# Testing code
print("collections deque based queue")
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
# print(q.dequeue()) # should generate an error
#%%
print("\n\nlist based queue")

## class using lists instead of collections deque
class MyQueue(object):
    def __init__(self, type): # Creates an empty deque
        self.elemType = type  # type can be int, str, float, etc...
        self.state = []  # Empty list
    def __str__(self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def enqueue(self, elem): # Adds an element to the end of queue
        assert type(elem) == self.elemType
        self.state.append(elem)
    def dequeue(self): # Removes an element from the front of the queue
        if self.empty():
            raise ValueError("Requested front of an empty queue")
        else:
            temp = self.state[0]
            self.state = self.state[1:]
            return temp   # return the list element zero
    def front(self): # Returns the front of a nonempty queue
        if self.empty():
            raise ValueError("Requested front of an empty queue")
        else:
            return self.state[0]
        
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
# print(q.dequeue()) # should generate an error

######################################################################
#Queue with only lists

print("\n#########\nusing only lists\n")
q = []    # q = MyQueue(int)
print(len(q) == 0)    # print(q.empty())
q.append(5)    # q.enqueue(5)
q.append(8)    # q.enqueue(8)
print(q[0])    # print(q.dequeue())
q = q[1:]
q.append(3)   # q.enqueue(3)
print(len(q) == 0)    # print(q.empty())
print(q[0])   # print(q.front())
print(q[0])    # print(q.dequeue())
q = q[1:]
print(q[0])    # print(q.dequeue())
q = q[1:]

######################################################################
#Queue with only arrays
import numpy as np

print("\n#########\nusing only arrays\n")
q = np.array([], dtype='int')    # q = MyQueue(int)
print(len(q) == 0)    # print(q.empty())
q = np.append(q,5)    # q.enqueue(5)
q = np.append(q,8)     # q.enqueue(8)
print(q[0])    # print(q.dequeue())
q = q[1:]
q = np.append(q,3)    # q.enqueue(3)
print(len(q) == 0)    # print(q.empty())
print(q[0])   # print(q.front())
print(q[0])    # print(q.dequeue())
q = q[1:]
print(q[0])    # print(q.dequeue())
q = q[1:]

#################################################################
# using only collections deque

from collections import deque # python collections double ended queue

print("\n#########\nusing only deque\n")
q = deque()    # q = MyQueue(int)
print(len(q) == 0)    # print(q.empty())
q.append(5)    # q.enqueue(5)
q.append(8)     # q.enqueue(8)
print(q.popleft())    # print(q.dequeue())
q.append(3)    # q.enqueue(3)
print(len(q) == 0)    # print(q.empty())
print(q[0])   # print(q.front())
print(q.popleft())    # print(q.dequeue())
print(q.popleft())    # print(q.dequeue())
