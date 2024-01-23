def nextGreaterElement(self, n: int) -> int:
    # https://www.youtube.com/watch?v=nyUJhLxbIDY
    # two pointers

    s = str(n)
    nums = [c for c in s]

    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        return -1

    i2 = len(nums) - 1
    while nums[i2] <= nums[i]:
        i2 -= 1

    nums[i], nums[i2] = nums[i2], nums[i]
    nums[i + 1:] = nums[i + 1:][::-1]
    ans = int("".join(nums))
    return ans if ans <= 2 ** 31 - 1 else -1
