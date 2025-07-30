class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        p=0
        q=n
        length=n
        if n==1:
            return s

        for i in range(n):
            for j in range(n-length+1):
                if s[p:q]==s[p:q][::-1]:
                    return s[p:q]
                
                p+=1
                q+=1
            p=0
            length-=1
            q=length

