def areAlmostEqual(self, s1: str, s2: str) -> bool:
    # TC: O(nlogn)

    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    # the count should be 2, then only we can do at most one string swap
    if count != 2:
        return False
    return True
