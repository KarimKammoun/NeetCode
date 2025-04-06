class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        combinaison=[]
        n=len(nums)

        def recherche(start,combinaison):
            res.append(combinaison[:])

            for i in range(start,n):
                combinaison.append(nums[i])
                recherche(i+1,combinaison)
                combinaison.pop()


        

        recherche(0,combinaison)
        return res