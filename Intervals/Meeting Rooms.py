"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        liste=[]
        n=len(intervals)


        for i in range(n):
            liste.append([intervals[i].start,intervals[i].end])
        liste.sort()




        
        for i in range(1,n):
            if liste[i][0]<liste[i-1][1] and liste[i][0]>=liste[i-1][0]:
                return False

        return True

