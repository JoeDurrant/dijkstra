from Graph import Graph
def dijkstra(graph, source):
    distance = {}
    unvisited = {}
    for i in range(graph.get_number_of_vertices()):
        distance[i] = 1000
        unvisited[i] = 1000
    distance[source] = 0
    unvisited[source] = 0
    
    while len(unvisited) > 0:
        current_node = min(unvisited, key=unvisited.get) # Should get ID number of source node on first loop
        print("node chosen is "  + str(current_node))
        unvisited.pop(current_node)
        print(distance)
        print(unvisited)
        neighbours = graph.neighbours(current_node)
        print(neighbours)
        for neighbour in neighbours:
            if neighbour in unvisited:
                a = distance[current_node] + graph.get_edge_value(current_node,neighbour)
                if a < distance[neighbour]:
                    distance[neighbour] = a
                    unvisited[neighbour] = a
    return distance
    
edges = [[0,0,0,0,1,4,0],
        [0,0,0,3,1,1,15],
        [0,0,0,6,0,0,3],
        [0,3,6,0,4,0,0],
        [1,1,0,4,0,0,0],
        [4,1,0,0,0,0,0],
        [0,15,3,0,0,0,0]]

graph1 = Graph(edges)

print(dijkstra(graph1,1))