# Binary Search Tree
class node:
  def __init__(self,value=None):
    self.value=value
    self.left_child=None
    self.right_child=None
    self.parent=None # pointer to parent node in tree

#created BTS class
class binary_search_tree:
  def __init__(self):
    self.root=None

# created the insert function
  def insert(self,value):
    if self.root==None:
      self.root=node(value)
    else:
      self._insert(value,self.root)

# created the recursive insert function
  def _insert(self,value,cur_node):
    if value<cur_node.value:
      if cur_node.left_child==None:
        cur_node.left_child=node(value)
        cur_node.left_child.parent=cur_node # set parent
      else:
        self._insert(value,cur_node.left_child)
    elif value>cur_node.value:
      if cur_node.right_child==None:
        cur_node.right_child=node(value)
        cur_node.right_child.parent=cur_node # set parent
      else:
        self._insert(value,cur_node.right_child)
    else:
      print ("Value already in tree!")

# created the print tree function
  def print_tree(self):
    if self.root!=None:
      self._print_tree(self.root)

  # created the recursive print tree function
  def _print_tree(self,cur_node):
    if cur_node!=None:
      self._print_tree(cur_node.left_child)
      print (str(cur_node.value))
      self._print_tree(cur_node.right_child)

# created the print tree height function
  def height(self):
    if self.root!=None:
      return self._height(self.root,0)
    else:
      return 0

# created the recursive print tree height function
  def _height(self,cur_node,cur_height):
    if cur_node==None: return cur_height
    left_height=self._height(cur_node.left_child,cur_height+1)
    right_height=self._height(cur_node.right_child,cur_height+1)
    return max(left_height,right_height)

# created the find a value function
  def find(self,value):
    if self.root!=None:
      return self._find(value,self.root)
    else:
      return None

# created the recursive find a value function
  def _find(self,value,cur_node):
    if value==cur_node.value:
      return cur_node
    elif value<cur_node.value and cur_node.left_child!=None:
      return self._find(value,cur_node.left_child)
    elif value>cur_node.value and cur_node.right_child!=None:
      return self._find(value,cur_node.right_child)

 # created the delete a value function
  def delete_value(self,value):
    return self.delete_node(self.find(value))

# created the delete a node function
  def delete_node(self,node):
    # avoid deleting a node not found in the tree
    if node==None or self.find(node.value)==None:
      print ("Node to be deleted not found in the tree!")
      return None


# created returns the node with min value function
    def min_value_node(n):
      current=n
      while current.left_child!=None:
        current=current.left_child
      return current

# vreated returns the number of children for the specified node function
    def num_children(n):
      num_children=0
      if n.left_child!=None: num_children+=1
      if n.right_child!=None: num_children+=1
      return num_children

# created search for a node function
  def search(self,value):
    if self.root!=None:
      return self._search(value,self.root)
    else:
      return False

# created recursive search for a node function
  def _search(self,value,cur_node):
    if value==cur_node.value:
      return True
    elif value<cur_node.value and cur_node.left_child!=None:
      return self._search(value,cur_node.left_child)
    elif value>cur_node.value and cur_node.right_child!=None:
      return self._search(value,cur_node.right_child)
    return False

my = binary_search_tree()
my.print_tree()