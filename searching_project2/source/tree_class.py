from node_class import Node


class Tree:
    def __init__ (self):
        self.root = None

    def insert(self, num):
        if self.root is None:
            return self.root.insert(num)

        else:
            self.root = Node(num)

    def node_exists(self, num):
        if self.root is not None:
            return self.root.node_exists(num)
        else:
            return False

