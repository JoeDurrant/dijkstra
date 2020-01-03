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
        unvisited.pop(current_node)
        neighbours = graph.neighbours(current_node)
        for neighbour in neighbours:
            if neighbour in unvisited:
                a = distance[current_node] + graph.get_edge_value(current_node,neighbour)
                if a < distance[neighbour]:
                    distance[neighbour] = a
                    unvisited[neighbour] = a
    return distance
    
with open(vertices.csv) as f: # Read vertices and edges from file
