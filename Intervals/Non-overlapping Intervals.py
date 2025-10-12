class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        res=0

        print(intervals)

        p=intervals[0][0]
        q=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]==p and intervals[i][1]<q:
                q=intervals[i][1]
                res=res+1
            elif intervals[i][0]>=p and intervals[i][1]<=q  :
                p=intervals[i][0]
                q=intervals[i][1]
                res=res+1
            elif  intervals[i][0]>=q:
                p=intervals[i][0]
                q=intervals[i][1]
            else:
                res=res+1




        return res
        