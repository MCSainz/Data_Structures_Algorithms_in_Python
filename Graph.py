# Class Graph create an undirected graph from a text input format a la Resnick 
# 4ed. of Algorithms (Section 4.1).

# The format of the graph is as follows: the first line is the number of vertices; the second line is
# the number of edges; the subsequent lines are edges. Sample *.txt graph input files found in
# https://github.com/aistrate/AlgorithmsSedgewick/blob/master/4-Graphs/4-1-UndirectedGraphs/

class Graph():
    # The '__init__' method implements a graph
    # using a dictionnary of lists.
    def __init__(self, graph_file_path):
        self.num_edges = None
        self.num_vertices = None
        self.graph = None
        
        with open(graph_file_path, 'r') as graph_file:
            lines = graph_file.readlines()

        # Creates a list with all the graph text file lines.
        graph_list = [str.strip(line) for line in lines]

        # Gets the number of vertices and edges.
        self.num_vertices = int(graph_list.pop(0))
        self.num_edges    = int(graph_list.pop(0))

        # List of list pairs for each edge.
        edge_list =(str.split(edge) for edge in graph_list )

        # Creates empty dictionnary of lists.
        # 'keys' is the list of vertices, e.g. ['0', '1', ..., 'N'].
        keys = [str(vertex) for vertex in range(self.num_vertices)]
        # The 'values' is a list of vertices lists e.g. [ ['0','5'], ..., ['5','3']].
        values = [[] for vertex in range(self.num_vertices)]
        self.graph = dict(zip(keys, values))

        # Build the graph by going through each vertex and edge.
        for vertex in keys:
            for edge in edge_list:
                self.add_edge(edge)
                edge_list.remove(edge)

    # An 'edge' is a list of two vertices.
    def add_edge(self, edge):
        vertex1, vertex2 = edge
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    # Returns a list of the adjacent nodes to some vertex.
    def adjacent_nodes(self, vertex):
        return self.graph[vertex]
