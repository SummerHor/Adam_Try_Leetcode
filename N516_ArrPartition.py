class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums) - 1, 2):
            result += min(nums[i], nums[i + 1])
        return result
