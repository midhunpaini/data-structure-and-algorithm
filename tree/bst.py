class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        new_node = BST(data)
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(data)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)


    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)

        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
        else:
            return True


    def remove(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_node = self.right.find_min()
                self.data = min_node.data
                self.right = self.right.remove(min_node.data)
        return self

    def find_min(self):
        if self.left is None:
            return self
        return self.left.find_min()


tree = BST(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(21)
tree.insert(31)
tree.insert(11)
tree.insert(12)

tree.in_order_traversal()
tree.remove(21)

tree.in_order_traversal()

