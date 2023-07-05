# Queue implementation using List
Queue = []


def add(data):
    Queue.append(data)


def remove():
    Queue.pop(0)


def display():
    for i in Queue:
        print(i)


def reverse():
    data = ""
    while Queue:
        data += Queue.pop()
    print(data)


Queue.append("H")
Queue.append("E")
Queue.append("L")
Queue.append("L")
Queue.append("O")
remove()
reverse()
# display()
