class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        n=len(nums)
        combinaison=[]
        s=0
        def recherche(start,s,combinaison):

            for i in range(start,n):
                
                s=s+nums[i]
                combinaison.append(nums[i])
                if s==target:
                    res.append(combinaison[:])
                elif s<target:
                    recherche(i,s,combinaison)
                s -= nums[i]
                combinaison.pop()


        recherche(0,s,combinaison)
        return res
