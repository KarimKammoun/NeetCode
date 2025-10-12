class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        i = 0
        m = nums[0]  
        res = 1      

        while i < n - 1:
            reach = i + m  
            if reach >= n - 1:
                return res 

            best = 0
            next_i = i

            for j in range(i + 1, reach + 1):
                if j + nums[j] > best:
                    best = j + nums[j]
                    next_i = j

            i = next_i
            m = nums[i]
            res += 1
            
        return res