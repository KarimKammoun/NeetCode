class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dic={}
        for i in queries:
            dic[i]=[100000,-1]
        res=[]




        for i in range(len(intervals)):
            for j in queries:
                if intervals[i][0]<=j<=intervals[i][1] and (intervals[i][1]-intervals[i][0])<dic[j][0]:
                    dic[j][0]=intervals[i][1]-intervals[i][0]
                    dic[j][1]=i

        for i in queries:
            if dic[i][0]==100000:
                res.append(-1)
            else:
                res.append(dic[i][0]+1)
        
        return res


