class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)

            result = max(result, max_prod)

        return result