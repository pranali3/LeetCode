from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # TC: O(nlogn)
    # SC: O(n)

    anagrams = {}

    for s in strs:
        # s.sort() does in place sort and sorted(s) returns a copy
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]

    return anagrams.values()
