class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # mapping char : fre
        mapping = {}
        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        fre = list(mapping.values())
        if fre:
            checker = fre[0]
            for num in fre[1:]:
                if checker ^ num != 0:
                    return False
        return True
