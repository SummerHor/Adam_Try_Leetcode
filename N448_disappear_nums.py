class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        disappear_nums = []
        set_nums = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in set_nums:
                disappear_nums.append(num)

        return disappear_nums
