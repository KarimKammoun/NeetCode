class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      a=0
      b=len(matrix)-1
      k=0
      while a<=b :
          if target>matrix[(a+b)//2][0]:
              a=(a+b)//2+1
          elif target<matrix[(a+b)//2][0]:
              b=(a+b)//2-1
          else:
              return True
      nums=matrix[b]
      a=0
      b=len(nums)-1
      while a<=b :
          if target>nums[(a+b)//2]:
              a=(a+b)//2+1
          elif target<nums[(a+b)//2]:
              b=(a+b)//2-1
          else:
              return True
      return False








