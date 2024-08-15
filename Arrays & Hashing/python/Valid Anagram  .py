class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic1 ={}
        for i in s : 
            dic[i] = dic.get(i,0)+1
        for i in t : 
            dic1[i] = dic1.get(i,0)+ 1
        if dic==dic1:
            return True
        else:
            return False
