class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        indices = []
        for i, num in enumerate(nums):
            if num == target:
                indices.append(i)
        return indices
