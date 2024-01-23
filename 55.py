from typing import List


def canJump(nums: List[int]) -> bool:
    # TC: O(n)

    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= goal - i:
            goal = i
    return True if goal == 0 else False
