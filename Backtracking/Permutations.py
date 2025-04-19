class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        combinaison=[]
        n=len(nums)
        visited=[0]*n



        def recherche(nums):
            if len(combinaison)==n:
                res.append(combinaison[:])
                return
            


            for i in range(n):
                if visited[i]==0:
                    combinaison.append(nums[i])
                    visited[i]=-1
                    recherche(nums)
                    visited[i]=0
                    combinaison.pop()
                else:
                    continue
        recherche(nums)
        return res
