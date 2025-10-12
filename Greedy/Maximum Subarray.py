class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        n=len(nums)

        res=nums[0]
        s=0

        while i<n and nums[i]<=0:
            if nums[i]>res:
                res=nums[i]
            i=i+1
        

        if i<n:

            res=nums[i]
            s=nums[i]
            i=i+1

            while i<n :
                
                if s==0 and nums[i]<0:
                    i=i+1
                    continue
                s=s+nums[i]
                print(s)

                if s>res:
                    res=s

                if s<0:
                    s=0

                i=i+1

        return res
            

        