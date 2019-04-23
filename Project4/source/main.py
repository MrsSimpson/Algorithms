from breadth_first_search import bfs
from depth_first_search import dfs


def main():
    bfs_adj_list = {
                1:[1, "w", 0, None,[2, 3]],
                2:[2, "w", 0, None,[1, 4, 5]],
                3:[3, "w", 0, None,[1, 5]],
                4:[4, "w", 0, None,[2, 5, 6]],
                5:[5, "w", 0, None,[2, 3, 4, 6]],
                6:[6, "w", 0, None,[4, 5]]}

    for key in bfs_adj_list:
        print(key, bfs_adj_list[key])

    bfs(bfs_adj_list)
    for key in bfs_adj_list:
        print(key, bfs_adj_list[key])

    dfs_adj_list = {
                1: [1, "w", 0, 0, None, [2, 3]],
                2: [2, "w", 0, 0, None, [1, 4, 5]],
                3: [3, "w", 0, 0, None, [1, 5]],
                4: [4, "w", 0, 0, None, [2, 5, 6]],
                5: [5, "w", 0, 0, None, [2, 3, 4, 6]],
                6: [6, "w", 0, 0, None, [4, 5]]}

    for key in dfs_adj_list:
        print(key, dfs_adj_list[key])
    dfs(dfs_adj_list)
    for key in dfs_adj_list:
        print(key, dfs_adj_list[key])

main()