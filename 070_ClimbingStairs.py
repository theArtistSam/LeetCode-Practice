class Solution:
    def climbStairs(self, n: int) -> int:
        # works but let's reduce the time complexity
        # Still needed to be worked on!
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
