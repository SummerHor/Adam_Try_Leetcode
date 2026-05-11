class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = 0
        YES = True
        mapping_word = {}
        mapping2 = {}
        for word in words:
            if word not in mapping_word:
                mapping_word[word] = {}
                for char in word:
                    if char not in mapping_word[word]:
                        mapping_word[word][char] = 1
                    else:
                        mapping_word[word][char] += 1
        for char in chars:
            if char not in mapping2:
                mapping2[char] = 1
            else:
                mapping2[char] += 1
        print(mapping_word, mapping2)
        for word in words:
            for char in mapping_word[word]:
                # Negate on the true case using De Morgan's Law   !(char in mapping2 and mapping_word[word][char]<= mapping2[char])
                if char not in mapping2 or mapping_word[word][char] > mapping2[char]:
                    YES = False

            if YES:
                print(word)
                count += len(word)
            YES = True
        return count


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(Solution().countCharacters(words, chars))
