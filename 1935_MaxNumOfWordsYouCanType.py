import re


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Creating pattern of the brokenLetters
        pattern = r"|".join(char for char in brokenLetters)
        Writable = []
        words = text.split(" ")
        if not pattern:
            return len(words)
        else:
            for word in words:
                if not re.search(pattern, word):
                    Writable.append(word)
            return len(Writable)
