# Reverse string in Stack
Stack = []


def add(data):
    Stack.append(data)


def remove(data):
    Stack.pop()


def display():
    for i in Stack:
        print(i, end="")


def reverse():
    data = ""
    while Stack:
        data += Stack.pop()
    print(end=" ")
    print(data)


def reverse_string(data):
    print(data[::-1])


Stack.append("H")
Stack.append("E")
Stack.append("L")
Stack.append("L")
Stack.append("O")
display()
reverse()
reverse_string("app")
