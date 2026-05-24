class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        indices = []
        for i, word in enumerate(words):
            if x in word:
                indices.append(i)
        return indices
