from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # TC: O(nlogn)

    intervals.sort(key=lambda i: i[0])

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i2[0] < i1[1]:
            return False
    return True
