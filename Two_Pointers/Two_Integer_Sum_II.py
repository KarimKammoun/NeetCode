class Solution:
    def twoSum(self,numbers, target):
      a=0
      b=len(numbers)-1
      for i in range(len(numbers)):
          d=numbers[a]+numbers[b]
          if d>target:
              b=b-1
          elif d<target:
              a=a+1
          else:
              break
      return([a+1,b+1])
    