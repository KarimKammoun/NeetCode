from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        visited = {}
        res = []

        for word in words:
            for char in word:
                graph[char] 

        def compare(w1, w2):
            min_len = min(len(w1), len(w2))
            for i in range(min_len):
                if w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    return True
            if len(w1) > len(w2):
                return False
        for i in range(len(words) - 1):
            test=compare(words[i], words[i + 1])
            if test==False:
                return ""

        def dfs(c):
            if c in visited:
                return visited[c] 
            visited[c] = True 
            for nei in graph[c]:
                if dfs(nei):
                    return True
            visited[c] = False 
            res.append(c)
            return False

        for c in graph:
            if c not in visited:
                if dfs(c):
                    return ""  
        return "".join(reversed(res))
