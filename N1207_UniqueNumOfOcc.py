class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # this hash map is used to store the element of the list which corresponds to its
        # occurrence
        mapping = {}
        for num in arr:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        unique_occ = set(mapping.values())
        if len(unique_occ) == len(mapping.values()):
            return True
        else:
            return False
