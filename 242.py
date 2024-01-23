from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    # TC = O(n^2)
    # SC = O(n)

    # sorted_s = sorted(s)
    # sorted_t = sorted(t)
    # return sorted_s == sorted_t

    count = defaultdict(int)

    for ch in s:
        count[ch] += 1

    for ch in t:
        count[ch] -= 1

    for key in count:
        if count[key] != 0:
            return False
    return True


s = "anagram"
t = "nagaram"
isAnagram(s, t)
