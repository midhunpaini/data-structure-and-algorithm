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

    def reverse(self):
        if self.head is None:
            return
        
        current = self.head
        self.tail = current
        prev = None
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

            

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



    def remove_dups(self):
        if self.head is None:
            return
        s = set()
        current = self.head
        s.add(current.data)
        prev = current
        current = current.next

        while current:
            if current.data in s:
                if current == self.tail:
                    self.tail = prev
                    prev.next = None
                    break
                else:
                    prev.next = current.next
            else:
                s.add(current.data)
                prev = current

            current = current.next
            

        
        
    def display(self):
        current = self.head

        while current:
            print(current.data, end=', ')
            current = current.next

linked_list = LinkedList()

for i in range(10):
    linked_list.append(i)

linked_list.display()
linked_list.reverse()
print()
linked_list.display()






