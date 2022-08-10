# Implementing Queue using modules
import collections

Queues = collections.deque()


# adding elements to Queue from the rear / back
def add_rear(elements):
    Queues.append(elements)


# removing elements from Queue from the rear / back
def remove_rear():
    if not Queues:
        print('Stack is empty')
    else:
        Queues.popleft()


# adding elements to Queue from the front / head
def add_front(elements):
    Queues.insert(0, elements)


# removing elements from Queue from the front / head
def remove_front():
    if not Queues:
        print("Queue is empty")
    else:
        e = Queues.pop()
        print("Elements removed", e)


# displaying elements in stack
def display():
    print(Queues)

display()
