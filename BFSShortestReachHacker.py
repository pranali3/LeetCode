# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import defaultdict


def bfs(n, m, edges, s):
    # Write your code here
    visited = set()
    queue = [s]
    visited.add(s)
    weight = 6
    shortestReach = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    graph = defaultdict(list)

    for edge in edges:
        parent[edge[1]] = edge[0]
        graph[edge[0]].append(edge[1])

    while queue:
        u = queue.pop(0)
        print(f"u {u}")

        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)
                if parent[v] == s:
                    shortestReach[v] = weight
                else:
                    shortestReach[v] = shortestReach[parent[v]] + weight
        print(shortestReach)

    result = []
    for node in range(1, n + 1):
        if s != node:
            result.append(shortestReach[node])
    return result


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
