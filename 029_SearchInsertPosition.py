from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        h = len(nums) - 1
        m = (l + h) // 2

        while l <= h:
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                m = (l + h) // 2
            elif nums[m] > target:
                h = m - 1
                m = (l + h) // 2

        return m + 1


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
