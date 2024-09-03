class Solution(object):
    def search(self, nums, target):
        a=0
        b=len(nums)-1
        while a<=b :
            if target>nums[(a+b)//2]:
                a=(a+b)//2+1
            elif target<nums[(a+b)//2]:
                b=(a+b)//2-1
            else:
                return((a+b)//2)
        return -1