class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        if len(s) != len(t):
            return False
        for char1, char2 in zip(s, t):
            if char1 not in mapping1:
                mapping1[char1] = 1
            else:
                mapping1[char1] += 1
            if char2 not in mapping2:
                mapping2[char2] = 1
            else:
                mapping2[char2] += 1

        for char in mapping1.keys():
            if char not in mapping2:
                return False
            elif char in mapping2:
                if mapping1[char] != mapping2[char]:
                    return False
        return True
