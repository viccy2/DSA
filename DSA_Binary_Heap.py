# implementing Binary Heap

import heapq

heap = [10, 2, 20, 4, 5, 90, 12]


# convert list to heap
def heapify():
    heapq.heapify(heap)
    print(heap)


# add element / node to heap
def push_heap(data):
    heapq.heappush(heap, data)
    print(heap)


# remove and display smallest node
def pop():
    heapq.heappop(heap)
    print(heap)


# pop the smallest element and replace
def replace(data):
    heapq.heapreplace(heap, data)
    print(heap)


# display smallest element
def mini():
    a = heapq.nsmallest(2, heap)
    print(a)


# display highest element
def maxi():
    a = heapq.nlargest(2, heap)
    print(a)


heapify()
mini()
maxi()
