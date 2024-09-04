class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    # Memorization helps avoiding unnecessary redundant code duplication
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        # Fibonacci series for the calculation
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)

        return memo[n]
