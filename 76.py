def minWindow(s: str, t: str) -> str:
    # TC: O(n)
    # SC: O(n)

    if t == "": return ""

    countT, window = {}, {}

    for c in t:
        countT[c] = countT.get(c, 0) + 1

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float('inf')
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            currLen = r - l + 1
            # update res
            if currLen < resLen:
                res = [l, r]
                resLen = currLen
            # popleft
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r + 1] if resLen != float('inf') else ""
