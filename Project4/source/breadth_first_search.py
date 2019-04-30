#Breadth First Search will use an adjacency list to find all vertex that exist in the graph.

def bfs(graph, starting_vert):
    #init the graph (only using this in case i want to call bfs again with different starting vert
    for key in graph:
        graph[key][1] = "w" #setting start color to white
        graph[key][2] = -99 #setting step count value to neg sentinal value
        graph[key][3] = None #setting parent to None

    graph[starting_vert][1] = 'g' #setting the starting vertex's color to gray
    graph[starting_vert][2] = 0 #setting the step count for starting vertex to 0

    Q = []  #creating my queue
    Q.append(graph[starting_vert]) #adding the starting node to the queue

    print("The path for the breadth first traversal with starting vertex as " + str(starting_vert) + " is: ")
    while Q: #while the queue is not empty
        vertex = Q.pop(0) #pop the vertex at the 0 position of the queue (the vertex that was added first in the q)
        print(vertex[0])
        for v in vertex[4]: #for all of the adjacent vertex in the popped vertex adjacency list
            if graph[v][1] is "w": #if the color of the adjacent vertex is white,
                graph[v][1] = "g"   #change it's color to gray
                graph[v][2] = vertex[2] + 1 #add the steps taken to travel to this vertex
                graph[v][3] = vertex[0] #set the parent to the vertex that was popped from the queue
                Q.append(graph[v]) #add the vertex to the queue
        vertex[1] = "b" #change the color of the popped vertex to black because it has been completed
