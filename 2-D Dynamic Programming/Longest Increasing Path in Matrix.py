class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        res=0
        visited=[[-1 for i in range(m)] for j in range(n)]


        def dfs(i,j,p):
            if i>=n or i<0 or j>=m or j<0:
                return 0
            if matrix[i][j]<=p:
                return 0
            if visited[i][j]!=-1:
                return visited[i][j]



            r1=1+dfs(i,j+1,matrix[i][j])
            r2=1+dfs(i,j-1,matrix[i][j])
            r3=1+dfs(i+1,j,matrix[i][j])
            r4=1+dfs(i-1,j,matrix[i][j])

            r=max(r1,r2,r3,r4)

            visited[i][j]=r

            return r






        for i in range(n):
            for j in range(m):
                r=dfs(i,j,-1) 
                if r>res:
                    res=r

        return res        
        