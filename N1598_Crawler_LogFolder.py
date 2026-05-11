import re


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0
        pattern = r"[a-z]*[0-9]*\/"
        for log in logs:
            if re.fullmatch(pattern, log):
                count += 1
            elif re.fullmatch(r"\.\.\/", log):
                if count > 0:
                    count -= 1
        return count
