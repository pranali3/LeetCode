from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # TC: O(n)
    # SC: O(n)

    n = len(nums)
    left_product = [1] * n

    for i in range(1, n):
        left_product[i] = nums[i - 1] * left_product[i - 1]

    right_product = 1
    for i in range(n - 1, -1, -1):
        left_product[i] = right_product * left_product[i]
        right_product *= nums[i]

    return left_product
