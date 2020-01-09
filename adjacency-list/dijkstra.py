from Graph import Graph, Vertex
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
    
import json

vertices = { 0:Vertex({4:1,5:4}, 0), 1:Vertex({3:3, 4:1, 5:1, 6:15}, 1), 
        2:Vertex({3:6, 6:3}, 2), 3:Vertex({1:3, 2:6, 4:4}, 3), 4:Vertex({0:1, 1:1, 3:4}, 4),
        5:Vertex({0:4, 1:1}, 5), 6:Vertex({1:15, 2:3}, 6)}

graph1 = Graph(vertices)

print(dijkstra(graph1, 0))