class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n=len(s)
        visited=[]

        for i in range(27):
            visited.append([-1,-1])

        res=[]

        for i in range(n):
            if visited[(ord(s[i]))-97][0]==-1:
                visited[(ord(s[i]))-97][0]=i
                visited[(ord(s[i]))-97][1]=i
            else:
                visited[(ord(s[i]))-97][1]=i
        print(visited)
            
        i=0

        m=0
        k=0
        while i<n:
            m=max(m,visited[(ord(s[i]))-97][1])

            
            
            print(i,m)
            if i==m:
                m=0
                res.append(i-k+1)
                
                k=i+1
            
            i=i+1

        return res

        