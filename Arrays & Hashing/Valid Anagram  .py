class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic1 ={}
        for c in s : 
            dic[c] = dic.get(c, 0) + 1
        for c in t : 
            dic1[c] = dic1.get(c, 0) + 1
        if dic==dic1:
            return True
        else:
            return False