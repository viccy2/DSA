# singly linked implementation list using linked list
# creating node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating linked list
class Linked_list:
    def __init__(self):
        self.head = None

    # transversing through all nodes are printing all nodes
    def display_linked_list(self):
        head_node = self.head
        if head_node is None:
            print("Node is empty")
        else:
            while head_node is not None:
                print(head_node.data, "===>", end=" ")
                head_node = head_node.next

    # adding new node at the head of node
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # adding new node at the tail of node
    def add_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            head_node = self.head
            while head_node.next is not None:
                head_node = head_node.next
            head_node.next = new_node

    # adding new node between nodes after given node
    def add_between_after(self, data, x):
        head_node = self.head
        while head_node is not None:
            if x == head_node.data:
                break
            head_node = head_node.next
        if head_node is None:
            print("Node doesnt exist")
        else:
            new_node = Node(data)
            new_node.next = head_node.next
            head_node.next = new_node

    # adding new node between nodes before given node
    def add_between_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('Node is empty')
            return
        if self.head.data == x:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            head_node = self.head
            while head_node.next is not None:
                if head_node.next.data == x:
                    break
                head_node = head_node.next
            if head_node.next is None:
                print('Node does not exist')
            else:
                new_node.next = head_node.next
                head_node.next = new_node

    # deleting nodes:

    # deleting node from the front
    def delete_front(self):
        if self.head is None:
            print('cant delete from empty node')
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print('node is empty')
        else:
            while self.head.next is not None:
                self.head = self.head.next
                return
            self.head.next = self.head
            if self.head.next is None:
                print('node not found')
            else:
                print('a')


L_list = Linked_list()
L_list.add_front(10)
L_list.add_front(20)
# L_list.add_front(30)
# L_list.add_end(40)
# L_list.add_between_after(4, 40)
# L_list.add_between_before(4, 40)
# L_list.delete_front()
L_list.delete_end()
L_list.display_linked_list()
