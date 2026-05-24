class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxi = max(nums)
        for i, num in enumerate(nums):
            if num == maxi:
                index = i
            if num != maxi and 2 * num > maxi:
                return -1
        return index
