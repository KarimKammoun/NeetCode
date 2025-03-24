class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=[0]*26

        n1=len(s1)
        n2=len(s2)
        p=0
        q=n1-1

        if n1>n2:
            return(False)

        for i in range(n1):
            a[ord(s1[i])-97]+=1


        s=0

        for i in range(n1):
            a[ord(s2[i])-97]-=1

            if a[ord(s2[i])-97]>=0:
                s=s+1


        while(s<n1 and q<n2-1):
            q=q+1
            a[ord(s2[q])-97]-=1

            if a[ord(s2[q])-97]>=0:
                s=s+1
            
            a[ord(s2[p])-97]+=1
            
            if a[ord(s2[p])-97]>0:
                s=s-1

            p=p+1

        if (s==n1):
            return (True)
        else:
            return (False)