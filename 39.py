from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # TC: O(2^target)
    # SC: O(k) len(res)
    # Decision tree - recursion

    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        # include cur candidate
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        # exclude cur candidate
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res
