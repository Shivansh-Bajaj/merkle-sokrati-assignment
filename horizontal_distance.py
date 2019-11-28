
# Tree Node Class
class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

# to build tree from level order traversal input
class Tree:
  def __init__(self):
    self.root = None

  def insert_level_order(self, arr, root, i, n):
    if i < n:
      if arr[i] == -1:
        return root
      temp = Node(arr[i])
      root = temp
      root.left = self.insert_level_order( arr, root.left, 2 * i + 1, n)
      root.right = self.insert_level_order( arr, root.right, 2 * i + 2, n)
    return root

  def build(self, arr):
    for val in arr:
      n = len(arr)
      self.root = self.insert_level_order(arr, self.root, 0, n)
      return self.root

# search horizonal distance class
class HorizontalDistance:

  # recursive search for val1 and val2 in same level and return distance
  def level_order_traversal(self, level_arr, val1, val2):
    child_arr = []
    indexes = [-1, -1] # to keep track of values
    if len([i for i in level_arr if i != None]) == 0:
      return -1
    for i in range(len(level_arr)):
      if level_arr[i] == None:
        child_arr.append(level_arr[i])
        child_arr.append(level_arr[i])
        continue
      if level_arr[i].key == val1 and indexes[0] == -1:
        indexes[0] = i
      if level_arr[i].key == val2 and indexes[1] == -1:
        indexes[1] = i
      child_arr.append(level_arr[i].left)
      child_arr.append(level_arr[i].right)
    if indexes[0] != -1 and indexes[1] != -1:
      return abs(indexes[0] - indexes[1]) # calculate distance in case of solution
    return self.level_order_traversal(child_arr, val1, val2)

  # find val1 and val2 distance in provided tree
  def find(self, root, val1, val2):
    if root == None or val1 == None or val2 == None:
      return -1
    if not isinstance(root, Node):
      return -1
    if val1 == val2:
      return 0
    return self.level_order_traversal([root], val1, val2)


