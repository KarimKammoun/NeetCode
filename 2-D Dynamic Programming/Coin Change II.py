class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(rest, start):
            if rest == 0:
                return 1 
            if rest < 0 or start >= n:
                return 0
            if (rest, start) in memo:
                return memo[(rest, start)]

            take = dfs(rest - coins[start], start)
            skip = dfs(rest, start + 1)

            memo[(rest, start)] = take + skip
            return memo[(rest, start)]

        return dfs(amount, 0)