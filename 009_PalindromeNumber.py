class Solution(object):
    def isPalindrome(self, x):
        # if the last digit is 0: never a palindrome
        if (x < 0 or (x != 0 and x % 10 == 0)):
            return False

        ori_x = x
        rev_x = 0
        while (x > 0):
            # reverse the number by adding the last digit
            # of the original number to the reverse number
            rev_x = rev_x * 10 + (x % 10)
            x //= 10

        return ori_x == rev_x
