class Solution:
    def isValid(self, s: str) -> bool:
      stack=[]
      dic={")":"(","]":"[","}":"{"}
      for i in range(len(s)):
          if s[i] in dic:
              if len(stack)>0  and  stack[-1]==dic[s[i]]:
                  stack.pop()
              else:
                  return(False)
          else:
              stack.append(s[i])
      return(len(stack)==0)