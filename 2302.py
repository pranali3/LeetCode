def countSubarrays(nums: List[int], k: int) -> int:
    # n = len(nums)
    # # lessThanK = []
    # count = 0
    #
    # for startPos in range(n):
    #     for grps in range(startPos, n + 1):
    #         li = nums[startPos:grps]
    #         if li:
    #             if sum(li) * len(li) < k:
    #                 # lessThanK.append(li)
    #                 count += 1
    # return count

    ### sliding window ###
    # TC: O(n)

    totalSum = 0
    res = 0
    left = 0

    for right in range(len(nums)):
        totalSum += nums[right]
        while totalSum*(right - left + 1) >= k:
            totalSum -=nums[left]
            left += 1
        res += right - left + 1
    return res


