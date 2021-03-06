
def dfs(graph):
    for vertex in graph:
        graph[vertex][1] = "w" #setting the color of the first vertex to 0
        graph[vertex][4] = None #setting the parent of the first vertex to None

    print("The path searched for depth first search traversal is: ")
    global time #time is a global variable
    time = 0
    for vertex in graph: #initialize each vertex's elements in the graph
        if graph[vertex][1] is "w":
            key_val = graph[vertex][0] #key_value equals the actual value of the vertex
            dfs_visit(graph, key_val)


def dfs_visit(graph, vertex):
    global time #making global time accessable in dfs_visit
    print(graph[vertex][0])
    graph[vertex][1] = "g" #set the vertex that was passed in to gray for discovered
    time += 1 #make the starting time incrememnt by 1
    graph[vertex][2] = time #set the vertex's starting time
    for v in graph[vertex][5]: #look through the list of adjacent vertex that are contained in the vertex
        if graph[v][1] is "w":  #if the adj vertex color is still white...
            graph[v][4] = graph[vertex][0] #set the parent of the adj vertex to the vertex that it came from
            dfs_visit(graph, graph[v][0]) #recursively call dfs_visit with the current adj node

    graph[vertex][1] = "b" #set the vertex's color to black because it is complete
    time += 1 #increment the finish time
    graph[vertex][3] = time #set the finish time for the completed vertex

