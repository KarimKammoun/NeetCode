class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        for i in range(n):
            stones[i]=stones[i]*-1

        heapq.heapify(stones)

        while n>1:
            print(stones)
            n1=-(heapq.heappop(stones))
            n2=-(heapq.heappop(stones))
            if n1==n2:
                n=n-2
                continue

            res=n1-n2
            heapq.heappush(stones,-res)
            n=n-1

        if len(stones)==0  :
            return 0
        else:
            return -stones[0]



        