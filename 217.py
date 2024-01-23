from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    if len(set(nums)) == len(nums):
        return False
    return True


nums = [1, 2, 3, 1]
containsDuplicate(nums)
