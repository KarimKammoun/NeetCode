class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}                   

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                return i == n

            match = i < n and (p[j] == s[i] or p[j] == '.')

            if j + 1 < m and p[j + 1] == '*':
                ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                ans = match and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)
