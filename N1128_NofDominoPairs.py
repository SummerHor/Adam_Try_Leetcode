class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        mapping = {}
        count = 0
        for pair in dominoes:
            pair = tuple(sorted(pair))
            if pair not in mapping:
                mapping[pair] = 1
            else:
                mapping[pair] += 1
        for pair in mapping:
            if mapping[pair] > 1:
                n = mapping[pair]
                count = count + n * (n - 1) // 2
        return count
