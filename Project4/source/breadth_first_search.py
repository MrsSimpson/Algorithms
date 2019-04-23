import math


def bfs(graph):
    for key in graph:
        graph[key][1] = "w"
        graph[key][2] = -99
        graph[key][3] = None

    graph[1][1] = 'g'
    graph[1][2] = 0
    graph[1][3] = None

    Q = []
    Q.append(graph[1])

    print("The path for the breadth first traversal is: ")
    while Q:
        vertex = Q.pop(0)
        print(vertex[0])
        for v in vertex[4]:
            if graph[v][1] is "w":
                graph[v][1] = "g"
                graph[v][2] = vertex[2] + 1
                graph[v][3] = vertex[0]
                Q.append(graph[v])
        vertex[1] = "b"
