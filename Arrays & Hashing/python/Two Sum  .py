class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,n in enumerate(nums):
            dif=target-n
            if dif in dic:
                return [dic[dif],i]
            dic[n]=i
