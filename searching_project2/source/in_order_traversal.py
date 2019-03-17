from tree_class import Tree
from node_class import Node


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left_child)
        print node.key
        in_order_traversal(node.right_child)

    else:
        print("Tree is empty")
        return
