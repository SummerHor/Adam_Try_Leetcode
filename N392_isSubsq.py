class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsq = ""
        for char in s:
            if char not in t:
                return False
            for index, c in enumerate(t):
                if char == c:
                    subsq += char
                    t = t[index + 1 :]
                    break
        return True if subsq == s else False


# s = "abc"
# t = "ahbgdc"
# s = "bb"
# t = "ahbgdc"
s = "aza"
t = "abzba"
print(Solution().isSubsequence(s, t))
