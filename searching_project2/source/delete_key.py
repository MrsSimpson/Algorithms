from tree_class import Tree
from node_class import Node
from find_successor import find_successor
from transplant import transplant
from find_min import find_minimum


def delete_node(tree, node):
    if node.left_child is None:
        transplant(tree, node, node.right_child)
    elif node.right is None:
        transplant(tree, node, node.left_child)
    else:
        new_node = find_minimum(node.right_child)
        if new_node.parent != node:
            transplant(tree, new_node, new_node.right_child)
            new_node.right_child = node.right_child
            new_node.right.parent = new_node
        transplant(tree, node, new_node)
        new_node.left_child = node.left_child
        new_node.left_child.parent = new_node





def delete_key(node):
    if node.left_child is None and node.right_child is None:
        node = None

    elif node.left_child is not None and node.right_child is None:
        parent_node = node.parent
        node.left_child.parent = parent_node
        node = node.left_child

    elif node.right_child is not None and node.left_child is None:
        parent_node = node.parent
        node = node.right_child

    elif node.left_child is not None and node.right_child is not None:
        successor_node = find_successor(node.right_child)
