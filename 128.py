from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # TC: O(n)

    maxlen = 0
    res = 0
    s = set(nums)

    for i in range(len(nums)):
        if nums[i] - 1 not in s:
            j = nums[i]
            while j in s:
                j += 1
            maxlen = max(maxlen, j - nums[i])
    return maxlen
