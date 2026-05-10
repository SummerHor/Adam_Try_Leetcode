class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        while num > 9:
            num = self.addDigit1(num)
        return num

    def addDigit1(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result


s1 = Solution().addDigits(38)
print(s1)
