# Stack using modules
import collections

Stack = collections.deque()


# adding elements to stack
def add(elements):
    Stack.append(elements)


# removing elements from stack
def remove():
    if not Stack:
        print('Stack is empty')
    else:
        Stack.pop()


# displaying elements in stack
def display():
    print(Stack)


display()
