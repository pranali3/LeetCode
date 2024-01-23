from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    # TC: O(n^3)
    # SC: O(1)

    quadruplets = set()
    nums.sort()
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            k = j + 1
            l = n - 1

            while k < l:
                calcSum = nums[i] + nums[j] + nums[k] + nums[l]
                if calcSum == target:
                    quadruplets.add((nums[i], nums[j], nums[k], nums[l]))
                    l -= 1
                    k += 1
                elif calcSum > target:
                    l -= 1
                else:
                    k += 1
    return list(quadruplets)
