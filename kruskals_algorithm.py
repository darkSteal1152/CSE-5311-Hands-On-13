class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class GraphKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        self.edges.sort(key=lambda edge: edge.weight)
        parent, rank = [], []
        mst = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for edge in self.edges:
            u, v, weight = edge.u, edge.v, edge.weight
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, weight))
                self.union(parent, rank, x, y)

        return mst

# a b c d e f g h i
# 0 1 2 3 4 5 6 7 8
g = GraphKruskal(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

mst = g.kruskal_mst()
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
