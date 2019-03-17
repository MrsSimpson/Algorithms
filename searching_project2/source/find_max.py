from tree_class import Tree
from node_class import Node

def find_maximum(node):
    while node.right is not None:
        node = node.right
    return node