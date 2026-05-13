import re


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        pattern = r"[A-Za-z]"
        s = list(s)
        while l < r:
            while l < r and not re.fullmatch(pattern, s[l]):
                l += 1
            while r > l and not re.fullmatch(pattern, s[r]):
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
