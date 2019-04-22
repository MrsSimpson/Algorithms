from source.breadth_first_search import bfs
def main():
    adj_list = {1:[1, "w", 0, None,[2, 3]],
                2:[2, "w", 0, None,[1, 4, 5]],
                3:[3, "w", 0, None,[1, 5]],
                4:[4, "w", 0, None,[2, 5, 6]],
                5:[5, "w", 0, None,[2, 3, 4, 6]],
                6:[6, "w", 0, None,[4, 5]]}
    adj_matrix = [[0,1,1,0,0,0],
                  [1,0,0,1,1,0],
                  [1,0,0,0,1,0],
                  [0,1,0,0,1,1],
                  [0,1,1,1,0,1],
                  [0,0,0,1,1,0]]

    for key in adj_list:
        print(key, adj_list[key])

    bfs(adj_list)
    for key in adj_list:
        print(key, adj_list[key])

main()