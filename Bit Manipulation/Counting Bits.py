class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        if n==2:
            return [0,1,1]
        
        if n==3:
            return [0,1,1,2]
        res=[0,1,1,2]

        k=1
        p=8
        for i in range(4,n+1):
            if i==p:
                k=k*2
                p=p*2

            res.append(res[-4*k]+1)
        return res

            
        