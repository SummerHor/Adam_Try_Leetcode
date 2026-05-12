class Solution:
    def toHex(self, num: int) -> str:
        mapping = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

        hexa = ""
        if num == 0:
            return "0"
        elif num < 0:
            num = pow(2, 32) + num

        while num > 0:
            hex_digit = num % 16
            num //= 16

            if hex_digit < 10:
                hexa = str(hex_digit) + hexa
            else:
                hexa = mapping[hex_digit] + hexa
        return hexa
