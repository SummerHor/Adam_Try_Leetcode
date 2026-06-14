class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums = sorted(nums)
        diff = []
        for i in range(0, len(nums) - k + 1):
            sub_arr = nums[i : i + k]
            diff.append(sub_arr[-1] - sub_arr[0])
        min_diff = min(diff)
        return min_diff
