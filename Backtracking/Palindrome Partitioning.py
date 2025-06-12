class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def ispalandrome(s):
            return s == s[::-1]

        def recherche(path, start):
            nonlocal res

            if start == len(s):
                res.append(path[:])
                return

            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]
                if ispalandrome(substring):
                    path.append(substring)     
                    recherche(path, i)        
                    path.pop()                 

        recherche([], 0)
        return res
