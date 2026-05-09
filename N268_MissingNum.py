class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mapping = set(nums)
        for num in range(0, max(nums) + 1):
            if num not in mapping:
                return num
        return max(nums) + 1
