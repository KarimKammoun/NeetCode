class Solution:
    def threeSum(self, nums):
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
      return liste

