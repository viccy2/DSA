# Binary Search Tree
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

    # traversing through tree
    # pre-order
    def preorder(self):
        print(self.key, end=' ')
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    # in-order
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key, end=' ')
        if self.right_child:
            self.right_child.inorder()

    # post-order
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key, end=' ')

    # deleting node from tree
    def delete(self, data, current_node):
        if self.key is None:
            print('Tree is empty')
            return
        if data < self.key:
            if self.left_child:
                self.left_child = self.left_child.delete(data, current_node)
            else:
                print('node does not exist')
        elif data > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete(data, current_node)
            else:
                print('node does not exist')
        else:
            # if data has one child node
            if self.left_child is None:
                a = self.right_child
                if data == current_node:
                    self.key = a.key
                    self.left_child = a.left_child
                    self.right_child = a.right_child
                    self.right_child = None
                    return
                self = None
                return a
            if self.right_child is None:
                a = self.left_child
                if data == current_node:
                    self.key = a.key
                    self.left_child = a.left_child
                    self.right_child = a.right_child
                    self.left_child = None
                    return
                self = None
                return a
            # if data has two child nodes
            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.delete(node.key, current_node)
        return self

    # print the node with minimum key in tree
    def min(self):
        if self.key is None:
            print('tree is empty')
        else:
            current_node = self
            while current_node.left_child:
                current_node = current_node.left_child
            print(current_node.key)

    # print the node with maximum key in tree
    def max(self):
        if self.key is None:
            print('tree is empty')
        else:
            current_node = self
            while current_node.right_child:
                current_node = current_node.right_child
            print(current_node.key)


# function to count all nodes in tree
def count(node):
    if node is None:
        return 0
    return 1 + count(node.left_child) + count(node.right_child)


root = BST(None)
root.insert(2)
lists = [1, 3, 4, 5, 6, 7, 8]
for i in lists:
    root.insert(i)
print('pre-order form')
root.preorder()
print(' ')
print('In-order form')
root.inorder()
print(' ')
print('Post-order form')
root.postorder()
print(' ')
# delete key / node method
if count(root) > 1:
    root.delete(2, root.key)
else:
    print('can not delete root node')
