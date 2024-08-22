class Solution:
    def evalRPN(self, tokens):
      stack=[]
      for i in range(len(tokens)):
          if tokens[i]=="+":
              stack[-2]=stack[-2]+stack[-1]
              stack.pop()
          elif tokens[i]=="/":
              stack[-2]=int(stack[-2]/stack[-1])
              stack.pop()
          elif tokens[i]=="*": 
              stack[-2]=stack[-2]*stack[-1]
              stack.pop()
          elif tokens[i]=="-": 
              stack[-2]=stack[-2]-stack[-1]
              stack.pop()
          else:
              stack.append(int(tokens[i]))
      return(stack[0])