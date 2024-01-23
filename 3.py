def lengthOfLongestSubstring(s: str) -> int:
    # TC: O(n)
    # SC: O(n)

    seen = {}
    l = 0
    ans = 0

    for r in range(len(s)):
        if s[r] not in seen:
            ans = max(ans, r - l + 1)
        else:
            # outside curr window
            if seen[s[r]] < l:
                ans = max(ans, r - l + 1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return ans
