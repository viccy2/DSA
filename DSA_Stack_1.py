# Stack Implementetion using List
Stack = []


def push_to_stack():
    elements = int(input("Enter values"))
    Stack.append(elements)
    print(Stack)


def pop_from_stack():
    if not Stack:
        print("Stack is empty")
    else:
        e = Stack.pop()
        print("Elements removed", e)
        print(Stack)


while True:
    print('Enter 1 to add to stack. 2 to remove from Stack. 3 to end task')
    choice = int(input())
    if choice == 1:
        push_to_stack()
    elif choice == 2:
        pop_from_stack()
    elif choice == 3:
        break
    else:
        print("choose correct option")


