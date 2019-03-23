from binary_search_tree import *


def main():

    test_data = [2]
    test_data2 = [40, 22]
    test_data3 = [50, 11, 4, 90, 70, 2, 89]
    test_data4 = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    binary_tree1 = Tree()

    for element in test_data4:
        a_node = Node(element)
        binary_tree1.insert_node(a_node)

    if binary_tree1 is None:
        print("Tree is empty")
    else:
        in_order_traversal(binary_tree1.root)

    print(tree_search(binary_tree1.root, 2))
    print(binary_tree1.find_maximum(binary_tree1.root).key)

    print(tree_search(binary_tree1.root, 3))
    print((binary_tree1.find_minimum(binary_tree1.root)).key)

    print((binary_tree1.find_successor(binary_tree1.find_minimum(binary_tree1.root))).key)
    print((binary_tree1.find_successor(binary_tree1.root)).key)
    print((binary_tree1.find_successor(binary_tree1.find_minimum(binary_tree1.root))).key)
    successor = binary_tree1.find_successor(binary_tree1.find_maximum(binary_tree1.root))
    if successor is not None:
        print(successor.key)
    else:
        print("Maximum node has no successor \n")

    binary_tree1.insert_node(Node(5))
    binary_tree1.insert_node(Node(0))
    binary_tree1.insert_node(Node(9))
    in_order_traversal(binary_tree1.root)
    print("")
    binary_tree1.delete_node(binary_tree1.root)
    in_order_traversal(binary_tree1.root)
    print("")
    binary_tree1.delete_node(binary_tree1.find_maximum(binary_tree1.root))
    in_order_traversal(binary_tree1.root)
    print("")
    binary_tree1.delete_node(binary_tree1.find_minimum(binary_tree1.root))
    in_order_traversal(binary_tree1.root)


main()