class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s and t:
            return t

        mapS = {}
        mapT = {}
        for char in s:
            if char not in mapS:
                mapS[char] = 1
            else:
                mapS[char] += 1
        for char in t:
            if char not in mapT:
                mapT[char] = 1
            else:
                mapT[char] += 1

        for char in mapT:
            if (char in mapS and mapT[char] > mapS[char]) or char not in mapS:
                return char
