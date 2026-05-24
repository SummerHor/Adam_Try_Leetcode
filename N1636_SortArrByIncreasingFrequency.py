class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        mapping = {}
        result = []
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        sorted_dict = dict(
            sorted(mapping.items(), key=lambda item: (item[1], -item[0]))
        )

        for key, val in sorted_dict.items():
            result += [key] * val
        return result
