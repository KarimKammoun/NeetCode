class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        visited=set()
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        if (n1+n2)!=n3:
            return False
        res=False

        def dfs1(p1,p2,n1,n2,k):
            nonlocal res

            if (p1,p2) in visited:
                return False

            if k==n3 :
                res=True
                return True

            
 
            i=p1


            while i<n1 and s1[i]==s3[k] and k<n3:
                
                test=dfs2(i+1,p2,n1,n2,k+1)
                if test==True:
                    return True
                i=i+1
                k=k+1
            visited.add((p1,p2))
            

            return False




        def dfs2(p1,p2,n1,n2,k):
            nonlocal res

            if (p1,p2) in visited:
                return False

            if k>=n3:
                res=True
                return True


            i=p2


            while i<n2 and s2[i]==s3[k] and k<n3:
                test=dfs1(p1,i+1,n1,n2,k+1)
                if test==True:
                    return True
                i=i+1
                k=k+1
            visited.add((p1,p2))
            


            return False
    




        dfs1(0,0,n1,n2,0)
        if res==True:
            return True
        visited=set()
        dfs2(0,0,n1,n2,0)

        return res















        