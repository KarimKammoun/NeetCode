class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m=0
        res=[]

        n=len(nums)

        for i in range(k):
            if nums[i]>m:
                m=nums[i]
        res.append(m)



        for i in range(k,n):
            
            if nums[i-k]==m:
                m=nums[i-k+1]
                for j in range(i-k+1,i):
                    if nums[j]>m:
                        m=nums[j]

            if nums[i]>=m:
                m=nums[i]
                res.append(m)
                continue

            res.append(m)

        return res


        