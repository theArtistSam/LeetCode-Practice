class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == b == "0":
            return "0"
        return self.to_binary(self.to_decimal(a) + self.to_decimal(b))

    def to_decimal(self, str):
        val = 0
        for i in range(len(str)-1, -1, -1):
            if str[i] == '1':
                val += 2 ** (len(str)-1 - i)

        return val

    def to_binary(self, num):
        b = ''
        while num > 0:
            b = str(num % 2) + b
            num //= 2
        return b


s = Solution()
print(s.addBinary('1010', '1011'))
