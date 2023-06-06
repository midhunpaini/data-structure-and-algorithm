class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node
    

    def dequeue(self):
        if self.front is None:
            return
        
        self.front = self.front.next
         


    def display(self):
        if self.front is None:
            return
        current = self.front
        while current:
            print(current.data,end=', ')
            current = current.next


q = Queue()

for i in range(10):
    q.enqueue(i)

q.display()
q.dequeue()
q.dequeue()
print()
q.display()
        


        

