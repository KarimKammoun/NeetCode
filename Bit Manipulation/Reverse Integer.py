class Solution:
    def reverse(self, x: int) -> int:
        MAX=2147483647
        MIN=-2147483648
        res=0
        test=False
        if x<0:
            x=-x
            test=True
        while x!=0:
            a=x%10
            x=x//10
            res=res+a
            res=res*10
        

            
        if test==True:
            res= -(res//10)
        else:
            res=res//10

        if res//10>MAX//10 or res//10 < (MIN//10):
            return 0
        elif res//10 == (MAX//10) and res%10 > (MAX%10):
            return 0

        elif res//10 == (MIN//10) and res%10 < (MAX%10):
            return 0
        return res

        

        