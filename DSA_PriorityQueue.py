# PriorityQueue Implementation using List
List = []


# based on priority lowest val highest priority
def add(elements):
    List.append(elements)
    List.sort()


def remove():
    List.pop(0)


def display():
    print(List)


# based on priority highest val highest priority

def add_2(elements):
    List.append(elements)
    List.sort(reverse=True)


# PriorityQueue Implementation using Module
import queue

List2 = queue.PriorityQueue()


# adding to priorityQueue using module
def add_3(elements):
    List2.put(elements)


# adding to priorityQueue using module
def remove_3():
    List2.get()


# display()

# PriorityQueue Implementation using tuple
List3 = []


def add_tuple(elements, values):
    # add elements to list
    List3.append((elements, values))
    # re-arranging elements in order of priority (lowet elements highest priority)
    List3.sort()
    # displaying list
    print(List3)

