# Reverse string in Stack
Stack = []


def push_to_stack(data):
    Stack.append(data)


def pop_from_stack():
    Stack.pop()


def display_stack():
    for i in Stack:
        print(i, end="")


def reverse_stack():
    elem = " "
    while Stack:
        elem += Stack.pop()
    print(elem)


push_to_stack('H')
push_to_stack('E')
push_to_stack('L')
push_to_stack('L')
push_to_stack('O')
display_stack()
reverse_stack()
