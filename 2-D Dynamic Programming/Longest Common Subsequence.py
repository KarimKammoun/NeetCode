class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)

        l=[[0 for _ in range(n+1)]for _ in range(m+1)]
        print(l)


        def dfs(i,j):
            if l[j][i]!=0:
                return l[j][i]
            if i==n or j==m:
                return 0
            if text1[i]==text2[j]:
                l[j][i]=1+dfs(i+1,j+1)
            
            else:
                l[j][i]=max(dfs(i,j+1),dfs(i+1,j))
            
            
            return l[j][i]


        dfs(0,0)
        print(l)
        return l[0][0]
