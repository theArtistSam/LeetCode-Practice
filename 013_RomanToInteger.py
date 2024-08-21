class Solution(object):
    def romanToInt(self, s):
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        sum = 0
        c = 0
        while c < len(s):
            # Check if the next two characters form a valid numeral
            if c < len(s) - 1 and s[c] + s[c + 1] in map:
                sum += map[s[c] + s[c + 1]]
                c += 2
            else:
                sum += map[s[c]]
                c += 1

        return sum
