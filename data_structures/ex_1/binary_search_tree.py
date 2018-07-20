class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # print(self.value)
    cb(self.value)    
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    queue = [self]
    # for i in queue:
    #   print('test',i.value)
    
    while len(queue) > 0:
      
      if queue[0].left:
        print("left", queue[0].value, queue[0].left.value)
        queue.append(queue[0].left)
      if queue[0].right:
        print("right", queue[0].value, queue[0].right.value)
        queue.append(queue[0].right)
        
      print(queue[0].value)
      cb(queue[0].value)      
      queue.pop(0)
    


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
