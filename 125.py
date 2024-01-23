def isPalindrome(s: str) -> bool:
    # TC: O(n)
    # SC: O(1)

    s = s.lower()
    s = "".join([ch for ch in s if ch.isalnum()])
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True
