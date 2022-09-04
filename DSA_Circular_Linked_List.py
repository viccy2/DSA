class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class link:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('node is null')
        else:
            head = self.head
            while head is not None:
                print(head.data, '=>', end=' ')
                head = head.next

    def add_front(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def add_tail(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = new

    def add_b(self, data, x):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            head = self.head
            while head.next is not None:
                if x == head.next.data:
                    break
                head = head.next
            if head.next is None:
                print('node not found')
            else:
                new.next = head.next
                head.next = new


L = link()
L.add_front(1)
L.add_front(2)
L.add_tail(3)
L.add_tail(4)
L.add_b(1, 1)

L.display()
