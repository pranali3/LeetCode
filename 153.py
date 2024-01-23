from typing import List


def findMin(nums: List[int]) -> int:
    # TC: O(logn)
    # SC: O(1)

    low = 0
    high = len(nums) - 1
    ans = nums[0]

    while low <= high:
        if nums[low] < nums[high]:
            return min(ans, nums[low])
        m = (low + high) // 2
        ans = min(ans, nums[m])
        if nums[m] >= nums[high]:
            low = m + 1
        else:
            high = m - 1
    return ans
