import heapq
import numpy as np

class Heap(list):
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        heapq.heapify(heap)
        super(Heap, self).__init__(heap)

    def __repr__(self):
        return 'Heap({})'.format(super(Heap, self).__repr__())

    def heappush(self, item):  # push item onto heap
        return heapq.heappush(self, item)

    def heappop(self):  # pop and return the smallest item from heap
        return heapq.heappop(self)

    def pushpop(self, item):   # push item onto heap and return the smallest items from heap
        return heapq.heappushpop(self, item)

    def replace(self, item):  # Pop and return the smallest item from the heap, and also push the new item
        return heapq.heapreplace(self, item)

    def nlargest(self, n, *args, **kwargs):  # returns a list with the n-largest items from heap
        return heapq.nlargest(n, self, *args, **kwargs)

    def nsmallest(self, n, *args, **kwargs):  # returns a list with the n smallest items from heap
        return heapq.nsmallest(n, self, *args, **kwargs)
    

l = np.random.choice(20, 10, replace=False)  # randomly choose 10 items from the range 0 to 20 without replacement
print("original list: ",l)
# init heap with Heap()
h = Heap(list(l))   # push all ten items to heap with the heapify command.  Reads in list, pushes items to heap
print(h)
print("pushpop: ",h.pushpop(21))  # push 21 to heap with heappushpop() and return smallest
print(h)
print("heappop: ",h.heappop())
print(h)
print("nlagest: ",h.nlargest(2))
print("nsmallest: ",h.nsmallest(5))
print(h)