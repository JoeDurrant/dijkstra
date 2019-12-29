class Graph:
    """Create an immutable mathematical graph data type

       Creates a graph object, based on an incidence matrix implementation
    """
    def __init__(self, edges):
        self.edges = edges
        
    def adjacent(self, source, destination):
        return edges[source][destination] > 0 # zero value indicates no edge between vertices

    def neighbours(self, vertex):
        neighbour_list = []
        for i in range(len(self.edges)):
            if self.edges[vertex][i] > 0:
                neighbour_list.append(i) # Append ID number of node
        return neighbour_list

    def get_edge_value(self, source, destination):
        return self.edges[source][destination]

    def get_number_of_vertices(self):
        return len(self.edges)
