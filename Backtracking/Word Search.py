class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[0 for _ in range(m)] for _ in range(n)] 

        res = False

        def recherche(i, j, k):
            nonlocal res, visited

            if k == len(word) - 1 and board[i][j] == word[k] and visited[i][j]==0:
                res = True
                return

            if board[i][j] != word[k] or visited[i][j] == 1 or res:
                return

            visited[i][j] = 1

            if i > 0:
                recherche(i - 1, j, k + 1)
            if i < n - 1:
                recherche(i + 1, j, k + 1)
            if j > 0:
                recherche(i, j - 1, k + 1)
            if j < m - 1:
                recherche(i, j + 1, k + 1)

            visited[i][j] = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    recherche(i, j, 0)
                    if res:
                        return True  

        return False 
