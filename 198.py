def rob(nums: List[int]) -> int:
    # TC: O(n)

    rob1, rob2 = 0, 0
    # [rob1, rob2, n, n+1]
    for n in nums:
        # take n + rob1 or take rob2 in arr[0:3]
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
