from typing import List


def maxSubArray(nums: List[int]) -> int:
    # TC: O(n)

    # set to min possible integer
    maxSum = float('-inf')
    currSum = 0

    for num in nums:
        currSum += num
        # check if the current sum currentSum is greater than the current maximum sum maxSum.
        #If it is, we update maxSum with the new value of currentSum. This means we have found a new maximum subarray sum.
        maxSum = max(currSum, maxSum)
        # If the current sum is negative, it indicates that including the current element in the subarray would reduce  the overall sum. So we reset currSum to 0. This effectively discards the current subarray and allows us to start a fresh subarray from the next element.
        if currSum < 0:
            currSum = 0

    return maxSum