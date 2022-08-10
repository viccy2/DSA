# Stack Implementetion using List
Queue = []


# adding elements to Queue from the rear / back
def add_rear():
    elements = int(input("Enter values"))
    Queue.append(elements)
    print(Queue)


# removing elements from Queue from the rear / back
def remove_rear():
    if not Queue:
        print("Queue is empty")
    else:
        e = Queue.pop(0)
        print("Elements removed", e)
        print(Queue)


# adding elements to Queue from the front / head
def add_front():
    elements = int(input("Enter values"))
    Queue.insert(0, elements)
    print(Queue)


# removing elements from Queue from the front / head
def remove_front():
    if not Queue:
        print("Queue is empty")
    else:
        e = Queue.pop()
        print("Elements removed", e)
        print(Queue)


while True:
    print(
        'Enter 1 to add to queue from the front. 2 To remove from Queue from the front. 3 to add to Queue from the '
        'rear. 4 To remove from Queue from the rear. 5 To end the task')
    choice = int(input())
    if choice == 1:
        add_front()
    elif choice == 2:
        remove_front()
    elif choice == 3:
        add_rear()
    elif choice == 4:
        remove_rear()
    elif choice == 5:
        break
    else:
        print("choose correct option")
