# Implementation of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pref = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    # transversing through nodes and printing node data :

    # transversing from head
    def display_from_head(self):
        if self.head is None:
            print('doubly linked list has no node')
        else:
            head_node = self.head
            while head_node is not None:
                print('<===', head_node.data, '===>', end=' ')
                head_node = head_node.next

    # transversing from tail
    def display_from_tail(self):
        if self.head is None:
            print('doubly linked list has no node')
        else:

            head_node = self.head
            while head_node.next is not None:
                head_node = head_node.next
            while head_node is not None:
                print('<===', ' ', head_node.data, '===>', end=' ')
                head_node = head_node.pref

    # adding new node as head
    def add_node(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('head node exist')

    # adding new node from head
    def add_from_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.pref = new_node
            self.head = new_node

    # adding new node from the tail
    def add_from_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            head_node = self.head
            while head_node.next is not None:
                head_node = head_node.next
            head_node.next = new_node
            new_node.pref = head_node

    # adding new node after any position x
    def add_from_after(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('list is empty')
            return
        if x == self.head.data:
            self.head = new_node
        else:
            head_node = self.head
            while head_node is not None:
                if head_node.data == x:
                    break
                head_node = head_node.next
            if head_node is None:
                print('node not found')
            else:
                new_node.next = head_node.next
                head_node.next = new_node
                new_node.pref = head_node
                head_node.pref = new_node

    # adding new node after any position x
    def add_from_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('list is empty')
            return
        if x == self.head.data:
            self.head = new_node
        else:
            head_node = self.head
            while head_node.next is not None:
                if x == head_node.next.data:
                    break
                head_node = head_node.next
            if head_node.next is None:
                print('node not found')
            else:
                new_node.next = head_node.next
                head_node.next = new_node
                new_node.pref = head_node
                head_node.next.pref = new_node

    # remove node from head
    def remove_head(self):
        if self.head is None:
            print('list is empty')
        else:
            self.head = self.head.next
            self.head.pref = None

    # removing node from tail
    def remove_tail(self):
        if self.head is None:
            print('list is empty')
        else:
            head_node = self.head
            while head_node.next is not None:
                head_node = head_node.next
            head_node.pref.next = None

    # removing from any position based on x value
    def remove_from_x_position(self, x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.pref = None
            return
        head_node = self.head
        while head_node.next is not None:
            if x == head_node.data:
                break
            head_node = head_node.next
        if head_node.next is not None:
            head_node.pref.next = head_node.next
            head_node.next.pref = head_node.pref
        else:
            if head_node.data == x:
                head_node.pref.next = None
            else:
                print('node not found')


D = doubly_linked_list()
D.add_node(1)
D.add_from_tail(2)
# D.add_from_head(5)
# D.add_from_after(0, 1)
# D.add_from_before(0, 1)
# D.remove_head()
# D.remove_head()
D.remove_from_x_position(2)
D.remove_from_x_position(1)
# D.remove_tail()
# D.remove_tail()
# D.display_from_tail()
print()
D.display_from_head()
