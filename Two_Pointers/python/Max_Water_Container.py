class Solution:
    def maxArea(self, heights):
      s=0
      a=0
      while a<len(heights)-1:
          for i in range(a+1,len(heights)):
              if min(heights[a],heights[i])*(i-a)>s:
                  s=min(heights[a],heights[i])*(i-a)
          a=a+1
      return(s)

























