class Graph:
    """Create an immutable mathematical graph data type

       Creates a graph object, based on an adjacency list implementation
    """
    def __init__(self, vertices = None):
        if vertices is None:
            vertices = {}
        self.vertices = vertices

    def adjacent(self, source, destination):
        return source.adjacency(destination)

    def neighbours(self, source):
        return source.neighbours()

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def remove_vertex(self, vertex):
        self.vertices.pop(vertex.id, None)
        
    def add_edge(self, source, destination, value):
        source.adjacency_list[destination.id] = value
        
    def remove_edge(self, source, destination):
        source.remove_edge(destination)

    """
    def get_vertex_value(self, vertex):
        return # Not yet implemented
    def set_vertex_value(self, vertex, value):
        return # Not yet implemented
    """

    def get_edge_value(self, source, destination):
        return source.get_edge_value(destination)

    def set_edge_value(self, source, destination, value):
        source.set_edge_value(destination, value)
    
class Vertex:
    """Used in conjunction with the Graph class to create a graph based on adjacency matrices
    
    """
    def __init__(self, adjacency_list, id):
        self.adjacency_list = adjacency_list
        self.id = id
    
    def adjacency(self, node):
        return node in self.adjacency_list
    
    def add_edge(self, node, value):
        self.adjacency_list[node] = value
    
    def remove_edge(self, node):
        self.adjacency_list.pop(node, None)

    def get_edge_value(self, node):
        return self.adjacency_list[node]
    
    def set_edge_value(self, node, value):
        self.adjacency_list[node] = value

    def neighbours(self):
        return list(self.adjacency_list.keys())