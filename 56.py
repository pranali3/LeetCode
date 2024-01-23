from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # TC: O(nlogn)

    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        prevEnd = output[-1][1]

        if start <= prevEnd:
            output[-1][1] = max(end, prevEnd)  # ele that was added last
        else:
            output.append([start, end])
    return output
