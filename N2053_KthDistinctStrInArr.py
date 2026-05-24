class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        mapping = {}
        for char in arr:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1
        order = 1
        for char in mapping:
            if mapping[char] == 1:
                if order == k:
                    return char
                order += 1
        return ""
