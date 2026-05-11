class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        indexes = []
        found_vowels = []
        index = 0
        for char in s:
            if char.lower() in vowels:
                indexes.append(index)
                found_vowels.append(char)
            index += 1
        s = list(s)
        reverse_found_vowels = found_vowels[::-1]
        for index, vowel in zip(indexes, reverse_found_vowels):
            s[index] = vowel
        return "".join(s)
