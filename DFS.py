from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, u, visited):
        visited.add(u)
        print(u, end=" ")

        for v in self.graph[u]:
            if v not in visited:
                self.DFS(v, visited)


if __name__ == "__main__":
    # O(V+E)
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    visited = set()
    g.DFS(0, visited)
