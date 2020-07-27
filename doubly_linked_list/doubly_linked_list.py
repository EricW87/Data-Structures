"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if(self.length == 0): #Empty List
            self.head = self.tail = ListNode(value)
        else: #One or more items in list
            self.head = ListNode(value, None, self.head)
            self.head.next.prev = self.head

        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if(self.length == 0):
            return None
        
        value = self.head.value

        if(self.length == 1):
            self.head = self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if(self.length == 0): #Empty List
            self.head = self.tail = ListNode(value)
        else: #One or more items in list
            self.tail.next = ListNode(value, self.tail, None)
            self.tail = self.tail.next

        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if(self.length == 0):
            return None
        
        value = self.tail.value

        if(self.length == 1):
            self.head = self.tail = None
            self.length = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if(self.length <= 1):
            return

        if(node.prev == None): #already in front
            return

        if(node.next == None): #node is tail
            self.tail = node.prev
            self.tail.next = None
        else: #node is in the middle somewhere
            node.prev.next = node.next #Connect node behind node to node in front of node
            node.next.prev = node.prev #Connect node in front of node to node behind node

        #stick node in front of list
        node.prev = None
        self.head.prev = node
        node.next = self.head
        self.head = node



        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if(self.length <= 1):
            return

        if(node.next == None): #already at end
            return

        if(node.prev == None): #node is head
            self.head = node.next
            self.head.prev = None
        else: #node is in the middle somewhere
            node.prev.next = node.next #Connect node behind node to node in front of node
            node.next.prev = node.prev #Connect node in front of node to node behind node

        #stick node to the end of the list
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if(self.length == 0): #empty list
            return

        if(self.length == 1): #One item in list
            self.head = self.tail = None
            self.length -= 1
        elif(node.next == None): #Is tail
            self.remove_from_tail()
        elif(node.prev == None): #Is head
            self.remove_from_head()
        else: #somewhere in the middle
            node.prev.next = node.next #Connect node behind node to node in front of node
            node.next.prev = node.prev #Connect node in front of node to node behind node
            self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        value = 0

        if(self.head):
            value = self.head.value
        else:
            return None

        check_node = self.head.next
        
        while check_node:
            if(check_node.value > value):
                value = check_node.value

            check_node = check_node.next

        return value