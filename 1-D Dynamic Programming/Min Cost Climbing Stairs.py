class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        mincost=[0]*n

        mincost[0]=cost[0]
        mincost[1]=cost[1]

        for i in range(2,n):
            mincost[i]=cost[i]+min(mincost[i-1],mincost[i-2])
        
        return min(mincost[n-1],mincost[n-2])