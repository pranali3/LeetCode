from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # TC = O(n)
    # SC = O(n)

    last_position = {}

    for i, num in enumerate(nums):
        if num in last_position and i - last_position[num] <= k:
            return True
        last_position[num] = i
    return False


nums = [1, 2, 3, 1]
k = 3
containsNearbyDuplicate(nums, k)
