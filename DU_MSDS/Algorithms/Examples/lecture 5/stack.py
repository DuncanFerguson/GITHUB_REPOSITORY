
# Stack ADT with list implementation
class MyStack(object):
    def __init__(self, type): # Creates an empty list, can be int, str, float...
        self.elemType = type
        self.state = []  # Empty list
    def __str__(self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)   # standard python list operation to append element to end of list
    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()    # this is a basic python list operation.  Deletes last element in list
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

# Testing code
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
# print(s.pop()) # should generate an error
t = MyStack(float)

###############################
# stack with only lists

print("\nstack with pure lists\n")
s = []   # s = MyStack(int)
print(len(s) == 0)    # print(s.empty())
s.append(5)    # s.push(5)
s.append(8)    # s.push(8)
print(s.pop())    # print(s.pop())
s.append(3)    # s.push(3)
print(len(s) == 0)    # print(s.empty())
print(s[-1])    # print(s.top())
print(s.pop())    # print(s.pop())
print(s.pop())    # print(s.pop())
# print(s.pop())    # # print(s.pop()) # should generate an error
# t = MyStack(float)

######################################################################
#stack with only arrays
import numpy as np

print("\nusing only numpy arrays\n")
s = np.array([], dtype='int')    # s = MyStack(int)
print(len(s) == 0)    # print(s.empty())
s = np.append(s, 5)    # s.push(5)
s = np.append(s, 8)    # s.push(8)
print(s[-1])    # print(s.pop())
s = s[0:-1]
s = np.append(s, 3)    # s.push(3)
print(len(s) == 0)    # print(s.empty())
print(s[-1])    # print(s.top())
print(s[-1])    # print(s.pop())
s = s[0:-1]
print(s[-1])    # print(s.pop())
s = s[0:-1]

#################################################################
# using only collections deque

from collections import deque # python collections double ended queue

print("\n#########\nusing only deque\n")

s = deque()    # s = MyStack(int)
print(len(s) == 0)    # print(s.empty())
s.append(5)    # s.push(5)
s.append(8)    # s.push(8)
print(s.pop())    # print(s.pop())
s.append(3)    # s.push(3)
print(len(s) == 0)    # print(s.empty())
print(s[-1])    # print(s.top())
print(s.pop())    # print(s.pop())
print(s.pop())    # print(s.pop())