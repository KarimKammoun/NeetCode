class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        
        for c in nums : 
            if c in dic and dic[c]==1 :
                return True
            dic[c] = dic.get(c, 0) + 1
        return False