class DepthFirstSearch:
    def __init__(self):
        self.marked = None
        self.count = 0

    def DepthFirstSearch(self, graph, vertex):
        self.marked = [False for vertex in range(graph.num_vertices)]
        self.dfs(graph, vertex)

    def dfs(self, graph, vertex):
        self.marked[int(vertex)] = True
        self.count += 1
        for v in graph.adjacent_nodes(vertex):
            if not(self.marked[int(v)]): self.dfs(graph, v)

    def marked_nodes(self, w):
        return self.marked[w]
    