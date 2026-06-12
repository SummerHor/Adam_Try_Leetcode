class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # store the char of allowed in hashmap
        hashmap = set(allowed)
        countChar = 0  # num of chars of each word that is a member of the set
        count = 0  # the ouput, number of consistent strings
        for word in words:
            for c in word:
                if c not in hashmap:
                    break
                else:
                    print(word, countChar, word)
                    countChar += 1
                    if countChar == len(word):
                        countChar = 0
                        count += 1
            countChar = 0
        return count


# print(
#     Solution().countConsistentStrings(
#         allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]
#     )
# )

print(Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))

