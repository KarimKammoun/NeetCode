class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        visited=[-1]*n

        def dfs(num,i):
            if visited[i]!=-1:
                return visited[i]
            nonlocal res,n
            if i==n-1:
                return 0

            s=0
            maxs=0


            for j in range(i+1,n):
                s=0
                if nums[j]>num:
                    k=dfs(nums[j],j)
                    s=1+k
                    print(s)
                    

                    if s>maxs:
                        maxs=s
                    s=s-k

            if visited[i]==-1:
                visited[i]=maxs
            
            return maxs

        for i in range(n):

            s=dfs(nums[i],i)
            
            if s>res:
                res=s


        return res+1











        