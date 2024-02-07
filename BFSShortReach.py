from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weight = 6
        self.shortestReach = [-1] * 5
        self.parent = [-1] * 5

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.parent[v] = u

    # def bfsShortReach(self, n, m, edges, s):
    #     shortestReach = []
    #
    #     for edge in edges:
    #         self.graph[edge[0]].append(edge[1])

    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)

        while queue:
            u = queue.pop(0)
            print(u, end=" ")

            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
                    if self.parent[v] == s:
                        self.shortestReach[v] = self.weight
                    else:
                        self.shortestReach[v] = self.shortestReach[self.parent[v]] + self.weight
        print(self.shortestReach)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(3, 4)

    g.BFS(1)

    # g.bfsShortReach(5, 3, [[1, 2], [1, 3], [3, 4]], 1)
