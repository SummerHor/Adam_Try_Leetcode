class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        m1 = {}
        m2 = {}
        for char in word1:
            if char not in m1:
                m1[char] = 1
            else:
                m1[char] += 1
        for char in word2:
            if char not in m2:
                m2[char] = 1
            else:
                m2[char] += 1

        for char in m1:
            if m1[char] - m2.get(char, 0) > 3:
                return False

        for char in m2:
            if m2[char] - m1.get(char, 0) > 3:
                return False
        return True
