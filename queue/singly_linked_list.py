class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        if(self.tail == None): #Empty List
            self.head = self.tail = Node(value)
        else: #One or more items in list
            oldtail = self.tail
            self.tail = Node(value)
            oldtail.set_next(self.tail)

    def add_to_head(self, value):
        if(self.head == None): #Empty List
            self.head = self.tail = Node(value)
        else: #One or more items in list
            self.head = Node(value, self.head)

    def remove_head(self):
        if(self.head == None): #Empty List Case
            return None
        elif(self.head != self.tail): # More than one item in list
            oldhead = self.head
            self.head = oldhead.get_next()
            return oldhead.get_value() #returns new head value
        else: #One item in list
            value = self.head.get_value()
            self.head = self.tail = None
            return value

    def contains(self, value):
        check_node = self.head

        while check_node:
            if(check_node.get_value() == value):
                return True
            else:
                check_node = check_node.get_next()

        return False
    
    def get_max(self):
        if(self.head):
            value = self.head.get_value()
        else:
            return None

        check_node = self.head.get_next()
        
        while check_node:
            if(check_node.get_value() > value):
                value = check_node.get_value()

            check_node = check_node.get_next()

        return value

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
