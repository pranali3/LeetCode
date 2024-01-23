from typing import List


def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    # TC: O(n)
    res, i = [], 0

    while i < len(s):
        num_s = ""
        while s[i] != "#":
            num_s += s[i]
            i += 1
        num = int(num_s)
        res.append(s[i + 1:i + 1 + num])
        i = i + 1 + num
    return res
