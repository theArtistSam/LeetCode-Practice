class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""
        c = 0

        while True:
            try:
                # Take the character at position c from the first string
                val = strs[0][c]
                # Compare it with the corresponding characters in the other strings
                for i in range(1, len(strs)):
                    if strs[i][c] != val:
                        return prefix
            except IndexError:
                # If we reach the end of any string, return the prefix
                return prefix

            # If all strings have the same character at position c, add it to the prefix
            prefix += val
            c += 1


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
