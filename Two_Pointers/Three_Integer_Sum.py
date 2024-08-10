nums =[-1,0,1,2,-1,-4]

liste=[]
a=0
b=1
c=2
test=True
while test==True:
    if nums[a]+nums[b]+nums[c]==0:
        s=[nums[a]]
        if nums[a]>=nums[b]:
            s=[nums[b]]+s
        else:
            s=s+[nums[b]]
        
        if s[0]>=nums[c]:
            s=[nums[c]]+s
        elif s[1]>=nums[c]:
            s=[s[0]]+[nums[c]]+[s[1]]
        else:
            s=s+[nums[c]]
        if s not in(liste):
            liste.append(s)
    c=c+1
    if a==(len(nums)-3):
        test=False
    if b==(len(nums)-2):
        a=a+1
        b=a+1
        c=b+1
    if c==(len(nums)):
        b=b+1
        c=b+1

print(liste)


""""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res"""



