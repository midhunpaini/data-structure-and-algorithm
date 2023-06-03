class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def add_node(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node 

        return    
        
        
    def insert(self,pos,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        if self.tail.data == pos:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return

        current = self.head
        while current:
            if current.data == pos:
                new_node.prev = current
                new_node.next = current.next
                current.next = new_node
            current = current.next
        return


    def display(self):
        if self.head is None:
            return

        current  = self.head
        while current:
            print(current.data,end=', ')
            current = current.next
        return


linked_list = LinkedList()

for i in range(10,19):
    linked_list.add_node(i)

linked_list.insert(18,25)
print('Head: ', linked_list.head.data)
print('Tail: ', linked_list.tail.data)
linked_list.display()