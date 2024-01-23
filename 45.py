from typing import List


def jump(nums: List[int]) -> int:
    # TC: O(n)

    currEndJump = 0
    jumps = 0
    maxEndJump = 0

    for i in range(len(nums) - 1):
        maxEndJump = max(maxEndJump, i + nums[i])

        if maxEndJump >= len(nums) - 1:
            jumps += 1
            break

        # from previous candidate, we can jump/reach max till ith pos
        if i == currEndJump:
            jumps += 1
            currEndJump = maxEndJump
    return jumps
