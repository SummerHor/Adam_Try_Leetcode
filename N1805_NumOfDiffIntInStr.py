import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        pattern = r"0*[0-9]+"
        diff = set([int(num) for num in re.findall(pattern, word)])
        numDiff = len(diff)
        return numDiff
