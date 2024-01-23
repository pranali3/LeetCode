from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # TC = O(n)
    # SC = O(1)

    l = 0
    h = len(numbers) - 1

    while l < h:
        if numbers[l] + numbers[h] == target:
            return [l + 1, h + 1]
        elif numbers[l] + numbers[h] > target:
            h -= 1
        else:
            l += 1
    return []
