class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = ""
        negative = False
        if num == 0:
            return "0"
        elif num < 0:
            num = -num
            negative = True
        while num > 0:
            b7_digit = num % 7
            num //= 7
            base7 = str(b7_digit) + base7
        if negative:
            return "-" + base7
        else:
            return base7
