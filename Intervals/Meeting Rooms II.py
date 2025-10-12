"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start=[]
        end=[]
        
        n=len(intervals)

        res=0

        if n==1:
            return 1


        for i in range(n):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        c=0

        start.sort()
        end.sort()

        p=0
        q=0
        while p<n :
            if start[p]< end[q]:
                c=c+1
                p=p+1
            else:
                c=c-1
                q=q+1
            if c>res:
                res=c
                
        return res


        