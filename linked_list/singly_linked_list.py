class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
          

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, pos, data):
        new_node = Node(data)
        current = self.head
        if self.tail.data == pos:
            self.tail.next = new_node
            self.tail = new_node
            return
        while current:
            if current.data == pos:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                    current.next = None
                    return
                else:
                    current.next = current.next.next
                    return
            current = current.next
                   
        
        
    def display(self):
        current = self.head

        while current:
            print(current.data, end=', ')
            current = current.next


linked_list = LinkedList()

for i in range(1, 6):
    linked_list.append(i)

linked_list.insert(5, 25)
linked_list.prepend(100)
linked_list.prepend(99)
print(linked_list.tail.data,' :tail')
linked_list.display()


