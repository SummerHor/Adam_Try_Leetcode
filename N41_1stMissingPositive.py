class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        smallest_postInt = 1
        for num in nums:
            if smallest_postInt == num:
                smallest_postInt += 1
        return smallest_postInt
