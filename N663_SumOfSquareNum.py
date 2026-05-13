import math
import re


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # This matches: Any digits, a literal dot, and exactly one zero at the end
        # ^ and $ ensure the whole string matches from start to finish
        integer_pattern = r"^\d+\.0$"
        if c == 0:
            return True
        num = 0
        while num**2 <= c:
            a = math.sqrt(c - (num**2))

            # Convert the float to a string and check the pattern
            if re.fullmatch(integer_pattern, str(a)):
                return True
            num += 1
        return False
