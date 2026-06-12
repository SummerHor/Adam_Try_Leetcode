import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Edge case: numbers less than or equal to 1 cannot be perfect numbers
        if num <= 1:
            return False

        # 1 is always a proper divisor for any number > 1
        divisor_sum = 1

        # Only loop up to the square root of num
        for n in range(2, int(math.isqrt(num)) + 1):
            if num % n == 0:
                divisor_sum += n
                paired_divisor = num // n

                # If the divisors are different, add the paired divisor too
                if paired_divisor != n:
                    divisor_sum += paired_divisor

        return divisor_sum == num
