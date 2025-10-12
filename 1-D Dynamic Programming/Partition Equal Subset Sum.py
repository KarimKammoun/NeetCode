class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        visited=[-1]*(s+1)
        

        if s%2==1:
            return False


        def dfs(i,rest):
            if rest < (s//2):
                return False
            if rest==s//2:
                return True
            
            if visited[rest]==1:
                return True
            visited[s-rest]=1



            for j in range(i-1,-1,-1):
                res=dfs(j,rest-nums[j])
                if res==True:
                    return True
            

            return False










        for i in range(n-1,-1,-1):
            res=dfs(i,s)
            if res==True:
                return True

        return False












        
        