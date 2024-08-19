class Solution:
    # nums: List[int]
    # target: int
    # Returns: List[int]
    def twoSum(self, nums, target):
        map = {}

        for i in range(len(nums)):
            # Complement is the value needed to reach the target
            complement = target - nums[i]
            # the current number + number in the map
            # crosspond to the target
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i

        return []  # No solution found
