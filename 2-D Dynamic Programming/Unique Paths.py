class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        visited = [[-1 for _ in range(n)] for _ in range(m)]


        def dfs(i, j):
            nonlocal res


            if i >= m or j >= n:
                return 0
            
            if visited[i][j]!=-1:
                res+=visited[i][j]
                return visited

            if i == m - 1 and j == n - 1:
                res += 1
                return 1
            s1=dfs(i + 1, j)
            s2=dfs(i, j + 1)
            visited[i][j]=s1+s2
            return s1+s2

        dfs(0, 0)
        return res
