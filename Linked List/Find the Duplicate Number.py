class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)

        for i in range(n):
            if (nums[nums[i]-1]==nums[i]) and (i+1)!=nums[i]:
                return nums[i]
            else:
                ox=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=ox