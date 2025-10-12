class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        visited={}
        res=0



        def dfs(i,j):
            if ((i,j) in visited):
                return visited[(i,j)]
            if j==m:
                return 1
            if i==n:
                return 0

            r1=0

            
            for c in range(i,n):
                if s[c]==t[j]:
                    r1=r1+dfs(c+1,j+1)
            

            visited[(i,j)]=r1

            
            return r1


        for i in range(n):
            if s[i]!=t[0]:
                continue
            res=dfs(i,0) 
            return res

        return 0      



        