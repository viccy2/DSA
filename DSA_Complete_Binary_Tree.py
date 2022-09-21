# implementing complete binary tree using recursion
class CompleteBT:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    # insert intO CBT
    def insert(self, data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        if self.leftChild is None:
            self.leftChild = CompleteBT(data)
        else:
            if self.rightChild is None:
                self.rightChild = CompleteBT(data)
            else:
                return
        if self.leftChild:
            a = self.leftChild
            if a.leftChild is None:
                print('eee')
                # self.leftChild.insert(data)
        else:
            a = self.leftChild
            if a.rightChild is None:
                self.leftChild.insert(data)
        if self.rightChild:
            self.rightChild.insert(data)

    # preorder transversal
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


root = CompleteBT(None)
root.insert(2)
root.insert(3)
root.insert(5)
root.insert(6)

root.preorder()
