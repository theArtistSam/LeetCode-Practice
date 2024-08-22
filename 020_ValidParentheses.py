class Solution(object):
    def isValid(self, s):
        map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        for char in s:
            if char in map:
                stack.append(char)
            elif not stack or map[stack.pop()] != char:
                return False
        return not stack
