class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def bfs(start):
            q = [start]
            visit = set()

            while q:
                index = q.pop(0)
                visit.add(index)

                if arr[index] == 0:
                    return True
                if index + arr[index] in range(n) and index + arr[index] not in visit:
                    q.append(index + arr[index])

                if index - arr[index] in range(n) and index - arr[index] not in visit:
                    q.append(index - arr[index])
            return False

        return bfs(start)
