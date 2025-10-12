class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n <=1:
            return intervals

        heapq.heapify(intervals)
        merged=[]

        current=heapq.heappop(intervals)

        while intervals:
            next_interval = heapq.heappop(intervals)

            if current[1] >= next_interval[0]:
                current[1] = max(current[1], next_interval[1])
            else:
                merged.append(current)
                current = next_interval

        merged.append(current)
        return merged