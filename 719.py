class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # TC: O(nlogn)

        def count_pairs(max_dist):
            count, right = 0, 0
            for left in range(len(nums)):
                # counts the number of pairs that have a difference of <= max_dist.
                while right < len(nums) and nums[right] - nums[left] <= max_dist:
                    right += 1
                count += right - left - 1
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        n = len(nums)

        while left < right:
            mid = (left + right) // 2
            # num of pairs up to mid
            if count_pairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
