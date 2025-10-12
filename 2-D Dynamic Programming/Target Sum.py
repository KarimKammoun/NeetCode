class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited={}
        res=0
        n=len(nums)




        def dfs(s,start):
            nonlocal res
            if (s,start) in visited:
                res=res+visited[(s,start)]
                return  visited[(s,start)]

            
            if s==target and start==n:
                res=res+1
                return 1
            elif start==n:
                return False



            r1=dfs(s+nums[start],start+1)
            r2=dfs(s-nums[start],start+1)

            visited[(s,start)]=r1+r2
            


            return r1+r2





            return 
            

        dfs(0,0)
        return res
        