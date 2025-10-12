class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)+1

        for i in range(n):
            nums.append (i)
        
        res=0
        for i in range((n*2)-1):
            res ^=nums[i]
        return res
