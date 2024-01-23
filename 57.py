from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # TC: O(n)

    res = []
    for i in range(len(intervals)):
        # new interval is before cur interval
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
            # new interval is after cur interval
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    res.append(newInterval)
    return res
