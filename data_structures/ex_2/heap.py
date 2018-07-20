def heapsort(arr):
  """
  create a heap using Heap().insert and for loop.
  at this point the first element in the heap should always have the greatest value,
  the items after will not be in order.  
  create empty list 
  could just use sorted, but that is cheating....
  while loop over heap, add first item then delete it.
  append adds to end. python function insert will add at any location. 
  x.insert({location to insert using zero index}, {value to insert})
  """
  sc_heap = Heap()
  answer = []

  for i in arr:
    sc_heap.insert(i)
  # print(sc_heap.storage, sc_heap.size, sc_heap.get_max())
  
  while sc_heap.get_size() > 0:
    answer.insert(0, sc_heap.get_max())
    sc_heap.delete()
  
  # print(answer)
  return answer

class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1