class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=0
        b=1
        if len(nums)>0:
            a=1
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i]==nums[i+1]-1 :
                b=b+1
                if b>a:
                    a=b
            else:
                b=1
        return a