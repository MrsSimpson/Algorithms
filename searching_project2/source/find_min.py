from tree_class import Tree
from node_class import Node

def find_minimum(node):
    while node.left_child is not None:
        node = node.left_child
    return node