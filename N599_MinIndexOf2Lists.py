class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        mapping = {}
        result = []
        for index1, word1 in enumerate(list1):
            if word1 in list2:
                index2 = list2.index(word1)
                mapping[word1] = index2 + index1

        # find min length in mapping
        minimum = list(mapping.values())[0]
        for length in mapping.values():
            if length < minimum:
                minimum = length

        for word in mapping:
            if mapping[word] == minimum:
                result.append(word)
        return result
