# dijkstra
Multiple implementations of a Graph data type, and Dijkstra's algorithm to find shortest paths

Default implementation uses an adjacency matrix, where edges[source][destination] returns the edge weight between source and destination. A zero value represents no adjacency.

The second implementation is in progress, and uses an adjacency list: vertices are stored as objects, each holding a list of vertices which are adjacent to them, and their respective distances.

The input that runs by default matches the provided image.

The dijkstra implementation takes a graph, and a source node as input: it then returns the length of shortest paths from the given source node to all nodes, and the paths along the graph from the source node to the target node.
