class Solution:
    def climbStairs(self, n: int) -> int:
        res=0
        s=0


        def dfs():
            nonlocal s,res
            if s==n:
                res+=1
                return
            if s>n:
                return
            
            s=s+1
            dfs()
            s=s-1
            s=s+2
            dfs()
            s=s-2


        dfs()
        return res
        