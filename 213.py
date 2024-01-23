def rob(nums: List[int]) -> int:
    # TC: O(n) -> 2*n
    # skip first house and skip last house

    def helper(nums):
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1]
        for n in nums:
            # take n + rob1 or take rob2 in arr[0:3]
            newRob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

    # nums[0] if there's only one house
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
