"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   >>>Implenting it with an array is much easier since you can use built in array methods.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList
from stack import Stack #For the stretch

class QueueA:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.pop(0)

class QueueB:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.remove_head()

        return None

### STRETCH ?? ###
class Queue:
    def __init__(self):
        self.storage = Stack()

    def __len__(self):
        return self.storage.__len__()

    def enqueue(self, value): # Hard work could have been here, but chose to put it into dequeue
        self.storage.push(value)

    def dequeue(self):
        reversed_storage = Stack()

        while True:
            value = self.storage.pop()

            if(value is not None):
                reversed_storage.push(value)
            else:
                break

        dequeue_value = reversed_storage.pop()

        while True:
            value = reversed_storage.pop()

            if(value is not None):
                self.storage.push(value)
            else:
                break

        return dequeue_value
