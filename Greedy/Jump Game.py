class Solution:
    def canJump(self, nums: List[int]) -> bool:


        n=len(nums)

        i=0
        maxe=nums[0]

        for i in range(n):
            if maxe<0:
                return False
            if nums[i]>maxe:
                maxe=nums[i]
            maxe=maxe-1



        
        return True
