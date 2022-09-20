# implementing binary Tree
class binaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    # insert into binary tree
    def insert(self, data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        if self.leftChild:
            if self.rightChild:
                self.leftChild.insert(data)
            else:
                self.rightChild = binaryTree(data)
                return
        else:
            self.leftChild = binaryTree(data)

    # preOrder transversal
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()


root = binaryTree(None)
root.insert(21)
root.insert(10)
root.insert(30)
root.insert(5)
root.insert(12)
root.insert(25)
root.insert(100)
root.insert(3)
root.insert(7)
root.preorder()

