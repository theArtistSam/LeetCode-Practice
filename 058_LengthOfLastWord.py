class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_start = False
        i = len(s) - 1
        c = 0
        while i >= 0 or ():
            if s[i] != ' ':
                c += 1
                is_start = True
            elif is_start and s[i] == ' ':
                return c
            i -= 1
        return c


s = Solution()
print(s.lengthOfLastWord('   fly me   to   the moon  '))
