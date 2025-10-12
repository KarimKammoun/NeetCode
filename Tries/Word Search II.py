from typing import List

class Node:
    def __init__(self, val, dic=None, fin=False, word=""):
        self.val = val
        self.dic = dic if dic is not None else {}
        self.fin = fin
        self.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        root = Node('', {}, False, '')
        n_words = len(words)

        def dfs(s, node, i):
            d = node.dic
            if s == '':
                node.fin = True
                node.word = words[i]
                return
            if s[0] in d:
                dfs(s[1:], d[s[0]], i)
            else:
                new_node = Node(s[0], {}, False, '')
                d[s[0]] = new_node
                dfs(s[1:], d[s[0]], i)

        for i in range(n_words):
            dfs(words[i], root, i)

        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def search(i, j, dic):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if visited[i][j] == 1:
                return

            if board[i][j] not in dic:
                return

            node = dic[board[i][j]]
            visited[i][j] = 1

            if node.fin:
                res.append(node.word)
                node.fin = False   

            search(i + 1, j, node.dic)
            search(i - 1, j, node.dic)
            search(i, j + 1, node.dic)
            search(i, j - 1, node.dic)

            visited[i][j] = 0

        for i in range(rows):
            for j in range(cols):
                search(i, j, root.dic)

        return res
