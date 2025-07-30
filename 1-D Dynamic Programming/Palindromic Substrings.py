class Solution:
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        if n<=1:
            return n

        res=n
        def recherche(i,j):
            nonlocal res
            if i<0 or j>=n:
                return
            if s[i]==s[j]:
                res+=1
                recherche(i-1,j+1)
            

        if s[0]==s[1] : 
            res+=1



        for i in range (1,n-1):
            if s[i]== s[i+1]:
                recherche(i,i+1)
            if s[i-1]==s[i+1]:
                recherche(i-1,i+1)

        return res
 