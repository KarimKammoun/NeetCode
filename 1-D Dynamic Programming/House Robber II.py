class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        n=n-1
        q=nums.pop()
        
        
        max_money=nums[0]
        maxmoney=[0]*n

        maxmoney[0]=nums[0]
        maxmoney[1]=nums[1]

        for i in range(2,n):
            maxmoney[i]=nums[i]+max_money
            if maxmoney[i-1]>max_money:
                max_money=maxmoney[i-1]
                print(max_money)
        res1= max(maxmoney[n-1], maxmoney[n-2])

        nums.append(q)
        nums=nums[1:]


        max_money=nums[0]
        maxmoney=[0]*n

        maxmoney[0]=nums[0]
        maxmoney[1]=nums[1]

        for i in range(2,n):
            maxmoney[i]=nums[i]+max_money
            if maxmoney[i-1]>max_money:
                max_money=maxmoney[i-1]
                print(max_money)
        res2= max(maxmoney[n-1], maxmoney[n-2])

        return max(res1,res2)




