class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for charS, charT in zip(s, t):
            if charS not in mapping:
                mapping[charS] = charT
            else:
                if mapping[charS] != charT:
                    return False
        if len(mapping.values()) > len(set(mapping.values())):
            return False
        return True
