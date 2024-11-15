from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack[::-1]

# a b c d e f g h i
# 0 1 2 3 4 5 6 7 8
g = Graph(9)
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

print("Topological Sort:", g.topological_sort())
