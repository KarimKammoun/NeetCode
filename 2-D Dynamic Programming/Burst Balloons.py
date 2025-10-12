class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        visited={}


        def dfs(l,s,n):

            if n==1:
                return l[0]
            
            if tuple(l) in visited:
                return visited[tuple(l)]
            m=0

            for i in range(n):
                if i==0:
                    r=l[i]*l[i+1]
                    k=r+dfs(l[i+1:],s+r,n-1)
                elif i==n-1:
                    r=l[i]*l[i-1]
                    k=r+dfs(l[0:i],s+r,n-1)
                else :
                    r=l[i]*l[i-1]*l[i+1]
                    k=r+dfs(l[0:i]+l[i+1:],s+r,n-1)

                if k>m:
                    m=k
            
            visited[tuple(l)]=m

            return m
            

        
        r=dfs(nums,0,n)   
        print(visited)
        return r


