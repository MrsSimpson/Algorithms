#The tree class has the root attribute to hold the starting node of the tree.
#The tree class also contains methods insert_node, find_maximum, find_minimum,
#find_successor, and transplant and delete node.
class Tree:
    def __init__(self):

        self.root = None

    # Insert_node method finds the appropriate position to place the node. The method searches
    # through the tree until it finds an appropriate leaf node. If the node's key is less
    # than the leaf nodes key it will be the left_child, if it's greater, the leaf node's
    # right child will be the node passed in.
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


    # simply find the maximum node of tree by looking at the most right child of the tree.
    def find_maximum(self, node):
        while node.right_child is not None:
            node = node.right_child
        return node

    # simply find the minimum node of tree by looking at the most left child.
    def find_minimum(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    # find_successor finds the next in line node whose value succeeds the node passed in.
    # if the node has a right child, the successor should be the minimum node of the node's
    # right child. If the parent_node is not Null and the node is the parent_node's
    # right_child step up to the parent node. If parent node is none when the while
    # loop finishes then the node that was passed in does not have a successor.
    def find_successor(self, node):
        if node.right_child is not None:
            return self.find_minimum(node.right_child)
        parent_node = node.parent
        while parent_node is not None and node is parent_node.right_child:
            node = parent_node
            parent_node = parent_node.parent
        return parent_node

    # transplant node is called when a node needs to be deleted. The transplant node method
    # ensures that the binary search tree structure is maintained by finding the
    # appropriate way to transplant subtree of the node that will be deleted. If the
    # node is deleted without transplant being used, we are likely to have problems with the
    # tree structure.
    def transplant(self, node, node_2):
        if node.parent is None:
            self.root = node_2
        elif node == node.parent.left_child:
            node.parent.left_child = node_2
        else:
            node.parent.right_child = node_2
        if node_2 is not None:
            node_2.parent = node.parent

    # Delete node must check one of three cases before deleting a node. It must check
    # to see if the node has one child(left or right), if so the transplant node is
    # called on the appropriate child. If it has more than one child, the minimum key
    # node must be found in the tree. if the minimum node's parent is not the node that we
    # want to delete, then we must call transplant on the min nodes right child because
    # it should be the successor of the node that we want to delete.
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


#The node class will create object nodes that contain the key(value) of the node,
#the parent(which will contain the address to the parent node, the left_child(address) and
#right_child(address) of the node.The methods of the Node class are tree_search to see if
#the tree contains a node with a particular key. The method in_order_traversal will print
#out all the nodes of the class in order.
class Node:
    def __init__(self, num):

        self.key = num
        self.parent = None
        self.left_child = None
        self.right_child = None


#Searches the tree for a given value
def tree_search(node, value):
    if node is None or value is node.key:
        return node
    if value < node.key:
        return tree_search(node.left_child, value)
    else:
        return tree_search(node.right_child, value)

#prints the tree in order
def in_order_traversal(node):

    if node is not None:
        in_order_traversal(node.left_child)
        print(node.key)
        in_order_traversal(node.right_child)




