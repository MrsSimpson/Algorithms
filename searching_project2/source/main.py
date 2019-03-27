from binary_search_tree import *

def print_node(value, node):
    if node is None:
        print("The value", value, "does not exist in the tree.")
    else:
        print("Value", value, "exists in the tree at address ",node)

def main():

    #the array are the tree values given in the prompt by Dr. Zou for project 2
    test_data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    #create binary search tree
    binary_tree1 = Tree()

    #store the elements of the array into nodes and add to the binary search tree.
    for element in test_data:
        a_node = Node(element)
        binary_tree1.insert_node(a_node)

    #print the binary tree if one exist using in order traversal
    if binary_tree1 is None:
        print("Tree is empty")
    else:
        in_order_traversal(binary_tree1.root)

    #search the tree for values
    find_val = tree_search(binary_tree1.root, 2)
    print_node(2, find_val)
    find_val = tree_search(binary_tree1.root, 4)
    print_node(4, find_val)
    find_val = tree_search(binary_tree1.root, 99)
    print_node(99, find_val)


    #find the min and max values of the tree
    print("The minimum value the tree contains is", binary_tree1.find_minimum(binary_tree1.root).key)
    print("The maximum value the tree contains is", binary_tree1.find_maximum(binary_tree1.root).key)

    #find the successors for nodes in the tree if a successor exists

    #find the successor for a node with two children (the root)
    print((binary_tree1.find_successor(binary_tree1.root)).key)
    #find the successor for a node with no right_child
    print((binary_tree1.find_successor(binary_tree1.find_minimum(binary_tree1.root))).key)
    #find a successor for a node with one child
    print((binary_tree1.find_successor(binary_tree1.root.left_child.right_child)).key)
    #prove that the maximum value of the tree has no successor
    successor = binary_tree1.find_successor(binary_tree1.find_maximum(binary_tree1.root))
    if successor is not None:
        print(successor.key)
    else:
        print("Maximum node has no successor \n")

    #insert nodes into the tree
    binary_tree1.insert_node(Node(5))
    binary_tree1.insert_node(Node(0))
    binary_tree1.insert_node(Node(9))
    binary_tree1.insert_node(Node(19))
    binary_tree1.insert_node(Node(15))

    print("\n Numbers 5, 0, 9, 19, and 15 have been inserted into the tree. I will now print them in_order:")
    in_order_traversal(binary_tree1.root)


    #prove that a node with two children can successfully be deleted
    print("\n Deleting the Nodes that were added")
    binary_tree1.delete_node(tree_search(binary_tree1.root, 5))
    binary_tree1.delete_node(tree_search(binary_tree1.root, 0))
    binary_tree1.delete_node(tree_search(binary_tree1.root, 9))
    binary_tree1.delete_node(tree_search(binary_tree1.root, 19))
    binary_tree1.delete_node(tree_search(binary_tree1.root, 15))
    in_order_traversal(binary_tree1.root)


    #prove that the delete function will properly handle deleting nodes with one child, two children, and no children
    print("Delete a node with one child")
    binary_tree1.delete_node((binary_tree1.root.left_child.right_child))
    in_order_traversal(binary_tree1.root)
    print("Deleting a node that has two children: ")
    binary_tree1.delete_node(binary_tree1.root)
    in_order_traversal(binary_tree1.root)
    print("Deleting a node that has no children ")
    binary_tree1.delete_node(binary_tree1.find_maximum(binary_tree1.root))
    in_order_traversal(binary_tree1.root)

main()