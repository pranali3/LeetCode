from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # TC: O(nlogn)

    intervals.sort(key=lambda i: i[0])
    res = 0
    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:
        # overlapping
        if start < prevEnd:
            res += 1
            prevEnd = min(end, prevEnd)
        else:
            prevEnd = end
    return res
