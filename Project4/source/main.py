#Lacy Simpson
#5/1/2019
#Algorithms Project 4 BFS and DFS
#this progam will perform a breadth first search as well as a depth first search using an adjacency list implemented
#as a python dictionary. The key of the dictonary will be the value of the vertex and the values associated with the
#key will hold the [value, color, steps from the starting vertex, the parent to the vertex, and the adjacent vertex list


from source.breadth_first_search import bfs
from source.depth_first_search import dfs


def main():
    print("BFS_adj_list = key:[value, color, steps, parent, [adjacent vertex list]]")
    bfs_adj_list = {
        # [value, color, steps, parent, [adjacent vertex]]
                1:[1, "w", 0, None,[2, 3]],
                2:[2, "w", 0, None,[1, 4, 5]],
                3:[3, "w", 0, None,[1, 5]],
                4:[4, "w", 0, None,[2, 5, 6]],
                5:[5, "w", 0, None,[2, 3, 4, 6]],
                6:[6, "w", 0, None,[4, 5]]}

    #printing the bfs_list to screen before calling bfs
    for key in bfs_adj_list:
        print(key, bfs_adj_list[key])


    #calling breadth first search on the list
    bfs(bfs_adj_list, 1)

    #printing out the list's keys and associated values after the search has been completed
    print("The bfs_adj_list keys and values after the search is completed")
    for key in bfs_adj_list:
        print(key, bfs_adj_list[key])

    print("\nDFS_adj_list = key:[value, color, start_time, finish_time, parent, [adjacent vertex list]]")
    dfs_adj_list = {
                1: [1, "w", 0, 0, None, [2, 3]],
                2: [2, "w", 0, 0, None, [1, 4, 5]],
                3: [3, "w", 0, 0, None, [1, 5]],
                4: [4, "w", 0, 0, None, [2, 5, 6]],
                5: [5, "w", 0, 0, None, [2, 3, 4, 6]],
                6: [6, "w", 0, 0, None, [4, 5]]}

    for key in dfs_adj_list:
        print(key, dfs_adj_list[key])

    #calling depth first search on the graph
    dfs(dfs_adj_list)

    print("The dfs_adj_list with key value pairs after the graph has been searched.")
    for key in dfs_adj_list:
        print(key, dfs_adj_list[key])

main()