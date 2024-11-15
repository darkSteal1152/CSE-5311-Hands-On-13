from collections import defaultdict

class GraphDFS:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.V
        print("DFS traversal starting from vertex", start)
        self.dfs_recursive(start, visited)

# a b c d e f g h i
# 0 1 2 3 4 5 6 7 8
g = GraphDFS(9)
g.add_edge(0, 1)
g.add_edge(0, 7)
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(2, 8)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(7, 8)

for i in range(9):
    g.dfs(i)
