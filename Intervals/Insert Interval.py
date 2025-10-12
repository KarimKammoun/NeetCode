class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0

        if n == 0:
            return [newInterval]

        if n == 1:
            if intervals[0][1] < newInterval[0]:
                intervals.append(newInterval)
            elif newInterval[1] < intervals[0][0]:
                intervals.insert(0, newInterval)
            else:
                intervals[0][0] = min(intervals[0][0], newInterval[0])
                intervals[0][1] = max(intervals[0][1], newInterval[1])
            return intervals

        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals

            elif newInterval[0] > intervals[i][1]:
                i += 1
                continue

            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                intervals.pop(i)
                continue

        intervals.append(newInterval)
        return intervals