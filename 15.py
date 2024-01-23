from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # TC = O(n^2)
    # SC = O(n)

    nums.sort()
    triplets = set()
    n = len(nums)

    for i in range(n - 2):
        firstNum = nums[i]
        j = i + 1
        k = n - 1

        while j < k:
            secondNum = nums[j]
            thirdNum = nums[k]

            calcSum = firstNum + secondNum + thirdNum
            if calcSum == 0:
                triplets.add((firstNum, secondNum, thirdNum))
                k -= 1
                j += 1
            elif calcSum > 0:
                k -= 1
            else:
                j += 1

    return list(triplets)
