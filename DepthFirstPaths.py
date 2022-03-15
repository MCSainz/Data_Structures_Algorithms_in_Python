class DepthFirstPaths:
    def __init__(self):
        self.marked = None
        self.edgeTo = []
        self.count = 0
        self.source = None
    
    def DepthFirstPaths(self, graph, vertex):
        self.marked = [False for vertex in range(graph.num_vertices)]
        self.dfs(graph, vertex)

    def dfs(self, graph, vertex):
        self.marked[int(vertex)] = True
        for v in graph.adjacent_nodes(vertex):
            if not(self.marked[int(v)]): 
                self.edgeTo[v] = v
                self.dfs(graph, v)

    def hasPathTo(self, vertex):
        return self.marked[int(vertex)]

    def pathTo(self, vertex):
        if not(self.hasPathTo(vertex)): return None