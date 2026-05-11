class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True

        mapping1 = {}
        mapping2 = {}
        for char1 in ransomNote:
            if char1 not in mapping1:
                mapping1[char1] = 1
            else:
                mapping1[char1] += 1

        for char2 in magazine:
            if char2 not in mapping2:
                mapping2[char2] = 1
            else:
                mapping2[char2] += 1

        for char1 in mapping1:
            if char1 not in mapping2:
                return False
            else:
                if mapping1[char1] > mapping2[char1]:
                    return False
        return True


ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"
print(Solution().canConstruct(ransomNote, magazine))
