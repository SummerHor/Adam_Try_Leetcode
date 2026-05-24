class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(arr)
        # Record num : rank
        rank = 1
        mapping = {}
        for num in sorted_arr:
            if num not in mapping:
                mapping[num] = rank
                rank += 1
        for i, num in enumerate(arr):
            if num in mapping:
                arr[i] = mapping[num]
        return arr
