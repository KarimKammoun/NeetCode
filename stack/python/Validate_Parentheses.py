class Solution(object):
    def isValid(self, s):
        def verif(s):
            if s == "":
                return True
            n = len(s)
            i = 0
            while i < n - 1:
                if (s[i] == "(" and s[i + 1] == ")") or (s[i] == "[" and s[i + 1] == "]") or (s[i] == "{" and s[i + 1] == "}"):
                    new_s = s[:i] + s[i+2:]
                    return verif(new_s)
                i += 1
            return False
        test=verif(s)
        return test
