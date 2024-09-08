class Solution(object):
    def findMin(self, nums):
        res=nums[0]
        a=0
        b=len(nums)-1
        while a<b:
            if nums[0]<nums[-1]:
                res=nums[0]
                break
            if a+1==b:
                res=nums[b]
                break
            if nums[(a+b)//2]>nums[a]:
                a=(a+b)//2
            elif nums[(a+b)//2]<nums[a]:
                b=(a+b)//2
                res=nums[b]
        return(res)



