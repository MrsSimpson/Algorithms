class Tree:
    def __init__(self):

        self.root = None

    def insert_node(self, a_node):
        parent_node = None
        current_node = self.root
        while current_node is not None:
            parent_node = current_node
            if a_node.key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
            a_node.parent = parent_node

        if parent_node is None:
            self.root = a_node  # if tree is empty
        elif a_node.key < parent_node.key:
            parent_node.left_child = a_node
        else:
            parent_node.right_child = a_node

    def find_maximum(self, node):
        while node.right_child is not None:
            node = node.right_child
        return node

    def find_minimum(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def find_successor(self, node):
        if node.right_child is not None:
            return self.find_minimum(node.right_child)
        parent_node = node.parent
        while parent_node is not None and node is parent_node.right_child:
            node = parent_node
            parent_node = parent_node.parent
        return parent_node

    def transplant(self, node, node_2):
        if node.parent is None:
            self.root = node_2
        elif node == node.parent.left_child:
            node.parent.left_child = node_2
        else:
            node.parent.right_child = node_2
        if node_2 is not None:
            node_2.parent = node.parent

    def delete_node(self, node):
        if node.left_child is None:
            self.transplant(node, node.right_child)
        elif node.right_child is None:
            self.transplant(node, node.left_child)
        else:
            new_node = self.find_minimum(node.right_child)
            if new_node.parent != node:
                self.transplant(new_node, new_node.right_child)
                new_node.right_child = node.right_child
                new_node.right_child.parent = new_node
            self.transplant(node, new_node)
            new_node.left_child = node.left_child
            new_node.left_child.parent = new_node


class Node:
    def __init__(self, num):

        self.key = num
        self.parent = None
        self.left_child = None
        self.right_child = None


def tree_search(node, value):
    if node is None or value is node.key:
        return node
    if value < node.key:
        return tree_search(node.left_child, value)
    else:
        return tree_search(node.right_child, value)


def in_order_traversal(node):

    if node is not None:
        in_order_traversal(node.left_child)
        print(node.key)
        in_order_traversal(node.right_child)




