class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # mapping char : word
        mapping = {}
        # store the existed words in mapping
        store = set()
        if len(pattern) != len(s):
            return False

        for char, word in zip(pattern, s):
            if char not in mapping:
                if word in store:
                    return False
                mapping[char] = word
                store.add(word)
            else:
                if mapping[char] != word:
                    return False
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matched = []
        for word in words:
            if self.wordPattern(pattern, word):
                matched.append(word)
        return matched
