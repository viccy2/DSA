# Implementing Queue using modules (Queues)
import queue

Queues = queue.Queue()


# adding elements to Queues
def add(elements):
    Queues.put(elements)


# remove element from Queues
def remove():
    Queues.get()


# display Queues
def display():
    print(Queues)

display()
