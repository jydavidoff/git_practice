# With Blossom, we want to give people lightning fast access to 
# all of the possible meanings of their favorite flowers.
#
# Blossom implements a hash map to relate the names of flowers 
# to their meanings. Separate chaining is used in order to avoid 
# collisions when the hashing function collides the names of two 
# flowers. The Linked List data structure is implemented for each 
# of these separate chains.

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions
class HashMap:
  
  # constructor takes in size and creates a list of that number
  # of items, all set to empty LinkedLists
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)]
    
  # use this string representation for debugging  
  def __repr__(self):
    result = ""
    index = 0
    for list in self.array:
      result += "index: " + str(index) + "\n" 
      for item in list:
        result += str(item)
      result += "\n"
      index += 1
    return result
  
  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    # check to see if this key already exists
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    # this key was not found, insert a new node
    list_at_array.insert(payload)
    
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None
    
# create a new instance of HashMap
blossom = HashMap(len(flower_definitions))
for fd in flower_definitions:
  blossom.assign(fd[0], fd[1])

#print(blossom)

print(blossom.retrieve("rose"))
