from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = '.' * n
        m = [s for _ in range(n)]

        visited_j = set()   
        visited_d1 = set()  
        visited_d2 = set()  

        def dfs(row: int):
            if row == n:          
                res.append(m[:])  
                return

            for j in range(n):
                if j in visited_j or (row + j) in visited_d1 or (row - j) in visited_d2:
                    continue

                m[row] = m[row][:j] + "Q" + m[row][j + 1:]
                visited_j.add(j)
                visited_d1.add(row + j)
                visited_d2.add(row - j)

                dfs(row + 1)

                m[row] = m[row][:j] + "." + m[row][j + 1:]
                visited_j.remove(j)
                visited_d1.remove(row + j)
                visited_d2.remove(row - j)

        dfs(0)
        return res
