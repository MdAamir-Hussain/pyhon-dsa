class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("DFS traversal starting from vertex 2:")
    graph.dfs(2)
