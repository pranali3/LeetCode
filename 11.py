from typing import List


def maxArea(height: List[int]) -> int:
    # TC: O(n)
    # SC: O(1)

    maxWater = 0
    l = 0
    r = len(height) - 1

    while l < r:
        length = min(height[l], height[r])
        breadth = r - l
        maxWater = max(maxWater, length * breadth)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxWater
