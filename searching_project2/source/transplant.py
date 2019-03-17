from tree_class import Tree
from node_class import Node

def transplant(tree, node, node_2):
    if node.parent is None:
        tree.root = node_2
    elif node == node.parent.left_child:
        node.parent.left_child = node_2
    else:
        node.parent.right_child = node_2
    if node_2 is not None:
        node_2.parent = node.parent