import math


class Solution:
    def isPrime(self, num: int) -> bool:
        # 1. Handle edge cases
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        # 2. Only check odd numbers up to sqrt(num) because num > 2 is prime only if it is not divisble.
        # We start at 3 and skip all even numbers (step=2)
        limit = int(math.sqrt(num))
        for i in range(3, limit + 1, 2):
            if num % i == 0:
                return False

        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(n):
            if self.isPrime(i):
                count += 1
        return count
