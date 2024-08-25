from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for the next unique element position
        unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        # The length of the array without duplicates is unique_index + 1
        return unique_index + 1


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = s.removeDuplicates(nums)
print(f"New length: {new_length}")
print(f"Array after removing duplicates: {nums[:new_length]}")
