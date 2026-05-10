class Solution:
    def isUgly(self, n: int) -> bool:
        # accepted_factors = {2, 3, 5}
        if n == 1:
            return True
        while n > 0 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            if n % 5 == 0:
                n //= 5
        if n == 1:
            return True
        else:
            return False
