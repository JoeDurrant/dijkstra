from Graph import Graph
def dijkstra(graph, source):
    distance = {}
    unvisited = {}
    previous_node = {}

    for i in range(graph.get_number_of_vertices()):
        distance[i] = 1000
        unvisited[i] = 1000
        previous_node[i] = -1 #Undefined at this point
    distance[source] = 0
    unvisited[source] = 0
    previous_node[source] = source

    while len(unvisited) > 0:
        current_node = min(unvisited, key=unvisited.get) # Should get ID number of source node on first loop
        unvisited.pop(current_node)
        neighbours = graph.neighbours(current_node)
        for neighbour in neighbours:
            if neighbour in unvisited:
                a = distance[current_node] + graph.get_edge_value(current_node,neighbour)
                if a < distance[neighbour]:
                    distance[neighbour] = a
                    unvisited[neighbour] = a
                    previous_node[neighbour] = current_node

    paths = {}
    #Calculate paths from source node to all nodes
    for i in range(graph.get_number_of_vertices()):
        target = i
        paths[i] = []
        while target != source:
            paths[i].append(target)
            target = previous_node[target] 
        paths[i].append(source)
    return distance, paths

edges = [[0,0,0,0,1,4,0],
        [0,0,0,3,1,1,15],
        [0,0,0,6,0,0,3],
        [0,3,6,0,4,0,0],
        [1,1,0,4,0,0,0],
        [4,1,0,0,0,0,0],
        [0,15,3,0,0,0,0]]

graph1 = Graph(edges)

distance, paths = dijkstra(graph1,1)
print(distance)
print(paths)