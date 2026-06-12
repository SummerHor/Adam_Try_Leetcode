import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r"[\!\?\'\,\;\. ]", paragraph)
        mapping = {}
        for word in words:
            word = word.lower()
            if word not in banned and word != "":
                if word not in mapping:
                    mapping[word] = 1
                else:
                    mapping[word] += 1

        mapping = dict(sorted(mapping.items(), key=lambda item: item[-1], reverse=True))
        if mapping:
            return list(mapping.keys())[0]
