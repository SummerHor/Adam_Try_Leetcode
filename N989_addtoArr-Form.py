class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        decimal = 0
        result = []
        for n in range(len(num)):
            decimal = decimal + (num[n] * pow(10, len(num) - n - 1))
        decimal += k

        while decimal > 0:
            digit = decimal % 10
            decimal //= 10
            result.insert(0, digit)
        return result


# decimal = 0
# num = [1, 2, 3]
# for n in range(len(num)):
#     decimal = decimal + (num[n] * pow(10, len(num) - n - 1))
#     print(decimal)
