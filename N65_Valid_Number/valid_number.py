import re


class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = (
            r"^[\-\+]?(\.[0-9]+|[0-9]+\.|[0-9]+|[0-9]+\.[0-9]+)([eE][\+\-]?[0-9]+)?$"
        )
        if re.fullmatch(pattern, s):
            return True
        else:
            return False
