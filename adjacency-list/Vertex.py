class Vertex:
    """Used in conjunction with the Graph class to create a graph based on adjacency matrices
    
    """
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
    
    def adjacency(self, node):
        return node in self.adjacency_list
    
    def get_edge_value(self, node):
        return self.adjacency_list[node]
    
    def neighbours(self):
        return list(self.adjacency_list.keys())