from typing import List
from collections import defaultdict


def countComponents(n: int, edges: List[List[int]]) -> int:
    # if not n:
    #     return 0

    # parent = [i for i in range(n)]

    # # num of connected nodes
    # rank = [1]*n

    # # find root parent
    # def find(n1):
    #     res = n1
    #     while res != parent[res]:
    #         parent[res] = parent[parent[res]]
    #         res = parent[res]
    #     return res

    # def union(n1, n2):
    #     # root parents of n1, n2
    #     p1, p2 = find(n1), find(n2)
    #     if p1 == p2:
    #         return 0
    #     if rank[p2] > rank[p1]:
    #         parent[p1] = p2
    #         rank[p2] += rank[p1]
    #     else:
    #         parent[p2] = p1
    #         rank[p1] += rank[p2]
    #     return 1

    # res = n
    # for n1, n2 in edges:
    #     res -= union(n1,n2)
    # return res

    adj = defaultdict(list)

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    visit = set()
    count = 0

    for i in range(n):
        if i not in visit:
            self.dfs(i, visit, edges, adj)
            count += 1
    return count


def dfs(self, i, visit, edges, adj):
    if i in visit:
        return
    visit.add(i)
    for neighbor in adj[i]:
        self.dfs(neighbor, visit, edges, adj)
