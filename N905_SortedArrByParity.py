class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        l, r = 0, len(nums) - 1
        while l < r:
            # if the nums in the l is already even, just move the pointer
            if nums[l] % 2 == 0:
                l += 1
            # if the nums in the r is already odd, just move the pointer
            elif nums[r] % 2 != 0:
                r -= 1
            # otherwise, swap them
            else:
                nums[l], nums[r] = nums[r], nums[l]
        return nums
