class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            0: ["+"],
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        res = [] 

        if not digits:
            return res  

        liste = [dic[int(ch)] for ch in digits]
        n = len(liste)  

        def recherche(ch, start):
            if len(ch) == n:
                res.append("".join(ch))  
                return

            for i in range(start, n):
                for j in range(len(liste[i])):
                    ch.append(liste[i][j])  
                    recherche(ch, i + 1)    
                    ch.pop()                

        recherche([], 0)
        return res
