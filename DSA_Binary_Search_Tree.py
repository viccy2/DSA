# Implementing Binary Search Tree
class BST:
    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None

    # inserting to tree
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BST(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BST(data)

    # searching node in BST
    def search(self, data):
        if self.key is None:
            print('Tree is empty')
            return
        if self.key == data:
            print('Node is present in BST')
            return
        if data < self.key:
            if self.left_child:
                self.left_child.search(data)
            else:
                print('Node is not present in BST')
        else:
            if self.right_child:
                self.right_child.search(data)
            else:
                print('Node is not present in BST')


root = BST(None)
root.insert(2)
lists = [1, 3, 4, 5, 6, 7, 8, 9]
for i in lists:
    root.insert(i)
root.search(30)
