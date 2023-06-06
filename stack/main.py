class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node
        return
    
    def pop(self):
        if self.top is None:
            print('Stack Underflow')
            return
        self.top = self.top.next

    def display(self):
        current = self.top
        while current:
            print(current.data, end=', ')
            current = current.next


stack = Stack()

for i in range(10):
    stack.push(i)

stack.display()
stack.pop()
print()
stack.display()