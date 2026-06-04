class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mapping num : frequency
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        # sort by frequencies
        sorted_mapping = dict(sorted(mapping.items(), key=lambda item: item[1]))
        return list(sorted_mapping.keys())[-k:]
