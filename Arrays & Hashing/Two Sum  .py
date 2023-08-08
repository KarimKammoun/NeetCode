class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=1
        for i in range (len(nums)):
            for c in range(a,len(nums)):
                if (nums[i]+nums[c])==target:
                    return [i,c]
            a=a+1