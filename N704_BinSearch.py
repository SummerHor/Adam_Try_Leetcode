class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower < upper:
            mid = (lower + upper) // 2
            if target > nums[mid]:
                lower = mid + 1
            else:
                upper = mid

        if target == nums[lower]:
            return lower
        else:
            return -1


solution1 = Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9)

solution2 = Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2)
print(solution2)
