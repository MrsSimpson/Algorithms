from tree_class import Tree
from node_class import Node
from find_min import find_minimum


def find_successor(node):
    if node.right_child is not None:
        return find_minimum(node.right_child)
    parent_node = node.parent
    while parent_node is not None and node == parent_node.right_child:
        node = parent_node
        parent_node = parent_node.parent
    return parent_node