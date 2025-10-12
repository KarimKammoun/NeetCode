class Solution:
    def checkValidString(self, s: str) -> bool:
        s1=""
        n=len(s)
        l1=[]
        l2=[]
        n1=0
        n2=0
        k=0
        for i in range(n):
            if s[i]=="(":
                n1=n1+1
                l1.append(["(",i])
                
            elif s[i]==")" and n1>=1 and l1[-1][0]=="(":
                l1.pop()
                n1=n1-1
            elif s[i]==")":
                n1=n1+1
                l1.append([")",i])
                
            else:
                l2.append(i)
                n2=n2+1

        
        i=0
        while n1>0 and i<n1:
            if l1[i][0]=='(' and n2>0 and l2[-1]>l1[i][1]:
                l2.pop()
                n2=n2-1
                i=i+1
            elif l1[i][0]==')' and n2>0 and l2[0]<l1[i][1]:
                l2.pop(0)
                n2=n2-1
                i=i+1
            else:
                return False




        return True

        