class Node:
    def __init__(self, num):

        self.key = num
        self.parent = None
        self.left_child = None
        self.right_child = None


    def insert_node(self, bi_tree, a_node):
        parent_node = None
        current_node = bi_tree.root
        while current_node is not None:
            parent_node = current_node
            if a_node.key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        current_node.parent = parent_node

        if parent_node is None:
            bi_tree.root = a_node  #if tree is empty
        elif a_node.key < parent_node.key:
            parent_node.left_child = a_node
        else:
            parent_node.right_child = a_node

    def tree_search(self, node, value):
        if node is None or value is node.key:
            return node
        if value < node.key:
            return self.tree_search(node.left_child, value)
        else:
            return self.tree_search(node.right_child)


    def find_node(self, num):
        if num is self.key:
            return True
        elif num < self.key:
            if self.left_child is None:
                return False
            else:
                return self.left_child.find_node(num)

        else:
            if self.right_child is None:
                return False
            else:
                return self.right_child.find_node(num)

