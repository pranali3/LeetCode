from typing import List


def search(nums: List[int], target: int) -> int:
    # TC: O(logn)
    # SC: O(1)

    low = 0
    high = len(nums) - 1
    index = -1

    while low <= high:
        m = (low + high) // 2
        if nums[m] == target:
            return m
        if nums[low] <= nums[m]:
            if nums[low] <= target <= nums[m]:
                high = m - 1
            else:
                low = m + 1
        else:
            if nums[m] <= target <= nums[high]:
                low = m + 1
            else:
                high = m - 1
    return index
