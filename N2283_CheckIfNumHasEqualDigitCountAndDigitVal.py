class Solution:
    def digitCount(self, num: str) -> bool:

        nums = sorted(num)
        if len(num) <= int(nums[-1]):
            fre_digits = [0] * (int(nums[-1]) + 1)
        else:
            fre_digits = [0] * len(num)  # frequency of digits in ascending order

        for n in nums:
            fre_digits[int(n)] += 1

        for i, n in enumerate(num):
            if int(n) != fre_digits[i]:
                return False
        return True

