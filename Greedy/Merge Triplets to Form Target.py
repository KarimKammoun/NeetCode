class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n=len(triplets)
        m=len(triplets[0])

        visited=[0]*m

        



        for i in range(n):
            dic=[]
            test=True
            for j in range(m):
                if triplets[i][j]==target[j]:
                    
                    dic.append(j)
                if triplets[i][j]>target[j]:
                    test=False
                    break
            if test==True:
                for j in range(len(dic)):
                    visited[dic[j]]=1
        s=0
        print(visited)
        for i in range(m):
            s=s+visited[i]


        return s==m





                    

        