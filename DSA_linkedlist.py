# Creating A linked List

# Create Node Class
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Create Linkedlist class
class linked_list:
    def __init__(self):
        self.head = node()

    # function to add to list

    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            current_node.next = new_node

        # function show the length of the list

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total

        # function to display all elements

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)


my_list = linked_list()
my_list.display()
my_list.append(11)
my_list.display()
