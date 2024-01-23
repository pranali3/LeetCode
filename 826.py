def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    diff_p_arr = [[difficulty[i], profit[i]] for i in range(len(profit))]
    diff_p_arr.sort()

    max_profit = diff_p_arr[0][1]

    for i in range(1, len(diff_p_arr)):
        max_profit = max(max_profit, diff_p_arr[i][1])
        diff_p_arr[i] = [diff_p_arr[i][0], max_profit]

    res = 0
    for w in worker:
        res += self.binary_search(diff_p_arr, w)
    return res

def binary_search(self, arr, w):
    l, r = 0, len(arr)
    while l < r:
        m = (l+r)//2
        if arr[m][0] <= w:
            l = m+1
        else:
            r = m
    if l == 0:
        return 0
    return arr[l-1][1]