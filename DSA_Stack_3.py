# Stack using modules (Queues)
import queue

Stack = queue.LifoQueue()


# adding elements to stack
def add(elements):
    Stack.put(elements)


# removing elements from stack
def remove():
    if not Stack:
        print('Stack is empty')
    else:
        Stack.get()


# displaying elements in stack
def display():
    print(Stack)


display()
