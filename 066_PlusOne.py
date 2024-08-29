from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = True
        count = len(digits) - 1
        while start:
            if digits[count] != 9:
                digits[count] += 1
                start = False
            elif count == 0 and start:
                digits[count] = 0
                digits.insert(0, 1)
                start = False
            else:
                digits[count] = 0
                count -= 1

        return digits


s = Solution()
print(s.plusOne([9, 9, 9]))
