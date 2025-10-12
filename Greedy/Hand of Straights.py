class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        visited=[0]*1000
        
        

        for i in range(n):
            visited[hand[i]]+=1
        


        for i in range(1000):
            if visited[i]!=0:
                k=visited[i]
                for j in range(i,i+groupSize ):
                    visited[j]=visited[j]-k
                    if visited[j]<0:
                        return False
        return True




