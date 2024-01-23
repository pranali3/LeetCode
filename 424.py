def characterReplacement(s: str, k: int) -> int:
    # TC: O(26n)

    freq = {}
    l = 0
    maxlen = 0

    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        currLen = r - l + 1
        if currLen - max(freq.values()) <= k:  # O(26) IMP
            maxlen = max(maxlen, currLen)
        else:
            freq[s[l]] -= 1
            l += 1
    return maxlen
