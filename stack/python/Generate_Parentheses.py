class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def search(ex, liste):
            if len(ex) == 2 * n:
                res.append(ex)
                return
            for i in range(2):
                if liste[i][1] == 0:
                    continue
                liste[i][1] -= 1
                search(ex + liste[i][0], liste)
                liste[i][1] += 1

        search("", [["(", n], [")", n]])
        
        def isValid(s):
            stack = []
            dic = {")": "(", "]": "[", "}": "{"}
            for i in range(len(s)):
                if s[i] in dic:
                    if len(stack) > 0 and stack[-1] == dic[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
            return len(stack) == 0

        i = 0
        while i < len(res):
            if not isValid(res[i]):
                del res[i]
                continue
            i += 1

        return res