from typing import List
from collections import defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # TC: O(nlogn)
    # SC: O(n)

    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    sorted_keys_list = sorted(count, key=lambda x: count[x] ,reverse=True)
    return sorted_keys_list[:k]