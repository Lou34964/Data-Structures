"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value

    # reference to the next node in the list
    self.next_node = next_node
    self.next = None

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def Length(self):
#         if is_empty(self)
#     def add_to_end(self, value):
#         new_node = Node(value)
        
#         if not self.head:
#             self.head = new_node

#         else:
#             current = self.head
#             while current.get_next() is not None:
#                 current = current.get_next()
#             current.set_next(new_node)

#     def remove_from_head(self):
#         if not self.head:
#             return None
#         else:
#             value = self.head.get_value()

#             self.head = self.head.get_next()
#             return value



class Stack:
    def __init__(self):
        #self.size = 0
        self.head = None

    def __len__(self):
        current = self.head
        
        length = 0

        while current:
            length += 1
            current = current.next

        return length
        #pass

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        
        #pass

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped
