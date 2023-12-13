# Linked List constructor

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def print_list(self):
        str_output = ''
        temp = self.head
        while temp:
            str_output += str(temp.data)+'->'
            temp = temp.next
        return str_output    
            
    def append(self,data):
        new_node = Node(data)
        
        if self.length == 0:
            self.head = self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length = 0
            return temp
        else:    
            prev = temp = self.head
            while temp.next:
                prev = temp 
                temp = temp.next
            self.tail = prev 
            self.tail.next = None
            self.length -= 1
            return temp
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp
    
    def get(self,index):
        temp = self.head
        if index < 0 or index >= self.length:
            raise ValueError('Invalid index')
        if index == 0:
            return temp.data
        else:
            for _ in range(index):
                temp = temp.next
            return temp.data
            
    def set_value(self,index,data):
        temp = self.head
        if index < 0 or index >= self.length:
            raise ValueError('Invalid index')
        if index == 0:
            temp.data = data
        else:
            for _ in range(index):
                temp = temp.next
            temp.data = data
        

    def insert(self,index,data):
        new_node = Node(data)
        prev = temp = self.head
        if index < 0 or index >= self.length:
            raise ValueError('Invalid index')
        if index == 0:
            self.prepend(new_node)
        if index == self.length -1:
            self.append(new_node)
        else:
            for _ in range(index):
                prev = temp
                temp = temp.next
            prev.next = new_node
            new_node.next = temp
            self.length += 1 
    
    def remove(self,index):
        prev = temp = self.head
        if index < 0 or index >= self.length:
            raise ValueError('Invalid index')
        if index == 0:
            self.pop_first()
        if index == self.length -1:
            self.pop()
        else:
            for _ in range(index):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            
    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self
        if self.length == 2:
            temp = self.head
            self.head = self.tail
            self.tail = temp
        else:
            before = None
            current = self.head
            after = current.next
            
            temp = self.head
            self.head = self.tail
            self.tail = temp
            
            while after:
                current.next = before
                before = current
                current = after
                after = after.next
            current.next = before
