from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # TC = O(n)
    # SC = O(n)

    remainder_dict = {}

    for i, num in enumerate(nums):
        if num in remainder_dict:
            return [i, remainder_dict[num]]
        remainder_dict[target-num] = i
    return []