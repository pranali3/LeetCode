from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    # TC: O(nlogn)

    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0, 0
    s_index, e_index = 0, 0

    while s_index < len(intervals):
        if start[s_index] < end[e_index]:
            s_index += 1
            count += 1
            res = max(res, count)
        else:
            e_index += 1
            count -= 1
    return res
