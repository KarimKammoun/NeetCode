class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        combinaison=[]
        n=len(candidates)
        s=0


        def recherche(start,combinaison):
            nonlocal s

            if s==target and combinaison not in (res):
                res.append(combinaison[:])
            elif (s>target):
                return

            for i in range(start,n):
                combinaison.append(candidates[i])
                s+=candidates[i]
                recherche(i+1,combinaison)
                s-=combinaison[-1]
                combinaison.pop()



        recherche(0,combinaison)
        return res