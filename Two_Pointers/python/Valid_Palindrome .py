class Solution:
    def isPalindrome(self):
        i=0
        j=len(s)-1
        teste=True
        while True:
            if len(s)==0:
                break
            while True:
                if not("A"<=s[i].upper()<="Z" or "0"<=s[i]<"9") and i<len(s)-1:
                    i=i+1
                else:
                    break
            while True:
                if not("A"<=s[j].upper()<="Z" or "0"<=s[j]<"9") and j>0 :
                    j=j-1
                else:
                    break
            if i==len(s)-1:
                break
            if (s[i].upper())!=(s[j].upper()):
                teste=False
                break
            i=i+1
            j=j-1
        return(teste)
        